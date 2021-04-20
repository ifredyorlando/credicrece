from django.urls import path
from . import views
app_name = 'caja'
urlpatterns = [
    path('caja/actualizar/<int:pk>/', views.CreditosUpdateView.as_view(), name='update_cash'),
    path('caja/listado-creditos/',views.ExpendCreditoView.as_view(),name='give_credit'),
    path('creditos/json_cajacreditos', views.JsonCreditosCaja.as_view(), name="jsoncreditoscaja"),
]