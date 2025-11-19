# urls.py
from django.urls import path
from .views import (STypeListCreate, STypeRetrieveUpdateDestroy, TelecomCusListCreate, TelecomCusRetrieveUpdateDestroy,
                   UploadJsonTelecomView, UploadFileTelecomListCreate, UploadFileTelecomRetrieveUpdateDestroy,TelecomBillListCreate,
                   TelecomBillRetrieveUpdateDestroy,UploadBillJsonFileView)

urlpatterns = [
    path('stype/', STypeListCreate.as_view(), name='stype-list-create'),
    path('stype/<int:pk>/', STypeRetrieveUpdateDestroy.as_view(), name='stype-detail'),
    path('telecom_cus/', TelecomCusListCreate.as_view(), name='telecomcus-list-create'),
    path('telecom_cus/<int:pk>/', TelecomCusRetrieveUpdateDestroy.as_view(), name='telecomcus_detail'),
    path('telecom_bill/', TelecomBillListCreate.as_view(), name='telecombill-list-create'),
    path('telecom_bill/<int:pk>/', TelecomBillRetrieveUpdateDestroy.as_view(), name='telecombill_detail'),
    path('upload-json-telecom/', UploadJsonTelecomView.as_view(), name='upload-json'),
    path('telecom-file/', UploadFileTelecomListCreate.as_view(), name='telecom-file-list-create'),
    path('telecom-file/<int:pk>/', UploadFileTelecomRetrieveUpdateDestroy.as_view(), name='telecom-file-detail'),
    path('upload-bill/', UploadBillJsonFileView.as_view(), name='upload-bill-json'),

]