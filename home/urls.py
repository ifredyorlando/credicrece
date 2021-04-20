from django.urls import path
from django.views.generic import TemplateView 
from . import views

app_name = 'home'

urlpatterns = [
    path('',TemplateView.as_view(template_name='main/index.html'),name='IndexView',),
    path('login/',views.LoginCustomView.as_view(),name='login')
]