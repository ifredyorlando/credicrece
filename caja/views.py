from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from caja.forms import CajaForm
from django.views.generic.detail import DetailView
from django.shortcuts import render
from caja.models import Caja
from creditos.models import Credito


from utils import UserAnyMixin, CreateViewMixinCustom, UpdateViewMixinCustom, DeleteJsonMixinCustom

from django.urls import reverse_lazy
from django_datatables_view.base_datatable_view import BaseDatatableView


class BasePermissionView(LoginRequiredMixin, UserAnyMixin):
    pass

class CreditosUpdateView(BasePermissionView, UpdateView, UpdateViewMixinCustom):
    model = Caja
    template_name = 'update_cash.html'
    form_class = CajaForm
    success_url = reverse_lazy('caja:update_cash' , kwargs={'pk': 1})

class JsonCreditosCaja(BasePermissionView,BaseDatatableView):
    model = Credito
    columns = ['id', 'cliente_asignado', 'monto', 'plazo']
    order_columns = ['id', 'cliente_asignado', 'monto', 'plazo']
    def get_initial_queryset(self):
        return Credito.objects.filter(desembolsado=False)


class ExpendCreditoView(BasePermissionView,ListView):
    model = Credito
    template_name = 'credit_list.html'
    context_object_name = 'clientes'
    paginate_by = 5

class CreditosCajaUpdateView(BasePermissionView, UpdateView, UpdateViewMixinCustom):
    model = Caja
    template_name = 'update_cash.html'
    form_class = CajaForm
    success_url = reverse_lazy('caja:update_cash' , kwargs={'pk': 1})