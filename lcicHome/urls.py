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
from .views import EnterpriseInfoViewSet, GetIndividualAPIView
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
from .views import get_last_lcicid, upload_enterprise_info,unload_statussubmit,error_statussubmit,unload_data,unload_statussubmitc
from .views import confirm_image
from .views import UserLoginView
from django.contrib.auth import views as auth_views
from .views import UserProfileView
from .views import UserManagementView, FCR_reportView, SidebarItemsView, RoleListView, SidebarItemListView, SidebarSubItemListView, AssignRoleView, ManageUserView,FCR_reportView,update_statussubmitc,confirm_uploadc
from . import cleanup_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    CustomerInfoINDView, 
    Bank_InfoINDView, 
    GetUserByUIDView,
    ChargeMatrixViewSet, 
    UpdateUserView, 
    InsertSearchLogView, 
    EnterpriseInfoMatch, 
    searchlog_reportView,
    charge_reportView, 
    SearchLogChartView,
    ChargeChartView,
    SearchLogChart_MonthView, 
    SearchLogChartByBankCodeView, 
    SearchLogChartByDateView,
    ChargeChartByDateView, 
    ChargeChartMonthView, 
    ChargeChartByBankView, 
    CatalogCatListView,
    MemberCountView,
    BankTypeCountView,
    TotalSearchLogByBankTypeView,
    SumTotalByBankType,
    SumTotalChgAmountByBankType,
    LocationView,
    filter_villages, 
    SumTotalByBankTypeMonth, 
    SumTotalByBankTypeYear, 
    ReportCatalogView,
    memberinfolistView,
    SumTotalByBankTypeEveryMonth, 
    SearchLogChargePerDayView,
    ChargeCountByHourView, 
    ChargeReportSummary,
    SearchlogReportDetailView, 
    SidebarCreateView, 
    update_searchlog_status,
    get_all_upload_files,
    BankUsersView,
    LoanCountByDate,
    CountSearchLogbyDate,
    CountFeebyDate,
    STypeView,
    UserListbyBank,
    UserByBankCodeView,
    DataSubmitUtilityView,
    UploadUtilityView,
    CreateMemberView,
    AddMemberAPIView, 
    DistinctBankCodeView, 
    BankBranchListView, 
    JsonFileUploadView,
    LoanStatsView,
    FileDeleteView,
    FileUploadView, 
    FileDetailView, 
    water_progress_view, 
    FileElectricView, 
    electric_progress_view,
    UtilityReportAPIView,
    ProvinceDistrictAPIView, 
    EDLProvinceAPIView, 
    SysUserLogin, 
    AddLCICSystemUser, 
    SysUserTokenRefresh,
    LCICSystemUserDetailView, 
    LCICSystemUserListView, 
    BankListCreateView,
    BankDetailView, 
    EDLProvinceDetailAPIView, 
    FileElectricListAPIView, 
    ElectricReportAPIView, 
    UserGroupViewSet,
    UploadTrackingListAPIView,
    UploadDataAPIView,
    UploadTrackingDetailAPIView,
    InitializeTrackingAPIView, 
    DebugAPIView,
    InitializeTestDataAPIView, 
    TestRealUploadAPIView, 
    InitializeDistrictsAPIView, 
    ChargeReportMainView, 
    ChargeReportDetailView,
    confirm_dispute_upload,
    edl_customer_search,
    water_customer_search,
    SearchLogReportMainView,
    SearchLogReportDetailView,
    ChargeReportSummaryView,
    WaterUploadDataAPIView,
    ReorderSidebarView,
    SearchIndividualBankView,
    SearchIndividualBankInfoView,
    IndividualInfoSearchView,
    IndividualFileUploadView,
    IndividualFileListView,
    IndividualFilePeriodListView, 
    ElectricCustomerSearchAPIView, 
    FCR_reportIndividualView,
    FileUploadViewIndividual,
    IndividualCollateralFileListView,
    EnterpriseMemberSubmitViewSet,
    BorrowerFileUploadView,
    BorrowerFileListView,
    BorrowerFilePeriodListView,
    confirm_upload_borrower,
    CustomerUnmergeViewSet,
    CompareJsonWithDBAPIView,
    RegisterCustomerBatchAPIView,
    MyUploadsListAPIView,
    AllUploadsListAPIView,
    AllUploadsFilteredAPIView,
    CustomerConfirmAPIView,
    
    CustomerManualRegisterAPIView,
    CustomerBatchRegisterAPIView,
    CustomerBatchFinalizeAPIView,
    MyUploadsListAPIView,
    CustomerAllUploadsAPIView,
    ApproveEnterpriseMappingView,
    CustomerUpdateIDAPIView,
    CustomerUpdateSegmentAPIView,
    CheckAndCreateEnterpriseViewList,
    group_enterprise_by_code,
    reject_borrower_loan_view,
    CollateralNewListView,
    CheckAndCreateEnterpriseView,
    update_group_status,
    MergeCompanyMappingsView
)
#tik
from .views import ( UserListAPIView,UserDetailAPIView,UserGroupList,MemberListView,MemberDetailView, MemberTypeListView, VillageInfoListView,DistrictInfoListView, ProvInfoListView,ChargeMatrixListCreateAPIView, ChargeMatrixDetailAPIView,RequestChargeDetailAPIView
                    ,RequestChargeSummaryAPIView,RequestChargeReportAllAPIView,UserLogoutView,UserAccessLogListView,ScoringIndividualInfoSearchView,CreditScoreAPIView,ScrAttTypeDescnewListCreateView, ScrAttTypeDescnewRetrieveUpdateDeleteView,ScrAttributeTablenewListCreateView
                    ,ScrAttributeTablenewRetrieveUpdateDeleteView,CreditScoreINDAPIView,ProductsByBankTypeAPIView,ToggleProductAccessAPIView
                    ,MemberListWithActiveCountAPIView)
                    

from .views import UserGroupView,EnterpriseByLCICView,LCICByEnterpriseView,process_dispute_notification, process_multiple_disputes,process_multiple_disputescollateral
from .views import upload_json,MemberInfoViewSet
from .views import SearchBatfileAPIView,MainCatalogCatViewSet,SubCatalogCatViewSet,CompareJsonWithDBAPIView
# from .views import FileUploadView, FileDeleteView
# from .views import upload_files
# from .views import enterprise_info_search
# router = DefaultRouter()
# router.register(r'enterpriseinfo', EnterpriseInfoViewSet)
router = DefaultRouter()
router.register(r'charges', ChargeMatrixViewSet)
router.register(r'members', MemberInfoViewSet)
router.register(r'investorinfo', InvestorInfoViewSet)
router.register(r'enterpriseinfo', EnterpriseInfoViewSet)
router.register(r'user-groups', UserGroupViewSet, basename='usergroup')
router.register(r'maincatalog', SubCatalogCatViewSet, basename='categorymain')
router.register(r'subcatalog', MainCatalogCatViewSet, basename='categorysub')
router.register(r'enterprises', EnterpriseMemberSubmitViewSet, basename='enterprise')
router.register(r'customer-unmerge', CustomerUnmergeViewSet, basename='customer-unmerge')
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})

 
# Water Supply Upload URL patterns
water_supply_patterns = [
    # Step 1: Initialize Month Tracking
    path('initialize/', views.InitializeWaterTrackingAPIView.as_view(), name='water-initialize'),
    
    # Step 2: Upload Water Supply Data (Fetches from Water API → Inserts into Utility_Bill)
    path('upload/', views.WaterUploadDataAPIView.as_view(), name='water-upload'),
    
    # Step 3: Monitor Progress - Get Tracking Status for Month
    path('tracking/', views.WaterUploadTrackingListAPIView.as_view(), name='water-tracking-list'),
    
    # Step 4: Monitor Progress - Get Detailed Logs  
    path('tracking/<int:tracking_id>/', views.WaterUploadTrackingDetailAPIView.as_view(), name='water-tracking-detail'),
    
    # NEW: Get District Statistics (grouped by Province and District)
    path('statistics/districts/', views.WaterDistrictStatisticsAPIView.as_view(), name='water-district-statistics'),
    
    # NEW: Get Upload Summary (all periods with customer counts)
    path('statistics/summary/', views.WaterUploadSummaryAPIView.as_view(), name='water-upload-summary'),
    # Debug and Testing endpoints
    # path('debug/', views.WaterDebugAPIView.as_view(), name='water-debug'),
    # path('test-upload/', views.WaterTestUploadAPIView.as_view(), name='water-test-upload'),
]

# Water Supply Summary URL patterns
water_summary_patterns = [
    # Overview endpoint - overall statistics and trends
    path('overview/', views.WaterSummaryOverviewAPIView.as_view(), name='water-summary-overview'),
    
    # Month detail endpoint - detailed view for specific month  
    path('month/', views.WaterSummaryByMonthAPIView.as_view(), name='water-summary-month'),
    
    # Export endpoint - export summary data
    path('export/', views.WaterSummaryExportAPIView.as_view(), name='water-summary-export'),
    
    # Quick stats endpoint - dashboard widgets data
    path('stats/', views.WaterSummaryStatsAPIView.as_view(), name='water-summary-stats'),
]

urlpatterns = [
   path('', include(router.urls)),
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
   path('check-enterprise/', CheckAndCreateEnterpriseView.as_view(), name='check-enterprise'),
   path('check-enterprise_list/', CheckAndCreateEnterpriseViewList.as_view(), name='check-enterprise-list'),
   path('api/company/create/', views.create_company_with_registration, name='create_company'),
   path('api/register/list/', views.get_register_customer_list, name='register_list'),
   path('api/company/info/<str:id_file>/', views.get_company_info_by_id_file, name='company_info'),
   path('api/approve-enterprise-mapping/', ApproveEnterpriseMappingView.as_view(), name='approve-enterprise-mapping'),
   path('merge-company-mappings/', MergeCompanyMappingsView.as_view(), name='merge-company-mappings'),
   path('api/group-by-code/', group_enterprise_by_code, name='group-by-code'),
   path('api/update_group_status/', update_group_status, name='update_group_status'),
   path('api/group/detail/', views.group_detail, name='group_detail'),

  
   
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
   path('reorder/', ReorderSidebarView.as_view(), name='reorder-sidebar'),
   path('api/searchcollateral/', SearchIndividualBankView.as_view(), name='search'),
   path('api/searchcollateral-info/', SearchIndividualBankInfoView.as_view(), name='search'),
   path('api/collateral/', CollateralNewListView.as_view(), name='collateral-list'),
   path('api/collateral/approve/', views.approve_collateral, name='approve_collateral'),
   path('api/collateral/reject/', views.reject_collateral, name='reject_collateral'),
   path('api/enterprises_list/', views.get_enterprises, name='get_enterprises'),
   

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
   path('api/search-individual/', IndividualInfoSearchView.as_view(), name='search-individual'),
   path('log_report/', searchlog_reportView.as_view(), name='report_searchlog'),
   path('log_report/detail/', SearchlogReportDetailView.as_view(), name='report_searchlog'),
   path('charge_report/', charge_reportView.as_view(), name='charge_report'),
   path('charge_report/summary/', ChargeReportSummary.as_view()),  # No extra arguments
   path('charge_report/<str:bnk_code>/', charge_reportView.as_view(), name='charge_report_by_bank'),
   path('log_report/<str:bnk_code>', searchlog_reportView.as_view(), name='report_searchlog'),
   path('charge_report/<str:bnk_code>', charge_reportView.as_view(), name='charge_searchlog'),
   path('searchlog_chart/', SearchLogChartView.as_view(), name='searchlog_chart'),
   path('api/individual-file-periods/', IndividualFilePeriodListView.as_view(), name='individual-file-periods'),
   path('api/borrower/periods/', BorrowerFilePeriodListView.as_view(), name='borrower-period-list'),
   
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
    path('api/v1/enterprise-info/by-lcic/<str:lcic_code>/', EnterpriseByLCICView.as_view(), name='enterprise_by_lcic'),
    path('api/v1/enterprise-info/by-enterprise/<str:enterprise_id>/', LCICByEnterpriseView.as_view(), name='lcic_by_enterprise'),

   path('enter', include(router.urls)),
   
   path('productinfo1/', get_product_info, name='get_product_info'),
   path('productinfo2/', get_product_infocode, name='get_product_info'),
   path('productinfo3/', get_product_info_by_id, name='get_product_info_by_id'),
   
    
   path('productinfo/<int:id>/', get_product_info_by_id, name='get_product_info_by_id'),
  #  update-models

  #  path('upload_files/', upload_files, name='upload_files'),
   


   
      #tik
    path('user/', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:uid>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('usergroup_list/', UserGroupList.as_view(), name='usergroup-list'),
    path('member_list/', MemberListView.as_view(),name='memberinfo'),
    path('member_list/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('membertypes/', MemberTypeListView.as_view(), name='membertype-list'),
    path('villageinfos/', VillageInfoListView.as_view(), name='villageinfo-list'),
    path('districtinfos/', DistrictInfoListView.as_view(), name='districtinfo-list'),
    path('provinfos/', ProvInfoListView.as_view(), name='provinfo-list'),
    path('charge-matrix/', ChargeMatrixListCreateAPIView.as_view(), name='charge-list-create'),
    path('charge-matrix/<int:pk>/', ChargeMatrixDetailAPIView.as_view(), name='charge-detail'),
    path('request-charge-summary/', RequestChargeSummaryAPIView.as_view(), name='request_charge_summary'),
    path('request-charge-detail/', RequestChargeDetailAPIView.as_view(), name='request-charge-detail'),
    path('request-charge-report-all/', RequestChargeReportAllAPIView.as_view(), name='request-charge-report-all'),
    path('logout_update/', UserLogoutView.as_view(), name='logout_new'),
    path('access-logs/', UserAccessLogListView.as_view(), name='access-logs'),
    path('api/scoring-individual/', ScoringIndividualInfoSearchView.as_view(), name='scoring-individual'),
    path('credit-score/calculate/', CreditScoreAPIView.as_view(), name='credit-score-calculate'),
    # path('att-types/', ScrAttTypeDescListCreateView.as_view(), name='atttype-list-create'),
    # path('att-types/<int:id_desc>/', ScrAttTypeDescRetrieveUpdateDeleteView.as_view(), name='atttype-detail'),
    # path('attributes/', ScrAttributeTableListCreateView.as_view(), name='attribute-list-create'),
    # path('attributes/<int:att_id>/', ScrAttributeTableRetrieveUpdateDeleteView.as_view(), name='attribute-detail'),
    path('att-types/', ScrAttTypeDescnewListCreateView.as_view(), name='atttype-list-create'),
    path('att-types/<int:id_desc>/', ScrAttTypeDescnewRetrieveUpdateDeleteView.as_view(), name='atttype-detail'),
    path('attributes/', ScrAttributeTablenewListCreateView.as_view(), name='attribute-list-create'),
    path('attributes/<int:att_id>/', ScrAttributeTablenewRetrieveUpdateDeleteView.as_view(), name='attribute-detail'),
    path('credit-score-ind/calculate/', CreditScoreINDAPIView.as_view(), name='credit_score_ind_calculate'),
    path('products-by-bank-type/', ProductsByBankTypeAPIView.as_view(), name='products-by-bank-type'),
    path('toggle-product-access/', ToggleProductAccessAPIView.as_view(), name='toggle-product-access'),
    path('members-with-count/', MemberListWithActiveCountAPIView.as_view()),    
    path('api/individual-files/', IndividualFileListView.as_view(), name='individual-file-list'),
    path('api/borrwor-files/', BorrowerFileListView.as_view(), name='borrwor-file-list'),
    path('api/files-individual-collateral/', IndividualCollateralFileListView.as_view(), name='files-individual-collateral'),
  
#    path('api/upload_files1', FileUploadView.as_view(), name='file-upload'),
    path('api/search-results/bulk-update-status/', 
         views.update_multiple_search_results_status, 
         name='bulk_update_search_results'),


    path('upload-files2/', UploadFileList.as_view(), name='upload-file-list'),
    path('api/upload-filesc2/', UploadFilecList.as_view(), name='upload-file-list'),
    path('api/data/', views.get_data_api, name='get_data_api'),
    path('api/datac/', views.get_c1_disputes_api, name='get_c1_disputes_api'),
    path('api/dispute-loans/', views.get_dispute_loans, name='get_dispute_loans'),
    path('api/dispute-collateral/', views.get_dispute_collateral, name='get_dispute_collateral'),
    path('api/disputes/confirmc/', views.confirm_dispute_colatteral, name='confirm_dispute_colatteral'),
    path('api/reject_individual_loan/<str:id_file>/', views.reject_individual_loan_view, name='reject_individual_loan'),
    path('api/reject_individual_collateral/<str:id_file>/', views.reject_individual_collateral_view, name='reject_individual_loan'),
    path('api/borrower/reject/<str:BID>/', reject_borrower_loan_view, name='reject-borrower'),

    
    path('api/rollback_reconfirm/', views.rollback_and_reconfirm_individual, name='rollback_reconfirm'),
    path('api/rollback_reconfirm_collateral/', views.rollback_and_reconfirm_collateral, name='rollback_reconfirm_collateral'),


    # path('api/search-individual/', views.search_individual_bank_advanced, name='search_individual_bank_advanced'),

    path('api/productinfo3/', get_data3, name='get_data_by_id_file_and_period'),
    path('api/productinfoc3/', get_data4, name='get_data_by_id_file_and_period'),
    path('api/productinfo4/', get_data_by_id_file, name='get_data_by_id_file'),
    path('confirm_upload/', views.confirm_upload, name='confirm_upload'),
    path('confirm_upload_individual/', views.confirm_upload_individual, name='confirm_upload_individual'),
    path('confirm_upload_individual_collateral/', views.confirm_upload_individual_collateral, name='confirm_upload_individual_collateral'),
    path('confirm_uploadc/', views.confirm_uploadc, name='confirm_uploadc'),
    path('unload_uploadc/', views.unload_data, name='unload_data'),
    path('api/borrower/confirm/', confirm_upload_borrower, name='confirm-borrower'),


    
    # path('check-upload-status/<str:FID>/', views.check_upload_status, name='check_upload_status'),

    # path('upload333/', FileUploadView3.as_view(), name='file-upload'),
    path('upload-files/', FileUploadView3.as_view(), name='upload_files_view'),
    path('api/borrower/upload/', BorrowerFileUploadView.as_view(), name='borrower-upload'),
    path('upload-files-individual-loan/', IndividualFileUploadView.as_view(), name='upload_files_view_loan'),
    path('upload-files-individual-collateral/', FileUploadViewIndividual.as_view(), name='upload_files_view_collateral'),
    path('process-files/', upload_files, name='upload_files'),
    path('unload-upload/', views.unload_upload, name='unload_upload'),
    path('api/disputes-by-confirm/', views.get_disputes_by_confirm_id, name='disputes_by_confirm'),
    path('api/disputes-by-confirm_collateral/', views.get_disputes_by_confirm_id_callateral, name='disputes-by-confirm_collateral'),
    path('upload-filesC/', FileUploadViewC.as_view(), name='upload_files_view'),
    path('process-filesC/', process_uploaded_file, name='process_uploaded_file'),

    path('api/update-statussubmit/', update_statussubmit, name='update_statussubmit'),
    path('api/unload_statussubmit/', unload_statussubmit, name='update_statussubmit'),
    path('api/error_statussubmit/', error_statussubmit, name='update_statussubmit'),
    path('api/update-statussubmitc/',  update_statussubmitc, name=' update_statussubmitc'),
    path('api/unload-statussubmitc/',  unload_statussubmitc, name=' update_statussubmitc'),

    path('api/upload_image/', upload_image, name='collateral-update'),
    path('api/upload_imagef/', upload_imageprofile, name='collateral-update'),
    path('api/get_collaterals/', get_collaterals, name='get_collaterals'),
    path('api/get_login3/', get_login3, name='get_login3'),
    path('api/disputes/confirm/', confirm_dispute_upload, name='confirm_dispute'),
    path('process-dispute/', views.process_dispute_notification, name='process_dispute_notification'),
    path('process-multiple-disputes/', process_multiple_disputes, name='process_multiple_disputes'),
    path('process-multiple-disputes-collateral/', process_multiple_disputescollateral, name='process_multiple_disputescollateral'),
    path('api/dispute-loan/<int:id_disput_loan>/status/', views.update_dispute_status, name='update_dispute_status'),
    path('api/dispute-collateral/<int:id_disput_loan>/status/', views.update_dispute_status_collateral, name='update_dispute_status_collateral'),
   

    path('api/enterprise-info/', views.create_enterprise_info, name='create_enterprise_info'),
    path('api/last-lcicid/', get_last_lcicid, name='get_last_lcicid'),
    #path('api/confirm_image/', confirm_image, name='confirm_image'),
    path('api/get_csrf_token/', views.get_csrf_token, name='get_csrf_token'),
    path('api/confirm_image/<int:id>/', views.confirm_image, name='confirm_image'),
    path('api/user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/upload-json/', upload_json, name='upload-json'),
    path('api/search-files/', SearchBatfileAPIView.as_view(), name='search_files_api'),
    # path('api/confirm_upload/', views.confirm_upload,)
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
    # Upload Utility
    # path('upload_utility/', UtilityUploadView.as_view(), name='upload_utility'),
    # path('upload_utility/', JSONFileUploadView.as_view(), name='upload_utility'),
    # path('water-api/upload-json/', JsonFileUploadView.as_view(), name='upload-json'),
    # path('water-api/upload-json/', FileUploadView.as_view(), name='file-upload'),
    # path('water-api/upload-json/<int:pk>/', FileUploadView.as_view(), name='file-update'),
    # path('water-api/upload-json/<int:pk>/', FileDeleteView.as_view(), name='file-delete'),
     
    path('water-api/upload-json/', FileDetailView.as_view(), name='file-list'),
    path('water-api/upload-json/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('water-api/upload-json/<int:pk>/progress/', water_progress_view, name='file-progress'),
    
    path('electric-api/upload-json/', FileElectricView.as_view(), name='electric-file-list'),
    path('electric-api/upload-json/<int:pk>/', FileElectricView.as_view(), name='electric-file-detail'),
    path('electric-api/upload-json/<int:pk>/progress/', electric_progress_view, name='electric-file-progress'),

    path('utility-report/<str:customer_id>/', UtilityReportAPIView.as_view(), name='credit-report'),
    path('utility-report/', UtilityReportAPIView.as_view(), name='credit-report-query'),
    path('edl-report/<str:customer_id>/', ElectricReportAPIView.as_view(), name='credit-report'),
    path('edl-report/', ElectricReportAPIView.as_view(), name='credit-report-query'),
    
    # Dashboard LCIC 
    path('dashboard/bank-user/', BankUsersView.as_view(), name='bankuser'),
    path('dashboard/loan-count-by-month/', LoanCountByDate.as_view(), name='loan-count-by-month'),
    path('dashboard/search-count-by-date/',CountSearchLogbyDate.as_view(), name='searchCount-by-Date'),
    path('dashboard/fee_count-by-date/', CountFeebyDate.as_view(), name='fee-count-by-date'),
    path('dashboard/LoanStatsView/', LoanStatsView.as_view(), name='LoanStatsView'),
     path('api/enterprise/search/', views.search_enterprise_view, name='search_enterprise'),
    path('search/<str:enterprise_id>/', views.search_enterprise_by_id, name='search_enterprise_by_id'),
    path('province-district/<str:pro_id>/', ProvinceDistrictAPIView.as_view(), name='province-district'),
    path('province-edl/', EDLProvinceAPIView.as_view(), name='province-edl'),
    path('province-edldetail/', EDLProvinceDetailAPIView.as_view(), name='province-edldetail'),
    path('filedetail-edl/', FileElectricListAPIView.as_view(), name='filedetail-edl'),
    
    #Tracking API Edl --------------------------
    path('edl-customer-search/', views.edl_customer_search, name='edl_customer_search'),
     path('api/edl-customer-search/', ElectricCustomerSearchAPIView.as_view(), name='electric-customer-search'),
    path('water-customer-search/', views.water_customer_search, name='water_customer_search'),
    
    # Step 1: Load Provinces
    path('provinces/', views.ProvinceListAPIView.as_view(), name='province-list'),
    # Step 2: Load Districts for Selected Province  
    path('districts/', views.DistrictListAPIView.as_view(), name='district-list'),
    # Step 3: Initialize Districts Tracking for Province + Month
    path('initialize-districts/', views.InitializeDistrictsAPIView.as_view(), name='initialize-districts'),
    # Step 4: Load Individual District Data (Upload Data → Fetches from EDL API → Inserts into Electric_Bill)
    path('upload-data/', views.UploadDataAPIView.as_view(), name='upload-data'),
    # Step 5: Monitor Progress - Get Tracking Status for Province
    path('upload-tracking/', views.UploadTrackingListAPIView.as_view(), name='upload-tracking-list'),
    # Step 6: Monitor Progress - Get Detailed Logs  
    path('upload-tracking/<int:tracking_id>/', views.UploadTrackingDetailAPIView.as_view(), name='upload-tracking-detail'),
    path('initialize-tracking/', InitializeTrackingAPIView.as_view(), name='initialize-tracking'),
    path('debug/', DebugAPIView.as_view(), name='debug-api'),
    path('init-test-data/', InitializeTestDataAPIView.as_view(), name='init-test-data'),
    path('api/test-real-upload/', TestRealUploadAPIView.as_view(), name='test-real-upload'),
    
    # Test DATA EDL
    path('initialize-districts-alt/', views.InitializeDistrictsAlternativeView.as_view(), name='initialize-districts-alt'),
    path('initialize-districts-func/', views.initialize_districts_function, name='initialize-districts-func'),
    path('debug-edl/', views.debug_edl_api, name='debug-edl'),
    
    path('bulk-upload-all/', views.BulkUploadAllProvincesAPIView.as_view(), name='bulk-upload-all'),
    path('bulk-upload-status/', views.BulkUploadStatusAPIView.as_view(), name='bulk-upload-status'),
    
    # Summarize EDL Data Loaded
    # EDL Summary APIs
    path('edl-summary/overview/', views.EDLSummaryOverviewAPIView.as_view(), name='edl-summary-overview'),
    path('edl-summary/province/', views.EDLSummaryByProvinceAPIView.as_view(), name='edl-summary-province'),
    path('edl-summary/district/', views.EDLSummaryByDistrictAPIView.as_view(), name='edl-summary-district'),
    path('edl-summary/export/', views.EDLExportSummaryAPIView.as_view(), name='edl-summary-export'),
    path('overview/', views.EDLSummaryOverviewAPIView.as_view(), name='overview'),
    
    path('water-supply/', include(water_supply_patterns)),
    path('water-summary/', include(water_summary_patterns)),
    
    # API Mai Sumlup LCIC -----------------
    path('charge_report_summary/', ChargeReportSummaryView.as_view(), name='charge-report-summary'),
    path('charge_report_main/', ChargeReportMainView.as_view(), name='charge-report-main'),
    path('charge_report_detail/', ChargeReportDetailView.as_view(), name='charge-report-detail'),
    path('report_individual/', FCR_reportIndividualView.as_view(), name='fcr-report-individual'),
    
    
    #---------------------------------------------
    #----- START POINTS -----------------------------
    
    # # Matching endpoints
    # path('find-candidates/', views.find_matching_candidates, name='find_candidates'),
    # path('candidates/', views.get_matching_candidates, name='get_candidates'),
    # path('review/', views.review_candidate, name='review_candidate'),
    # # Merge/Unmerge endpoints
    # path('merge/', views.merge_customers, name='merge_customers'),
    # path('unmerge/', views.unmerge_customer, name='unmerge_customer'),
    # # Customer data endpoints
    # path('customer/<str:lcic_id>/identifiers/', views.get_customer_identifiers, name='get_identifiers'),
    # path('customer/<str:lcic_id>/history/', views.get_merge_history, name='get_history'),
    # # Statistics
    # path('statistics/', views.get_statistics, name='statistics'),
    
    # Matching Candidates
    path('find-candidates/', views.find_matching_candidates, name='find_matching_candidates'),
    path('candidates/', views.list_matching_candidates, name='list_matching_candidates'),
    path('review/', views.review_candidate, name='review_candidate'),
    
    # Merged Customers (IndividualBankIbkInfo)
    path('merged-customers/', views.list_merged_customers, name='list_merged_customers'),
    path('customer/<str:lcic_id>/', views.get_customer_details, name='get_customer_details'),
    
    # Approved Matches
    path('approved-matches/', views.list_approved_matches, name='list_approved_matches'),
    
    # Manual Operations
    path('merge/', views.manual_merge, name='manual_merge'),
    path('unmerge/', views.unmerge_customer, name='unmerge_customer'),
    
    # Statistics
    path('statistics/', views.get_statistics, name='get_statistics'),

    path('cleanup/duplicates/', cleanup_views.list_duplicate_info_records, name='list_duplicate_info_records'),
    path('cleanup/merge/', cleanup_views.merge_info_records, name='merge_info_records'),
    path('cleanup/statistics/', cleanup_views.get_cleanup_statistics, name='get_cleanup_statistics'),
    
    
    # Customer Merge Information
    path('customer/<str:lcic_id>/merge-info/', 
         views.get_customer_merge_info, 
         name='get_customer_merge_info'),
    
    # NEW: List all merged customers with optional filters
    path('customers/merged/', 
         views.list_merged_customers, 
         name='list_merged_customers'),
    
    # NEW: Get merge statistics
    path('customers/merged/statistics/', 
         views.get_merge_statistics, 
         name='get_merge_statistics'),
    
    # General customer search (requires search term)
    path('customers/search/', 
         views.search_customers, 
         name='search_customers'),
    
    # List all merge operations
    path('merges/history/', 
         views.list_all_merges, 
         name='list_all_merges'),
    
    #Create Customer With LCIC ID
    path('new/customer/create/',CompareJsonWithDBAPIView.as_view(), name="create_customer_with_lcic_id"),
    path('customer/register/batch/', RegisterCustomerBatchAPIView.as_view(), name="register_customer_batch"),
    # Main endpoints
    path('register/customer/my-uploads/', MyUploadsListAPIView.as_view(), name='my-uploads'),
    # path('register/customer/all-uploads/', AllUploadsListAPIView.as_view(), name='all-uploads'),
    # Optional: More powerful filtering
    path('register/customer/uploads/', AllUploadsFilteredAPIView.as_view(), name='uploads-filtered'),
    # path('register/customer/confirm/', CustomerConfirmAPIView.as_view(), name='customer-confirm'),
    
        # Manual customer registration
    path('register/customer/manual/', 
         CustomerManualRegisterAPIView.as_view(), 
         name='customer-manual-register'),
    
    # Batch customer registration
    path('register/customer/batch/', 
         CustomerBatchRegisterAPIView.as_view(), 
         name='customer-batch-register'),
    path('register/customer/batch/finalize/', 
         CustomerBatchFinalizeAPIView.as_view(), 
         name='customer-batch-finalize'),
    
    # My uploads list
    path('register/customer/my-uploads/', 
         MyUploadsListAPIView.as_view(), 
         name='my-uploads'),
        # Get all uploaded customers (Admin)
    path('register/customer/all-uploads/', 
         CustomerAllUploadsAPIView.as_view(), 
         name='customer-all-uploads'),
    
    # Confirm customers with matching
    path('register/customer/confirm/', 
         CustomerConfirmAPIView.as_view(), 
         name='customer-confirm'),
    
    path('register/customer/update-id/', 
     CustomerUpdateIDAPIView.as_view(), 
     name='customer-update-id'),
    
    path('register/customer/update-segment/', 
     CustomerUpdateSegmentAPIView.as_view(), 
     name='customer-update-segment'),
    
    #---------------------------------------------
    #----- END POINTS -----------------------------
    
    # SearchLog Reports  
    path('searchlog_report_main/', SearchLogReportMainView.as_view(), name='searchlog-report-main'),
    path('searchlog_report_detail/', SearchLogReportDetailView.as_view(), name='searchlog-report-detail'),
    
    #--------------------------------------
    path('systemlogin/', SysUserLogin.as_view(), name='sys_user_login'),
    path('sys-add-user/', AddLCICSystemUser.as_view(), name='add_system_user'),
    path('token/refresh/', SysUserTokenRefresh.as_view(), name='token_refresh'),
    path('sys-list-user/', LCICSystemUserListView.as_view(), name='add_system_user'),
     path('sys-detail-user/<int:pk>/', LCICSystemUserDetailView .as_view(), name='add_system_user'),
   
    path('banks/', BankListCreateView.as_view(), name='bank_list_create'),
    path('banks/<int:pk>/', BankDetailView.as_view(), name='bank_detail'),
    path('', views.location_form, name='location_form'),
    path('api/provinces/', views.get_all_provinces, name='get_all_provinces'),
    path('api/districts/', views.get_districts_by_province, name='get_districts_by_province'),
    path('api/villages/', views.get_villages_by_district, name='get_villages_by_district'),
    path('api/investors/', views.get_all_investors_api, name='get_all_investors'),
    path('api/investors/<int:investor_id>/', views.get_investor_by_id_api, name='get_investor_by_id'),
    path('api/investors/search/', views.search_investors_api, name='search_investors'),
    path('api/investors/statistics/', views.get_investor_statistics_api, name='investor_statistics'),
    path('api/investors/enterprise/<str:enterprise_id>/', views.get_investors_by_enterprise_api, name='get_investors_by_enterprise'),
    path('api/investors/nationality/<str:nationality>/', views.get_investors_by_nationality_api, name='get_investors_by_nationality'),
#   sssss
    path('match/', CompareJsonWithDBAPIView.as_view(), name='compare_json_with_db'),
    path('creditscore/', GetIndividualAPIView.as_view(), name="individual_api"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     