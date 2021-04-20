from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from creditos.forms import CreditoForm
from django.views.generic.detail import DetailView
from django.shortcuts import render
from creditos.models import Credito
from django.dispatch import receiver
from caja.models import Caja
from utils import UserAnyMixin, CreateViewMixinCustom, UpdateViewMixinCustom, DeleteJsonMixinCustom

from django.urls import reverse_lazy
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.http import *
from django.shortcuts import redirect

class BasePermissionView(LoginRequiredMixin, UserAnyMixin):
    pass


class JsonCreditos(BasePermissionView, BaseDatatableView):
    model = Credito
    columns = ['id', 'cliente_asignado', 'monto', 'plazo']
    order_columns = ['id', 'cliente_asignado', 'monto', 'plazo']

    def get_initial_queryset(self):
        return Credito.objects.all()


class JsonCreditosDeleted(BasePermissionView, BaseDatatableView):
    model = Credito
    columns = ['id', 'cliente_asignado', 'monto', 'plazo']
    order_columns = ['id', 'cliente_asignado', 'monto', 'plazo']

    def get_initial_queryset(self):
        return Credito.objects.filter(active=False)

@method_decorator(login_required, name='dispatch')
class CreditosList(BasePermissionView, ListView):
    model = Credito
    template_name = 'credit_list.html'
    context_object_name = 'clientes'
    paginate_by = 5

class CreditosDeletedIndex(BasePermissionView, TemplateView):
    template_name = 'credit_deleted.html'

class CreditosCreateView(BasePermissionView, CreateView, CreateViewMixinCustom):
    template_name = 'create_credit.html'
    form_class = CreditoForm
    model = Credito
    success_url = reverse_lazy('creditos:index_credits')

class CreditosDetailView(BasePermissionView, DetailView):
    model = Credito
    template = 'detail_customer.html'
    context_object_name = 'clientes'

class CreditosUpdateView(BasePermissionView, UpdateView, UpdateViewMixinCustom):
    model = Credito
    template_name = 'update_credit.html'
    form_class = CreditoForm
    success_url = reverse_lazy('creditos:index_credits')

class CreditosDeleteView(BasePermissionView, DeleteView):
    model = Credito

    def delete(self,request, *args, **kwargs):
        credito = self.get_object()
        credito.active = False
        credito.save()
        return JsonResponse({'result': 'OK'})

class ResumenView(BasePermissionView, TemplateView):
    template_name = 'resumen.html'

    def get(self,request,*args,**kwargs):
        context = self.get_context_data()
        credito = Credito.objects.get(pk=int(kwargs.get('pk')))
        context['cliente'] = credito.cliente_asignado
        context['monto'] = credito.monto
        context['plazo'] = credito.plazo
        context['descripcion_garantia'] = credito.descripcion_garantia
        context['marca'] = credito.marca
        context['numero_serie'] = credito.numero_serie
        context['modelo'] = credito.modelo
        context['cic'] = credito.cic
        context['cuota_capital'] = credito.cuota_capital
        context['cuota_interes'] = credito.cuota_interes
        context['cuota_total'] = credito.cuota_total
        context['cuotas_pendientes'] = credito.cuotas_pendientes
        context['cuota_total_diaria'] = credito.cuota_total_diaria
        context['cuota_interes_diaria'] = credito.cuota_interes_diaria
        context['pk'] = self.kwargs.get('pk',0)

        return self.render_to_response(context)

def updateCash(request,credit_id):
    credito = Credito.objects.get(id=credit_id)
    cash = Caja.objects.get(id=1)
    if credito.monto > cash.monto:
        return HttpResponseNotFound('<h1>No se cuenta con suficiente credito</h1>')
        
        
    else:
        cash.monto = cash.monto - credito.monto
        cash.save()
    cc = credito.monto/26
    ci = credito.monto*0.15
    credito.cuota_capital = cc
    credito.cuota_interes = ci
    if credito.plazo == 'diario':
        credito.cuota_total = round((ci/26),2)
        credito.cuota_total_diaria = ci/26
        credito.cuota_interes_diaria = round(cc + (ci/26),2)
        credito.cuotas_pendientes = 26
    if credito.plazo == 'semanal':
        credito.cuota_total = round((ci/4),2)
        credito.cuota_total_diaria = round((credito.monto*0.15)/4,2)
        credito.cuota_interes_diaria = round((cc + ci/4),2)
        credito.cuotas_pendientes = 4
    if credito.plazo == 'quincenal':
        credito.cuota_total = round(((credito.monto*0.15)/2),2)
        credito.cuota_total_diaria = round((credito.monto*0.15)/2,2)
        credito.cuota_interes_diaria = round((cc + ci/2),2)
        credito.cuotas_pendientes = 2
    if credito.plazo == 'mensual':
        credito.cuota_total = ci
        credito.cuota_interes_diaria = ci + cc
        
    credito.desembolsado = True
    credito.save() 
    
    return redirect(request.META['HTTP_REFERER'])





        