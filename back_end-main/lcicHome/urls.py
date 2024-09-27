# from django.conf.urls import url
from django.conf.urls import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import render_pdf_view
# from .views import searchListfee
from .views import CustomerInfoINDView, Bank_InfoINDView,UserManagementView
from .views import Bank_InfoINDView
from .views import STypeView
from .views import UserGroupView
from .views import login_view, UserLoginView
from .views import login_view1
from .views import get_csrf_token, login_view, LoginView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from .views import LoginView, M
from rest_framework.routers import DefaultRouter
from .views import EnterpriseInfoViewSet, InvestorInfoViewSet, FCR_reportView, SidebarItemsView, RoleListView, SidebarItemListView, SidebarSubItemListView, UpdateUserView, AssignRoleView, GetUserByUIDView
from rest_framework.routers import DefaultRouter
from .views import Search
from .views import EnterpriseInfoSearch, ManageUserView
from .views import EnterpriseInfoViewSet, InvestorInfoViewSet
from rest_framework.routers import DefaultRouter
from django.urls import re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from .views import enterprise_info_search
# router = DefaultRouter()
# router.register(r'enterpriseinfo', EnterpriseInfoViewSet)
router = DefaultRouter()


router.register(r'investorinfo', InvestorInfoViewSet)
router.register(r'enterpriseinfo', EnterpriseInfoViewSet)
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})

urlpatterns = [
   path('',views.index, name='index'),
   #path('',views.newsinfo_listview.as_view(), name='index'),
   path('newsdetail/',views.hnewsDetail, name='newsdetail'),
   path('newsInfo/',views.hnews, name='newsInfo'),
   path('contact/',views.contact, name='contact'),
   path('history/',views.history, name='history'),
   path('orgChart/',views.orgChart, name='orgChart'),
   path('drChart/',views.directorChart, name='directorChart'),
   path('mdChart/',views.ManagerChart, name='ManagerChart'),
   # path('home/',views.HomeTest, name='HomeTest'),
   path('en/',views.EN_Lang, name='EN_Lang'),
   path('loginPage/',views.loginPage, name='loginPage'),
   path('home/',views.home, name='home'),
   path('logout',views.logout, name='logout'),
   # path('manageUser/', views.ManageUser, name="manageUser"),
   path('<int:UID>', views.view_user, name="view_user"),
   path('addUser/', views.addUser, name='addUser'),
   #path('addUser/', views.addUser, name='addUser'),
   path('editUser/<int:UID>/', views.editUser, name='editUser'),
   path('deleteUser/<int:UID>/', views.deleteUser, name='deleteUser'),
   path ('showUploadfile', views.showUploadfile, name='showUploadfile' ),
   path('uploadFile/', views.uploadFile, name='uploadFile'),
   path('search/', views.search, name='search'),
   path('searchIndividual/', views.searchIndividual, name='searchIndividual'),
   path('searchEnterpise/', views.searchEnterpise, name='searchEnterpise'),
   path('searchConfirm/', views.searchConfirm, name='searchConfirm'),
   path('searchList/', views.searchList, name='searchList'),
   path('searchListfee/<slug:object_id>', views.searchListfee, name='searchListfee'),
   path('searchListConfirm/<slug:object_id>', views.searchListConfirm, name='searchListConfirm'),
   path('render_pdf_view/<slug:object_id>', render_pdf_view, name='render_pdf_view'),
   path('progress/<slug:object_id>', views.progress, name='progress'),
   path('tax_invoice', views.tax, name='tax'),
   
# new urls 
   path('customers/', CustomerInfoINDView.as_view(), name='customer-info-ind'),
   path('bank/', Bank_InfoINDView.as_view(), name='bank_info'),
   path('userList/', ManageUserView.as_view(), name='mangeuser'),
   path('create_user/',UserManagementView.as_view(), name='create_user'),
   path('edit_user/', UserManagementView.as_view(), name='edit-user'),
   path('update_user/<str:UID>/', UpdateUserView.as_view(), name='update-user'),
   path('delete_user/<int:UID>/', UserManagementView.as_view(), name='delete_user'),
   path('get_user/<str:UID>/', GetUserByUIDView.as_view(), name='get-user-by-uid'),
   path('stypes/', STypeView.as_view(), name='stype-view'),
   path('user-groups/', UserGroupView.as_view(), name='user-groups'),
   
   path('api1/login/', login_view, name='login'),
   path('api1/login1/', login_view1, name='login'),
   path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
   path('login/', UserLoginView.as_view(), name='login'),
   # path('api2/login/', LoginView.as_view(), name='login'),
   path('report/', FCR_reportView.as_view(),  name='report'),
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('sidebar_items/' ,SidebarItemsView.as_view(), name='sidebar_items'),    
   path('roles/', RoleListView.as_view(), name='roles'),
   path('sidebar-items/', SidebarItemListView.as_view(), name='sidebar-items'),
   path('sidebar-sub-items/', SidebarSubItemListView.as_view(), name='sidebar-sub-items'),
   path('assign-role/', AssignRoleView.as_view(), name='assign-role'),
   # path('test1', include(router.urls)),
   path('api2/', include(router.urls)),
   
   
   #path paylay
   # Search Enterprise 
   # path('api/search/', Search.as_view(), name='search'),
     path('api/v1/enterprise-info/search/', EnterpriseInfoSearch.as_view(), name='enterprise-info-search'),
     
   # path('api/v2/enterprise-info/search/', enterprise_info_search),
   
   path('enter', include(router.urls)),
     






]
