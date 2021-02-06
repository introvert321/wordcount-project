
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='cool'),
    path('About/', views.about, name='about'),
    path('Info/', views.info, name='awei'),
]
