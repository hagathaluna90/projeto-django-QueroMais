from django.urls import path
from . import views

app_name = 'queromais'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('catalogo/', views.catalogo, name='catalogo'),
]