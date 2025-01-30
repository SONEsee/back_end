# from django.conf.urls import url
from django.conf.urls import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import render_pdf_view
# from .views import searchListfee
from .views import CustomerInfoINDView
from .views import STypeView
from .views import UserGroupView
from .views import login_view
from .views import login_view1
from .views import get_csrf_token, login_view
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from .views import LoginView
from .views import LoginView1
from rest_framework.routers import DefaultRouter
from .views import EnterpriseInfoViewSet
from rest_framework.routers import DefaultRouter
from .views import EnterpriseInfoViewSet
from .views import Search
from .views import EnterpriseInfoSearch
from .views import EnterpriseInfoViewSet, InvestorInfoViewSet
from rest_framework.routers import DefaultRouter
from .views import get_product_info
from .views import get_product_infocode
from .views import get_product_info, get_product_detail
from .views import get_product_info_by_id
# from .views import upload_files
# from .views import FileUploadView
from .views import UploadFileList
from .views import UploadFilecList
from .views import upload_file_view
from .views import FileUploadViewC, process_uploaded_file
from .views import FileUploadView3, upload_files
from .views import get_data3,get_data4
from .views import get_data_by_id_file
from .views import update_statussubmit
from .views import confirm_upload
from .views import upload_image, upload_imageprofile
from .views import get_collaterals
from .views import get_login3
from .views import get_last_lcicid, upload_enterprise_info
from .views import confirm_image
from .views import UserLoginView
from django.contrib.auth import views as auth_views
from .views import UserProfileView
from .views import UserManagementView, FCR_reportView, SidebarItemsView, RoleListView, SidebarItemListView, SidebarSubItemListView, AssignRoleView, ManageUserView,FCR_reportView,update_statussubmitc,confirm_uploadc
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomerInfoINDView, Bank_InfoINDView, GetUserByUIDView, UpdateUserView, InsertSearchLogView, EnterpriseInfoMatch, searchlog_reportView,charge_reportView, SearchLogChartView,ChargeChartView,SearchLogChart_MonthView, SearchLogChartByBankCodeView, SearchLogChartByDateView,ChargeChartByDateView, ChargeChartMonthView, ChargeChartByBankView, CatalogCatListView,MemberCountView,BankTypeCountView,TotalSearchLogByBankTypeView,SumTotalByBankType,SumTotalChgAmountByBankType,LocationView,filter_villages, SumTotalByBankTypeMonth, SumTotalByBankTypeYear, ReportCatalogView,memberinfolistView,SumTotalByBankTypeEveryMonth, SearchLogChargePerDayView,ChargeCountByHourView, ChargeReportSummary,SearchlogReportDetailView, SidebarCreateView, update_searchlog_status,get_all_upload_files,BankUsersView,LoanCountByDate,CountSearchLogbyDate,CountFeebyDate
from .views import STypeView,UserListbyBank,UserByBankCodeView,DataSubmitUtilityView,UploadUtilityView,CreateMemberView,AddMemberAPIView, DistinctBankCodeView, BankBranchListView

from .views import UserGroupView
from .views import upload_json
from .views import SearchBatfileAPIView

# from .views import FileUploadView, FileDeleteView
# from .views import upload_files
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
   path('manageUser', views.manageUser, name="manageUser"),
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
   path('stypes/', STypeView.as_view(), name='stype-view'),
   path('user-groups/', UserGroupView.as_view(), name='user-groups'),
   
   path('api1/login/', login_view, name='login'),
   path('api1/login1/', login_view1, name='login'),
   path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
  #  path('login/', LoginView.as_view(), name='login'),
   path('login/', UserLoginView.as_view(), name='login'),
   path('login1/', LoginView1.as_view(), name='login'),
   path('api2/login/', LoginView.as_view(), name='login'),
  #  paylay Pherm
   path('sidebar_items/' ,SidebarItemsView.as_view(), name='sidebar_items'),
   path('create_sidebar/', SidebarCreateView.as_view(),name='create_sidebar'),
   path('create_sidebar/<int:pk>/', SidebarCreateView.as_view(),name='create_sidebar_update'),
   path('roles/', RoleListView.as_view(), name='roles'),
   path('sidebar-items/', SidebarItemListView.as_view(), name='sidebar-items'),
   path('sidebar-sub-items/', SidebarSubItemListView.as_view(), name='sidebar-sub-items'),
   path('assign-role/', AssignRoleView.as_view(), name='assign-role'),
   path('userList/', ManageUserView.as_view(), name='mangeuser'),
   path('create_user/',UserManagementView.as_view(), name='create_user'),
   path('api2/', include(router.urls)),
   path('customers/', CustomerInfoINDView.as_view(), name='customer-info-ind'),
   path('bank/', Bank_InfoINDView.as_view(), name='bank_info'),
#    path('memberinfo/', MemberInfoListView.as_view(), name='member_info'),
   path('edit_user/', UserManagementView.as_view(), name='edit-user'),
   path('update_user/<str:UID>/', UpdateUserView.as_view(), name='update-user'),
   path('delete_user/<int:uid>/', UserManagementView.as_view(), name='delete_user'),
   path('get_user/<str:UID>/', GetUserByUIDView.as_view(), name='get-user-by-uid'),
   path('stypes/', STypeView.as_view(), name='stype-view'),
   path('user-groups/', UserGroupView.as_view(), name='user-groups'),
   path('report/', FCR_reportView.as_view(),  name='report'),
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('insert_searchlog/', InsertSearchLogView.as_view(), name='insert_searchlog'),
   path('log_report/', searchlog_reportView.as_view(), name='report_searchlog'),
   path('log_report/detail/', SearchlogReportDetailView.as_view(), name='report_searchlog'),
   path('charge_report/', charge_reportView.as_view(), name='charge_report'),
   path('charge_report/summary/', ChargeReportSummary.as_view()),  # No extra arguments
   path('charge_report/<str:bnk_code>/', charge_reportView.as_view(), name='charge_report_by_bank'),
   path('log_report/<str:bnk_code>', searchlog_reportView.as_view(), name='report_searchlog'),
   path('charge_report/<str:bnk_code>', charge_reportView.as_view(), name='charge_searchlog'),
   path('searchlog_chart/', SearchLogChartView.as_view(), name='searchlog_chart'),
   
   path('searchlog_chart/month/<str:month_year>', SearchLogChart_MonthView.as_view(), name='searchlog_chartbymonth'),
   path('searchlog_chart/month/', SearchLogChart_MonthView.as_view(), name='searchlog_chart_current_month'),
   path('searchlog_chart/month/<str:month_year>/', SearchLogChart_MonthView.as_view(), name='searchlog_chart_month'),  
   
   path('searchlog_chart/date/<str:inquiry_date>', SearchLogChartByDateView.as_view(), name='searchlog_chartbydate'),
   
   path('searchlog_chart/perday/',SearchLogChargePerDayView.as_view(), name='searchlog_chartperday'),
   
    path('charge-count/', ChargeCountByHourView.as_view(), name='charge-count-by-hour'),
   
   path('searchlog_chart/bank/<str:bnk_code>', SearchLogChartByBankCodeView.as_view(), name='searchlog_chartbybank'),
   path('charge_chart/',ChargeChartView.as_view(), name='charge_report_chart'),
   path('charge_chart/date/<str:charge_date>', ChargeChartByDateView.as_view(), name='charge-chart-by-date'),
   path('charge_chart/month/<str:month_year>',ChargeChartMonthView.as_view(), name='charge-chart-by-month'),
   path('charge_chart/month/',ChargeChartMonthView.as_view(),name='charge-chart-by-monthnow'),
   path('charge_chart/bank/<str:bnk_code>', ChargeChartByBankView.as_view(), name='charge-chart-bank'),
   path('catalog-cats/',CatalogCatListView.as_view(), name='catalog-cats'),
   path('member-count/', MemberCountView.as_view(), name='member-count'),
   path('banktype-count/', BankTypeCountView.as_view(), name='member-count'),
   path('banktype_searchlog/', TotalSearchLogByBankTypeView.as_view(), name='banktype_searchlog'),
   path('sumbanktype_searchlog/', SumTotalByBankType.as_view(), name='sumbanktype_searchlog'),
#    path('sumbanktype_searchlog/datenow/', SumTotalSearchByBankTypeByDate.as_view(), name='sumbanktype_searchlog_date'),
   path('sumbanktype_searchlog/month/', SumTotalByBankTypeMonth.as_view(), name='sumbanktype_searchlog_month'),
   path('sumbanktype_searchlog/year/', SumTotalByBankTypeYear.as_view(),   name='sumbanktype_searchlog_year'),
   path('sumbanktype_chargeamount/', SumTotalChgAmountByBankType.as_view(), name='sumbanktype_chargeamount'),
   path('sumbanktype_chargeamount/month/<str:month_year>/', SumTotalChgAmountByBankType.as_view(), name='sumbanktype_chargeamount_bymonth'),
   path('sumbanktype_chargeamount/month/', SumTotalChgAmountByBankType.as_view(), name='sumbanktype_chargeamount_bymonth'),
   path('sumbanktype_chargeamount/anymonth/', SumTotalByBankTypeEveryMonth.as_view(), name='sumbanktype_chargeamount_byanymonth'),
   
   path('locations/', LocationView.as_view(), name='location-list'),
   path('filter_villages/', filter_villages, name='filter_villages'),
   path('report_catalog/', ReportCatalogView.as_view(), name='report_catalog'),
   path('report_catalog/<int:pk>/', ReportCatalogView.as_view(), name='report-catalog-detail'),
   path('memberinfo/', memberinfolistView.as_view(),name='memberinfo'),
   
   
   
   path('enterprisematch/', EnterpriseInfoMatch.as_view(), name='enterprise-info-match'),
   
   path('api/v1/enterprise-info/search/', EnterpriseInfoSearch.as_view(), name='enterprise-info-search'),
   
  
   
   
   path('enter', include(router.urls)),
   
   path('productinfo1/', get_product_info, name='get_product_info'),
   path('productinfo2/', get_product_infocode, name='get_product_info'),
   path('productinfo3/', get_product_info_by_id, name='get_product_info_by_id'),
   
    
   path('productinfo/<int:id>/', get_product_info_by_id, name='get_product_info_by_id'),
  #  update-models

  #  path('upload_files/', upload_files, name='upload_files'),
   
   
  
#    path('api/upload_files1', FileUploadView.as_view(), name='file-upload'),


    path('upload-files2/', UploadFileList.as_view(), name='upload-file-list'),
    path('api/upload-filesc2/', UploadFilecList.as_view(), name='upload-file-list'),

    path('api/productinfo3/', get_data3, name='get_data_by_id_file_and_period'),
    path('api/productinfoc3/', get_data4, name='get_data_by_id_file_and_period'),
    path('api/productinfo4/', get_data_by_id_file, name='get_data_by_id_file'),
    path('confirm_upload/', views.confirm_upload, name='confirm_upload'),
    path('confirm_uploadc/', views.confirm_uploadc, name='confirm_uploadc'),

    # path('upload333/', FileUploadView3.as_view(), name='file-upload'),
    path('upload-files/', FileUploadView3.as_view(), name='upload_files_view'),
    path('process-files/', upload_files, name='upload_files'),



    path('upload-filesC/', FileUploadViewC.as_view(), name='upload_files_view'),
    path('process-filesC/', process_uploaded_file, name='process_uploaded_file'),



    path('api/update-statussubmit/', update_statussubmit, name='update_statussubmit'),
    path('api/update-statussubmitc/',  update_statussubmitc, name=' update_statussubmitc'),
    path('api/upload_image/', upload_image, name='collateral-update'),
    path('api/upload_imagef/', upload_imageprofile, name='collateral-update'),
    path('api/get_collaterals/', get_collaterals, name='get_collaterals'),
    path('api/get_login3/', get_login3, name='get_login3'),
  
    path('api/enterprise-info/', views.create_enterprise_info, name='create_enterprise_info'),
    path('api/last-lcicid/', get_last_lcicid, name='get_last_lcicid'),
    #path('api/confirm_image/', confirm_image, name='confirm_image'),
    path('api/get_csrf_token/', views.get_csrf_token, name='get_csrf_token'),
    path('api/confirm_image/<int:id>/', views.confirm_image, name='confirm_image'),
    path('api/user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/upload-json/', upload_json, name='upload-json'),
    path('api/search-files/', SearchBatfileAPIView.as_view(), name='search_files_api'),
    
    path("api/get-search-results/<int:id>/", views.get_search_results, name="get_search_results"),
    path('update_searchlog_status/', update_searchlog_status, name='update_searchlog_status'),
    path('upload-enterprise-info/', upload_enterprise_info, name='upload-enterprise-info'),
     path('api/get-enterprise-info/', views.get_enterprise_info, name='get_enterprise_info'),
     path('api/get-enterprise/<int:id_file>/', views.get_all_enterprise, name='get_enterprise'),
      path('api/get-all-upload-files/', views.get_all_upload_files, name='get_all_upload_files'),
      path('branches/', BankBranchListView.as_view(), name='branch-list'),
      
    path('distinct-bnk-codes/', DistinctBankCodeView.as_view(), name='distinct-bnk-codes'),
    path('add-member/', AddMemberAPIView.as_view(), name='add-member'),
    path('create_member/', CreateMemberView.as_view(), name='create-member'),
    path('upload-json/', UploadUtilityView.as_view(), name='upload_json_api'),
	 path('submitutility/',DataSubmitUtilityView.as_view(), name='submitutility'),
    path('userbanklist/',UserListbyBank.as_view(), name='userbanklist'),
    # Dashboard LCIC 
    path('dashboard/bank-user/', BankUsersView.as_view(), name='bankuser'),
    path('dashboard/loan-count-by-month/', LoanCountByDate.as_view(), name='loan-count-by-month'),
    path('dashboard/search-count-by-date/',CountSearchLogbyDate.as_view(), name='searchCount-by-Date'),
    path('dashboard/fee_count-by-date/', CountFeebyDate.as_view(), name='fee-count-by-date'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     