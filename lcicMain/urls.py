from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def home(request):
    return HttpResponse("System is running!")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('lcicHome.urls', 'lcicHome'), namespace='lcic')),
    path('news/', include(('lcicNews.urls', 'lcicNews'), namespace='news')),
    path('api/', include('lcicHome.urls')),
    path('', home, name='home'),

    # path('sql/', include('ned_sql.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# import requests
# import smtplib
# from email.mime.text import MIMEText

# # ຕັ້ງຄ່າ Email
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USER = 'sonesdv164@gmail.com'
# EMAIL_PASSWORD = ''  # ໃສ່ App Password ທີ່ໄດ້ມາ
# TO_EMAIL = 'seedavanhsone@mail.com'

# # URL ຂອງລະບົບ
# url = "http://192.168.45.54:35729"

# def send_alert(subject, message):
#     msg = MIMEText(message)
#     msg['Subject'] = subject
#     msg['From'] = EMAIL_USER
#     msg['To'] = TO_EMAIL

#     with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
#         server.starttls()
#         server.login(EMAIL_USER, EMAIL_PASSWORD)
#         server.send_message(msg)

# try:
#     response = requests.get(url, timeout=5)
#     if response.status_code == 200:
#         print("ລະບົບປົກກະຕິ!")
#     else:
#         error_msg = f"ບັນຫາ! Status: {response.status_code}"
#         print(error_msg)
#         send_alert("ລະບົບມີບັນຫາ", error_msg)
# except Exception as e:
#     error_msg = f"ເຊື່ອມຕໍ່ບໍ່ໄດ້: {e}"
#     print(error_msg)
#     send_alert("ລະບົບບໍ່ຕອບສະໜອງ", error_msg)