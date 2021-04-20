from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView


from users.forms.forms_user import UserCreateForm, UserUpdateForm, ChangePasswordUserForm
from users.models import Users
from utils.mixinCustom import UserIsAdminGerenteMixin, DeleteJsonMixinCustom, UpdateViewMixinCustom




class BasePermissionView(LoginRequiredMixin, UserIsAdminGerenteMixin):
    pass


class UserIndex(BasePermissionView, TemplateView):
    template_name = 'index.html'


class ListUsers(BasePermissionView, BaseDatatableView):
    model = User
    columns = ['id', 'username', 'nombre', 'email',  'is_active', 'rol', 'perfiluser.bloqueo']
    order_columns = ['id', 'username', 'nombre', 'email',  'is_active', 'rol', 'perfiluser.bloqueo']

    def render_column(self, row, column):
        if column == 'is_active':
            return 'Activo' if row.is_active else 'Inactivo'
        if column == 'nombre':
            return row.first_name + ' ' + row.last_name
        if column == 'rol':
            return row.groups.all().first().name
        else:
            return super(ListUsers, self).render_column(row, column)

    def get_initial_queryset(self):
        user = User.objects.filter(is_staff=False, is_superuser=False).exclude(id=self.request.user.id)
        if not self.request.user.is_superuser and self.request.user.groups.all().first().name != 'Administrador':
            user = user.filter(~Q(groups__name='Administrador'), perfiluser__sucursal__id=self.request.user.perfiluser.sucursal.id)
        return user


class CrearUsuario(BasePermissionView, CreateView):
    template_name = 'create_user.html'
    form_class = UserCreateForm
    model = User
    success_url = reverse_lazy('main:index-users')

    def get_form_kwargs(self):
        kwargs = super(CrearUsuario, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    @transaction.atomic
    def form_valid(self, form):
        form_clean = form.clean()
        usuarios = form.save(commit=False)
        my_group = Group.objects.get(name=form_clean['groups'].name)
        sucursal = form_clean['sucursales']
        usuarios.save()
        usuarios.groups.add(my_group.id)
        Users.objects.create(usuario=usuarios)
        messages.success(self.request, 'Se ha creado el exitosamente el registro')
        return HttpResponseRedirect(self.success_url)


class UpdateUser(BasePermissionView, UpdateView):
    template_name = 'update_user.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('main:index-users')

    def get_form_kwargs(self):
        kwargs = super(UpdateUser, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_initial(self):
        self.initial = {
            'username': self.object.username,
            'first_name': self.object.first_name,
            'last_name': self.object.last_name,
            'email': self.object.email,
            'groups': self.object.groups.all().first().pk,
        }
        return self.initial.copy()

    @transaction.atomic
    def form_valid(self, form):
        form_clean = form.clean()
        usuario = User.objects.get(pk=self.object.id)
        usuario.username = form_clean['username']
        usuario.first_name = form_clean['first_name']
        usuario.last_name = form_clean['last_name']
        usuario.email = form_clean['email']
        usuario.is_active = form_clean['is_active']
        group = form_clean['groups']
        usuario.groups.clear()
        group.user_set.add(self.object)
        usuario.save()
        perfil = Users.objects.get(usuario=usuario)
        perfil.save()
        messages.warning(self.request, 'Se ha editado el registro exitosamente')
        return HttpResponseRedirect(self.success_url)


class DeleteUser(BasePermissionView, DeleteJsonMixinCustom):
    model = User

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs.get('pk'))
        Perfil.objects.get(usuario=user).delete()
        user.delete()
        return JsonResponse({'result': 'OK'})


class ChangePasswordUser(BasePermissionView, UpdateView, UpdateViewMixinCustom):
    template_name = 'change_password.html'
    model = User
    form_class = ChangePasswordUserForm
    success_url = reverse_lazy('main:index-users')

    def get_form_kwargs(self):
        kwargs = {'initial': self.get_initial(), 'instance': self.object, 'prefix': self.get_prefix()}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({'data': self.request.POST, 'files': self.request.FILES})
        return kwargs


class UnlockUser(BasePermissionView, UpdateView):

    def post(self, request, *args, **kwargs):
        perfil = Users.objects.filter(usuario_id=self.kwargs.get('pk', 0)).first()
        if perfil is not None:
            perfil.is_blocked = 0
            perfil.save()
            return JsonResponse({'result': 'OK'})
        else:
            return JsonResponse({'result': 'Error'})
