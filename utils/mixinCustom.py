from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.admin.helpers import Fieldset
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages


# funtion to verify user permissions
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ModelFormMixin, DeletionMixin


def is_administrador(request):
    return request.user.is_staff or request.user.groups.filter(name='Administrador').exists()


def is_colaboradores(request):
    return request.user.groups.filter(name='Colaboradores').exists()


def is_gerente(request):
    return request.user.groups.filter(name='Gerente Sucursal').exists()


class UserIsAdminMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        has_permission = is_administrador(self.request)
        if not has_permission:
            messages.warning(self.request, 'No tienes permiso para realizar esta accion.')
        return has_permission


class UserIsAdminGerenteMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        has_permission = is_administrador(self.request)
        if not has_permission:
            has_permission = is_gerente(self.request)
        if not has_permission:
            messages.warning(self.request, 'No tienes permiso para realizar esta accion.')
        return has_permission


class UserAnyMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        return User.objects.filter(id=self.request.user.id).exists()


class FieldModelModalFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_names = self.fields.keys()
        self.helper = FormHelper(self)
        self.helper.html5_required = True
        self.helper.label_class = 'col-lg-3 col-form-label'
        self.helper.field_class = 'col-lg-9'
        self.helper.wrapper_class = 'form-group row'
        self.helper.form_tag = False

    def set_legend(self, text):
        self.helper.layout = Fieldset(text, *self.field_names)

    def set_action(self, action):
        self.helper.form_action = action


class CreateViewMixinCustom(ModelFormMixin):

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Se ha creado el registro exitosamente.')
        return super().form_valid(form)


class DeleteJsonMixinCustom(SingleObjectMixin, DeletionMixin, View):

    # Delete object of table
    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return JsonResponse({'result': 'OK'})


class UpdateViewMixinCustom(ModelFormMixin):

    def form_valid(self, form):
        form.save()
        messages.warning(self.request, 'Se ha editado el registro exitosamente.')
        return super().form_valid(form)