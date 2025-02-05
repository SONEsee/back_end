from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    path('enterprise/', views.EnterpriseInfoListView.as_view(), name='enterprise-list'),
]