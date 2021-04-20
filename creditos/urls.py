from django.urls import path

from . import views
app_name = 'creditos'
urlpatterns = [
    path('creditos/', views.CreditosList.as_view(), name='index_credits'),
    path('creditos/json_clientes', views.JsonCreditos.as_view(), name="jsoncredits"),
    path('creditos/crear/', views.CreditosCreateView.as_view(), name='create_credits'),
    path('creditos/detalle/<int:pk>/', views.CreditosDetailView.as_view(), name='detail_credits'),
    path('creditos/actualizar/<int:pk>/', views.CreditosUpdateView.as_view(), name='update_credits'),
    path('creditos/eliminar/<int:pk>/', views.CreditosDeleteView.as_view(), name='delete_credits'),
    path('creditos/json-deleted/', views.JsonCreditosDeleted.as_view(), name='deleted-credits-json'),
    path('creditos/list-deleted/', views.CreditosDeletedIndex.as_view(), name='list-credits-clientes'),
    path('caja/desembolsar-credito/<int:credit_id>/',views.updateCash,name='disburse_redit'),
    path('creditos/resumen/<int:pk>/', views.ResumenView.as_view(), name='detail_customer'),
]