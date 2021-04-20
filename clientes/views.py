from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from clientes.forms import ClienteForm
from django.views.generic.detail import DetailView
from django.shortcuts import render
from clientes.models import Cliente


from utils import UserAnyMixin, CreateViewMixinCustom, UpdateViewMixinCustom, DeleteJsonMixinCustom

from django.urls import reverse_lazy
from django_datatables_view.base_datatable_view import BaseDatatableView


class BasePermissionView(LoginRequiredMixin, UserAnyMixin):
    pass


class JsonClientes(BasePermissionView, BaseDatatableView):
    model = Cliente
    columns = ['id', 'primer_nombre', 'tercer_nombre', 'correo_electronico']
    order_columns = ['id', 'primer_nombre', 'tercer_nombre', 'correo_electronico']

    def get_initial_queryset(self):
        return Cliente.objects.all()


class JsonClientesDeleted(BasePermissionView, BaseDatatableView):
    model = Cliente
    columns = ['id', 'primer_nombre', 'tercer_nombre', 'correo_electronico']
    order_columns = ['id', 'primer_nombre', 'tercer_nombre', 'correo_electronico']

    def get_initial_queryset(self):
        return Cliente.objects.filter(active=False)

@method_decorator(login_required, name='dispatch')
class CustomersList(BasePermissionView, ListView):
    model = Cliente
    template_name = 'customers_list.html'
    context_objecta_name = 'clientes'
    paginate_by = 5

class ClientesDeletedIndex(BasePermissionView, TemplateView):
    template_name = 'clientes_deleted.html'

class CustomerCreateView(BasePermissionView, CreateView, CreateViewMixinCustom):
    template_name = 'create_customer.html'
    form_class = ClienteForm
    model = Cliente
    success_url = reverse_lazy('clientes:index_customers')

class CustomersDetailView(BasePermissionView, DetailView):
    model = Cliente
    template = 'detail_customer.html'
    context_object_name = 'clientes'

class CustomersUpdateView(BasePermissionView, UpdateView, UpdateViewMixinCustom):
    model = Cliente
    template_name = 'update_customer.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:index_customers')

class CustomerDeleteView(BasePermissionView, DeleteView):
    model = Cliente

    def delete(self,request, *args, **kwargs):
        cliente = self.get_object()
        cliente.active = False
        cliente.save()
        return JsonResponse({'result': 'OK'})