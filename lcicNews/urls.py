from django import urls
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('detail/', views.NewDetail, name = 'detail'),
    path('job/', views.jobs, name = 'jobs'),
    path('members/',views.members, name = 'members'),  
    path('products/',views.products, name='products'),
    path('docInfo/',views.documentInfo, name='docInfo')
    
]