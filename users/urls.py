from __future__ import unicode_literals

from django.urls import path

from users import views 
app_name = 'users'
urlpatterns = [
    # index template users
    path('', views.UserIndex.as_view(), name='index-users'),
    path('listUsers/', views.ListUsers.as_view(), name='list_users'),
    path('crear/', views.CrearUsuario.as_view(), name='create_user'),
    path('editar/<int:pk>/', views.UpdateUser.as_view(), name='update_user'),
    path('eliminar/<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
    path('cambiar-password/<int:pk>/', views.ChangePasswordUser.as_view(), name='password_user'),
    path('desbloquear/<int:pk>/', views.UnlockUser.as_view(), name='unlock_user')
]
