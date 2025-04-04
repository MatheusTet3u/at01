from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='home'),
    path('produto/<int:pk>/', views.detalhes_produto, name='detalhes'),
]
