#from asyncio.windows_events import NULL
from contextlib import nullcontext
from datetime import datetime
from multiprocessing import context
from crispy_forms.helper import FormHelper
from re import M
from tkinter.messagebox import NO
from django.http import request
from django.shortcuts import render, redirect
from .models import Login,Group_User, GroupSubMenu, H_imageBar,H_productInfo,H_newsInfo,H_Lang, User_Group, User_Login, Menu, SubMenu, Upload_File, CustomerWater, SegmentType, EnterpriseInfo, InvestorInfo, user_logged, searchLog, request_charge, bank_bnk, C1, C1_disptes, C_error, col_real_estates, col_money_mia, col_equipment_eqi, col_project_prj, col_vechicle_veh, col_guarantor_gua, col_goldsilver_gold
from lcicNews.models import*
# from ..lcicNews.models import newsType, newsInfo
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import hashlib
from django.http import HttpResponseRedirect
from django.urls import reverse
# from .forms import*
from lcicHome.forms import*
from django.core.files.storage import FileSystemStorage
import calendar
import pathlib
import os
import json
from xhtml2pdf import pisa
from psycopg2.extras import Json
import psycopg2
from django.http import JsonResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist, ValidationError
import os
from django.http import HttpResponse
from django.template.loader import get_template
#from xhtml2pdf import pisa
from crispy_forms.layout import Layout, Row, Column
import tempfile
import subprocess
from weasyprint import HTML, CSS
import datetime
from django_weasyprint import WeasyTemplateResponse
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from .serializers import * 
import logging
import binascii
from .models import CustomLoginToken
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
#import requests
# import pymysql

# def EN_Lang(request):
    
#     Lang= request.GET.get('Lang')
#     H_imageBar_v = H_imageBar.objects.filter(published=True)
#     H_products_v = H_productInfo.objects.filter(published=True)
#     H_newsInfo_v = H_newsInfo.objects.filter(published=True )
#     H_Lang_v = H_Lang.objects.filter(id=1)
#     H_com = H_Lang.objects.filter(id=2)
#     H_notice = H_Lang.objects.filter(id=4)
#     H_pro = H_Lang.objects.filter(id=5)
#     H_mem = H_Lang.objects.filter(id=6)
#     H_form = H_Lang.objects.filter(id=7)
#     H_about = H_Lang.objects.filter(id=8)
#     H_job = H_Lang.objects.filter(id=9)
#     H_contact = H_Lang.objects.filter(id=10)
#     H_la = H_Lang.objects.filter(id=11)
#     H_en = H_Lang.objects.filter(id=12)
#     H_history = H_Lang.objects.filter(id=13)
#     H_organize = H_Lang.objects.filter(id=14)
#     H_bod = H_Lang.objects.filter(id=15)
#     H_md = H_Lang.objects.filter(id=16)
#     H_memlcic = H_Lang.objects.filter(id=17)
#     H_allmem = H_Lang.objects.filter(id=18)
#     H_mi = H_Lang.objects.filter(id=19)
#     H_pros = H_Lang.objects.filter(id=20)
#     H_allpro = H_Lang.objects.filter(id=21)
#     H_news = H_Lang.objects.filter(id=22)
#     H_new = H_Lang.objects.filter(id=23)
#     H_more = H_Lang.objects.filter(id=24)
#     H_rmore = H_Lang.objects.filter(id=25)
#     H_ofl = H_Lang.objects.filter(id=26)
#     H_loca = H_Lang.objects.filter(id=27)
#     H_cap = H_Lang.objects.filter(id=28)
 
#     # paginator = Paginator(H_newsInfo_v, 10)
#     # page = request.GET.get('page')
#     # try:
#     #     H_newsInfo_v = paginator.page(page)
#     # except PageNotAnInteger:
#     #     H_newsInfo_v = paginator.page(1)
#     # except EmptyPage:
#     #     H_newsInfo_v = paginator.page(paginator.num_pages)
    
#     return render(request,'English/index.html',{'Lang':Lang,'H_imageBar_v':H_imageBar_v,'H_products_v':H_products_v,'H_newsInfo_v':H_newsInfo_v,'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap })

def index(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    # elif Change_Lang == "la" and Lang == "la":
    #     Lang = 'la'
    H_imageBar_v = H_imageBar.objects.filter(published=True)
    H_products_v = H_productInfo.objects.filter(published=True)
    H_newsInfo_v = H_newsInfo.objects.filter(published=True )
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_login = H_Lang.objects.filter(id=46)

    paginator = Paginator(H_newsInfo_v, 10)
    page = request.GET.get('page')
    try:
        H_newsInfo_v = paginator.page(page)
    except PageNotAnInteger:
        H_newsInfo_v = paginator.page(1)
    except EmptyPage:
        H_newsInfo_v = paginator.page(paginator.num_pages)


    return render(request,'Home/index.html',{'Lang':Lang,'H_imageBar_v':H_imageBar_v,'H_products_v':H_products_v,'H_newsInfo_v':H_newsInfo_v,'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_login':H_login })

def hnewsDetail(request):
    slugID = request.GET.get('slug')
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_login = H_Lang.objects.filter(id=46)

    if slugID:
        H_newsInfo_v = H_newsInfo.objects.filter(published=True)
        H_newsInfo_v = H_newsInfo_v.filter(id=slugID)

    return render(request,'Home/hnewsDetail.html',{'Lang':Lang,'H_newsInfo_v':H_newsInfo_v,'slugID':slugID, 'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact, 'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_login':H_login  })

def hnews(request):
    H_newsInfo_v = H_newsInfo.objects.all()
    H_newsInfo_v = H_newsInfo.objects.filter(published=True)
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_login = H_Lang.objects.filter(id=46)

    paginator = Paginator(H_newsInfo_v, 20)
    page = request.GET.get('page')
    try:
        H_newsInfo_v = paginator.page(page)
    except PageNotAnInteger:
        H_newsInfo_v = paginator.page(1)
    except EmptyPage:
        H_newsInfo_v = paginator.page(paginator.num_pages)

    return render(request,'Home/hnews.html',{'Lang':Lang,'H_newsInfo_v':H_newsInfo_v, 'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact, 'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_login':H_login  })

def products(request):
    H_products_v = H_productInfo.objects.filter(published=True)
    return render(request,'Home/productsInfo.html',{'H_products_v':H_products_v,})

def contact(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_login = H_Lang.objects.filter(id=46)
    return render(request,'Home/contact.html',{'Lang':Lang,'H_Lang_v':H_Lang_v, 'H_com':H_com,  'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact, 'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_login':H_login })

def history(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_t2 = H_Lang.objects.filter(id=34)
    H_p1 = H_Lang.objects.filter(id=33)
    H_t3 = H_Lang.objects.filter(id=36)
    H_p2 = H_Lang.objects.filter(id=35)
    H_t4 = H_Lang.objects.filter(id=38)
    H_p3 = H_Lang.objects.filter(id=37)
    H_t5 = H_Lang.objects.filter(id=40)
    H_p4 = H_Lang.objects.filter(id=39)
    H_t6 = H_Lang.objects.filter(id=42)
    H_p5 = H_Lang.objects.filter(id=41)
    H_t7 = H_Lang.objects.filter(id=44)
    H_p6 = H_Lang.objects.filter(id=43)
    H_p7 = H_Lang.objects.filter(id=45)
    H_login = H_Lang.objects.filter(id=46)
    return render(request,'Home/history.html',{'Lang':Lang, 'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact, 'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_p1':H_p1, 'H_t2':H_t2, 'H_p2':H_p2, 'H_t3': H_t3, 'H_p3': H_p3, 'H_t4':H_t4, 'H_p4':H_p4, 'H_t5':H_t5, 'H_p5': H_p5, 'H_t6':H_t6, 'H_p6': H_p6, 'H_t7':H_t7, 'H_p7': H_p7, 'H_login':H_login})

def orgChart(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_login = H_Lang.objects.filter(id=46)
    return render(request,'Home/orgChart.html',{'Lang':Lang, 'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_login':H_login })

def directorChart(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_login = H_Lang.objects.filter(id=46)
    return render(request,'Home/orgMain.html',{'Lang':Lang, 'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_login':H_login  })

def ManagerChart(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_login = H_Lang.objects.filter(id=46)
    return render(request,'Home/orgSub.html',{'Lang':Lang, 'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_login':H_login })
    
def HomeTest(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_login = H_Lang.objects.filter(id=46)
    return render(request,'News/hometest.html',{'Lang':Lang, 'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_login':H_login })



def EN_Lang(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_imageBar_v = H_imageBar.objects.filter(published=True)
    H_products_v = H_productInfo.objects.filter(published=True)
    H_newsInfo_v = H_newsInfo.objects.filter(published=True )
    H_Lang_v = H_Lang.objects.filter(id=1)
    H_com = H_Lang.objects.filter(id=2)
    H_notice = H_Lang.objects.filter(id=4)
    H_pro = H_Lang.objects.filter(id=5)
    H_mem = H_Lang.objects.filter(id=6)
    H_form = H_Lang.objects.filter(id=7)
    H_about = H_Lang.objects.filter(id=8)
    H_job = H_Lang.objects.filter(id=9)
    H_contact = H_Lang.objects.filter(id=10)
    H_la = H_Lang.objects.filter(id=11)
    H_en = H_Lang.objects.filter(id=12)
    H_history = H_Lang.objects.filter(id=13)
    H_organize = H_Lang.objects.filter(id=14)
    H_bod = H_Lang.objects.filter(id=15)
    H_md = H_Lang.objects.filter(id=16)
    H_memlcic = H_Lang.objects.filter(id=17)
    H_allmem = H_Lang.objects.filter(id=18)
    H_mi = H_Lang.objects.filter(id=19)
    H_pros = H_Lang.objects.filter(id=20)
    H_allpro = H_Lang.objects.filter(id=21)
    H_news = H_Lang.objects.filter(id=22)
    H_new = H_Lang.objects.filter(id=23)
    H_more = H_Lang.objects.filter(id=24)
    H_rmore = H_Lang.objects.filter(id=25)
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    H_login = H_Lang.objects.filter(id=46)
    

    paginator = Paginator(H_newsInfo_v, 10)
    page = request.GET.get('page')
    try:
        H_newsInfo_v = paginator.page(page)
    except PageNotAnInteger:
        H_newsInfo_v = paginator.page(1)
    except EmptyPage:
        H_newsInfo_v = paginator.page(paginator.num_pages)
        
    


    return render(request,'English/index.html',{'Lang':Lang,'H_imageBar_v':H_imageBar_v,'H_products_v':H_products_v,'H_newsInfo_v':H_newsInfo_v,'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_login':H_login})



def loginPage(request):
    if request.method == 'POST':
        Change_Lang= request.GET.get('Lang')
        Lang='la'
        if Change_Lang == "la" and Lang == "la":
            Lang ='la'
        elif Change_Lang == "en" and Lang == "la":
            Lang = 'en'
        elif Change_Lang == "en" and Lang == "la":
            Lang = 'la'
        username = request.POST.get('username')
        password = request.POST.get('password')
        encypt_pwd = hashlib.md5(password.encode()).hexdigest()
        user = Login.objects.filter(username=username, password= encypt_pwd,is_active=True)
        #U_ID = Login.objects.filter(username=username).values_list('UID',flat=True)
        if Login.objects.filter(username=username).exists():
            U_ID = Login.objects.filter(username=username).values_list('UID',flat=True)
            user_info = Login.objects.filter(UID=U_ID[0])
        else:
            messages.info(request, 'Username OR Password is incorrect')           
            return render(request,'Login/login.html')
        G_ID = Login.objects.filter(username=username).values_list('GID_id',flat=True)
        # M_ID get filter user_id
        M_ID = Login.objects.filter(username=username).values_list('MID_id',flat=True)
        GSM_ID = GroupSubMenu.objects.filter(GID=G_ID[0]).values_list('GSMID',flat=True)
        G_nameL = User_Group.objects.filter(GID=G_ID[0])
        G_nameE = User_Group.objects.filter(GID=G_ID[0])
        M_code= memberInfo.objects.filter(id=M_ID[0])
        M_nameL = memberInfo.objects.filter(id=M_ID[0])
        M_nameE = memberInfo.objects.filter(id=M_ID[0])
        Main = Menu.objects.filter(MID=1)
        Management = Menu.objects.filter(MID=2)
        Report = Menu.objects.filter(MID=3)
        User = Menu.objects.filter(MID=4)
        Service = Menu.objects.filter(MID=5)
        Search = Menu.objects.filter(MID=6)
        CusManage = SubMenu.objects.filter(SMID=1)
        MemManage = SubMenu.objects.filter(SMID=2)
        RpManage = SubMenu.objects.filter(SMID=3)
        UserReport = SubMenu.objects.filter(SMID=4)
        MemReport = SubMenu.objects.filter(SMID=5)
        UseSysReport = SubMenu.objects.filter(SMID=6)
        H_ofl = H_Lang.objects.filter(id=26)
        H_loca = H_Lang.objects.filter(id=27)
        H_cap = H_Lang.objects.filter(id=28)
        MMenu = Menu.objects.all()
        SMenu = SubMenu.objects.all()
        
        global u, uname, code, ugroup,L,gsm_id,check_UserGroup,check_member, cus_manage, mem_manage, report_manage, user_report, mem_report, usesys_report, Main_Menu, Management_Menu, Report_Menu, User_Menu, Service_Menu, Search_Menu,office, location, capital
        uname = user_info
        code = M_code
        ugroup = G_nameL
        u= user
        L=Lang   
        gsm_id = GSM_ID 
        # pa kard hai user_id pen global
        check_UserGroup= G_ID[0]
        check_member = M_ID[0]
        Main_Menu = Main
        Management_Menu = Management
        Report_Menu = Report
        User_Menu = User
        Service_Menu = Service
        Search_Menu = Search
        cus_manage = CusManage
        mem_manage = MemManage
        report_manage = RpManage
        user_report = UserReport
        mem_report = MemReport
        usesys_report = UseSysReport
        office = H_ofl
        location = H_loca
        capital = H_cap
        # check user_id
        print("user_id check----->", check_UserGroup)
        request.session['check_UserGroup'] = check_UserGroup
        if user.exists():
            return render(request, 'Login/main.html',{'u':u,'G_nameL':G_nameL,
            'G_nameE':G_nameE,'M_code':M_code,'M_nameL':M_nameL,'M_nameE':M_nameE,
            'Lang':Lang,'user_info':user_info,'uname':uname,'code':code,'ugroup':ugroup,
            'L':L,'gsm_id':gsm_id, 'MMenu':MMenu, 'SMenu':SMenu, 'Main_Menu':Main_Menu,
            'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,
            'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report,
            'G_ID':G_ID, 'check_UserGroup':check_UserGroup,'check_member':check_member,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap})
        else:
            messages.info(request, 'Username OR Password is incorrect')           
    return render(request,'Login/login.html')
    
def home(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    return render(request, 'Login/main.html',{'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'Search_Menu':Search_Menu,'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap,})

def logout(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    return render(request, 'Home/index.html',{'Lang':Lang})


def manageUser(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    alluser = Login.objects.order_by("UID")
    p = Paginator(Login.objects.order_by("UID"),5)
    page = request.GET.get('page')
    users = p.get_page(page)
    paginate_by = 3
    member = memberInfo.objects.all()
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    
    return render(request, 'Management/manageUser.html', {'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member, 'users':users})
    
def view_user(request, UID):
    users= Login.objects.get(pk=UID)
    return HttpResponseRedirect(reverse('Management/manageUser.html',{}))


# def addUser(request):
#    Change_Lang= request.GET.get('Lang')
#    Lang='la'
#    if Change_Lang == "la" and Lang == "la":
#         Lang ='la'
#    elif Change_Lang == "en" and Lang == "la":
#         Lang = 'en'
#    elif Change_Lang == "en" and Lang == "la":
#         Lang = 'la'
#    member = memberInfo.objects.all()
#    password = request.POST.get('password')
#    p = Paginator(Login.objects.order_by("UID"),2)
#    page = request.GET.get('page')
#    users = p.get_page(page)
#    H_ofl = H_Lang.objects.filter(id=26)
#    H_loca = H_Lang.objects.filter(id=27)
#    H_cap = H_Lang.objects.filter(id=28)
#    if request.method == 'POST':
#        form =  addUserForm1(request.POST)
#        if form.is_valid():
#            new_uid = Login.objects.order_by("UID").values_list("UID", flat=True).last()
#            new_username = form.cleaned_data['username']
#            new_password = hashlib.md5(password.encode()).hexdigest()
#            new_nameL = form.cleaned_data['nameL']
#            new_surnameL = form.cleaned_data['surnameL']
#            new_nameE = form.cleaned_data['nameE']
#            new_surnameE = form.cleaned_data['surnameE']
#            new_is_active = form.cleaned_data['is_active']
#            new_GID_id = form.cleaned_data['GID']
#            new_MID_id = form.cleaned_data['MID']
           
#            new_user = Login(
#                UID = new_uid+1,
#                username = new_username,
#                password = new_password,
#                nameL = new_nameL,
#                surnameL = new_surnameL,
#                nameE = new_nameE,
#                surnameE = new_surnameE,
#                is_active = new_is_active,
#                GID = new_GID_id,
#                MID = new_MID_id
#            )
#            new_user.save()
#            return render(request, 'Management/Form_AddUser.html',{
#                'form':addUserForm1(),
#                'success': True,
#                'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
#             'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
#             'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
#             'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
#             'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'member':member, 'users':users
#            })
#    else:
#     form = addUserForm1()   
#    return render(request, 'Management/Form_AddUser.html',{
#     'form':addUserForm1(),
#     'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
#             'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
#             'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
#             'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
#             'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'member':member, 'users':users
#     })
   
   
def addUser(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    alluser = Login.objects.all()
    member = memberInfo.objects.all()
    new_uid = Login.objects.order_by("UID").values_list("UID", flat=True).last()
    password = request.POST.get('password')
    p = Paginator(Login.objects.order_by("UID"),5)
    page = request.GET.get('page')
    users = p.get_page(page)
    # check_password = request.POST.get('check_password')
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    form = addUserForm2(request.POST or None)
    if form.is_valid():
        new_username = form.cleaned_data['username']
        new_password = hashlib.md5(password.encode()).hexdigest()
        new_nameL = form.cleaned_data['nameL']
        new_surnameL = form.cleaned_data['surnameL']
        new_nameE = form.cleaned_data['nameE']
        new_surnameE = form.cleaned_data['surnameE']
        new_GID_id = form.cleaned_data['GID']
        new_MID_id = form.cleaned_data['MID']
           
        new_user = Login(
            UID = new_uid+1,
            username = new_username,
            password = new_password,
            nameL = new_nameL,
            surnameL = new_surnameL,
            nameE = new_nameE,
            surnameE = new_surnameE,
            GID = new_GID_id,
            MID = new_MID_id
           )
        new_user.save()
        # form.save()
        messages.success(request, "ສຳເລັດການເພີ່ມຂໍ້ມູນຜູ້ໃຊ້ລະບົບ")
        context1 = {
        "form":form,
        'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member, 'users':users
        }
        return redirect('/addUser',context1)
    context2 = {
        "form":form,
        'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member, 'users':users
    }
    return render(request, 'Management/addUser.html', context2)


def editUser(request, UID):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    alluser = Login.objects.order_by("UID")
    member = memberInfo.objects.all()
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    p = Paginator(Login.objects.order_by("UID"),5)
    page = request.GET.get('page')
    users = p.get_page(page)
    if request.method == 'POST':
        uusers= Login.objects.get(pk=UID)
        password = request.POST.get('password')
        new_password = hashlib.md5(password.encode()).hexdigest()
        edit_date = datetime.datetime.now()
        form = editUserForm(request.POST, instance=uusers)
        if form.is_valid():
            # new_username = form.cleaned_data['username']
           
            # print(new_password)
            # new_nameL = form.cleaned_data['nameL']
            # new_surnameL = form.cleaned_data['surnameL']
            # new_nameE = form.cleaned_data['nameE']
            # new_surnameE = form.cleaned_data['surnameE']
            # new_GID_id = form.cleaned_data['GID']
            # new_MID_id = form.cleaned_data['MID']
            
            # form = Login(
            #     username = new_username,
            #     password = new_password,
            #     nameL = new_nameL,
            #     surnameL = new_surnameL,
            #     nameE = new_nameE,
            #     surnameE = new_surnameE,
            #     GID = new_GID_id,
            #     MID = new_MID_id
            # )
            # new_user.save()
            edit= form.save(commit=False)
            edit.password = new_password
            edit.updateDate = edit_date
            edit.save()
            messages.success(request, "ສຳເລັດແກ້ໄຂຂໍ້ມູນຜູ້ໃຊ້ລະບົບ !")
            return HttpResponseRedirect('/manageUser',{
               'form':form,
               'success': True,
               'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member, 'users':users
           })
    else:
        uusers= Login.objects.get(pk=UID)
        form =editUserForm(instance=uusers)
    return render(request, 'Management/editUser.html',{
            'form':form,
            'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member, 'users':users
           })
    
def deleteUser(request, UID):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    alluser = Login.objects.order_by("UID")
    member = memberInfo.objects.all()
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    p = Paginator(Login.objects.order_by("UID"),5)
    page = request.GET.get('page')
    users = p.get_page(page)
    if request.method == 'POST':
        users = Login.objects.get(pk=UID)
        users.delete()
        messages.success(request, "ສຳເລັດລຶບຂໍ້ມູນຜູ້ໃຊ້ລະບົບ !")
    # return HttpResponseRedirect(reverse('Management/Manage_User.html'),{
    #         'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
    #         'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
    #         'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
    #         'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
    #         'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member
    #        })
    return HttpResponseRedirect('/manageUser',{
            'success': True,
            'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member, 'users':users
           })  
#class newsinfo_listview(ListView):
#    model = newsInfo
#    template_name = 'News/index.html'
#    context_object_name ='newsInfo_v'
#    paginate_by = 5
#    def get_queryset(self):
#        return newsInfo.objects.filter(published=True)
#    def get_context_data(self, *args , **kwargs ):
#        newsInfo_p =  super(newsinfo_listview,self).get_context_data(*args, **kwargs)
#        newsInfo_p.update({
#            'newsType_v': newsType.objects.all(),
#        })
#        return newsInfo_p

# Calculate File Size
def sizify(value):
        if value < 512000:
            value = value / 1024.0
            ext = "KB"
        elif value < 4194304000:
            value = value / 1048576.0
            ext = "MB"    
        else:
            value = value / 107341824.0           
            ext = "MB"   
        return '%s %s' %(str(round(value, 2)), ext)


def showUploadfile(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    form = showUploadForm(request.POST or None)
    alluser = Login.objects.order_by("UID")
    print(alluser, "showiploadfile in views")
    member = memberInfo.objects.all()
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    segment_type = request.GET.get('Stype')
    if segment_type == "1":
        showFiles = Upload_File.objects.filter(SType_id="1")
    elif segment_type == "2":
        showFiles = Upload_File.objects.filter(SType_id="2")
    elif segment_type == "3":
        showFiles = Upload_File.objects.filter(SType_id="3")
    elif segment_type == "4":
        showFiles = Upload_File.objects.filter(SType_id="4")
    elif segment_type == "5":
        showFiles = Upload_File.objects.filter(SType_id="5")
    elif segment_type == "6":
        showFiles = Upload_File.objects.filter(SType_id="6")
    elif segment_type == "7":
        showFiles = Upload_File.objects.filter(SType_id="7")
    elif segment_type == "8":
        showFiles = Upload_File.objects.filter(SType_id="8")
    elif segment_type == "9":
        showFiles = Upload_File.objects.filter(SType_id="9")
    elif segment_type == "10":
        showFiles = Upload_File.objects.filter(SType_id="10")    
    elif segment_type == "11":
        showFiles = Upload_File.objects.filter(SType_id="11")
    elif segment_type == "12":
        showFiles = Upload_File.objects.filter(SType_id="12")
    elif segment_type == "13":
        showFiles = Upload_File.objects.filter(SType_id="13")
    elif segment_type == "14":
        showFiles = Upload_File.objects.filter(SType_id="14")
    else:
        showFiles= Upload_File.objects.all()
    return render(request,'Upload_File/showUploadfile.html',{"form":form,'showFiles':showFiles,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
    'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
    'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
    'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
    'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
    
    
def uploadFile(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    alluser = Login.objects.order_by("UID")
    new_fid = Upload_File.objects.order_by("FID").values_list("FID", flat=True).last()
    GID = User_Group.objects.filter(GID=check_UserGroup).values_list('GID',flat=True)
    MID = Login.objects.filter(MID_id=check_member).values_list('MID_id',flat=True)
    # stype = SegmentType.objects.get(SType='A')
    # print(stype)
    member = memberInfo.objects.all()
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    Month = datetime.datetime.now()
    Year = datetime.datetime.now()
    
    period= Upload_File.objects.filter(MID_id=check_member).values_list('period', flat=True).exists()
    print(period)
    
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploadfile = form.cleaned_data['fileUpload']
            stype = form.cleaned_data['SType']
            utype = form.cleaned_data['UType']
            print(utype)
            print(stype)
            print(check_member)
            if stype.nameL == "ສຳລັບຜູ້ກູ້ຢືມທີ່ເປັນວິສາຫະກິດ":
                Stype = stype
                filename = uploadfile.name
                if filename[14:16]+'-'+filename[16:20] in Upload_File.objects.filter(MID_id=check_member).values_list('period', flat=True):
                    messages.error(request, "ທ່ານໄດ້ນຳສົ່ງຂໍ້ມູນຂອງເດືອນນີ້ແລ້ວ ^_^")
                    form = uploadForm()
                    return HttpResponseRedirect('/uploadFile','Upload_File/uploadFile.html',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
                    'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
                    'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage,         'report_manage':report_manage, 
                    'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report,  'check_UserGroup':check_UserGroup,
                    'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
                else:
                    if filename.endswith('.json'):
                        print('file is .json')
                        attach = FileSystemStorage('media/fileUploads')
                        Files = attach.save(uploadfile.name, uploadfile)
                        #calculation size of file
                        size = uploadfile.size
                        if size < 512000:
                            size = size / 1024.0
                            ext = "KB"
                        elif size < 4194304000:
                            size = size / 1048576.0
                            ext = "MB"    
                        else:
                            size = size / 107341824.0           
                            ext = "MB"   
                            # return '%s %s' %(str(round(size, 2)), ext)
                            
                    if new_fid == 0 or new_fid ==  None:
                        new_fid = 1
                    else:
                        new_fid= new_fid+1
                    new_file = Upload_File(
                        FID = new_fid,
                        MID = memberInfo.objects.get(id=MID[0]),
                        GID= User_Group.objects.get(GID=GID[0]),
                        SType = Stype,
                        fileName = uploadfile,
                        fileUpload = Files,
                        fileSize = '%s %s' %(str(round(size, 2)), ext),
                        path = attach.url("/fileUploads/"+Files),
                        insertDate = datetime.now(),
                        updateDate = datetime.now(),
                        period = filename[14:16]+'-'+filename[16:20],
                        status = "Test",
                        status_upload ="Test",
                        FileType = ".json",
                        UType = utype
                        )        
                    new_file.save()
                
                    path = 'media/fileUploads/'
                    with open(path+str(uploadfile),'r', encoding="utf-8") as data_file:
                        json_data = json.loads(data_file.read())
                                #json_data = form.cleaned_data['fileUpload']
                                #data = json_data
                        list_data =[]
                        for data in json_data:
                            list_data.append((data['lcicID'], data['com_enterprise_code'], data['segmentType'], data['lon_sys_id'], data['bnk_code'], data['customer_id'], data['branch_id'], data['loan_id'], data['lon_open_date'], data['lon_exp_date'], data['lon_ext_date'], data['lon_int_rate'], data['lon_purpose_code'], data['lon_credit_line'], data['lon_currency_code'], data['lon_outstanding_balance'], data['lon_account_no'], data['lon_no_days_slow'], data['lon_class'], data['lon_type'], data['lon_term'], data['lon_status'], data['lon_insert_date'], data['lon_update_date'], data['lon_applied_date'], data['is_disputed']))
                                
                        conn = psycopg2.connect(host="localhost", database="lcicwebsitedb", user="postgres", password="Lcic@123")
                        cur = conn.cursor()
                        
                        query = 'insert into "lcicHome_b1"("lcicID", "com_enterprise_code", "segmentType", "bnk_code", "customer_id", "branch_id", "lon_sys_id", "loan_id", "lon_open_date", "lon_exp_date", "lon_ext_date", "lon_int_rate", "lon_purpose_code", "lon_credit_line", "lon_currency_code", "lon_outstanding_balance", "lon_account_no", "lon_no_days_slow", "lon_class", "lon_type", "lon_term", "lon_status", "lon_insert_date", "lon_update_date", "lon_applied_date", "is_disputed") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                        json_data = list_data
                        try:
                            cur.executemany(query,json_data)
                            conn.commit()
                            print("Data stored to database", json_data)
                        except conn.DatabaseError as message:
                            if conn:
                                conn.rollback()
                                print("Error occured", message)
                        finally:
                            if cur:
                                cur.close()
                            if conn:
                                conn.close()
                                    
                        messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
                        return HttpResponseRedirect('/uploadFile',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
                        'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
                        'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
                        'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
                        'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})    
            elif  stype.nameL == "ລາຍລະອຽດຂອງເງິນກູ້ຢືມ":
                    Stype = stype
                    print(stype)
                    filename = uploadfile.name
                    if filename.endswith('.json'):
                        print('file is .json')
                        attach = FileSystemStorage('media/fileUploads')
                        Files = attach.save(uploadfile.name, uploadfile)
                        #calculation size of file
                        size = uploadfile.size
                        if size < 512000:
                            size = size / 1024.0
                            ext = "KB"
                        elif size < 4194304000:
                            size = size / 1048576.0
                            ext = "MB"    
                        else:
                            size = size / 107341824.0           
                            ext = "MB"   
                            # return '%s %s' %(str(round(size, 2)), ext)
                            
                        if new_fid == 0 or new_fid ==  None:
                            new_fid = 1
                        else:
                            new_fid= new_fid+1
                        new_file = Upload_File(
                        FID = new_fid,
                        MID = memberInfo.objects.get(id=MID[0]),
                        GID= User_Group.objects.get(GID=GID[0]),
                        SType = Stype,
                        fileName = uploadfile,
                        fileUpload = Files,
                        fileSize = '%s %s' %(str(round(size, 2)), ext),
                        path = attach.url("/fileUploads/"+Files),
                        insertDate = datetime.now(),
                        updateDate = datetime.now(),
                        period = Month.strftime("%m")+"-"+Year.strftime("%Y"),
                        status = "Test",
                        status_upload ="Test",
                        FileType = ".json",
                        UType = utype
                        )        
                        new_file.save()
                        
                        path = 'media/fileUploads/'
                        with open(path+str(uploadfile),'r', encoding="utf-8") as data_file:
                            json_data = json.loads(data_file.read())
                                    # json_data = form.cleaned_data['fileUpload']
                                    #data = json_data
                        list_data =[]
                        for data in json_data:
                            list_data.append((data['lcicID'], data['com_enterprise_code'], data['segmentType'],  data['customer_id'], data['branch_id'], data['loan_id'], data['lon_open_date'], data['lon_exp_date'], data['lon_ext_date'], data['lon_int_rate'], data['lon_purpose_code'], data['lon_credit_line'], data['lon_currency_code'], data['lon_outstanding_balance'], data['lon_account_no'], data['lon_no_days_slow'], data['lon_class'], data['lon_type'], data['lon_term'], data['lon_status'], data['lon_update_date']))
                                    
                        conn = psycopg2.connect(host="localhost", database="lcicwebsitedb", user="postgres", password="Lcic@123")
                        cur = conn.cursor()
                        query = 'insert into "lcicHome_b1"("lcicID", "com_enterprise_code", "segmentType", "customer_id", "branch_id", "loan_id", "lon_open_date", "lon_exp_date", "lon_ext_date", "lon_int_rate", "lon_purpose_code", "lon_credit_line", "lon_currency_code", "lon_outstanding_balance", "lon_account_no", "lon_no_days_slow", "lon_class", "lon_type", "lon_term", "lon_status", "lon_update_date") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                        json_data = list_data
                        try:
                            cur.executemany(query,json_data)
                            conn.commit()
                            print("Data stored to database", json_data)
                        except conn.DatabaseError as message:
                            if conn:
                                conn.rollback()
                                print("Error occured", message)
                        finally:
                            if cur:
                                cur.close()
                            if conn:
                                conn.close()
                                        
                        messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
                        return HttpResponseRedirect('/uploadFile',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
                                                'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
                                                'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
                                                'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
                                                'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
                    else:
                        messages.error(request,"ກວດສອບປະເພດຂໍ້ມູນທີ່ຕ້ອງການນຳສົ່ງຄືນອີກຄັ້ງ TT")
                        return HttpResponseRedirect('/uploadFile',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
                                                'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
                                                'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
                                                'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
                                                'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
                
                # elif stype == "6":
                #     stype =6
                #     filename = uploadfile.name
                #     if filename.endswith('.json'):
                #         print('file is .json')
                #         attach = FileSystemStorage('media/fileUploads')
                #         Files = attach.save(uploadfile.name, uploadfile)
                #         #calculation size of file
                #         size = uploadfile.size
                #         if size < 512000:
                #             size = size / 1024.0
                #             ext = "KB"
                #         elif size < 4194304000:
                #             size = size / 1048576.0
                #             ext = "MB"    
                #         else:
                #             size = size / 107341824.0           
                #             ext = "MB"   
                #             # return '%s %s' %(str(round(size, 2)), ext)
                            
                #     if new_fid == 0 or new_fid ==  None:
                #         new_fid = 1
                #     else:
                #         new_fid= new_fid+1
                #     new_file = Upload_File(
                #     FID = new_fid,
                #     MID = memberInfo.objects.get(id=MID[0]),
                #     GID= User_Group.objects.get(GID=GID[0]),
                #     SType = stype,
                #     fileName = uploadfile,
                #     fileUpload = Files,
                #     fileSize = '%s %s' %(str(round(size, 2)), ext),
                #     path = attach.url("/fileUploads/"+Files),
                #     insertDate = datetime.now(),
                #     updateDate = datetime.now(),
                #     period = Month.strftime("%m")+"-"+Year.strftime("%Y"),
                #     status = "Test",
                #     status_upload ="Test",
                #     uploadType = ".json"
                #     )        
                #     new_file.save()
                #                 # BASE_URL = 'http://127.0.0.1:8000/'
                #                 # ENDPOINT = 'api/'
                #                 # json_data = requests.get(BASE_URL+ENDPOINT)
                #                 # data = json_data.json()
                #                 # messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
                #     path = 'C:/Users/Dell/Documents/VS Code Project/Website LCIC/Backup15.11.2021/lcicMain/media/uploadFiles/'
                #     with open(path+str(uploadfile),'r', encoding="utf-8") as data_file:
                #         json_data = json.loads(data_file.read())
                #                 # json_data = form.cleaned_data['fileUpload']
                #                 #data = json_data
                #     list_data =[]
                #     for water_data in json_data:
                #         list_data.append((water_data['lcicID'], water_data['com_enterprise_code'], water_data['segmentType'],  water_data['customer_id'], water_data['branch_id'], water_data['loan_id'], water_data['lon_open_date'], water_data['lon_exp_date'], water_data['lon_ext_date'], water_data['lon_int_rate'], water_data['lon_purpose_code'], water_data['lon_credit_line'], water_data['lon_currency_code'], water_data['lon_outstanding_balance'], water_data['lon_account_no'], water_data['lon_no_days_slow'], water_data['lon_class'], water_data['lon_type'], water_data['lon_term'], water_data['lon_status'], water_data['lon_update_date']))
                                
                #     conn = psycopg2.connect(host="localhost", database="LCICWebsiteDB", user="postgres", password="Lcic@123")
                #     cur = conn.cursor()
                #     query = 'insert into "lcicHome_a2"("lcicID", "com_enterprise_code", "segmentType", "customer_id", "branch_id", "loan_id", "lon_open_date", "lon_exp_date", "NULLIF(lon_ext_date)", "lon_int_rate", "lon_purpose_code", "lon_credit_line", "lon_currency_code", "lon_outstanding_balance", "lon_account_no", "lon_no_days_slow", "lon_class", "lon_type", "lon_term", "lon_status", "lon_update_date") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                #     json_data = list_data
                #     try:
                #         cur.executemany(query,json_data)
                #         conn.commit()
                #         print("Data stored to database", json_data)
                #     except conn.DatabaseError as message:
                #         if conn:
                #             conn.rollback()
                #             print("Error occured", message)
                #     finally:
                #         if cur:
                #             cur.close()
                #         if conn:
                #             conn.close()
                                    
                #         messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
                #         return HttpResponseRedirect('/upload_file',{"form":form,'u':u,'showFiles':showFiles,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
                #                             'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
                #                             'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
                #                             'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
                #                             'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})

            else:
                return render(request,'Upload_File/uploadFile.html',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang, 
                'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
                'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
                'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
                'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
    else:
        form = uploadForm()
        return render(request,'Upload_File/uploadFile.html',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'Search_Menu':Search_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
            
# def import_facility_from_file(self):
#     Change_Lang= request.GET.get('Lang')
#     Lang='la'
#     if Change_Lang == "la" and Lang == "la":
#         Lang ='la'
#     elif Change_Lang == "en" and Lang == "la":
#         Lang = 'en'
#     elif Change_Lang == "en" and Lang == "la":
#         Lang = 'la'
#     alluser = Login.objects.order_by("UID")
#     new_fid = Upload_File.objects.order_by("FID").values_list("FID", flat=True).last()
#     GID = User_Group.objects.filter(GID=check_UserGroup).values_list('GID',flat=True)
#     MID = Login.objects.filter(MID_id=check_member).values_list('MID_id',flat=True)
#     member = memberInfo.objects.all()
#     H_ofl = H_Lang.objects.filter(id=26)
#     H_loca = H_Lang.objects.filter(id=27)
#     H_cap = H_Lang.objects.filter(id=28)
#     Month = datetime.now()
#     Year = datetime.now()
#     # print(Month.month)
#     # print(Year.year)
#     if request.method == 'POST':
#         form = uploadForm(request.POST, request.FILES)
#         # uploadfile = request.FILES.get('fileUpload')
#         # split_tup = os.path.splitext(upload_file)
#         # filetype = split_tup[1]
#         # print(uploadfile)
#         # uploadfile = form.cleaned_data['fileUpload']
#         # filetype = pathlib.Path(uploadfile).suffix
#         # print(filetype)
#         if form.is_valid():
#             # try :
#                 uploadfile = form.cleaned_data['fileUpload']
#                 filename = uploadfile.name
#                 if filename.endswith('.json'):
#                     print('file is .json')
#                     attach = FileSystemStorage('media/fileUploads')
#                     Files = attach.save(uploadfile.name, uploadfile)
#                     #calculation size of file
#                     size = uploadfile.size
#                     if size < 512000:
#                         size = size / 1024.0
#                         ext = "KB"
#                     elif size < 4194304000:
#                         size = size / 1048576.0
#                         ext = "MB"    
#                     else:
#                         size = size / 107341824.0           
#                         ext = "MB"   
#                         # return '%s %s' %(str(round(size, 2)), ext)
                    
#                     if new_fid == 0 or new_fid ==  None:
#                         new_fid =1
#                         new_file = Upload_File(
#                         FID = new_fid,
#                         MID = memberInfo.objects.get(id=MID[0]),
#                         GID= User_Group.objects.get(GID=GID[0]),
#                         fileName = uploadfile,
#                         fileUpload = Files,
#                         fileSize = '%s %s' %(str(round(size, 2)), ext),
#                         insertDate = datetime.now(),
#                         period = Month.strftime("%m")+"-"+Year.strftime("%Y"),
#                         status = "Test",
#                         status_upload ="Test"
#                         )
#                         new_file.save()
#                         # messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
#                         json_data = form.cleaned_data['fileUpload']
#                         data = json_data.json()
#                         list_data =[]
#                         for edata in data:
#                             list_data.append((edata['ID'], edata['CustomerID'], edata['CompanyName'], edata['Name'], edata['Surname'], edata['NationalID'], edata['Passport'], edata['Address'], edata['districtInfo'], edata['provInfo'], edata['Tel'], edata['Email'], edata['ConsumerType'], edata['RegisDate']))
#                         conn = psycopg2.connect(host="localhost", database="LCICWebsiteDB", user="postgres", password="Lcic@123")
#                         cur = conn.cursor()
#                         query = 'INSERT INTO CustomerWater (ID, CustomerID, CompanyName, Name, Surname, NationalID, Passport, Address, districtInfo, provInfo, Tel, Email, ConsumerType, RegisDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
#                         data = list_data
#                         try:
#                             cur.executemany(query, data)
#                             conn.commit()
#                             print("Data stored to database")
#                         except conn.DatabaseError as message:
#                             if conn:
#                                 conn.rollback()
#                                 print("Error occured", message)
#                         finally:
#                             if cur:
#                                 cur.close()
#                             if conn:
#                                 conn.close()
#                         messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
#                     elif new_fid >= 1 : 
#                         new_file = Upload_File(
#                         FID = new_fid+1,
#                         MID = memberInfo.objects.get(id=MID[0]),
#                         GID= User_Group.objects.get(GID=GID[0]),
#                         fileName = uploadfile,
#                         fileUpload = Files,
#                         fileSize = '%s %s' %(str(round(size, 2)), ext),
#                         insertDate = datetime.now(),
#                         period = Month.strftime("%m")+"-"+Year.strftime("%Y"),
#                         status = "Test",
#                         status_upload ="Test"
#                         )
                        
#                         new_file.save()
#                         # BASE_URL = 'http://127.0.0.1:8000/'
#                         # ENDPOINT = 'upload_file/'
#                         # json_data = request.get(BASE_URL+ENDPOINT)
#                         # # json_data = form.cleaned_data['fileUpload']
#                         # data = json_data.json()
#                         # list_data =[]
#                         # for edata in data:
#                         #     list_data.append((edata['ID'], edata['CustomerID'], edata['CompanyName'], edata['Name'], edata['Surname'], edata['NationalID'], edata['Passport'], edata['Address'], edata['districtInfo'], edata['provInfo'], edata['Tel'], edata['Email'], edata['ConsumerType'], edata['RegisDate']))
#                         # conn = psycopg2.connect(host="localhost", database="LCICWebsiteDB", user="postgres", password="Lcic@123")
#                         # cur = conn.cursor()
#                         # query = 'INSERT INTO lcicHome_CustomerWater (ID, CustomerID, CompanyName, Name, Surname, NationalID, Passport, Address, districtInfo, provInfo, Tel, Email, ConsumerType, RegisDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
#                         # data = list_data
#                         # try:
#                         #     cur.executemany(query, data)
#                         #     conn.commit()
#                         #     print("Data stored to database")
#                         # except conn.DatabaseError as message:
#                         #     if conn:
#                         #         conn.rollback()
#                         #         print("Error occured", message)
#                         # finally:
#                         #     if cur:
#                         #         cur.close()
#                         #     if conn:
#                         #         conn.close()
#                         path = 'C:/Users/Dell/Documents/VS Code Project/Website LCIC/Backup15.11.2021/lcicMain/media/uploadFiles/info_example2.json'
#                         with open(path, encoding="utf8") as data_file:
#                             json_data = json.loads(data_file.read())
#                             for Water_data in json_data:
#                                 ID = Water_data.get('ID',None),
#                                 CustomerID = Water_data.get('CustomerID',None),
#                                 CompanyName = Water_data.get('CompanyName',None),
#                                 Name = Water_data.get('Name',None),
#                                 Surname = Water_data.get('Surname',None),
#                                 NationalID = Water_data.get('NationalID',None),
#                                 Passport = Water_data.get('Passport',None),
#                                 Address = Water_data.get('Address',None),
#                                 districtInfo = Water_data.get('districtInfo',None),
#                                 provInfo = Water_data.get('provInfo',None),
#                                 Tel = Water_data.get('Tel',None),
#                                 Email = Water_data.get('Email',None),
#                                 ConsumerType = Water_data.get('ConsumerType',None),
#                                 RegisDate = Water_data.get('RegisDate',None)
#                                 try:
#                                     CustomerWater, created = CustomerWater.objects.get_or_create(
#                                         ID = ID,
#                                         CustomerID = CustomerID,
#                                         CompanyName = CompanyName,
#                                         Name = Name,
#                                         Surname = Surname,
#                                         NationalID = NationalID,
#                                         Passport = Passport,
#                                         Address = Address,
#                                         districtInfo = districtInfo,
#                                         provInfo = provInfo,
#                                         Tel = Tel,
#                                         Email = Email,
#                                         ConsumerType = ConsumerType,
#                                         RegisDate = RegisDate,
#                                     )
#                                     if created:
#                                         CustomerWater.save()
#                                         display_format = "\CustomerWater, {}, has been saved."
#                                         print(display_format.format(CustomerWater))
#                                 except Exception as ex:
#                                     print(str(ex))
#                                     msg="\n\nSomething went wrong saving this CustomerWater: {}\n{}".format(Name, str(ex))
#                                     print(msg)
#                                 messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
#                                 return HttpResponseRedirect('/upload_file',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
#                                 'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
#                                 'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
#                                 'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
#                                 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
                            
                        
#                 if filename.endswith('.txt'):
#                     print('file is .txt')
#                     attach = FileSystemStorage('media/fileUploads')
#                     Files = attach.save(uploadfile.name, uploadfile)
            
#                     #calculation size of file
#                     size = uploadfile.size
#                     if size < 512000:
#                         size = size / 1024.0
#                         ext = "KB"
#                     elif size < 4194304000:
#                         size = size / 1048576.0
#                         ext = "MB"    
#                     else:
#                         size = size / 107341824.0           
#                         ext = "MB"   
#                         # return '%s %s' %(str(round(size, 2)), ext)
                    
#                     if new_fid == 0 or new_fid ==  None:
#                         new_fid =1
#                         new_file = Upload_File(
#                         FID = new_fid,
#                         MID = memberInfo.objects.get(id=MID[0]),
#                         GID= User_Group.objects.get(GID=GID[0]),
#                         fileName = uploadfile,
#                         fileUpload = Files,
#                         fileSize = '%s %s' %(str(round(size, 2)), ext),
#                         insertDate = datetime.now(),
#                         period = Month.strftime("%m")+"-"+Year.strftime("%Y"),
#                         status = "Test",
#                         status_upload ="Test"
#                         )
#                         new_file.save()
#                         messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
#                         # with open(uploadfile, encoding='utf-8') as data_file:
#                         #     json_data = json.loads(data_file.read())
#                         #     for Water_data in json_data:
#                         #         water = CustomerWater.create(Water_data)
#                         # messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
#                     elif new_fid >= 1 : 
#                         new_file = Upload_File(
#                         FID = new_fid+1,
#                         MID = memberInfo.objects.get(id=MID[0]),
#                         GID= User_Group.objects.get(GID=GID[0]),
#                         fileName = uploadfile,
#                         fileUpload = Files,
#                         fileSize = '%s %s' %(str(round(size, 2)), ext),
#                         insertDate = datetime.now(),
#                         period = Month.strftime("%m")+"-"+Year.strftime("%Y"),
#                         status = "Test",
#                         status_upload ="Test"
#                         )
                        
#                         new_file.save()
#                         # with open(uploadfile, encoding='utf-8') as data_file:
#                         #     json_data = json.loads(data_file.read())
#                         #     for Water_data in json_data:
#                         #         water = CustomerWater.create(Water_data)
#                         messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
#                 if filename.endswith('.xml'):
#                     print('file is .xml')
#                     attach = FileSystemStorage('media/fileUploads')
#                     Files = attach.save(uploadfile.name, uploadfile)
            
#                     #calculation size of file
#                     size = uploadfile.size
#                     if size < 512000:
#                         size = size / 1024.0
#                         ext = "KB"
#                     elif size < 4194304000:
#                         size = size / 1048576.0
#                         ext = "MB"    
#                     else:
#                         size = size / 107341824.0           
#                         ext = "MB"   
#                         # return '%s %s' %(str(round(size, 2)), ext)
                    
#                     if new_fid == 0 or new_fid ==  None:
#                         new_fid =1
#                         new_file = Upload_File(
#                         FID = new_fid,
#                         MID = memberInfo.objects.get(id=MID[0]),
#                         GID= User_Group.objects.get(GID=GID[0]),
#                         fileName = uploadfile,
#                         fileUpload = Files,
#                         fileSize = '%s %s' %(str(round(size, 2)), ext),
#                         insertDate = datetime.now(),
#                         period = Month.strftime("%m")+"-"+Year.strftime("%Y"),
#                         status = "Test",
#                         status_upload ="Test"
#                         )
#                         new_file.save()
#                         messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
#                         # with open(uploadfile, encoding='utf-8') as data_file:
#                         #     json_data = json.loads(data_file.read())
#                         #     for Water_data in json_data:
#                         #         water = CustomerWater.create(Water_data)
#                         # messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
#                     elif new_fid >= 1 : 
#                         new_file = Upload_File(
#                         FID = new_fid+1,
#                         MID = memberInfo.objects.get(id=MID[0]),
#                         GID= User_Group.objects.get(GID=GID[0]),
#                         fileName = uploadfile,
#                         fileUpload = Files,
#                         fileSize = '%s %s' %(str(round(size, 2)), ext),
#                         insertDate = datetime.now(),
#                         period = Month.strftime("%m")+"-"+Year.strftime("%Y"),
#                         status = "Test",
#                         status_upload ="Test"
#                         )
                        
#                         new_file.save()
#                         # with open(uploadfile, encoding='utf-8') as data_file:
#                         #     json_data = json.loads(data_file.read())
#                         #     for Water_data in json_data:
#                         #         water = CustomerWater.create(Water_data)
#                         messages.success(request, "ສຳເລັດການນຳສົ່ງຂໍ້ມູນ :3")
#                 #uploadfile = form.cleaned_data['fileUpload']
#                 # filetype = pathlib.Path(uploadfile).suffix
#                 # split_tup = os.path.splitext(upload_file)
#                 # filetype = split_tup[1]
#                 # if filetype == ".json":
#                 #     print(filetype)
                
#                 # else:
#                 #     messages.error(request, "ກວດສອບໄຟຣ໌ທີ່ຕ້ອງການອັບໂຫຼດຄືນອີກຄັ້ງ")
#             # except :
#             #     messages.error(request, "ກວດສອບໃຫ້ແນ່ໃຈວ່າທ່ານເລືອກໄຟຣ໌ສຳລັບການນຳສົ່ງຂໍ້ມູນແລ້ວ ຫຼື ຍັງ?")
#             # return HttpResponseRedirect('/upload_file',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
#             # 'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
#             # 'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
#             # 'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
#             # 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
#             # print(uploadfile.name)
#             # print(uploadfile.size)
#             # print(GID[0])
#             # print(MID[0])
#             # insertDate = datetime.now()
#         else:
#             return render(request,'Upload_File/upload_file.html',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
#             'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
#             'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
#             'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
#             'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
#     else:
#         form = uploadForm()
#         return render(request,'Upload_File/upload_file.html',{"form":form,'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
#         'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
#         'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'report_manage':report_manage, 
#         'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
#         'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'alluser':alluser, 'member':member})
    
# def handle(self, *args, **options):
        # """
        # Call the function to import data
        # """
        # self.import_facility_from_file()
        
        
        
def search(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    
    # print user_id jark login
    check_UserGroup = request.session.get('check_UserGroup', None)
    if check_UserGroup is not None:
        print("user_id from loginpage : ",check_UserGroup)
    else:
        print("error")
    # print(check_UserGroup,"<-- My user_id")
    return render(request, 'Search/search.html',{'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'Search_Menu':Search_Menu,'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap,})
    
    
def searchIndividual(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    
    form= searchIndividualForm(request.POST or None)
    if form.is_valid():
        ind_lao_name = form.cleaned_data['ind_lao_name']
        ind_lao_surname = form.cleaned_data['ind_lao_surname']
        ind_name = form.cleaned_data['ind_name']
        ind_surname = form.cleaned_data['ind_surname']
        customerid = form.cleaned_data['customerid']
        global lao_name, lao_surname, name, surname, id
    
        lao_name=ind_lao_name
        lao_surname=ind_lao_surname
        name=ind_name
        surname=ind_surname
        id=customerid
     
        # ind_lao_surname = Customer_Info_IND.objects.filter(ind_lao_surname__contains = form.cleaned_data['ind_lao_surname'])
        # ind_name = Customer_Info_IND.objects.filter(ind_name__contains= form.cleaned_data['ind_name'])
        # ind_surname = Customer_Info_IND.objects.filter(ind_surname__contains=form.cleaned_data['ind_surname'])
        # customerid = Customer_Info_IND.objects.filter(customerid__contains=form.cleaned_data['customerid'])
            
            
        return render(request,'Search/searchConfirm.html',{'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
            'Main_Menu':Main_Menu,'form':form, 'lao_name':lao_name,
            'lao_surname':lao_surname,
            'name':name,
            'surname':surname,
            'id':id,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
            'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'Search_Menu':Search_Menu,'report_manage':report_manage, 
            'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
            'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap,})    
    
    
    return render(request, 'Search/searchIndividual.html',{'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
                'Main_Menu':Main_Menu,'form':form, 'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
                'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'Search_Menu':Search_Menu,'report_manage':report_manage, 
                'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
                'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap,})
    
def function_confirm(request):
    return render(request, 'Search/searchListconfirm')

def searchEnterpise(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    
    form = SearchEnterpise(request.GET)
    # test_UID = Login.objects.filter(UID=2)
    check_UserGroup = request.session.get('check_UserGroup', None)
    
    if check_UserGroup is not None:
        print("kep log jark user_id login : ",check_UserGroup)
    else:
        print("error")
        
    if form.is_valid():
        # Process the form data
        enterprise_id = form.cleaned_data.get('enterprise_id')
        lcic_id = form.cleaned_data.get('lcic_id')
        
        try:
            enterprise_object = EnterpriseInfo.objects.get(EnterpriseID=enterprise_id, LCICID=lcic_id)
            invs_name = InvestorInfo.objects.get(EnterpriseID=enterprise_id)
            # creditType = H_productInfo.objects.filter(code='p002').values()
            # for i in creditType:
            #     print("test nameL in ProductInfo ", i['nameL'])
            creditType = H_productInfo.objects.get(code='p002')
            sys_user = Login.objects.get(UID=check_UserGroup)
            print("Login: UID -->", sys_user)
            # user_object = Login.objects.get(UID=check_UserGroup)
            # print("User_id_check in searchPage",check_UserGroup)
            # print("======> Check_UserGroup", check_UserGroup)
            print("=====> En_Objects ", invs_name.EnterpriseID)
            print("=====> LCIC Objects", enterprise_object.LCICID)
            # print("=====> CreditType",  i['nameL'])
            # kep bank code jark user_member 
            print("=====> bnk_code", sys_user.MID)
            print("=====> branch(010)",)
            print("=====> sys_user", sys_user)
            print("=====> CreditType",  creditType)
            print("=====> inquiry_date", )
            print("=====> inquiry_month", )
            print("=====> inquiry_time", )
            print("=====> com_tel", invs_name.investorMobile )
            print("=====> com_location", )
            print("=====> rec_loan_amount_currency",  )
            print("=====> rec_loan_amoount",  )
            print("=====> rec_loan_purpose",  )
            print("=====> rec_enquiry_type",  )
            # kep jark phu thuek khon ha 
            print("=====> cusType", )
    
            # Search Log for Enterprise
            search_log_insert = searchLog.objects.create(enterprise_ID=invs_name.EnterpriseID, LCIC_ID=enterprise_object.LCICID,
            bnk_code = (sys_user.MID).id,
            cus_ID=sys_user.UID,
            credit_type=creditType.code,
            com_tel=invs_name.investorMobile)
            
            print(search_log_insert)

            # print*("====> invs_name", invs_name)
            context = {'object': enterprise_object, 'invs_name': invs_name,
                       
                       }

            return render(request, 'Search/searchList.html', context)

        except ObjectDoesNotExist:
            messages.error(request, "ບໍ່ພົບຂໍ້ມູນ ກະລຸນາກວດເບິ່ງລະຫັດອີກຄັ້ງ!")
            
            print("Object does not exist")
            
            # Handle the case when the object is not found, maybe display an error message or redirect to a different page.
    # context = {
    #     'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
    #         'Main_Menu':Main_Menu,'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
    #         'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'Search_Menu':Search_Menu,'report_manage':report_manage, 
    #         'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
    #         'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap,
    #     }
    # return render(request, 'Search/searchEnterpise', context)

    # If form is not valid or if the object is not found, render the original form page with the results
    results = EnterpriseInfo.objects.all()
    context = {'results': results, 'form': form, 'check_UserGroup':check_UserGroup,}
    return render(request, 'Search/searchEnterpise.html', context)
    
   
def searchConfirm(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    form= searchIndividualForm(request.POST or None)
    if form.is_valid():
        ind_lao_name = form.cleaned_data['ind_lao_name']
        ind_lao_surname = form.cleaned_data['ind_lao_surname']
        ind_name = form.cleaned_data['ind_name']
        ind_surname = form.cleaned_data['ind_surname']
        customerid = form.cleaned_data['customerid']
        
        lao_name=ind_lao_name
        lao_surname=ind_lao_surname
        name=ind_name
        surname=ind_surname
        id=customerid
        
        context={
        'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
                'Main_Menu':Main_Menu, 'Management_Menu':Management_Menu,'form':form,
                'lao_name':lao_name,
                'lao_surname':lao_surname,
                'name':name,
                'surname':surname,
                'id':id, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
                'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'Search_Menu':Search_Menu,'report_manage':report_manage, 
                'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
                'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap,
        }
        return render(request,'Search/searchConfirm.html',context)
    
    context={
        'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
                'Main_Menu':Main_Menu, 'Management_Menu':Management_Menu,'form':form,
                'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
                'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'Search_Menu':Search_Menu,'report_manage':report_manage, 
                'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
                'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap,
        }
    return render(request,'Search/searchIndividual.html',context)

def searchList(request,object):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    
    next = request.POST.get('btn_detail')
    if next:
        try:
            url = reverse('searchListfee')
            return render(request, 'Search/searchListfee.html',{'url':url, 'check_UserGroup':check_UserGroup,})
        except:
            pass
    return render(request, 'Search/searchList.html',{'url':url}) 

def searchListfee(request, object_id):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)
    
    check_UserGroup = request.session.get('check_UserGroup', None)
    # mydata = request.GET.get(data)
    print("=====>",object_id)
    charge_amount = H_productInfo.objects.get(code='p002')
    sys_user = Login.objects.get(UID=check_UserGroup)
    reportType = productInfo.objects.get(id='2')
    # bank_code = memberInfo.objects.get()
    print("Bank_code : ", sys_user.MID )

    fee_data = EnterpriseInfo.objects.filter(
            EnterpriseID=object_id)
    
    listfee = EnterpriseInfo.objects.get(EnterpriseID=object_id)
    
    fee_info = H_productInfo.objects.get(code='p002')
    
    print(fee_info)
    print("!====ListFee",listfee.LCICID)
    
    print("Mydata==>", fee_data)
    return render(request, 'Search/searchListfee.html', {'object_id':object_id, 'fee_data':fee_data, 'listfee':listfee, 'fee_info':fee_info})
    # return render(request, 'Search/searchListfee.html',{'u':u,'uname':uname,'code':code,'ugroup':ugroup,'L':L,'Lang':Lang,
    #             'Main_Menu':Main_Menu, 'Management_Menu':Management_Menu, 'Report_Menu':Report_Menu, 'User_Menu':User_Menu, 
    #             'Service_Menu':Service_Menu,'cus_manage':cus_manage, 'mem_manage':mem_manage, 'Search_Menu':Search_Menu,'report_manage':report_manage, 
    #             'user_report':user_report, 'mem_report':mem_report, 'usesys_report':usesys_report, 'check_UserGroup':check_UserGroup,
    #             'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap,})

   
def searchListConfirm(request, object_id):
    Change_Lang = request.GET.get('Lang')
    Lang = 'la'
    
    if Change_Lang == "la" and Lang == "la":
        Lang = 'la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'

    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)

    report_data = EnterpriseInfo.objects.get(EnterpriseID=object_id)
    print("Myreport ===> Data",report_data)
    report_invs = InvestorInfo.objects.get(EnterpriseID=object_id)
    report_detail = H_productInfo.objects.get(code='p002')
    now = datetime.datetime.now()
    formatted_datetime = now.strftime("%d-%m-%Y %H:%M")
    
    check_UserGroup = request.session.get('check_UserGroup', None)
    # mydata = request.GET.get(data)
    print("=====>",object_id)
    charge_amount_data = H_productInfo.objects.get(code='p002')
    sys_user = Login.objects.get(UID=check_UserGroup)
    reportType = productInfo.objects.get(id='2')
    # bank_code = memberInfo.objects.get()
    print("Bank_code : ", sys_user.MID )
    fee_data = EnterpriseInfo.objects.get(EnterpriseID=object_id)
    listfee = EnterpriseInfo.objects.get(EnterpriseID=object_id)
    fee_info = H_productInfo.objects.get(code='p002')
    
    rec_charge = request.POST.get('object_id')

    print("=====> charge amount: ", charge_amount_data.price)
    # rec_charges = request_charge.objects.create(bnk_code = sys_user.MID,chg_amount = charge_amount.price,chg_code = charge_amount.code,status = 'InActive',insert_date = '',update_date = '',rtp_code = '1',chg_unit = 'LAK',user_sys_id = sys_user,LCIC_ID = fee_data
    #         )
    # print(rec_charges)
    
    print(fee_data, " : Data get from FeeData")
    
    rec_charge_insert = request_charge.objects.create(
        bnk_code = (sys_user.MID).id,
        chg_amount = charge_amount_data.price,
        chg_code = charge_amount_data.code,
        status = 'InActive',
        # insert_date = '',
        # update_date = '',
        rtp_code = '1',
        chg_unit = 'LAK',
        user_sys_id = sys_user.UID,
        LCIC_ID = fee_data.LCICID,
        cusType = ''
    )
    
    
    context ={
        'report_data':report_data,
        'report_invs':report_invs,
        'report_detail':report_detail,
        'report_date':now,
        'formatted_datetime':formatted_datetime,
        'object_id': object_id
    }

    return render(request, 'Search/searchListConfirm.html', context)
   
def progress (request, object_id):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Change_Lang == "la" and Lang == "la":
        Lang ='la'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'en'
    elif Change_Lang == "en" and Lang == "la":
        Lang = 'la'
    H_ofl = H_Lang.objects.filter(id=26)
    H_loca = H_Lang.objects.filter(id=27)
    H_cap = H_Lang.objects.filter(id=28)

    print(object_id)
    return render(request, 'Search/progress.html')
    
# Function Print Report
def render_pdf_view(request, object_id):
    # # -------------------------------- Method 1
    # template_path = 'Search/progress.html'
    # # context = {'object':object,'invs_name':invs_name}
    # context = {}
    # # Create a Django response object, and specify content_type as pdf
    # response = HttpResponse(content_type='application/pdf')
    
    # # Download Only -------
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    # # Display Only  -------
    # # response['Content-Disposition'] = 'filename="report.pdf"'
    # # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    # # find the template and render it.
    # template = get_template(template_path)
    # html = template.render(context)

    # # create a pdf
    # pisa_status = pisa.CreatePDF(
    #    html, dest=response, encoding='utf-8')
    # # if error then show some funny view
    # if pisa_status.err:
    #    return HttpResponse('We had some errors <pre>' + html + '</pre>')
    #     # return HttpResponse(f'Error creating PDF: {pisa_status.err}')
    # return response
     # ----------------------------------- Method 2
    
    # html_file = "searchListConfirm.html"
    
    # pdf_file = "report_fcr.pdf"

    # HTML(html_file).write_pdf(pdf_file)
    
    # pdf_document = fitz.open(pdf_file)
    
    # printer = fitz.open_printer() 
    # printer.print_document(pdf_document)  
    # printer.finish()  

    # # Close the PDF document
    # pdf_document.close()
         
    # ------------------------------------ Method 3
    template_path = 'Search/progress.html'
    
    # image_lcic = '../static/images/lcic_logo.png'
    # Replace context_data with the data you want to pass to the template
    print(object_id)
    report_data = EnterpriseInfo.objects.get(EnterpriseID=object_id)
    # print("Myreport ===> Data",report_data)
    # report_invs = InvestorInfo.objects.get(EnterpriseID=object_id)
    report_detail = H_productInfo.objects.get(code='p002')
    now = datetime.datetime.now()
    formatted_datetime = now.strftime("%d-%m-%Y %H:%M")  

    # Test Print Data
    print("====> Report Data ", report_data)

    context_data = {
        'image_path': 'D:\MY PROJECT\From Github\LCICEnterpriseWebsite\static\images\logo.png',
        'report_data':report_data,
        # 'report_invs':report_invs,
        'report_detail':report_detail,
        'report_date':now,
        'formatted_datetime':formatted_datetime
        
    }
    pdf = render_to_pdf(template_path, context_data)

    response = HttpResponse(pdf, content_type='application/pdf')
    # download files pdf 
    # response['Content-Disposition'] = 'filename="report_fcr.pdf"'

    return response

def render_to_pdf(template_path, context_dict):
    template = get_template(template_path)
    html_string = template.render(context_dict)
    
    font_file_path = os.path.abspath('../css/NotoSansLao.ttf')
    # font_file_path = os.path.abspath('D:/MY PROJECT/From Github/LCICEnterpriseWebsite/static/css/NotoSansLao.ttf')
 
    css_string = f'''

         @font-face {{
             font-family: "NotoSansLao";
             src: url("../css/NotoSansLao.ttf");
             src: url('{font_file_path}') format('truetype');
         }}
     
         body {{
             font-family: "Times New Roman", sans-serif;
         }}
    '''
    print(css_string)
    return HTML(string=html_string).write_pdf(stylesheets=[CSS(string=css_string)])   
 
def your_view(request):
    # Add your view logic here
    return render(request, 'Search/progress.html', {})

def tax(request):
    return render(request, 'Search/tax_invoice.html', {})

# gold API keys
def make_gapi_request():
    api_key = "goldapi-aylvjurlrhfyjm1-io"
    symbol = "XAU"
    curr = "USD"
    date = ""

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # result = response.text
        # print(result)
        
        result_json = response.json()
        
        price = result_json["price"]
        print(price)
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

result = make_gapi_request()    




# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SType
from .serializers import STypeSerializer

class STypeView(APIView):
    def get(self, request):
        stypes = SType.objects.all()
        serializer = STypeSerializer(stypes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User_Group
from .serializers import UserGroupSerializer

class UserGroupView(APIView):
    def get(self, request):
        user_groups = User_Group.objects.all()
        serializer = UserGroupSerializer(user_groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# views.py
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def login_view(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return JsonResponse({'token': str(refresh.access_token)})
    else:
        return JsonResponse({'error': 'ຂໍ້ມູນຜູ້ໃຊ້ງານບໍ່ຖືກຕອ້ງ'}, status=400)
    
    
    
    
from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from .models import User_Login
import json

@csrf_exempt
def login_view1(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')

        user = get_object_or_404(User_Login, UserName=username)
        
        if user.Password == password:
            # Generate token (you can use Django Rest Framework or any other method)
            token = "your_generated_token"  # Replace with actual token generation logic
            return JsonResponse({'token': token}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)


# login
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from lcicHome.models import User_Login  # Adjust the import according to your models



from lcicHome.models import EnterpriseInfo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Search(APIView):
    def post(self, request):
        LCICID = request.data.get('LCICID')
        EnterpriseID = request.data.get('EnterpriseID')
        
        if LCICID is not None and EnterpriseID is not None:
            # Perform search operation based on LCICID and EnterpriseID
            # Example logic:
            # result = perform_search(LCICID, EnterpriseID)
            # return Response({'data': result}, status=status.HTTP_200_OK)
            return Response({'message': 'Search performed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'LCICID and EnterpriseID are required fields'}, status=status.HTTP_400_BAD_REQUEST)

# get Enterprise
from rest_framework import viewsets
from .models import EnterpriseInfo
from .serializers import EnterpriseInfoSerializer

class EnterpriseInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EnterpriseInfo.objects.all()
    serializer_class = EnterpriseInfoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer_Info_IND
from .serializers import CustomerInfoINDSerializer

class CustomerInfoINDView(APIView):
    def get(self, request):
        customers = Customer_Info_IND.objects.all()
        serializer = CustomerInfoINDSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import bank_bnk
from .serializers import Bank_InfoINDSerializer
import logging
logger = logging.getLogger(__name__)

class Bank_InfoINDView(APIView):
    def get(self, request):
        try:
            bank = bank_bnk.objects.all()
            if not bank.exists():
                return Response({"detail": "No bank information found."}, status=status.HTTP_404_NOT_FOUND)
            
            logger.info(f"Retrieved {bank.count()} bank records.")
            serializer = Bank_InfoINDSerializer(bank, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            return Response({"detail": "An error occurred while retrieving bank information."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Login
from .serializers import LoginSerializer
from django.contrib.auth.hashers import make_password

class ManageUserView(APIView):

    def get(self, request, format=None):
        all_user = Login.objects.all()
        s_user = LoginSerializer(all_user, many=True)
        combined_data = {
            'all_user': s_user.data,
        }
        return Response(combined_data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(data['password']))
            return Response(LoginSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EnterpriseInfo
from .serializers import EnterpriseInfoSerializer

# Search Enterprise

# views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import EnterpriseInfo
# from .serializers import EnterpriseInfoSerializer

# class Search(APIView):
#     def post(self, request):
#         LCICID = request.data.get('LCICID')
#         EnterpriseID = request.data.get('EnterpriseID')
        
#         if LCICID is not None and EnterpriseID is not None:
#             # Perform search operation based on LCICID and EnterpriseID
#             results = EnterpriseInfo.objects.filter(LCICID=LCICID, EnterpriseID=EnterpriseID)
#             serializer = EnterpriseInfoSerializer(results, many=True)
#             return Response({'data': serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'LCICID and EnterpriseID are required fields'}, 
#             status=status.HTTP_400_BAD_REQUEST)

# search 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EnterpriseInfo, InvestorInfo
from .serializers import EnterpriseInfoSerializer

class EnterpriseInfoSearch(APIView):
    def post(self, request):
        LCICID = request.data.get('LCICID')
        EnterpriseID = request.data.get('EnterpriseID')
        
        # print("LCIC: ",LCICID)
        # print("Enterpriseid: ",EnterpriseID)
        
        if LCICID is not None and EnterpriseID is not None:
            try:
                enterprise_info = EnterpriseInfo.objects.filter(LCICID=LCICID, EnterpriseID=EnterpriseID)
                investor_info = InvestorInfo.objects.filter(EnterpriseID=EnterpriseID)
                for i in investor_info:
                    invesinfo = i.investorName
                    # print(invesinfo)
                    
                print("Search_Log Are Taken Here")
                print("UserID, ")
                
                
                serializer = EnterpriseInfoSerializer(enterprise_info, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except EnterpriseInfo.DoesNotExist:
                return Response({'error': 'EnterpriseInfo not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'LCICID and EnterpriseID are required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         if username is None or password is None:
#             return Response({'error': 'Please provide both username and password'},
#                             status=status.HTTP_400_BAD_REQUEST)

#         user = authenticate(username=username, password=password)
#         login_user = User_Login.objects.filter(UserName=username, Password=password).first()

#         if login_user is not None:
#             return Response({'success': 'Done'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
from rest_framework import viewsets
from .models import EnterpriseInfo, InvestorInfo
from .serializers import EnterpriseInfoSerializer, InvestorInfoSerializer

class EnterpriseInfoViewSet(viewsets.ModelViewSet):
    queryset = EnterpriseInfo.objects.all()
    serializer_class = EnterpriseInfoSerializer

class InvestorInfoViewSet(viewsets.ModelViewSet):
    queryset = InvestorInfo.objects.all()
    serializer_class = InvestorInfoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Login, User_Group, memberInfo
from .serializers import LoginSerializer
from django.contrib.auth.hashers import make_password
import logging
logger = logging.getLogger(__name__)


class UserManagementView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'success': 'User created successfully',
                'user': {
                    'UID': user.UID,
                    'username': user.username,
                    'nameL': user.nameL,
                    'surnameL': user.surnameL,
                    'nameE': user.nameE,
                    'surnameE': user.surnameE,
                    'GID': user.GID.pk if user.GID else None,
                    'MID': user.MID.pk if user.MID else None,
                    'is_active': user.is_active,
                    'is_staff': user.is_staff
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        try:
            all_user = Login.objects.all()
            if not all_user.exists():
                return Response({"detail": "No User information found."}, status=status.HTTP_404_NOT_FOUND)
            
            logger.info(f"Retrieved {all_user.count()} Users records.")
            serializer = LoginSerializer(all_user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            return Response({"detail": "An error occurred while retrieving User information."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, UID):
        try:
            user = Login.objects.get(UID=UID)
            
            print(user)
            user.delete()
            return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Login.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, UID):
    #     try:
    #         user = Login.objects.get(UID=UID)
    #         serializer = LoginSerializer(user, data=request.data, partial=True)  # partial=True allows partial updates
    #         if serializer.is_valid():
    #             user = serializer.save()
    #             return Response({
    #                 'success': 'User updated successfully',
    #                 'user': {
    #                     'UID': user.UID,
    #                     'username': user.username,
    #                     'nameL': user.nameL,
    #                     'surnameL': user.surnameL,
    #                     'nameE': user.nameE,
    #                     'surnameE': user.surnameE,
    #                     'GID': user.GID.pk if user.GID else None,
    #                     'MID': user.MID.pk if user.MID else None,
    #                     'is_active': user.is_active,
    #                     'is_staff': user.is_staff
    #                 }
    #             }, status=status.HTTP_200_OK)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Login.DoesNotExist:
    #         return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

class UpdateUserView(APIView):
    def put(self, request, UID):
        try:
            user = Login.objects.get(UID=UID)
            serializer = LoginSerializer(user, data=request.data, partial=True)  # partial=True allows partial updates
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': 'User updated successfully',
                    'user': serializer.data
                }, status=status.HTTP_200_OK)
            else:
                # Log serializer errors for debugging
                print(serializer.errors)  # Debugging line
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Login.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GetUserByUIDView(APIView):
    def get(self, request, UID):
        try:
            user = Login.objects.get(UID=UID)
            serializer = LoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Login.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# class FCR_report(APIView):
    # def post(self, request):
    #     if request.method == 'POST':
    #         enterprise = request.POST.get('EnterpriseID')
    #         lcic = request.POST.get('LCICID')            
    #     try:
    #         ent_id = EnterpriseInfo.objects.get(enterprise=enterprise, lcic=lcic)
    #         fcrInfo = EnterpriseInfo.filter(LCICID='LCICID').filter(EnterpriseID='EnterpriseID')
    #         context={
    #             'ent_id':ent_id,
    #             'fcrInfo':fcrInfo
    #         }
    #         return Response({'success': 'Done'}, status=status.HTTP_200_OK)
    #     except:
    #         return Response({"detail": "An error occurred while retrieving bank information."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EnterpriseInfo, B1_Yearly, InvestorInfo, B1_Monthly, C1
from django.forms.models import model_to_dict
from .serializers import EnterpriseInfoSerializer, B1_YearlySerializer, InvestorInfoSerializer, B1Serializer

class FCR_reportView(APIView):    
    def get(self, request):
        enterprise_id = request.GET.get('EnterpriseID')
        lcic_id = request.GET.get('LCICID')

        print(enterprise_id)
        print(lcic_id)

        status_inactive = "INACTIVE"
        status_active = "ACTIVE"

        try:
            # Retrieve the specific EnterpriseInfo objects
            ent_info = EnterpriseInfo.objects.filter(EnterpriseID=enterprise_id, LCICID=lcic_id)
            loan_info = B1.objects.filter(com_enterprise_code=enterprise_id, lon_status=status_active).order_by('lon_status')
            inves_info = InvestorInfo.objects.filter(EnterpriseID=enterprise_id)

            print("Enterprise_info:", ent_info)
            print("Loan_Info:", loan_info)
            print("Investor_Info:", inves_info)

            if not ent_info.exists():
                return Response({"detail": "Enterprise information not found."}, status=status.HTTP_404_NOT_FOUND)

            loan_info_list_active = []   

            # Collateral Models Mapping
            # col_type_to_model = {
            #     'RealEstate': col_real_estates,
            #     'Money': col_money_mia,
            #     'Equipment': col_equipment_eqi,
            #     'Project': col_project_prj,
            #     'Vehicle': col_vechicle_veh,
            #     'Guarenty': col_guarantor_gua,
            #     'gold_silver': col_goldsilver_gold,
            #     'c2.1': col_real_estates.C2_1,
            #     'c2.2': col_money_mia.C2_2,
            #     'c2.3': col_equipment_eqi.C2_3,
            #     'c2.4': col_project_prj.C2_4,
            #     'c2.5': col_vechicle_veh.C2_5,
            #     'c2.6': col_guarantor_gua.C2_6,
            #     'c2.7': col_goldsilver_gold.C2_7,
            # }
            col_type_to_model = {
                'c2.1': col_real_estates,
                'c2.2': col_money_mia,
                'c2.3': col_equipment_eqi,
                'c2.4': col_project_prj,
                'c2.5': col_vechicle_veh,
                'c2.6': col_guarantor_gua,
                'c2.7': col_goldsilver_gold,
            }
            
            for loan in loan_info:
                if loan.lon_status == status_active:  # Ensure processing only active loans
                    lon_class_history = B1_Monthly.objects.filter(
                        com_enterprise_code=enterprise_id,
                        bnk_code=loan.bnk_code,
                        customer_id=loan.customer_id,
                        branch_id=loan.branch_id,
                        loan_id=loan.loan_id,
                    ).order_by('-period')

                    lon_class_history_list = list(lon_class_history.values())

                    # Get Collateral Records
                    colleteral_list = C1.objects.filter(
                        com_enterprise_code=enterprise_id,
                        bnk_code=loan.bnk_code,
                        branch_id_code=loan.branch_id,
                        bank_customer_ID=loan.customer_id,
                        loan_id=loan.loan_id,
                    )
                    print("Colleteral ---------------> : ", colleteral_list)
                    
                    # for colleteral in colleteral_list:
                    #     print("Col_id ----->", colleteral.col_id)
                    
                    # test_col = col_real_estates.objects.filter(
                    #     com_enterprise_code=enterprise_id,
                    #     bnk_code=loan.bnk_code,
                    #     branch_id_code=loan.branch_id,
                    #     bank_customer_ID=loan.customer_id,
                    #     loan_id=loan.loan_id,
                    # )
                    # print("Test Colleteral ---------------> : ", test_col)
                    
                        # check_col_id = col_real_estates.objects.filter(
                        #     col_id = colleteral.col_id
                        # )
                        # print("<---------------- Col_id",check_col_id)

                    collateral_history_list = []
                    for collateral in colleteral_list:
                        col_id = collateral.col_id
                        col_type = collateral.col_type

                        print("Check_Col_id ====> :", col_id)  
                        print("Check_Col_type ====> :", col_type)  
                        

                        # Get the related model based on col_type
                        related_model = col_type_to_model.get(col_type)
                        print("related_model: ======>", related_model)

                        if related_model:
                            # Query the related table using col_id
                            related_record = related_model.objects.filter(col_id=col_id).first()
                                
                            print("get Related_Records : ====> ", related_record)

                            if related_record:
                                related_record_dict = model_to_dict(related_record)
                                collateral_dict = model_to_dict(collateral)

                                # Add the related record to collateral history list
                                collateral_history_list.append({
                                    "col_id": col_id,
                                    "col_type": col_type,
                                    "collateral_info": collateral_dict, #C1
                                    "related_record": related_record_dict, #C2.n
                                })
                        else:
                            print(f"Unrecognized col_type: {col_type} for collateral ID {col_id}")

                    loan_data_active = {
                        "id": loan.loan_id,
                        "lon_update_date": loan.lon_update_date,
                        "bank": loan.bnk_code,
                        "lon_insert_date": loan.lon_insert_date,
                        "lon_credit_line": loan.lon_credit_line,
                        "lon_outstanding_balance": loan.lon_outstanding_balance,
                        "lon_currency_code": loan.lon_currency_code,
                        "lon_no_days_slow": loan.lon_no_days_slow,
                        "lon_class": loan.lon_class,
                        "period": loan.period,
                        "lon_open_date": loan.lon_open_date,
                        "lon_exp_date": loan.lon_exp_date,
                        "lon_ext_date": loan.lon_ext_date,
                        "lon_int_rate": loan.lon_int_rate,
                        "lon_purpose_code": loan.lon_purpose_code,
                        "lon_account_no": loan.lon_account_no,
                        "lon_status": loan.lon_status,
                        "lon_type": loan.lon_type,
                        "lon_term": loan.lon_term,
                        "is_disputed": loan.is_disputed,
                        "lon_applied_date": loan.lon_applied_date,
                        "lon_class_history": lon_class_history_list,
                        "collateral_history": collateral_history_list,
                    }

                    loan_info_list_active.append(loan_data_active)
                    print("Loan Data For Active: -------> ", loan_info_list_active)
                else:
                    print("Non Active List")

            ent_info_serializer = EnterpriseInfoSerializer(ent_info, many=True)
            loan_info_serializer = B1Serializer(loan_info, many=True)
            inves_info_serializer = InvestorInfoSerializer(inves_info, many=True)
            
            response_data = {
                'enterprise_info': ent_info_serializer.data,
                'loan_info': loan_info_serializer.data,
                'inves_info': inves_info_serializer.data,
                'active_loans': loan_info_list_active,
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return Response({"detail": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         try:
#             # Check if the user exists
#             user_exists = Login.objects.filter(username=username).first()
#             print("Login Check: ", user_exists)
            
#         except Login.DoesNotExist:
#             return Response({"detail": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

#         # Authenticate the user
#         user = authenticate(username=username, password=password)
#         print("User: ", user)

#         if user is not None:
#             # User exists and is authenticated
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         else:
#             # Credentials are invalid
#             return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer,UserLoginSerializer
from django.contrib.auth import login
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta

# class UserLoginView(APIView):
#     serializer_class = UserLoginSerializer

#     # def post(self, request, *args, **kwargs):
#     #     serializer = self.serializer_class(data=request.data)
#     #     if serializer.is_valid(raise_exception=True):
#     #         user = serializer.validated_data['user']
#     #         login(request, user)
#     #         return Response({'detail': 'Successfully logged in.'}, status=status.HTTP_200_OK)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.validated_data['user']
#             login(request, user)
            
#             # Generate or retrieve the custom token
#             # token = self.generate_token(user)
            
#             return Response({
#                 'detail': 'Successfully logged in.',
#                 # 'token': token.key
#             }, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            # print("User_info: ", user)
            
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            # user_role = user.GID
            user_data = UserLoginSerializer(user).data
            
            return Response({
                'detail': 'Successfully logged in.',
                'access': str(access_token),
                'refresh': str(refresh),
                'user':user_data,
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .serializers import MemberInfoSerializer
class memberinfolistView(APIView):
    def get(self, request):
        member_info = memberInfo.objects.all()
        serializer = MemberInfoSerializer(member_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from .serializers import SidebarItemSerializer
from .models import SidebarItem, Role
# class SidebarItemsView(APIView):
#     def get(self, request):
#         # Get the user's roles, assuming roles are sent in headers or from user data
#         user_roles = request.headers.get('X-User-Roles')  # Or use request.user if applicable
        
#         if not user_roles:
#             return Response({'detail': 'User roles not provided.'}, status=status.HTTP_400_BAD_REQUEST)

#         user_roles = user_roles.split(',')  # Assuming roles are provided as a comma-separated string

#         try:
#             # Filter sidebar items by roles
#             sidebar_items = SidebarItem.objects.filter(roles__name__in=user_roles).distinct()
#             serializer = SidebarItemSerializer(sidebar_items, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'detail': f'Error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SidebarItemsView(APIView):
    def get(self, request):
        # Get the user's GID from the X-User-Roles header
        user_gid = request.headers.get('X-User-Roles')
        print("USER_GID: ", user_gid)
            
        if not user_gid:
            return Response({'detail': 'User GID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Filter the roles by the provided GID
            roles = Role.objects.filter(id=user_gid)
            if not roles.exists():
                return Response({'detail': 'Invalid GID provided.'}, status=status.HTTP_404_NOT_FOUND)
            
            print("GID from Vue: ", roles)

            # Filter sidebar items by roles associated with the GID
            sidebar_items = SidebarItem.objects.filter(roles__in=roles).distinct()
            
            # Optionally filter subitems here if needed
            # sidebar_subitems = SidebarSubItem.objects.filter(roles__in=roles).distinct()

            # Serialize the sidebar items
            serializer = SidebarItemSerializer(sidebar_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'detail': f'Error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

#SideBar Fetching
from .serializers import RoleSerializer, SidebarItemSerializer, SidebarSubItemSerializer

# API for fetching all roles
class RoleListView(APIView):
    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# API for fetching all sidebar items
class SidebarItemListView(APIView):
    def get(self, request):
        sidebar_items = SidebarItem.objects.all()
        serializer = SidebarItemSerializer(sidebar_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# API for fetching all sidebar sub-items
class SidebarSubItemListView(APIView):
    def get(self, request):
        sidebar_sub_items = SidebarSubItem.objects.all()
        serializer = SidebarSubItemSerializer(sidebar_sub_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# API for assigning role to sidebar items and sub-items
# class AssignRoleView(APIView):
#     def post(self, request):
#         role_id = request.data.get('role_id')
#         sidebar_item_ids = request.data.get('sidebar_items', [])
#         sidebar_sub_item_ids = request.data.get('sidebar_sub_items', [])

#         try:
#             # Get the role instance
#             role = Role.objects.get(id=role_id)

#             # Assign sidebar items to the role
#             sidebar_items = SidebarItem.objects.filter(id__in=sidebar_item_ids)
#             for item in sidebar_items:
#                 item.roles.add(role)

#             # Assign sidebar sub-items to the role
#             sidebar_sub_items = SidebarSubItem.objects.filter(id__in=sidebar_sub_item_ids)
#             for sub_item in sidebar_sub_items:
#                 sub_item.roles.add(role)

#             return Response({"detail": "Role assigned successfully"}, status=status.HTTP_200_OK)

#         except Role.DoesNotExist:
#             return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AssignRoleView(APIView):
    def post(self, request):
        role_id = request.data.get('role_id')
        sidebar_item_ids = request.data.get('sidebar_items', [])
        sidebar_sub_item_ids = request.data.get('sidebar_sub_items', [])

        # Debugging log
        print(f"Received role_id: {role_id}, sidebar_item_ids: {sidebar_item_ids}, sidebar_sub_item_ids: {sidebar_sub_item_ids}")

        try:
            # Check if the role exists
            role = Role.objects.get(id=role_id)

            # Debugging log
            print(f"Found role: {role}")

            # Assign SidebarItems to the Role
            sidebar_items = SidebarItem.objects.filter(id__in=sidebar_item_ids)
            for item in sidebar_items:
                item.roles.add(role)

            # Assign SidebarSubItems to the Role
            sidebar_sub_items = SidebarSubItem.objects.filter(id__in=sidebar_sub_item_ids)
            for sub_item in sidebar_sub_items:
                sub_item.roles.add(role)

            return Response({"detail": "Role assigned successfully"}, status=status.HTTP_200_OK)

        except Role.DoesNotExist:
            # Log the error
            print(f"Role with id {role_id} does not exist.")
            return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error: {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
