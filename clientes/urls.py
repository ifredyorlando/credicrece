from django.urls import path

from . import views
app_name = 'clientes'
urlpatterns = [
    path('clientes/', views.CustomersList.as_view(), name='index_customers'),
    path('clientes/json_clientes', views.JsonClientes.as_view(), name="jsonclientes"),
    path('clientes/crear/', views.CustomerCreateView.as_view(), name='create_customer'),
    path('clientes/detalle/<int:pk>/', views.CustomersDetailView.as_view(), name='detail_customer'),
    path('clientes/actualizar/<int:pk>/', views.CustomersUpdateView.as_view(), name='update_customer'),
    path('clientes/eliminar/<int:pk>/', views.CustomerDeleteView.as_view(), name='delete_customer'),
    path('clientes/json-deleted/', views.JsonClientesDeleted.as_view(), name='deleted-clientes-json'),
    path('clientes/list-deleted/', views.ClientesDeletedIndex.as_view(), name='list-deleted-clientes'),
]