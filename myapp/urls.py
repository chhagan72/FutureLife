from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/', views.BoolDiscovery, name='booldiscovery'),
    path('getintouchform/', views.BookDiscoveryForm, name='getintouchform'),
    path('submitbioform/', views.submitBioForm, name='submitbioform'),
]
