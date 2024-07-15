
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='url-home' ),
    path('login/', views.logIndex, name= 'url-log'),
    path('cadastro/', views.cadIndex, name= 'url-cad'),
    path('classe/', views.classIndex, name='url-class'),
    path('logado/', views.okIndex, name='url-logado')
]