#from asyncio.windows_events import NULL
from contextlib import nullcontext
from datetime import datetime
from multiprocessing import context
from crispy_forms.helper import FormHelper
from re import M
from tkinter.messagebox import NO
from django.http import request
from django.shortcuts import render, redirect
from .models import Login,Group_User, GroupSubMenu, H_imageBar,H_productInfo,H_newsInfo,H_Lang, User_Group, User_Login, Menu, SubMenu, Upload_File, CustomerWater, SegmentType, EnterpriseInfo, InvestorInfo, user_logged, searchLog, request_charge
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
import requests
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from .serializers import * 
import logging
import binascii
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
# from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from .models import Login  # Ensure you import your Login model
# from .models import CustomLoginToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


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
            search_log_insert = searchLog.objects.create(enterprise_ID=invs_name.EnterpriseID, LCIC_code=enterprise_object.LCIC_code,
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
    
    # rec_charge_insert = request_charge.objects.create(
    #     bnk_code = (sys_user.MID).id,
    #     chg_amount = charge_amount_data.price,
    #     chg_code = charge_amount_data.code,
    #     status = 'InActive',
    #     # insert_date = '',
    #     # update_date = '',
    #     rtp_code = '1',
    #     chg_unit = 'LAK',
    #     user_sys_id = sys_user.UID,
    #     LCIC_ID = fee_data.LCICID,
    #     cusType = ''
    # )
    
    
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
# def make_gapi_request():
#     api_key = "goldapi-aylvjurlrhfyjm1-io"
#     symbol = "XAU"
#     curr = "USD"
#     date = ""

#     url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
#     headers = {
#         "x-access-token": api_key,
#         "Content-Type": "application/json"
#     }
    
#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()

#         # result = response.text
#         # print(result)
        
#         result_json = response.json()
        
#         price = result_json["price"]
#         print(price)
#     except requests.exceptions.RequestException as e:
#         print("Error:", str(e))

# result = make_gapi_request()    




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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import bank_bnk
from .serializers import Bank_InfoINDSerializer
import logging

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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
class UpdateUserView(APIView):
    parser_classes = [MultiPartParser, FormParser]
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
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Login.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)













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




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import EnterpriseInfo, InvestorInfo, searchLog
# from .serializers import EnterpriseInfoSerializer
# from datetime import datetime



# class EnterpriseInfoSearch(APIView):
    
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
        
#         user = request.user
#         UID = user.UID 
#         bank = user.MID
        
#         bank_info = bank_bnk.objects.get(bnk_code=bank.bnk_code)
      
#         LCIC_code = request.data.get('LCIC_code')
#         EnterpriseID = request.data.get('EnterpriseID')
#         loan_purpose = request.data.get('CatalogID')
#         sys_usr = f"{str(user.UID)}-{str(bank.bnk_code)}"
        
    
#         if LCIC_code is not None and EnterpriseID is not None:
#             try:
#                 enterprise_info = EnterpriseInfo.objects.filter(LCIC_code=LCIC_code, EnterpriseID=EnterpriseID)
#                 investor_info = InvestorInfo.objects.filter(EnterpriseID=EnterpriseID)
#                 for i in investor_info:
#                     invesinfo = i.investorName
                    
                
#                 serializer = EnterpriseInfoSerializer(enterprise_info, many=True)
                
#                 inquiry_month = datetime.now().strftime('%Y-%m')
               
#                 search_log = searchLog.objects.create(
#                     enterprise_ID=EnterpriseID,
#                     LCIC_code=LCIC_code,
#                     bnk_code=bank_info.bnk_code,
#                     bnk_type=bank_info.bnk_type,
#                     branch='',
#                     cus_ID='',
#                     cusType='enterprise',
#                     credit_type='Full Loan Report',
#                     inquiry_month=inquiry_month,
#                     com_tel='',
#                     com_location='',
#                     rec_loan_amount=0.0,
#                     rec_loan_amount_currency='',
#                     rec_loan_purpose=loan_purpose,
#                     rec_enquiry_type='',
#                     sys_usr=sys_usr  
#                 )

#                 search_log.save()
#                 print("Searchlog Insert Successfully ======>")
                
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except EnterpriseInfo.DoesNotExist:
#                 return Response({'error': 'EnterpriseInfo not found'}, status=status.HTTP_404_NOT_FOUND)
#             except Exception as e:
#                 return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import EnterpriseInfo, InvestorInfo, searchLog, bank_bnk
from .serializers import EnterpriseInfoSerializer
from datetime import datetime
from django.db.models import Q


class EnterpriseInfoSearch(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            UID = user.UID 
            bank = user.MID
            
            # Get bank information
            bank_info = bank_bnk.objects.get(bnk_code=bank.bnk_code)
          
            # Extract request data
            LCIC_code = request.data.get('LCIC_code', '').strip()
            EnterpriseID = request.data.get('EnterpriseID', '').strip()
            loan_purpose = request.data.get('CatalogID', '')
            sys_usr = f"{str(user.UID)}-{str(bank.bnk_code)}"
            
            # Validate that at least one search parameter is provided
            if not LCIC_code and not EnterpriseID:
                return Response(
                    {'error': 'At least LCIC_code or EnterpriseID is required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        
            # Build dynamic query using Q objects for OR condition
            query = Q()
            if LCIC_code:
                query |= Q(LCIC_code=LCIC_code)
            if EnterpriseID:
                query |= Q(EnterpriseID=EnterpriseID)
                
            # Get all matching records first
            all_enterprise_info = EnterpriseInfo.objects.filter(query).order_by('EnterpriseID', 'LCIC_code', '-LCICID')
            
            if not all_enterprise_info.exists():
                return Response(
                    {'error': 'EnterpriseInfo not found'}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Manual deduplication - keep the one with the highest LCICID (or non-zero LCICID)
            seen_combinations = set()
            unique_enterprises = []
            
            for enterprise in all_enterprise_info:
                # Create a unique key based on EnterpriseID and LCIC_code
                unique_key = (enterprise.EnterpriseID, enterprise.LCIC_code)
                
                if unique_key not in seen_combinations:
                    # Prefer records with non-zero LCICID
                    if enterprise.LCICID and enterprise.LCICID > 0:
                        unique_enterprises.append(enterprise)
                        seen_combinations.add(unique_key)
                    else:
                        # Check if we haven't found a better record yet
                        has_better_record = False
                        for existing in all_enterprise_info:
                            if (existing.EnterpriseID == enterprise.EnterpriseID and 
                                existing.LCIC_code == enterprise.LCIC_code and 
                                existing.LCICID and existing.LCICID > 0):
                                has_better_record = True
                                break
                        
                        if not has_better_record:
                            unique_enterprises.append(enterprise)
                            seen_combinations.add(unique_key)
            
            # Alternative approach using dictionary for cleaner deduplication
            enterprise_dict = {}
            for enterprise in all_enterprise_info:
                key = f"{enterprise.EnterpriseID}_{enterprise.LCIC_code}"
                
                # If we haven't seen this combination before, or if current record has better LCICID
                if (key not in enterprise_dict or 
                    (enterprise.LCICID and enterprise.LCICID > 0 and 
                     (not enterprise_dict[key].LCICID or enterprise_dict[key].LCICID == 0))):
                    enterprise_dict[key] = enterprise
            
            # Use the cleaner approach
            unique_enterprises = list(enterprise_dict.values())
            
            print(f"Found {all_enterprise_info.count()} total records, {len(unique_enterprises)} unique enterprises")
            
            # Get unique enterprise IDs from deduplicated results
            enterprise_ids = [enterprise.EnterpriseID for enterprise in unique_enterprises]
            
            # Get investor information for these enterprises
            investor_info = InvestorInfo.objects.filter(EnterpriseID__in=enterprise_ids)
            
            # Process investor information and remove duplicates
            investor_names = []
            seen_names = set()
            for investor in investor_info:
                if investor.investorName and investor.investorName.strip():
                    clean_name = investor.investorName.strip()
                    if clean_name not in seen_names:
                        investor_names.append(clean_name)
                        seen_names.add(clean_name)
                
            # Serialize enterprise data
            serializer = EnterpriseInfoSerializer(unique_enterprises, many=True)
            
            # Create search log entry using the first enterprise result
            first_enterprise = unique_enterprises[0]
            log_enterprise_id = EnterpriseID if EnterpriseID else first_enterprise.EnterpriseID
            log_lcic_code = LCIC_code if LCIC_code else first_enterprise.LCIC_code
            
            inquiry_month = datetime.now().strftime('%Y-%m')
           
            search_log = searchLog.objects.create(
                enterprise_ID=log_enterprise_id,
                LCIC_code=log_lcic_code,
                bnk_code=bank_info.bnk_code,
                bnk_type=bank_info.bnk_type,
                branch='',
                cus_ID='',
                cusType='enterprise',
                credit_type='Full Loan Report',
                inquiry_month=inquiry_month,
                com_tel='',
                com_location='',
                rec_loan_amount=0.0,
                rec_loan_amount_currency='',
                rec_loan_purpose=loan_purpose or '',
                rec_enquiry_type='',
                sys_usr=sys_usr  
            )

            print(f"Searchlog Insert Successfully ======> Returning {len(unique_enterprises)} unique enterprise(s)")
            
            # Prepare response data
            response_data = {
                'enterprise_info': serializer.data,
                'investor_names': investor_names,
                'total_found': len(unique_enterprises),
                'debug_info': {
                    'total_raw_records': all_enterprise_info.count(),
                    'unique_records_returned': len(unique_enterprises),
                    'search_criteria': {
                        'LCIC_code': LCIC_code,
                        'EnterpriseID': EnterpriseID
                    }
                }
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except bank_bnk.DoesNotExist:
            return Response(
                {'error': 'Bank information not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Error in EnterpriseInfoSearch: {str(e)}")
            return Response(
                {'error': 'Internal server error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
class EnterpriseByLCICView(APIView):
    """
    ດືງຂໍ້ມູນ Enterprise ID ຈາກ LCIC code
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, lcic_code):
        try:
            lcic_code = lcic_code.strip()
            
            # ລອງຫາດ້ວຍ LCIC code ຕົງໆ ກ່ອນ
            enterprise = EnterpriseInfo.objects.filter(
                LCIC_code=lcic_code
            ).order_by('-LCICID').first()
            
            # ຖ້າບໍ່ເຈົ້າ, ລອງຫາດ້ວຍ LCIC code ທີ່ມີ prefix
            if not enterprise:
                enterprise = EnterpriseInfo.objects.filter(
                    LCIC_code__icontains=lcic_code
                ).order_by('-LCICID').first()
            
            # ຖ້າຍັງບໍ່ເຈົ້າ, ລອງຫາດ້ວຍ LCICID ຖ້າເປັນຕົວເລກ
            if not enterprise and lcic_code.isdigit():
                enterprise = EnterpriseInfo.objects.filter(
                    LCICID=int(lcic_code)
                ).first()
            
            if not enterprise:
                return Response(
                    {'error': 'Enterprise not found for this LCIC code'}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # ເອົາຊື່ວິສາຫະກິດ
            enterprise_name = ''
            if hasattr(enterprise, 'enterpriseNameLao') and enterprise.enterpriseNameLao:
                enterprise_name = enterprise.enterpriseNameLao
            elif hasattr(enterprise, 'eneterpriseNameEnglish') and enterprise.eneterpriseNameEnglish:
                enterprise_name = enterprise.eneterpriseNameEnglish
            
            return Response(
                {
                    'lcic_code': enterprise.LCIC_code or '',
                    'enterprise_id': enterprise.EnterpriseID or '',
                    'enterprise_name': enterprise_name,
                    'lcic_id': enterprise.LCICID,
                    'success': True
                }, 
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            print(f"Error in EnterpriseByLCICView: {str(e)}")
            return Response(
                {'error': 'Internal server error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class LCICByEnterpriseView(APIView):
    """
    ດືງຂໍ້ມູນ LCIC code ຈາກ Enterprise ID
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, enterprise_id):
        try:
            enterprise_id = enterprise_id.strip()
            
            # ຫາຂໍ້ມູນວິສາຫະກິດຈາກ Enterprise ID
            enterprise = EnterpriseInfo.objects.filter(
                EnterpriseID=enterprise_id
            ).order_by('-LCICID').first()
            
            if not enterprise:
                return Response(
                    {'error': 'Enterprise not found for this Enterprise ID'}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # ເອົາຊື່ວິສາຫະກິດ
            enterprise_name = ''
            if hasattr(enterprise, 'enterpriseNameLao') and enterprise.enterpriseNameLao:
                enterprise_name = enterprise.enterpriseNameLao
            elif hasattr(enterprise, 'eneterpriseNameEnglish') and enterprise.eneterpriseNameEnglish:
                enterprise_name = enterprise.eneterpriseNameEnglish
            
            return Response(
                {
                    'enterprise_id': enterprise.EnterpriseID or '',
                    'lcic_code': enterprise.LCIC_code or '',
                    'enterprise_name': enterprise_name,
                    'lcic_id': enterprise.LCICID,
                    'success': True
                }, 
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            print(f"Error in LCICByEnterpriseView: {str(e)}")
            return Response(
                {'error': 'Internal server error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
class EnterpriseInfoMatch(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        user = request.user
        
        UID = user.UID  
        bank = str(user.MID.id)  
        branch = str(user.GID.GID)  
        
        LCIC_code = request.data.get('LCIC_code')
        EnterpriseID = request.data.get('EnterpriseID')

        print("Authenticated User ID (UID):", UID)
        print("Authenticated Bankname:", bank)
        print("Authenticated Branchname:", branch)
        
        print("LCIC_code:", LCIC_code)
        print("EnterpriseID:", EnterpriseID)
        # print("Login :",Login._meta.get_fields())
        if LCIC_code is not None and EnterpriseID is not None:
            try:
                # enterprise_info = EnterpriseInfo.objects.filter(LCICID=LCICID, EnterpriseID=EnterpriseID)
                enterprise_info = B1.objects.filter(LCIC_code=LCIC_code, com_enterprise_code=EnterpriseID)
                investor_info = InvestorInfo.objects.filter(EnterpriseID=EnterpriseID)                              
                for i in investor_info:
                    invesinfo = i.investorName
                    # print(invesinfo)
                
                serializer = EnterpriseInfoSerializer(enterprise_info, many=True)
                
                return Response(serializer.data, status=status.HTTP_200_OK)
            except EnterpriseInfo.DoesNotExist:
                return Response({'error': 'EnterpriseInfo not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        login_user = User_Login.objects.filter(UserName=username, Password=password).first()

        if login_user is not None:
            return Response({'success': 'Done'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
from rest_framework import viewsets
from .models import EnterpriseInfo, InvestorInfo
from .serializers import EnterpriseInfoSerializer, InvestorInfoSerializer

class EnterpriseInfoViewSet(viewsets.ModelViewSet):
    queryset = EnterpriseInfo.objects.all()
    serializer_class = EnterpriseInfoSerializer

class InvestorInfoViewSet(viewsets.ModelViewSet):
    queryset = InvestorInfo.objects.all()
    serializer_class = InvestorInfoSerializer



# get ທຳມະດາ
from django.http import JsonResponse
from .models import H_productInfo

def get_product_info(request):
    products = H_productInfo.objects.all().values('code', 'slug', 'nameL', 'nameE', 'descE', 'descL', 'price', 'proType', 'pimage', 'pFiles', 'published', 'insertDate', 'updateDate')
    products_list = list(products)
    return JsonResponse(products_list, safe=False)


# get ຕາມໄອດີ

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import H_productInfo

# def get_product_info(request):
#     products = H_productInfo.objects.all().values('code', 'slug', 'nameL', 'nameE', 'descE', 'descL', 'price', 'proType', 'pimage', 'pFiles', 'published', 'insertDate', 'updateDate')
#     products_list = list(products)
#     return JsonResponse(products_list, safe=False)

def get_product_detail(request, id):
    product = get_object_or_404(H_productInfo, pk=id)
    data = {
        'code': product.code,
        'slug': product.slug,
        'nameL': product.nameL,
        'nameE': product.nameE,
        'descE': product.descE,
        'descL': product.descL,
        'price': product.price,
        'proType': product.proType_id,
        'pimage': product.pimage.url if product.pimage else '',
        'pFiles': product.pFiles.url if product.pFiles else '',
        'published': product.published,
        'insertDate': product.insertDate,
        'updateDate': product.updateDate,
    }
    return JsonResponse(data)


# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
# from .models import H_productInfo

def get_product_info_by_id(request, id):
    product = get_object_or_404(H_productInfo, id=id)
    data = {
        'code': product.code,
        'slug': product.slug,
        'nameL': product.nameL,
        'nameE': product.nameE,
        'descE': product.descE,
        'descL': product.descL,
        'price': product.price,
        'proType': product.proType_id,
        'pimage': product.pimage.url if product.pimage else None,
        'pFiles': product.pFiles.url if product.pFiles else None,
        'published': product.published,
        'insertDate': product.insertDate,
        'updateDate': product.updateDate,
    }
    return JsonResponse(data)


from django.http import JsonResponse
from .models import H_productInfo

def get_product_infocode(request):
    code = request.GET.get('code', None)
    if code:
        products = H_productInfo.objects.filter(code=code).values('code', 'slug', 'nameL', 'nameE', 'descE', 'descL', 'price', 'proType', 'pimage', 'pFiles', 'published', 'insertDate', 'updateDate','user_id')
    else:
        products = H_productInfo.objects.all().values('code', 'slug', 'nameL', 'nameE', 'descE', 'descL', 'price', 'proType', 'pimage', 'pFiles', 'published', 'insertDate', 'updateDate','user_id')
    products_list = list(products)
    return JsonResponse(products_list, safe=False)




from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import process_large_file

@api_view(['POST'])
def upload_file_view(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        file_path = os.path.join('uploads', file.name)  # ສ້າງ path ສຳຫຼັບຟາຍ(file)
        process_large_file.delay(file_path)  # Celery
        # async_task('path.to.process_large_file', file_path)  # Django Q
        return Response({'message': 'ກຳລັງປະມວນຜົນຟາຍເບືອງຫຼັງ'}, status=202)
    return Response({'error': 'ບໍ່ມີຟາຍ'}, status=400)




from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.utils import timezone
import json
from django.utils.encoding import smart_str
from .models import Upload_File_C, col_money_mia, col_real_estates,  col_equipment_eqi, col_project_prj ,col_vechicle_veh, col_guarantor_gua,col_goldsilver_gold, C_error
from .serializers import FileSerializer


class FileUploadViewC(generics.CreateAPIView):
    queryset = Upload_File_C.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        if not user_id:
            return JsonResponse({'status': 'error', 'message': 'User ID is required'}, status=400)

        files = request.FILES.getlist('file')
        if not files:
            return JsonResponse({'status': 'error', 'message': 'No files uploaded'}, status=401)

        csrf_token = request.META.get('CSRF_COOKIE', '')
        for file in files:
            if file.name.endswith('.json'):
                try:
                    file_content = file.read().decode('utf-8')
                    file_data = json.loads(file_content)
                    if isinstance(file_data, list):
                        file_data = file_data[0]

                    bnk_code = file_data.get('bnk_code')
                    if bnk_code is None:
                        return JsonResponse({'status': 'error', 'message': 'bnk_code is required'}, status=400)
                    if str(user_id)  != str(bnk_code):
                        return JsonResponse({'status': 'error', 'message': 'User ID does not match bnk_code'}, status=401)
                    
                    file_name_parts = file.name.split('_')
                    if len(file_name_parts) >= 4:
                        period = file_name_parts[3][1:]
                    else:
                        return JsonResponse({'status': 'error', 'message': 'Invalid file name format'}, status=400)
                    
                    if Upload_File_C.objects.filter(fileName=file.name, user_id=user_id).exists():
                        return JsonResponse({'status': 'error', 'message': 'File already exists'}, status=404)
                    file_name_parts = file.name.split('_')
                    if len(file_name_parts) >= 4:
                        period_str = file_name_parts[3]
                        period_month = int(period_str[1:3])
                        
                        period_year = int(period_str[3:])
                        
                        
                        file_period = int(f"{period_year:04d}{period_month:02d}")
                        print("file_period:", file_period)
                        

                        c1_entries = C1.objects.filter(bnk_code=bnk_code)
                        
                        if c1_entries.exists():
                            latest_c1 = c1_entries.order_by('-period').first()

                            
                            c1_period = latest_c1.period
                            
                            
                            if len(c1_period) == 6:
                                c1_period_month = c1_period[:2]
                                
                                c1_period_year = c1_period[2:]
                                
                                c1_period = int(c1_period) if isinstance(c1_period, str) else c1_period
                                print("c1_period:", c1_period)
                                
                            else:
                                return JsonResponse({'status': 'error', 'message': 'Invalid C1 period format'}, status=406)
                            
                            if file_period < c1_period:
                             return JsonResponse({'status': 'error', 'message': 'File period is less than C1 period'}, status=408)

                                # return JsonResponse({'status': 'error', 'message': 'File period is less than C1 period'}, status=408)
                        else:
                                pass
                    else:
                        return JsonResponse({'status': 'error', 'message': 'Invalid file name format'}, status=400)
                    
                            
                    file_instance = Upload_File_C.objects.create(
                        fileUpload=file,
                        user_id=user_id,
                        fileName=file.name,
                        fileSize=str(file.size),
                        path="uploadFilesC/" + file.name,
                        period=file_period,
                        status='new',
                        statussubmit='Pending',
                        status_upload='in_progress',
                        FileType='json',
                        percentage=0.0
                    )

                    
                    result = process_uploaded_file(file_instance, user_id, period,file_period)

                    status_value = result.get('status', None)
                    if status_value == '400':
                        file_instance.status_upload = 'failed'
                    else:
                        file_instance.status_upload = 'completed'

                  

                except Exception as e:
                   
                    return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
                

        response = JsonResponse({'status': 'success', 'message': 'All files processed successfully'})
        response.set_cookie('csrftoken', csrf_token)
        return response







import json
from django.utils.encoding import smart_str
from django.utils import timezone
from .models import EnterpriseInfo, C_error,C1_disptes,CDL,col_guarantor_com


    
from datetime import datetime


def human_readable_sizec(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
        return f"{size:.2f} TB"
def process_uploaded_file(uploaded_data,  user_id, period, file_period):
    try:
        total_records = 0
        error_records = 0
        
        with uploaded_data.fileUpload.open('rb') as file:
            file_content = file.read()
            json_content = json.loads(smart_str(file_content))
        file_size = file.size
        file_size_hrc = human_readable_sizec(file.size)

        total_records = len(json_content)
        print("total_records",total_records)
        print("period",period)

        for item in json_content:
            LCIC_code = item.get('LCIC_code', None)
            if LCIC_code == '':
                LCIC_code = None    

            com_enterprise_code = item.get('com_enterprise_code', '')
            cid = uploaded_data.CID

            lcic_exists = EnterpriseInfo.objects.filter(LCIC_code=LCIC_code).exists()
            enterprise_code_exists = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).exists()

            if not LCIC_code and not com_enterprise_code:
                collateral_status = '33'
                datamatch = ''
            elif not LCIC_code:
                if enterprise_code_exists:
                    collateral_status = '01'
                    datamatch = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first().LCIC_code
                else:
                    collateral_status = '03'
                    datamatch = ''
            elif not com_enterprise_code:
                if lcic_exists:
                    collateral_status = '10'
                    datamatch = EnterpriseInfo.objects.filter(LCIC_code=LCIC_code).first().EnterpriseID
                else:
                    collateral_status = '30'
                    datamatch = ''
            elif lcic_exists and not enterprise_code_exists:
                collateral_status = '31'
                datamatch = EnterpriseInfo.objects.filter(LCIC_code=LCIC_code).first().EnterpriseID
            elif not lcic_exists and enterprise_code_exists:
                collateral_status = '13'
                datamatch = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first().LCIC_code
            elif not lcic_exists and not enterprise_code_exists:
                collateral_status = '11'
                datamatch = ''
            elif LCIC_code and com_enterprise_code:
                matching_record = EnterpriseInfo.objects.filter(LCIC_code=LCIC_code, EnterpriseID=com_enterprise_code).exists()
                if not matching_record:
                    collateral_status = '44'  
                else:
                    collateral_status = '00'
            elif lcic_exists and enterprise_code_exists:
                collateral_status = '00'
                datamatch = '' 
                
            if collateral_status != '00':
                C_error.objects.create(
                    id_file=cid,
                    LCIC_code=LCIC_code,
                    com_enterprise_code=com_enterprise_code,
                    bnk_code=item.get('bnk_code', ''),
                    branch_id_code=item.get('branch_id_code', ''),
                    bank_customer_ID=item.get('bank_customer_ID', ''),
                    loan_id=item.get('loan_id', ''),
                    col_id=item.get('col_id', ''),
                    col_type=item.get('col_type', ''),
                    collateral_status=collateral_status,
                    datamatch=datamatch,
                    user_id=user_id,
                    period = file_period,
                    collateral_insert_date=timezone.now(),
                    collateral_update_date=timezone.now()
                )
                error_records += 1
                print("error_records",error_records)
                continue

            # ການກວດສອບຄວາມບໍ່ສອດຄ່ອງຂອງຂໍ້ມູນ (Data Inconsistency Check)
            bank_customer_ID = item.get('bank_customer_ID', '')
            bnk_code = item.get('bnk_code', '')
            loan_id = item.get('loan_id', '')
            col_id = item.get('col_id', '')

            inconsistency_found = False

            # ກໍລະນີທີ 1: bank_customer_ID, bnk_code, loan_id, col_id ຄືກັນ ແຕ່ com_enterprise_code ຫຼື LCIC_code ຕ່າງກັນ
            # ໝາຍຄວາມວ່າ: ລູກຄ້າຄົນດຽວກັນ ໃນທະນາຄານດຽວກັນ ມີເງິນກູ້ ແລະ collateral ດຽວກັນ 
            # ແຕ່ລະຫັດວິສາຫະກິດບໍ່ກົງກັນ (ຂໍ້ມູນບໍ່ສອດຄ່ອງ)
            case1_inconsistent = C1.objects.filter(
                bank_customer_ID=bank_customer_ID,
                bnk_code=bnk_code,
                loan_id=loan_id,
                col_id=col_id
            ).exclude(
                com_enterprise_code=com_enterprise_code,
                LCIC_code=LCIC_code
            )

            # ກໍລະນີທີ 2: bank_customer_ID, loan_id, col_id, com_enterprise_code, LCIC_code ຄືກັນ ແຕ່ bnk_code ຕ່າງກັນ
            # ໝາຍຄວາມວ່າ: ລູກຄ້າ, ເງິນກູ້, collateral, ວິສາຫະກິດດຽວກັນ ແຕ່ປະກົດຢູ່ໃນທະນາຄານຕ່າງກັນ
            # (ອາດເປັນຂໍ້ມູນຜິດພາດ ຫຼື ການປ່ຽນທະນາຄານທີ່ບໍ່ໄດ້ອັບເດດ)
            case2_inconsistent = C1.objects.filter(
                bank_customer_ID=bank_customer_ID,
                loan_id=loan_id,
                col_id=col_id,
                com_enterprise_code=com_enterprise_code,
                LCIC_code=LCIC_code
            ).exclude(
                bnk_code=bnk_code
            )

            # ບັນທຶກຂໍ້ມູນທີ່ບໍ່ສອດຄ່ອງ (Data Inconsistency)
            # ກໍລະນີທີ 1: ລະຫັດວິສາຫະກິດບໍ່ກົງກັນ
            if case1_inconsistent.exists():
                C1_disptes.objects.create(
                    LCIC_code=LCIC_code,
                    id_file=cid,
                    user_id=user_id,
                    period=file_period,
                    com_enterprise_code=com_enterprise_code,
                    bank_customer_ID=bank_customer_ID,
                    bnk_code=bnk_code,
                    branch_id_code=item.get('branch_id_code', ''),
                    loan_id=loan_id,
                    col_id=col_id,
                    col_type=item.get('col_type', ''),
                    insert_date=timezone.now(),
                    update_date=timezone.now()
                )
                inconsistency_found = True

            # ກໍລະນີທີ 2: ລະຫັດທະນາຄານບໍ່ກົງກັນ
            if case2_inconsistent.exists():
                C1_disptes.objects.create(
                    LCIC_code=LCIC_code,
                    id_file=cid,
                    user_id=user_id,
                    period=file_period,
                    com_enterprise_code=com_enterprise_code,
                    bank_customer_ID=bank_customer_ID,
                    bnk_code=bnk_code,
                    branch_id_code=item.get('branch_id_code', ''),
                    loan_id=loan_id,
                    col_id=col_id,
                    col_type=item.get('col_type', ''),
                    insert_date=timezone.now(),
                    update_date=timezone.now()
                )
                inconsistency_found = True

            # ຖ້າພົບຄວາມບໍ່ສອດຄ່ອງ ໃຫ້ຂ້າມການບັນທຶກເລກອດ໌ນີ້
            if inconsistency_found:
                continue

            try:
                mia_insert_date = datetime.strptime(item.get('mia_insert_date', ''), '%Y-%m-%d')
            except ValueError:
                mia_insert_date = None

            if item.get('col_type', '').lower() == "c2.2":
                CDL.objects.create(
                    id_file=cid,
                    c1=LCIC_code,
                    col_type=item.get('col_type', ''),
                    c2=com_enterprise_code,
                    c3=item.get('bnk_code', ''),
                    c4=item.get('bank_customer_ID', ''),
                    c5=item.get('branch_id_code', ''),
                    c6=item.get('loan_id', ''),
                    c7=item.get('col_id', ''),
                    c8=item.get('account_no', ''),
                    c9=item.get('account_type', ''),
                    c10=item.get('value', ''),
                    c11=item.get('value_unit', ''),
                    c12=item.get('mia_status', ''),
                    c13=mia_insert_date,  
                    c14=item.get('owner_name', ''),
                    c15=item.get('owner_surname', ''),
                    c16=item.get('owner_gender', ''),
                    c17=item.get('owner_lao_name', ''),
                    c18=item.get('owner_lao_surname', ''),
                    c39=item.get('segmentType',''),
                    period = file_period,
                    user_id=user_id,
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.1":
                CDL.objects.create(
                    id_file=cid,
                    c1=LCIC_code,
                    col_type=item.get('col_type', ''),
                    c2=com_enterprise_code,
                    c3=item.get('bnk_code', ''),
                    c4=item.get('bank_customer_ID', ''),
                    c5=item.get('branch_id_code', ''),
                    c6=item.get('loan_id', ''),
                    c7=item.get('col_id', ''),
                    c8=item.get('col_value', ''),
                    c9=item.get('land_plot_no', ''),
                    c10=item.get('land_area', ''),
                    c11=item.get('land_unit', ''),
                    c12=item.get('land_map_no', ''),
                    c13=item.get('land_document_no', ''),
                    c14=item.get('land_registry_book_no', ''),
                    c15=item.get('land_type', ''),
                    c16=item.get('land_no', ''),
                    c17=item.get('land_out_time', ''),
                    c18=item.get('land_regis_date', ''),
                    c19=item.get('place_regist', ''),
                    c20=item.get('plot_vilid', ''),
                    c21=item.get('plot_unit', ''),
                    c22=item.get('owner_name', ''),
                    # c23=item.get('owner_surname', ''),
                    c23=item.get('owner_birth_date', ''),
                    c24=item.get('owner_nationality', ''),
                    c25=item.get('owner_occupation', ''),
                    c26=item.get('current_vilid', ''),
                    c27=item.get('current_unit', ''),
                    c28=item.get('ownership_status', ''),
                    c29=item.get('spous_name', ''),
                    c30=item.get('spous_birth_date', ''),
                    c31=item.get('spous_nationality', ''),
                    c32=item.get('spous_occupation', ''),
                    c33=item.get('spous_acquisition', ''),
                    c39=item.get('segmentType',''),
                    c42=item.get('rel_insert_date', ''),
                    user_id=user_id,
                    period = file_period,
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.3":
                CDL.objects.create(
                    id_file=cid,
                    c1=LCIC_code,
                    col_type=item.get('col_type', ''),
                    c2=com_enterprise_code,
                    c3=item.get('bnk_code', ''),
                    c4=item.get('bank_customer_ID', ''),
                    c5=item.get('branch_id_code', ''),
                    c6=item.get('loan_id', ''),
                    c7=item.get('col_id', ''),
                    c8=item.get('machine_type', ''),
                    c9=item.get('machine_no', ''),
                    c10=item.get('value', ''),
                    c11=item.get('value_unit', ''),
                    c12=item.get('machine_status', ''),
                    c13=item.get('machine_insert_date', ''),
                    c14=item.get('owner_name', ''),
                    c15=item.get('owner_surname', ''),
                    c16=item.get('owner_gender', ''),
                    c17=item.get('owner_lao_name', ''),
                    c18=item.get('owner_lao_surname', ''),
                    c39=item.get('segmentType',''),
                    user_id=user_id,
                    period = file_period,
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.4":
                CDL.objects.create(
                    id_file=cid,
                    c1=LCIC_code,
                    col_type=item.get('col_type', ''),
                    c2=com_enterprise_code,
                    c3=item.get('bnk_code', ''),
                    c4=item.get('bank_customer_ID', ''),
                    c5=item.get('branch_id_code', ''),
                    c6=item.get('loan_id', ''),
                    c7=item.get('col_id', ''),
                    c8=item.get('ministry', ''),
                    c9=item.get('project_name_en', ''),
                    c10=item.get('project_name_la', ''),
                    c11=item.get('project_number', ''),
                    c12=item.get('value', ''),
                    c13=item.get('value_unit', ''),
                    c14=item.get('project_status', ''),
                    c15=item.get('project_insert_date', ''),
                    c16=item.get('owner_name', ''),
                    c17=item.get('owner_surname', ''),
                    c18=item.get('owner_gender', ''),
                    c19=item.get('owner_lao_name', ''),
                    c20=item.get('owner_lao_surname', ''),
                    c39=item.get('segmentType',''),
                    user_id=user_id,
                    period = file_period,
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.5":
                CDL.objects.create(
                    id_file=cid,
                    c1=LCIC_code,
                    col_type=item.get('col_type', ''),
                    c2=com_enterprise_code,
                    c3=item.get('bnk_code', ''),
                    c4=item.get('bank_customer_ID', ''),
                    c5=item.get('branch_id_code', ''),
                    c6=item.get('loan_id', ''),
                    c7=item.get('col_id', ''),
                    c8=item.get('plate_number', ''),
                    c9=item.get('engine_number', ''),
                    c10=item.get('body_number', ''),
                    c11=item.get('model', ''),
                    c12=item.get('value', ''),
                    c13=item.get('value_unit', ''),
                    c14=item.get('vehicle_status', ''),
                    c15=item.get('vehicle_insert_date', ''),
                    c16=item.get('owner_name', ''),
                    c17=item.get('owner_surname', ''),
                    c18=item.get('owner_gender', ''),
                    c19=item.get('owner_lao_name', ''),
                    c20=item.get('owner_lao_surname', ''),
                    c39=item.get('segmentType',''),
                    user_id=user_id,
                    period = file_period,
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.6":
                CDL.objects.create(
                    id_file=cid,
                    c1=LCIC_code,
                    col_type=item.get('col_type', ''),
                    c2=com_enterprise_code,
                    c3=item.get('bnk_code', ''),
                    c4=item.get('bank_customer_ID', ''),
                    c5=item.get('branch_id_code', ''),
                    c6=item.get('loan_id', ''),
                    c7=item.get('col_id', ''),
                    c8=item.get('value', ''),
                    c9=item.get('value_unit', ''),
                    c10=item.get('gua_ind_status', ''),
                    c11=item.get('gua_ind_insert_date', ''),
                    c12=item.get('guarantor_nationality', ''),
                    c13=item.get('gua_national_id', ''),
                    c14=item.get('national_id_expiry_date', ''),
                    c15=item.get('gua_passport_id', ''),
                    c16=item.get('gua_passport_expiry_date', ''),
                    c17=item.get('gua_familybook_id', ''),
                    c18=item.get('familybook_province_code', ''),
                    c19=item.get('familybook_issue_date', ''),
                    c20=item.get('gua_birthdate', ''),
                    c21=item.get('gua_gender',''),
                    c22=item.get('gua_name', ''),
                    c23=item.get('gua_surname', ''),
                    c24=item.get('gua_lao_name', ''),
                    c25=item.get('gua_lao_surname', ''),
                    c26=item.get('adress_number_street_eng', ''),
                    c27=item.get('adress_vill_eng', ''),
                    c28=item.get('adress_district_eng', ''),
                    c29=item.get('adress_number_street_la', ''),
                    c30=item.get('adress_vill_la', ''),
                    c31=item.get('adress_district_la', ''),
                    c32=item.get('adress_province_code', ''),
                    c33=item.get('owner_name', ''),
                    c34=item.get('owner_surname', ''),
                    c35=item.get('owner_gender', ''),
                    c36=item.get('owner_lao_name', ''),
                    c37=item.get('owner_lao_surname', ''),
                    c39=item.get('segmentType',''),
                    user_id=user_id,
                    period = file_period,
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.7":
                CDL.objects.create(
                    id_file=cid,
                    c1=LCIC_code,
                    col_type=item.get('col_type', ''),
                    c2=com_enterprise_code,
                    c3=item.get('bnk_code', ''),
                    c4=item.get('bank_customer_ID', ''),
                    c5=item.get('branch_id_code', ''),
                    c6=item.get('loan_id', ''),
                    c7=item.get('col_id', ''),
                    c8=item.get('weight', ''),
                    c9=item.get('value', ''),
                    c10=item.get('unit', ''),
                    c11=item.get('value_unit', ''),
                    c12=item.get('gld_status', ''),
                    c13=item.get('gld_insert_date', ''),
                    c14=item.get('owner_name', ''),
                    c15=item.get('owner_surname', ''),
                    c16=item.get('owner_gender', ''),
                    c17=item.get('owner_lao_name', ''),
                    c18=item.get('owner_lao_surname', ''),
                    c39=item.get('segmentType',''),
                    user_id=user_id,
                    period = file_period,
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.8":
                CDL.objects.create(
                    id_file=cid,
                    c1=LCIC_code,
                    col_type=item.get('col_type', ''),
                    c2=com_enterprise_code,
                    c3=item.get('bnk_code', ''),
                    c4=item.get('bank_customer_ID', ''),
                    c5=item.get('branch_id_code', ''),
                    c6=item.get('loan_id', ''),
                    c7=item.get('col_id', ''),
                    c8=item.get('value', ''),
                    c9=item.get('value_unit', ''),
                    c10=item.get('gua_com_status', ''),
                    c11=item.get('gua_com_insert_date', ''),
                    c12=item.get('gua_enterprise_code', ''),
                    c13=item.get('enterprise_regist_date', ''),
                    c14=item.get('enterprise_regist_place', ''),
                    c15=item.get('company_name', ''),
                    c16=item.get('company_lao_name', ''),
                    c17=item.get('enterprise_category', ''),
                    c18=item.get('owner_name', ''),
                    c19=item.get('owner_surname', ''),
                    c20=item.get('owner_gender', ''),
                    c21=item.get('owner_lao_name', ''),
                    c22=item.get('owner_lao_surname', ''),
                    c39=item.get('segmentType',''),
                    user_id=user_id,
                    period = file_period,
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )

        # ຄິດໄລ່ເປີເຊັນ error
        t2 = (error_records/total_records)*100 

        uploaded_data.percentage = t2
        uploaded_data.statussubmit = "2" if t2> 15 else "1"
        uploaded_data.save()
        
        print("t2",t2)
        
        # ແກ້ບັນຫາ: return ຄັ້ງດຽວເທົ່ານັ້ນ
        return JsonResponse({
            'status': 'success', 
            'message': 'File uploaded successfully',
            'warning': total_records,
            'error_records': error_records
        })
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'status': 'error', 'message': str(e)}
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

@csrf_exempt
@require_POST
def confirm_uploadc(request):
    try:
   
        CID = request.POST.get('CID')
        if not CID:
            return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)
        
        

        
        data_edits = CDL.objects.filter(id_file=CID)
        if not data_edits.exists():
            return JsonResponse({'status': 'error', 'message': 'No data found for the provided File ID'}, status=404)
        first_item = data_edits.first()
        current_bnk_code = first_item.c3
        current_period = first_item.period
        latest_c1_period = C1.objects.filter(bnk_code=current_bnk_code).order_by('-period').values_list('period', flat=True).first()
        if latest_c1_period is not None:
            try:
                current_period_int = int(current_period)
                latest_c1_period_int = int(latest_c1_period)
                if current_period_int < latest_c1_period_int:
                    Upload_File_C.objects.filter(CID=CID).update(statussubmit='1')
                    return JsonResponse({'status': 'error', 'message': 'File period is less than existing C1 period'}, status=408)
                
            except (ValueError, TypeError):
                

                pass

        
        for item in data_edits:
            col_type = item.col_type.lower()  
    
            if col_type == "c2.2" or col_type == "C2.2":
                obj, created = col_money_mia.objects.update_or_create(
                    LCIC_code=item.c1,
                    period=item.period,    
                    com_enterprise_code=item.c2,
                    bnk_code=item.c3,
                    bank_customer_ID=item.c4,
                    branch_id_code=item.c5,
                    loan_id=item.c6,
                    col_id=item.c7,
                
                    defaults={
                        'account_no': item.c8,
                        'period': item.period,
                        'user_id': item.user_id,
                        'col_type': item.col_type,
                        'account_type': item.c9,
                        'segmentType': item.c39,
                        'value_unit': item.c11,
                        'value': item.c10,
                        'mia_insert_date': item.c13,
                        'mia_status': item.c12,
                        'owner_gender': item.c16,
                        'owner_name': item.c14,
                        'owner_surname': item.c15,
                        'owner_lao_name': item.c17,
                        'owner_lao_surname': item.c18,
                        'id_file': CID,
                        'insert_date': timezone.now().date(),
                        'update_date': timezone.now().date()
                    }
                )

            elif col_type == "c2.1":
                
                obj, created = col_real_estates.objects.update_or_create(
                    LCIC_code=item.c1, 
                    com_enterprise_code=item.c2,
                    period=item.period,
                    bnk_code=item.c3,
                    bank_customer_ID=item.c4, 
                    branch_id_code=item.c5,
                    loan_id=item.c6,
                    col_id=item.c7,
                    defaults={
                        'col_value': item.c8,
                        'col_type': col_type,
                        'plot_vilid': item.c20,  
                        'segmentType': item.c39,
                        'plot_unit': item.c21,
                        'land_no': item.c16,
                        'land_out_time': item.c17,
                        'value_unit': item.c11,
                        'land_type': item.c15,
                        'col_area': item.c10,
                        'land_registry_book_no': item.c14,
                        'land_document_no': item.c13,
                        'place_regist_land': item.c19,
                        'land_map_no': item.c12,
                        'land_plot_no': item.c9,
                        'land_regis_date': item.c18,
                        'land_area': item.c10,
                        'land_unit': item.c11,
                        'owner_name': item.c22,
                        'owner_birth_date': item.c23,
                        'owner_nationality': item.c24,
                        'owner_occupation': item.c25,
                        'current_unit': item.c27,
                        'current_vilid': item.c26,
                        'spouse_name': item.c29,
                        'spouse_birth_date': item.c30,
                        'spouse_nationality': item.c31,
                        'spouse_occupation': item.c32,
                        'land_acquisition': item.c33,
                        'ownership_status': item.c28,
                        'user_id': item.user_id,
                    
                        'user_id': item.user_id,
                        'period': item.period,
                        'id_file': CID,
                        'insert_date': timezone.now(),
                        'update_date': timezone.now()
                    }
                )
            elif col_type == "c2.3":
                obj, created = col_equipment_eqi.objects.update_or_create(
                    LCIC_code=item.c1,  
                    com_enterprise_code=item.c2,
                    period=item.period,
                    bnk_code=item.c3,
                    bank_customer_ID=item.c4,
                    branch_id_code=item.c5,
                    loan_id=item.c6,
                    col_id=item.c7,
                    defaults={
                        'machine_type': item.c8,
                        'machine_no': item.c9,
                        'value': item.c10,
                        'value_unit': item.c11,
                        'machine_status': item.c12,
                        'machine_insert_date': item.c13,
                        'owner_name': item.c14,
                        'owner_surname': item.c15,
                        'owner_gender': item.c16,
                        'owner_lao_name': item.c17,
                        'owner_lao_surname': item.c18,
                        'segmentType': item.c39,
                        'user_id': item.user_id,
                        'period': item.period,
                        'id_file': CID,
                        'update_date': timezone.now(),
                        'insert_date': timezone.now()
                    }
                )
            elif col_type == "c2.4":
                obj, created = col_project_prj.objects.update_or_create(
                    LCIC_code=item.c1,  
                    com_enterprise_code=item.c2,
                    period=item.period,
                    bnk_code=item.c3,
                    bank_customer_ID=item.c4,
                    branch_id_code=item.c5,
                    loan_id=item.c6,
                    col_id=item.c7,
                    defaults={
                        'ministry': item.c8,  
                        'project_name_en': item.c9, 
                        'project_name_la': item.c10,
                        'project_number': item.c11,
                        'value': item.c12,
                        'value_unit': item.c13,
                        'project_status': item.c14,
                        'project_insert_date': item.c15,
                        'owner_name': item.c16,
                        'owner_surname': item.c17,
                        'owner_gender': item.c18,
                        'owner_lao_name': item.c19,
                        'owner_lao_surname': item.c20,
                        'segmentType': item.c39,
                        'user_id': item.user_id,
                        'period': item.period,
                        'id_file': CID,
                        'insert_date': timezone.now(),
                        'update_date': timezone.now()
                    }
                )
            elif col_type == "c2.5":
                 obj, created = col_vechicle_veh.objects.update_or_create(
                     LCIC_code=item.c1,  
                     com_enterprise_code=item.c2,
                     period=item.period,
                     bnk_code=item.c3,
                     bank_customer_ID=item.c4,
                     branch_id_code=item.c5,
                     loan_id=item.c6,
                     col_id=item.c7,
                     defaults={
                         'plate_number': item.c8,
                         'engine_number': item.c9,
                         'body_number': item.c10,
                         'model': item.c11,
                         'value': item.c12,
                         'value_unit': item.c13,
                         'vehicle_status': item.c14,
                         'vehicle_insert_date': item.c15,
                         'owner_name': item.c16,
                         'owner_surname': item.c17,
                         'owner_gender': item.c18,
                         'owner_lao_name': item.c19,
                         'owner_lao_surname': item.c20,
                         'segmentType': item.c39,
                         'user_id': item.user_id,
                         'period': item.period,
                         'id_file': CID,
                         'insert_date': timezone.now(),
                         'update_date': timezone.now()


                     }
                 )
            elif col_type == "c2.6":
                obj, created = col_guarantor_gua.objects.update_or_create(
                    LCIC_code=item.c1,  
                    com_enterprise_code=item.c2,
                    period=item.period,
                    bnk_code=item.c3,
                    bank_customer_ID=item.c4,
                    branch_id_code=item.c5,
                    loan_id=item.c6,
                    col_id=item.c7,
                    defaults={
                        'value': item.c8,
                        'value_unit': item.c9,
                        'gua_ind_status': item.c10,
                        'gua_ind_insert_date': item.c11,
                        'guarantor_nationality': item.c12,
                        'gua_national_id': item.c13,
                        'national_id_expiry_date': item.c14,
                        'gua_passport': item.c15,
                        'passport_expiry_date': item.c16,
                        'gua_familybook_id': item.c17,
                        'familybook_provision_code': item.c18,
                        'familybook_issue_date': item.c19,
                        'gua_birthday': item.c20,
                        'gua_gender': item.c21,
                        'gua_name': item.c22,
                        'gua_surname': item.c23,
                        'gua_lao_name': item.c24,
                        'gua_lao_surname': item.c25,
                        'address_number_street_eng': item.c26,
                        'address_vill_eng': item.c27,
                        'address_district_eng': item.c28,
                        'address_number_street_la': item.c29,
                        'address_vill_la': item.c30,
                        'address_district_la': item.c31,
                        'address_province_code': item.c32,
                        'owner_name': item.c33,
                        'owner_surname': item.c34,
                        'owner_gender': item.c35,
                        'owner_lao_name': item.c36,
                        'owner_lao_surname': item.c37,
                        'segmentType': item.c39,
                        'user_id': item.user_id,
                        'period': item.period,
                        'id_file': CID,
                        'insert_date': timezone.now(),
                        'update_date': timezone.now()


                    }
                )
            elif col_type == "c2.7":
                obj, created = col_goldsilver_gold.objects.update_or_create(
                    LCIC_code=item.c1, 
                    com_enterprise_code=item.c2,  
                    period=item.period,
                    bnk_code=item.c3,
                    bank_customer_ID=item.c4,
                    branch_id_code=item.c5,
                    loan_id=item.c6,
                    col_id=item.c7,
                    defaults={
                        'weight': item.c8,
                        'value': item.c9,
                        'unit': item.c10,
                        'value_unit': item.c11,
                        'gld_status': item.c12,
                        'gld_insert_date': item.c13,
                        'owner_name': item.c14,
                        'owner_surname': item.c15,
                        'owner_gender': item.c16,
                        'owner_lao_name': item.c17,
                        'owner_lao_surname': item.c18,
                        'segmentType': item.c39,
                        'user_id': item.user_id,
                        'period': item.period,
                        'id_file': CID,
                        'insert_date': timezone.now,
                        'update_date': timezone.now

                    }
                )
            elif col_type == "c2.8":
                obj, created = col_guarantor_com.objects.update_or_create(
                    LCIC_code=item.c1,  
                    com_enterprise_code=item.c2,
                    period=item.period,
                    bnk_code=item.c3,
                    bank_customer_ID=item.c4,
                    branch_id_code=item.c5,
                    loan_id=item.c6,
                    col_id=item.c7,

                    defaults={
                        'value': item.c8,
                        'value_unit': item.c9,
                        'gua_com_status': item.c10,
                        'gua_com_insert_date': item.c11,
                        'gua_enterprise_code': item.c12,
                        'enterprise_regist_date': item.c13,
                        'enterprise_regist_place': item.c14,
                        'company_name': item.c15,
                        'company_lao_name': item.c16,
                        'enterprise_category': item.c17,
                        'owner_name': item.c18,
                        'owner_surname': item.c19,
                        'owner_gender': item.c20,
                        'owner_lao_name': item.c21,
                        'owner_lao_surname': item.c22,
                        'segmentType': item.c39,
                        'user_id': item.user_id,
                        'period': item.period,
                        'insert_date': timezone.now(),
                        'id_file': CID,
                        'update_date': timezone.now()


                    }
                )
            C1.objects.update_or_create(
                LCIC_code=item.c1,  
                com_enterprise_code=item.c2,
                bnk_code=item.c3,
                bank_customer_ID=item.c4,
                branch_id_code=item.c5,
                loan_id=item.c6,
                col_id=item.c7,
                defaults={
                    'segmentType': item.c39,
                    'user_id': item.user_id,
                    'period': item.period,
                    'col_type': item.col_type,
                    'id_file': CID,
                    'insert_date': timezone.now(),
                    
                    

                }

            )
        Upload_File_C.objects.filter(CID=CID).update(statussubmit='0')


        return JsonResponse({'status': 'success', 'message': 'File processed successfully'})
                  

    except Exception as e:
        print(f"An error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
from django.db import connection
from django.apps import apps

@csrf_exempt
@require_POST
def unload_data(request):
    try:
       
        CID = request.POST.get('CID')
        if not CID:
            return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)
        
       
        c1_records = C1.objects.filter(id_file=CID)
        if not c1_records.exists():
            return JsonResponse({'status': 'error', 'message': 'No data found for the provided File ID'}, status=404)
        if c1_records.exists():
            first_record = c1_records.first()
            bnk_code = first_record.bnk_code
            current_period = first_record.period
            latest_period = C1.objects.filter(bnk_code=bnk_code).exclude(id_file=CID).order_by('-period').values_list('period', flat=True).first()
            if latest_period is not None:
                try:
                    current_period_int = int(current_period)
                    latest_period_int = int(latest_period)
                    if current_period_int < latest_period_int:
                        Upload_File_C.objects.filter(CID=CID).update(statussubmit='0')
                        return JsonResponse({
                            'status': 'error', 
                            'message': 'ທ່ານບໍ່ສາມາດອັນໂຫຼດຂໍ້ມູນໄດ້ເພາະວ່າຍັງມີຂໍ້ມູນທີ່ໃໝ່ກວ່າຢູ່ໃນລະບົບ ທ່ານຕອ້ງອັນຂໍ້ມູນຍອ້ນຫຼັງຕາມລຳດັບຈື່ງສາມາດອັນໂຫຼດໄດ້',
                        }, status=406)
                    
                except (ValueError, TypeError):
                    pass
            
        
       
        records_info = []
        for record in c1_records:
            records_info.append({
                'LCIC_code': record.LCIC_code,
                'com_enterprise_code': record.com_enterprise_code,
                'bnk_code': record.bnk_code,
                'bank_customer_ID': record.bank_customer_ID,
                'branch_id_code': record.branch_id_code,
                'loan_id': record.loan_id,
                'col_id': record.col_id,
                'col_type': record.col_type.lower(),
                'segmentType': record.segmentType,
                'period': record.period,
                'user_id': record.user_id
            })
        
        
        c1_records.delete()
        
       
        restored_count = 0
        error_count = 0
        
   
        for record_data in records_info:
            col_type = record_data['col_type']
            lcic = record_data['LCIC_code']
            com_code = record_data['com_enterprise_code']
            bnk = record_data['bnk_code']
            cust_id = record_data['bank_customer_ID']
            branch = record_data['branch_id_code']
            loan = record_data['loan_id']
            
            try:
                
                latest_record = None
                
                if col_type == "c2.1":
                    latest_record = col_real_estates.objects.filter(
                        LCIC_code=lcic,
                        com_enterprise_code=com_code,
                        bnk_code=bnk,
                        bank_customer_ID=cust_id,
                        branch_id_code=branch,
                        loan_id=loan
                    ).exclude(id_file=CID).order_by('-id').first()
                    
                elif col_type == "c2.2":
                    latest_record = col_money_mia.objects.filter(
                        LCIC_code=lcic,
                        com_enterprise_code=com_code,
                        bnk_code=bnk,
                        bank_customer_ID=cust_id,
                        branch_id_code=branch,
                        loan_id=loan
                    ).exclude(id_file=CID).order_by('-id').first()
                    
                elif col_type == "c2.3":
                    latest_record = col_equipment_eqi.objects.filter(
                        LCIC_code=lcic,
                        com_enterprise_code=com_code,
                        bnk_code=bnk,
                        bank_customer_ID=cust_id,
                        branch_id_code=branch,
                        loan_id=loan
                    ).exclude(id_file=CID).order_by('-id').first()
                    
                elif col_type == "c2.4":
                    latest_record = col_project_prj.objects.filter(
                        LCIC_code=lcic,
                        com_enterprise_code=com_code,
                        bnk_code=bnk,
                        bank_customer_ID=cust_id,
                        branch_id_code=branch,
                        loan_id=loan
                    ).exclude(id_file=CID).order_by('-id').first()
                    
                elif col_type == "c2.5":
                    latest_record = col_vechicle_veh.objects.filter(
                        LCIC_code=lcic,
                        com_enterprise_code=com_code,
                        bnk_code=bnk,
                        bank_customer_ID=cust_id,
                        branch_id_code=branch,
                        loan_id=loan
                    ).exclude(id_file=CID).order_by('-id').first()
                    
                elif col_type == "c2.6":
                    latest_record = col_guarantor_gua.objects.filter(
                        LCIC_code=lcic,
                        com_enterprise_code=com_code,
                        bnk_code=bnk,
                        bank_customer_ID=cust_id,
                        branch_id_code=branch,
                        loan_id=loan
                    ).exclude(id_file=CID).order_by('-id').first()
                    
                elif col_type == "c2.7":
                    latest_record = col_goldsilver_gold.objects.filter(
                        LCIC_code=lcic,
                        com_enterprise_code=com_code,
                        bnk_code=bnk,
                        bank_customer_ID=cust_id,
                        branch_id_code=branch,
                        loan_id=loan
                    ).exclude(id_file=CID).order_by('-id').first()
                    
                elif col_type == "c2.8":
                    latest_record = col_guarantor_com.objects.filter(
                        LCIC_code=lcic,
                        com_enterprise_code=com_code,
                        bnk_code=bnk,
                        bank_customer_ID=cust_id,
                        branch_id_code=branch,
                        loan_id=loan
                    ).exclude(id_file=CID).order_by('-id').first()
                
               
                if latest_record:
                    try:
                       
                        new_c1 = C1(
                            LCIC_code=lcic,
                            com_enterprise_code=com_code,
                            bnk_code=bnk,
                            bank_customer_ID=cust_id,
                            branch_id_code=branch,
                            loan_id=loan,
                            col_id=record_data['col_id'],
                            segmentType=record_data['segmentType'],
                            user_id=record_data['user_id'],
                            # period=record_data['period'],
                            col_type=record_data['col_type'].upper(),
                            insert_date=timezone.now(),
                            update_date=timezone.now(),
                            id_file=latest_record.id_file,
                            period=latest_record.period,
                            lcicID='',  
                            collateral_status='',  
                            data_status=''  
                        )
                        new_c1.save()
                        restored_count += 1
                    except Exception as create_error:
                        print(f"Error creating C1 record: {create_error}")
                        error_count += 1
                        
            except Exception as e:
                print(f"Error processing record: {e}")
                error_count += 1
        
        
        col_real_estates.objects.filter(id_file=CID).delete()
        col_money_mia.objects.filter(id_file=CID).delete() 
        col_equipment_eqi.objects.filter(id_file=CID).delete()
        col_project_prj.objects.filter(id_file=CID).delete()
        col_vechicle_veh.objects.filter(id_file=CID).delete()
        col_guarantor_gua.objects.filter(id_file=CID).delete()
        col_goldsilver_gold.objects.filter(id_file=CID).delete()
        col_guarantor_com.objects.filter(id_file=CID).delete()
        
       
        Upload_File_C.objects.filter(CID=CID).update(statussubmit='5')  
        
       
        message = f'Unload completed successfully. Restored {restored_count} records with latest data.'
        if error_count > 0:
            message += f' There were {error_count} errors during processing.'
            
        return JsonResponse({'status': 'success', 'message': message})
    
    except Exception as e:
        error_message = str(e)
        print(f"An error occurred during unload: {error_message}")
        return JsonResponse({'status': 'error', 'message': error_message}, status=500)

def get_latest_real_estates(record, exclude_id_file):
    try:
        return col_real_estates.objects.filter(
            LCIC_code=record['LCIC_code'],
            com_enterprise_code=record['com_enterprise_code'],
            bnk_code=record['bnk_code'],
            bank_customer_ID=record['bank_customer_ID'],
            branch_id_code=record['branch_id_code'],
            loan_id=record['loan_id'],
            col_id=record['col_id']
        ).exclude(id_file=exclude_id_file).order_by('-id').first()
    except:
        return None

def get_latest_money_mia(record, exclude_id_file):
    try:
        return col_money_mia.objects.filter(
            LCIC_code=record['LCIC_code'],
            com_enterprise_code=record['com_enterprise_code'],
            bnk_code=record['bnk_code'],
            bank_customer_ID=record['bank_customer_ID'],
            branch_id_code=record['branch_id_code'],
            loan_id=record['loan_id'],
            col_id=record['col_id']
        ).exclude(id_file=exclude_id_file).order_by('-id').first()
    except:
        return None

def get_latest_equipment_eqi(record, exclude_id_file):
    try:
        return col_equipment_eqi.objects.filter(
            LCIC_code=record['LCIC_code'],
            com_enterprise_code=record['com_enterprise_code'],
            bnk_code=record['bnk_code'],
            bank_customer_ID=record['bank_customer_ID'],
            branch_id_code=record['branch_id_code'],
            loan_id=record['loan_id'],
            col_id=record['col_id']
        ).exclude(id_file=exclude_id_file).order_by('-id').first()
    except:
        return None

def get_latest_project_prj(record, exclude_id_file):
    try:
        return col_project_prj.objects.filter(
            LCIC_code=record['LCIC_code'],
            com_enterprise_code=record['com_enterprise_code'],
            bnk_code=record['bnk_code'],
            bank_customer_ID=record['bank_customer_ID'],
            branch_id_code=record['branch_id_code'],
            loan_id=record['loan_id'],
            col_id=record['col_id']
        ).exclude(id_file=exclude_id_file).order_by('-id').first()
    except:
        return None

def get_latest_vechicle_veh(record, exclude_id_file):
    try:
        return col_vechicle_veh.objects.filter(
            LCIC_code=record['LCIC_code'],
            com_enterprise_code=record['com_enterprise_code'],
            bnk_code=record['bnk_code'],
            bank_customer_ID=record['bank_customer_ID'],
            branch_id_code=record['branch_id_code'],
            loan_id=record['loan_id'],
            col_id=record['col_id']
        ).exclude(id_file=exclude_id_file).order_by('-id').first()
    except:
        return None

def get_latest_guarantor_gua(record, exclude_id_file):
    try:
        return col_guarantor_gua.objects.filter(
            LCIC_code=record['LCIC_code'],
            com_enterprise_code=record['com_enterprise_code'],
            bnk_code=record['bnk_code'],
            bank_customer_ID=record['bank_customer_ID'],
            branch_id_code=record['branch_id_code'],
            loan_id=record['loan_id'],
            col_id=record['col_id']
        ).exclude(id_file=exclude_id_file).order_by('-id').first()
    except:
        return None

def get_latest_goldsilver_gold(record, exclude_id_file):
    try:
        return col_goldsilver_gold.objects.filter(
            LCIC_code=record['LCIC_code'],
            com_enterprise_code=record['com_enterprise_code'],
            bnk_code=record['bnk_code'],
            bank_customer_ID=record['bank_customer_ID'],
            branch_id_code=record['branch_id_code'],
            loan_id=record['loan_id'],
            col_id=record['col_id']
        ).exclude(id_file=exclude_id_file).order_by('-id').first()
    except:
        return None

def get_latest_guarantor_com(record, exclude_id_file):
    try:
        return col_guarantor_com.objects.filter(
            LCIC_code=record['LCIC_code'],
            com_enterprise_code=record['com_enterprise_code'],
            bnk_code=record['bnk_code'],
            bank_customer_ID=record['bank_customer_ID'],
            branch_id_code=record['branch_id_code'],
            loan_id=record['loan_id'],
            col_id=record['col_id']
        ).exclude(id_file=exclude_id_file).order_by('-id').first()
    except:
        return None
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# from django.utils import timezone

# @csrf_exempt
# @require_POST
# def confirm_uploadc(request):
#     try:
   
#         CID = request.POST.get('CID')
#         if not CID:
#             return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

        
#         data_edits = CDL.objects.filter(id_file=CID)
#         if not data_edits.exists():
#             return JsonResponse({'status': 'error', 'message': 'No data found for the provided File ID'}, status=404)

        
#         for item in data_edits:
#             col_type = item.col_type.lower()  # ບໍ່ໃຊ້ item.get()
    
#             if col_type == "c2.2" or col_type == "C2.2":
#                 obj, created = col_money_mia.objects.update_or_create(
#                     lcicID=item.c1,  # ບໍ່ໃຊ້ item.get('c1', '')
#                     com_enterprise_code=item.c2,
#                     bnk_code=item.c3,
#                     bank_customer_ID=item.c4,
#                     branch_id_code=item.c5,
#                     loan_id=item.c6,
#                     col_id=item.c7,
#                     defaults={
#                         'account_no': item.c8,
#                         'period': item.period,
#                         'user_id': item.user_id,
#                         'col_type': item.col_type,
#                         'account_type': item.c9,
#                         'segmentType': item.c39,
#                         'value_unit': item.c11,
#                         'value': item.c10,
#                         'mia_insert_date': item.c13,
#                         'mia_status': item.c12,
#                         'owner_gender': item.c16,
#                         'owner_name': item.c14,
#                         'owner_surname': item.c15,
#                         'owner_lao_name': item.c17,
#                         'owner_lao_surname': item.c18,
#                         'id_file': CID,
                        
#                         'insert_date': timezone.now().date(),
#                         'update_date': timezone.now().date()
#                     }
#                 )

#             elif col_type == "c2.1":
                
#                 obj, created = col_real_estates.objects.update_or_create(
#                     lcicID=item.c1,
#                     com_enterprise_code=item.c2,
#                     bnk_code=item.c3,
#                     bank_customer_ID=item.c4, 
#                     branch_id_code=item.c5,
#                     loan_id=item.c6,
#                     col_id=item.c7,
#                     defaults={
#                         'col_value': item.c8,
#                         'col_type': col_type,
#                         'plot_vilid': item.c20,  
#                         'segmentType': item.c39,
#                         'plot_unit': item.c21,
#                         'land_no': item.c16,
#                         'land_out_time': item.c17,
#                         'value_unit': item.c11,
#                         'land_type': item.c15,
#                         'col_area': item.c10,
#                         'land_registry_book_no': item.c14,
#                         'land_document_no': item.c13,
#                         'place_regist_land': item.c19,
#                         'land_map_no': item.c12,
#                         'land_plot_no': item.c9,
#                         'land_regis_date': item.c18,
#                         'land_area': item.c10,
#                         'land_unit': item.c11,
#                         'owner_name': item.c22,
#                         'owner_birth_date': item.c23,
#                         'owner_nationality': item.c24,
#                         'owner_occupation': item.c25,
#                         'current_unit': item.c27,
#                         'current_vilid': item.c26,
#                         'spouse_name': item.c29,
#                         'spouse_birth_date': item.c30,
#                         'spouse_nationality': item.c31,
#                         'spouse_occupation': item.c32,
#                         'land_acquisition': item.c33,
#                         'ownership_status': item.c28,
#                         'user_id': item.user_id,
                    
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'id_file': CID,
#                         'insert_date': timezone.now(),
#                         'update_date': timezone.now()
#                     }
#                 )
#             elif col_type == "c2.3":
#                 obj, created = col_equipment_eqi.objects.update_or_create(
#                     lcicID=item.c1,  
#                     com_enterprise_code=item.c2,
#                     bnk_code=item.c3,
#                     bank_customer_ID=item.c4,
#                     branch_id_code=item.c5,
#                     loan_id=item.c6,
#                     col_id=item.c7,
#                     defaults={
#                         'machine_type': item.c8,
#                         'machine_no': item.c9,
#                         'value': item.c10,
#                         'value_unit': item.c11,
#                         'machine_status': item.c12,
#                         'machine_insert_date': item.c13,
#                         'owner_name': item.c14,
#                         'owner_surname': item.c15,
#                         'owner_gender': item.c16,
#                         'owner_lao_name': item.c17,
#                         'owner_lao_surname': item.c18,
#                         'segmentType': item.c39,
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'id_file': CID,
#                         'update_date': timezone.now(),
#                         'insert_date': timezone.now()
#                     }
#                 )
#             elif col_type == "c2.4":
#                 obj, created = col_project_prj.objects.update_or_create(
#                     lcicID=item.c1,  # ບໍ່ໃຊ້ item.get('c1', '')
#                     com_enterprise_code=item.c2,  # ບໍ່ໃຊ້ item.get('c2', '')
#                     bnk_code=item.c3,
#                     bank_customer_ID=item.c4,
#                     branch_id_code=item.c5,
#                     loan_id=item.c6,
#                     col_id=item.c7,
#                     defaults={
#                         'ministry': item.c8,  
#                         'project_name_en': item.c9, 
#                         'project_name_la': item.c10,
#                         'project_number': item.c11,
#                         'value': item.c12,
#                         'value_unit': item.c13,
#                         'project_status': item.c14,
#                         'project_insert_date': item.c15,
#                         'owner_name': item.c16,
#                         'owner_surname': item.c17,
#                         'owner_gender': item.c18,
#                         'owner_lao_name': item.c19,
#                         'owner_lao_surname': item.c20,
#                         'segmentType': item.c39,
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'id_file': CID,
#                         'insert_date': timezone.now(),
#                         'update_date': timezone.now()
#                     }
#                 )
#             elif col_type == "c2.5":
#                  obj, created = col_vechicle_veh.objects.update_or_create(
#                      lcicID=item.c1,  
#                      com_enterprise_code=item.c2,
#                      bnk_code=item.c3,
#                      bank_customer_ID=item.c4,
#                      branch_id_code=item.c5,
#                      loan_id=item.c6,
#                      col_id=item.c7,
#                      defaults={
#                          'plate_number': item.c8,
#                          'engine_number': item.c9,
#                          'body_number': item.c10,
#                          'model': item.c11,
#                          'value': item.c12,
#                          'value_unit': item.c13,
#                          'vehicle_status': item.c14,
#                          'vehicle_insert_date': item.c15,
#                          'owner_name': item.c16,
#                          'owner_surname': item.c17,
#                          'owner_gender': item.c18,
#                          'owner_lao_name': item.c19,
#                          'owner_lao_surname': item.c20,
#                          'segmentType': item.c39,
#                          'user_id': item.user_id,
#                          'period': item.period,
#                          'id_file': CID,
#                          'insert_date': timezone.now(),
#                          'update_date': timezone.now()


#                      }
#                  )
#             elif col_type == "c2.6":
#                 obj, created = col_guarantor_gua.objects.update_or_create(
#                     lcicID=item.c1,  
#                     com_enterprise_code=item.c2,
#                     bnk_code=item.c3,
#                     bank_customer_ID=item.c4,
#                     branch_id_code=item.c5,
#                     loan_id=item.c6,
#                     col_id=item.c7,
#                     defaults={
#                         'value': item.c8,
#                         'value_unit': item.c9,
#                         'gua_ind_status': item.c10,
#                         'gua_ind_insert_date': item.c11,
#                         'guarantor_nationality': item.c12,
#                         'gua_national_id': item.c13,
#                         'national_id_expiry_date': item.c14,
#                         'gua_passport_id': item.c15,
#                         'gua_passport_expiry_date': item.c16,
#                         'gua_familybook_id': item.c17,
#                         'familybook_province_code': item.c18,
#                         'familybook_issue_date': item.c19,
#                         'gua_birthdate': item.c20,
#                         'gua_gender': item.c21,
#                         'gua_name': item.c22,
#                         'gua_surname': item.c23,
#                         'gua_lao_name': item.c24,
#                         'gua_lao_surname': item.c25,
#                         'adress_number_street_eng': item.c26,
#                         'adress_vill_eng': item.c27,
#                         'adress_district_eng': item.c28,
#                         'adress_number_street_la': item.c29,
#                         'adress_vill_la': item.c30,
#                         'adress_district_la': item.c31,
#                         'adress_province_code': item.c32,
#                         'owner_name': item.c33,
#                         'owner_surname': item.c34,
#                         'owner_gender': item.c35,
#                         'owner_lao_name': item.c36,
#                         'owner_lao_surname': item.c37,
#                         'segmentType': item.c39,
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'id_file': CID,
#                         'insert_date': timezone.now(),
#                         'update_date': timezone.now()


#                     }
#                 )
#             elif col_type == "c2.7":
#                 obj, created = col_goldsilver_gold.objects.update_or_create(
#                     lcicID=item.c1,
#                     com_enterprise_code=item.c2,  
#                     bnk_code=item.c3,
#                     bank_customer_ID=item.c4,
#                     branch_id_code=item.c5,
#                     loan_id=item.c6,
#                     col_id=item.c7,
#                     defaults={
#                         'weight': item.c8,
#                         'value': item.c9,
#                         'unit': item.c10,
#                         'value_unit': item.c11,
#                         'gld_status': item.c12,
#                         'gld_insert_date': item.c13,
#                         'owner_name': item.c14,
#                         'owner_surname': item.c15,
#                         'owner_gender': item.c16,
#                         'owner_lao_name': item.c17,
#                         'owner_lao_surname': item.c18,
#                         'segmentType': item.c39,
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'id_file': CID,
#                         'insert_date': timezone.now,
#                         'update_date': timezone.now

#                     }
#                 )
#             elif col_type == "c2.8":
#                 obj, created = col_guarantor_com.objects.update_or_create(
#                     lcicID=item.c1,
#                     com_enterprise_code=item.c2,
#                     bnk_code=item.c3,
#                     bank_customer_ID=item.c4,
#                     branch_id_code=item.c5,
#                     loan_id=item.c6,
#                     col_id=item.c7,
#                     defaults={
#                         'value': item.c8,
#                         'value_unit': item.c9,
#                         'gua_com_status': item.c10,
#                         'gua_com_insert_date': item.c11,
#                         'gua_enterprise_code': item.c12,
#                         'enterprise_regist_date': item.c13,
#                         'enterprise_regist_place': item.c14,
#                         'company_name': item.c15,
#                         'company_lao_name': item.c16,
#                         'enterprise_category': item.c17,
#                         'owner_name': item.c18,
#                         'owner_surname': item.c19,
#                         'owner_gender': item.c20,
#                         'owner_lao_name': item.c21,
#                         'owner_lao_surname': item.c22,
#                         'segmentType': item.c39,
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'insert_date': timezone.now(),
#                         'id_file': CID,
#                         'update_date': timezone.now()


#                     }
#                 )
#             C1.objects.update_or_create(
#                 lcicID=item.c1,
#                 com_enterprise_code=item.c2,
#                 bnk_code=item.c3,
#                 bank_customer_ID=item.c4,
#                 branch_id_code=item.c5,
#                 loan_id=item.c6,
#                 col_id=item.c7,
#                 defaults={
#                     'segmentType': item.c39,
#                     'user_id': item.user_id,
#                     'period': item.period,
#                     'col_type': item.col_type,
#                     'id_file': CID,
#                     'insert_date': timezone.now(),
                    
                    

#                 }

#             )


#         return JsonResponse({'status': 'success', 'message': 'File processed successfully'})

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


            
            
            

            # elif col_type == "c2.4" or col_type == "C2.4":
            #     obj, created = col_project_prj.objects.update_or_create(
            #         bank_customer_ID=item.get('bank_customer_ID', ''),
            #         lcicID=lcicID,
            #         com_enterprise_code=com_enterprise_code,
            #         bnk_code=item.get('bnk_code', ''),
            #         branch_id_code=item.get('branch_id_code', ''),
            #         loan_id=item.get('loan_id', ''),
            #         col_id=item.get('col_id', ''),
            #         defaults={
            #             'project_type': item.get('project_type', ''),
            #             'project_name_en': item.get('project_name_en', ''),
            #             'segmentType': item.get('segmentType', ''),
            #             'col_type': item.get('col_type', ''),
            #             'period': item.get('period', ''),
            #             'user_id': item.get('user_id', ''),
            #             'ministry': item.get('ministry', ''),
            #             'project_namber': item.get('project_namber', ''),
            #             'value_unit': item.get('value_unit', ''),
            #             'project_name_la': item.get('project_name_la', ''),
            #             'value': item.get('value', ''),
            #             'project_status': item.get('project_status', ''),
            #             'owner_gender': item.get('owner_gender', ''),
            #             'owner_name': item.get('owner_name', ''),
            #             'owner_surname': item.get('owner_surname', ''),
            #             'owner_lao_name': item.get('owner_lao_name', ''),
            #             'owner_lao_surname': item.get('owner_lao_surname', ''),
            #             'id_file': CID,

            #             'insert_date': timezone.now().date(),
            #             'update_date': timezone.now().date()
            #         }
            #     )
            
            # elif col_type == "c2.5" or col_type == "C2.5":
            #     obj, created = col_vechicle_veh.objects.update_or_create(
            #         bank_customer_ID=item.get('bank_customer_ID', ''),
            #         lcicID=lcicID,
            #         com_enterprise_code=com_enterprise_code,
            #         bnk_code=item.get('bnk_code', ''),
            #         branch_id_code=item.get('branch_id_code', ''),
            #         loan_id=item.get('loan_id', ''),
            #         col_id=item.get('col_id', ''),
            #         defaults={
            #             'vehicle_type': item.get('vehicle_type', ''),
            #             'license_plate_no': item.get('license_plate_no', ''),
            #             'segmentType': item.get('segmentType', ''),
            #             'col_type': item.get('col_type', ''),
            #             'value': item.get('value', ''),
            #             'value_unit': item.get('value_unit', ''),
            #             'user_id': item.get('user_id', ''),
            #             'period': item.get('period', ''),
            #             # 'vehicle_value_unit': item.get('vehicle_value_unit', ''),
            #             'vehicle_status': item.get('vehicle_status', ''),
            #             'owner_gender': item.get('owner_gender', ''),
            #             'owner_name': item.get('owner_name', ''),
            #             'owner_surname': item.get('owner_surname', ''),
            #             'owner_lao_name': item.get('owner_lao_name', ''),
            #             'owner_lao_surname': item.get('owner_lao_surname', ''),
            #             'id_file': CID,
            #             'insert_date': timezone.now().date(),
            #             'update_date': timezone.now().date()
            #         }
            #     )
            
            # elif col_type == "c2.6" or col_type == "C2.6":
            #     obj, created = col_guarantor_gua.objects.update_or_create(
            #         bank_customer_ID=item.get('bank_customer_ID', ''),
            #         lcicID=lcicID,
            #         com_enterprise_code=com_enterprise_code,
            #         bnk_code=item.get('bnk_code', ''),
            #         branch_id_code=item.get('branch_id_code', ''),
            #         loan_id=item.get('loan_id', ''),
            #         col_id=item.get('col_id', ''),
            #         defaults={
            #             'guarantor_name': item.get('guarantor_name', ''),
            #             'segmentType': item.get('segmentType', ''),
            #             'user_id': item.get('user_id', ''),
            #             'period': item.get('period', ''),
            #             'col_type': item.get('col_type', ''),
            #             'guarantor_type': item.get('guarantor_type', ''),
            #             'guarantor_no': item.get('guarantor_no', ''),
            #             'value_unit': item.get('value_unit', ''),   
            #             'value': item.get('value', ''),
            #             'id_file':CID,
            #             'insert_date': timezone.now().date(),
            #             'update_date': timezone.now().date()
            #         }
            #     )
            
            # elif col_type == "c2.8" or col_type == "C2.8":
            #     obj, created = col_goldsilver_gold.objects.update_or_create(
            #         bank_customer_ID=item.get('bank_customer_ID', ''),
            #         lcicID=lcicID,
            #         com_enterprise_code=com_enterprise_code,
            #         bnk_code=item.get('bnk_code', ''),
            #         branch_id_code=item.get('branch_id_code', ''),
            #         loan_id=item.get('loan_id', ''),
            #         col_id=item.get('col_id', ''),
            #         defaults={
            #             'gold_type': item.get('gold_type', ''),
            #             'gold_weight': item.get('gold_weight', ''),
            #             'segmentType': item.get('segmentType', ''),
            #             'col_type': item.get('col_type', ''),
            #             'user_id': item.get('user_id', ''),
            #             'period':item.get('period', ''),
            #             'gold_purity': item.get('gold_purity', ''),
            #             'value': item.get('value', ''),
            #             'id_file': CID,
            #             'gold_status': item.get('gold_status', ''),
            #             'owner_gender': item.get('owner_gender', ''),
            #             'value_unit': item.get('value_unit', ''),
            #             'owner_name': item.get('owner_name', ''),
            #             'owner_surname': item.get('owner_surname', ''),
            #             'owner_lao_name': item.get('owner_lao_name', ''),
            #             'owner_lao_surname': item.get('owner_lao_surname', ''),
            #             'insert_date': timezone.now().date(),
            #             'update_date': timezone.now().date()
            #         }
            #     )
            # C1.objects.update_or_create(
            #     lcicID=lcicID,
            #     com_enterprise_code=com_enterprise_code,
            #     bnk_code=item.get('bnk_code', ''),
            #     branch_id_code=item.get('branch_id_code', ''),
            #     loan_id=item.get('loan_id', ''),
            #     col_id=item.get('col_id', ''),
            #     bank_customer_ID=item.get('bank_customer_ID', ''),
                
            #     defaults={
            #         # 'bnk_code': item.get('bnk_code', ''),
            #         # 'bank_customer_ID': item.get('bank_customer_ID', ''),
            #         # 'branch_id_code': item.get('branch_id_code', ''),
            #         # 'loan_id': item.get('loan_id', ''),
            #         # 'col_id': item.get('col_id', ''),
            #         'col_type': col_type,
            #         'user_id': item.get('user_id', ''),
            #         'period': item.get('period', ''),
            #         'id_file': CID,
            #         'insert_date': timezone.now().date(),
            #         'update_date': timezone.now().date()
            #     }
            # )    
            
    #         total_records += 1

    

    # except Exception as e:
    #     result['status'] = 'error'
    #     result['message'] = str(e)
    # print(e)

    # return result



# def process_uploaded_file(uploaded_data,  user_id, period):
#     try:
#         total_records = 0
#         error_records = 0
        
#         with uploaded_data.fileUpload.open('rb') as file:
#             file_content = file.read()
#             json_content = json.loads(smart_str(file_content))

#         result = {'status': 'success'}

#         for item in json_content:
#             lcicID = item.get('lcicID', None)
#             if lcicID == '':
#                 lcicID = None

#             com_enterprise_code = item.get('com_enterprise_code', '')
#             cid = uploaded_data.CID

#             lcic_exists = EnterpriseInfo.objects.filter(LCICID=lcicID).exists()
#             enterprise_code_exists = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).exists()

#             if not lcicID and not com_enterprise_code:
#                 collateral_status = '33'
#                 datamatch = ''
#             elif not lcicID:
#                 if enterprise_code_exists:
#                     collateral_status = '01'
#                     datamatch = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first().LCICID
#                 else:
#                     collateral_status = '03'
#                     datamatch = ''
#             elif not com_enterprise_code:
#                 if lcic_exists:
#                     collateral_status = '10'
#                     datamatch = EnterpriseInfo.objects.filter(LCICID=lcicID).first().EnterpriseID
#                 else:
#                     collateral_status = '30'
#                     datamatch = ''
#             elif lcic_exists and not enterprise_code_exists:
#                 collateral_status = '31'
#                 datamatch = EnterpriseInfo.objects.filter(LCICID=lcicID).first().EnterpriseID
#             elif not lcic_exists and enterprise_code_exists:
#                 collateral_status = '13'
#                 datamatch = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first().LCICID
#             elif not lcic_exists and not enterprise_code_exists:
#                 collateral_status = '11'
#                 datamatch = ''
#             elif lcicID and com_enterprise_code:
#                 matching_record = EnterpriseInfo.objects.filter(LCICID=lcicID, EnterpriseID=com_enterprise_code).exists()
#                 if not matching_record:
#                     collateral_status = '44'  # ບໍ່ມີຄູ່ກັນລະຫວ່າງ lcicID ແລະ com_enterprise_code
#                 else:
#                     collateral_status = '00'
#             elif lcic_exists and enterprise_code_exists:
#                 collateral_status = '00'
#                 datamatch = '' 
            
#             if collateral_status != '00':
#                 C_error.objects.create(
#                     id_file=cid,
#                     lcicID=lcicID,
#                     com_enterprise_code=com_enterprise_code,
#                     bnk_code=item.get('bnk_code', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     bank_customer_ID=item.get('bank_customer_ID', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     col_type=item.get('col_type', ''),
#                     collateral_status=collateral_status,
#                     datamatch=datamatch,
#                     user_id=user_id,
#                     period = period,
#                     collateral_insert_date=timezone.now(),
#                     collateral_update_date=timezone.now()
#                 )
#                 error_records += 1
#                 continue

#             bank_customer_ID = item.get('bank_customer_ID', '')
#             existing_c1_record = C1.objects.filter(lcicID=lcicID, com_enterprise_code=com_enterprise_code).first()
#             if existing_c1_record and existing_c1_record.bank_customer_ID != bank_customer_ID:
#                 C1_disptes.objects.create(
#                     lcicID=lcicID,
#                     id_file=cid,
#                     user_id=user_id,
#                     period=period,
#                     com_enterprise_code=com_enterprise_code,
#                     bank_customer_ID=bank_customer_ID,
#                     bnk_code=item.get('bnk_code', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     col_type=item.get('col_type', ''),
#                     insert_date=timezone.now(),
#                     update_date=timezone.now()
#                 )
#                 continue

#             col_type = item.get('col_type', '').lower()

#             if col_type == "c2.2" or col_type == "C2.2":
#                 obj, created = col_money_mia.objects.update_or_create(
#                     lcicID=lcicID,
#                     com_enterprise_code=com_enterprise_code,
#                     bnk_code=item.get('bnk_code', ''),
#                     bank_customer_ID=item.get('bank_customer_ID', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     defaults={
#                         'account_no': item.get('account_no', ''),
#                         'period': period,
#                         'user_id': user_id,
#                         'col_type': item.get('col_type', ''),
#                         'account_type': item.get('account_type', ''),
#                         'segmentType': item.get('segmentType', ''),
#                         'value_unit': item.get('value_unit', ''),
#                         'value': item.get('value', ''),
#                         'mia_value_unit': item.get('mia_value_unit', ''),
#                         'status': item.get('status', ''),
#                         'owner_gender': item.get('owner_gender', ''),
#                         'owner_name': item.get('owner_name', ''),
#                         'owner_surname': item.get('owner_surname', ''),
#                         'owner_lao_name': item.get('owner_lao_name', ''),
#                         'owner_lao_surname': item.get('owner_lao_surname', ''),
#                         'id_file': cid,
#                         'insert_date': timezone.now().date(),
#                         'update_date': timezone.now().date()
#                     }
#                 )
            
#             elif col_type == "c2.1" or col_type == "C2.1":
#                 obj, created = col_real_estates.objects.update_or_create(
#                     lcicID=lcicID,
#                     com_enterprise_code=com_enterprise_code,
#                     bnk_code=item.get('bnk_code', ''),
#                     bank_customer_ID=item.get('bank_customer_ID', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     defaults={
#                         'col_value': item.get('col_value', ''),
#                         'col_type': col_type,
#                         'plot_vilid': item.get('plot_vilid', ''),
#                         'segmentType': item.get('segmentType', ''),
#                         'plot_unit': item.get('plot_unit', ''),
#                         'land_no': item.get('land_no', ''),
#                         'land_out_time': item.get('land_out_time', ''),
#                         'value_unit': item.get('value_unit', ''),
#                         'land_type': item.get('land_type', ''),
#                         'col_area': item.get('col_area', ''),
#                         'land_registry_book_no': item.get('land_registry_book_no', ''),
#                         'land_document_no': item.get('land_document_no', ''),
#                         'place_regist_land': item.get('place_regist_land', ''),
#                         'land_map_no': item.get('land_map_no', ''),
#                         'land_plot_no': item.get('land_plot_no', ''),
#                         'land_regis_date': item.get('land_regis_date', ''),
#                         'land_area': item.get('land_area', ''),
#                         'land_unit': item.get('land_unit', ''),
#                         'owner_name': item.get('owner_name', ''),
#                         'owner_birth_date': item.get('owner_birth_date', ''),
#                         'owner_nationality': item.get('owner_nationality', ''),
#                         'owner_occupation': item.get('owner_occupation', ''),
#                         'current_unit': item.get('current_unit', ''),
#                         'current_vilid': item.get('current_vilid', ''),
#                         'spouse_name': item.get('spouse_name', ''),
#                         'spouse_birth_date': item.get('spouse_birth_date', None),
#                         'spouse_nationality': item.get('spouse_nationality', ''),
#                         'spouse_occupation': item.get('spouse_occupation', ''),
#                         'land_acquisition': item.get('land_acquisition', ''),
#                         'ownership_status': item.get('ownership_status', ''),
#                         'user_id': user_id,
#                         'period': period,
#                         'id_file': cid,
#                         'insert_date': timezone.now().date(),
#                         'update_date': timezone.now().date()
#                     }
#                 )
            
#             elif col_type == "c2.3" or col_type == "C2.3":
#                 obj, created = col_equipment_eqi.objects.update_or_create(
#                     bank_customer_ID=item.get('bank_customer_ID', ''),
#                     lcicID=lcicID,
#                     com_enterprise_code=com_enterprise_code,
#                     bnk_code=item.get('bnk_code', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     defaults={
#                         'machine_type': item.get('machine_type', ''),
#                         'col_type': item.get('col_type', ''),
#                         'segmentType': item.get('segmentType', ''),
#                         'period': period,
#                         'user_id': user_id,
#                         'machine_no': item.get('machine_no', ''),
#                         'value_unit': item.get('value_unit', ''),
#                         'id_file': cid,
#                         'value': item.get('value', ''),
#                         'owner_name': item.get('owner_name', ''),
#                         'owner_surname': item.get('owner_surname', ''),
#                         'owner_lao_name': item.get('owner_lao_name', ''),
#                         'owner_lao_surname': item.get('owner_lao_surname', ''),
#                         'insert_date': timezone.now().date(),
#                         'update_date': timezone.now().date()
#                     }
#                 )
            
#             elif col_type == "c2.4" or col_type == "C2.4":
#                 obj, created = col_project_prj.objects.update_or_create(
#                     bank_customer_ID=item.get('bank_customer_ID', ''),
#                     lcicID=lcicID,
#                     com_enterprise_code=com_enterprise_code,
#                     bnk_code=item.get('bnk_code', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     defaults={
#                         'project_type': item.get('project_type', ''),
#                         'project_name_en': item.get('project_name_en', ''),
#                         'segmentType': item.get('segmentType', ''),
#                         'col_type': item.get('col_type', ''),
#                         'period': period,
#                         'user_id': user_id,
#                         'ministry': item.get('ministry', ''),
#                         'project_namber': item.get('project_namber', ''),
#                         'value_unit': item.get('value_unit', ''),
#                         'project_name_la': item.get('project_name_la', ''),
#                         'value': item.get('value', ''),
#                         'project_status': item.get('project_status', ''),
#                         'owner_gender': item.get('owner_gender', ''),
#                         'owner_name': item.get('owner_name', ''),
#                         'owner_surname': item.get('owner_surname', ''),
#                         'owner_lao_name': item.get('owner_lao_name', ''),
#                         'owner_lao_surname': item.get('owner_lao_surname', ''),
#                         'id_file': cid,

#                         'insert_date': timezone.now().date(),
#                         'update_date': timezone.now().date()
#                     }
#                 )
            
#             elif col_type == "c2.5" or col_type == "C2.5":
#                 obj, created = col_vechicle_veh.objects.update_or_create(
#                     bank_customer_ID=item.get('bank_customer_ID', ''),
#                     lcicID=lcicID,
#                     com_enterprise_code=com_enterprise_code,
#                     bnk_code=item.get('bnk_code', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     defaults={
#                         'vehicle_type': item.get('vehicle_type', ''),
#                         'license_plate_no': item.get('license_plate_no', ''),
#                         'segmentType': item.get('segmentType', ''),
#                         'col_type': item.get('col_type', ''),
#                         'value': item.get('value', ''),
#                         'value_unit': item.get('value_unit', ''),
#                         'user_id': user_id,
#                         'period': period,
#                         # 'vehicle_value_unit': item.get('vehicle_value_unit', ''),
#                         'vehicle_status': item.get('vehicle_status', ''),
#                         'owner_gender': item.get('owner_gender', ''),
#                         'owner_name': item.get('owner_name', ''),
#                         'owner_surname': item.get('owner_surname', ''),
#                         'owner_lao_name': item.get('owner_lao_name', ''),
#                         'owner_lao_surname': item.get('owner_lao_surname', ''),
#                         'id_file': cid,
#                         'insert_date': timezone.now().date(),
#                         'update_date': timezone.now().date()
#                     }
#                 )
            
#             elif col_type == "c2.6" or col_type == "C2.6":
#                 obj, created = col_guarantor_gua.objects.update_or_create(
#                     bank_customer_ID=item.get('bank_customer_ID', ''),
#                     lcicID=lcicID,
#                     com_enterprise_code=com_enterprise_code,
#                     bnk_code=item.get('bnk_code', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     defaults={
#                         'guarantor_name': item.get('guarantor_name', ''),
#                         'segmentType': item.get('segmentType', ''),
#                         'user_id': user_id,
#                         'period': period,
#                         'col_type': item.get('col_type', ''),
#                         'guarantor_type': item.get('guarantor_type', ''),
#                         'guarantor_no': item.get('guarantor_no', ''),
#                         'value_unit': item.get('value_unit', ''),   
#                         'value': item.get('value', ''),
#                         'id_file': cid,
#                         'insert_date': timezone.now().date(),
#                         'update_date': timezone.now().date()
#                     }
#                 )
            
#             elif col_type == "c2.8" or col_type == "C2.8":
#                 obj, created = col_goldsilver_gold.objects.update_or_create(
#                     bank_customer_ID=item.get('bank_customer_ID', ''),
#                     lcicID=lcicID,
#                     com_enterprise_code=com_enterprise_code,
#                     bnk_code=item.get('bnk_code', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     defaults={
#                         'gold_type': item.get('gold_type', ''),
#                         'gold_weight': item.get('gold_weight', ''),
#                         'segmentType': item.get('segmentType', ''),
#                         'col_type': item.get('col_type', ''),
#                         'user_id': user_id,
#                         'period': period,
#                         'gold_purity': item.get('gold_purity', ''),
#                         'value': item.get('value', ''),
#                         'id_file': cid,
#                         'gold_status': item.get('gold_status', ''),
#                         'owner_gender': item.get('owner_gender', ''),
#                         'value_unit': item.get('value_unit', ''),
#                         'owner_name': item.get('owner_name', ''),
#                         'owner_surname': item.get('owner_surname', ''),
#                         'owner_lao_name': item.get('owner_lao_name', ''),
#                         'owner_lao_surname': item.get('owner_lao_surname', ''),
#                         'insert_date': timezone.now().date(),
#                         'update_date': timezone.now().date()
#                     }
#                 )
#             C1.objects.update_or_create(
#                 lcicID=lcicID,
#                 com_enterprise_code=com_enterprise_code,
#                 bnk_code=item.get('bnk_code', ''),
#                 branch_id_code=item.get('branch_id_code', ''),
#                 loan_id=item.get('loan_id', ''),
#                 col_id=item.get('col_id', ''),
#                 bank_customer_ID=item.get('bank_customer_ID', ''),
                
#                 defaults={
#                     # 'bnk_code': item.get('bnk_code', ''),
#                     # 'bank_customer_ID': item.get('bank_customer_ID', ''),
#                     # 'branch_id_code': item.get('branch_id_code', ''),
#                     # 'loan_id': item.get('loan_id', ''),
#                     # 'col_id': item.get('col_id', ''),
#                     'col_type': col_type,
#                     'user_id': user_id,
#                     'period': period,
#                     'id_file': cid,
#                     'insert_date': timezone.now().date(),
#                     'update_date': timezone.now().date()
#                 }
#             )    
            
#             total_records += 1

#         result['total_records'] = total_records
#         result['error_records'] = error_records

#     except Exception as e:
#         result['status'] = 'error'
#         result['message'] = str(e)

#     return result
class FileUploadView3(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        if not user_id:
            return JsonResponse({'status': 'error', 'message': 'User ID is required'}, status=400)

        files = request.FILES.getlist('file')
        csrf_token = request.META.get('CSRF_COOKIE', '')

        for file in files:
            if file.name.endswith('.json'):
                try:
                    file_content = file.read().decode('utf-8')
                    file_data = json.loads(file_content)

                   
                    if isinstance(file_data, list):
                        file_data = file_data[0]
                    
                    bnk_code = file_data.get('bnk_code')
                    print("bnk_code:", bnk_code)
                    if bnk_code is None:
                        return JsonResponse({'status': 'error', 'message': 'bnk_code not found in the file'}, status=402)
                    if str(user_id) != str(bnk_code):
                        return JsonResponse({'status': 'error', 'message': 'User ID does not match bnk_code'}, status=401)

                    
                    if Upload_File.objects.filter(fileName=file.name, user_id=user_id).exists():
                        return JsonResponse({'status': 'error', 'message': 'File with this name already exists for this user'}, status=403)

                    
                    file_name_parts = file.name.split('_')
                    if len(file_name_parts) >= 4:
                        period_str = file_name_parts[3]
                        period_month = int(period_str[1:3])
                        period_year = int(period_str[3:])
                        file_period = int(f"{period_year:04d}{period_month:02d}")
                        print("File Period (Original):", file_period)

                       
                        max_b1_period = B1.objects.filter(bnk_code=bnk_code).aggregate(Max('period'))['period__max']
                        if max_b1_period is not None:
                            b1_period_str = str(max_b1_period)
                            if len(b1_period_str) == 6:
                                b1_period_month = b1_period_str[2:]
                                b1_period_year = b1_period_str[:2]
                                b1_period = int(f"{b1_period_year}{b1_period_month}")
                                print("B1 Period (Converted to YYYYMM):", b1_period)

                                
                                if file_period < b1_period:
                                    return JsonResponse({'status': 'error', 'message': 'Cannot upload data for a previous period'}, status=405)
                            else:
                                return JsonResponse({'status': 'error', 'message': 'Invalid B1 period format'}, status=404)
                        else:
                           
                            pass
                    else:
                        return JsonResponse({'status': 'error', 'message': 'Invalid file name format'}, status=400)

                  
                    file_instance = File.objects.create(file=file, user_id=user_id)
                    file_id = file_instance.id

                    
                    upload_url = request.build_absolute_uri(reverse('upload_files'))
                    with file.open('rb') as f:
                        files_data = {'file': f}
                        headers = {'X-CSRFToken': csrf_token}
                        response = requests.post(upload_url, files=files_data, headers=headers, data={'period': file_period, 'file_id': file_id, 'user_id': user_id})
                        if response.status_code != 200:
                            return JsonResponse({'status': 'error', 'message': 'Failed to process file'}, status=500)

                except json.JSONDecodeError:
                    return JsonResponse({'status': 'error', 'message': 'Invalid JSON format in file'}, status=400)

        return JsonResponse({'status': 'success', 'message': 'File uploaded successfully'})



from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Upload_File, data_edit, B_Data_is_damaged, EnterpriseInfo
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

def human_readable_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"

@csrf_exempt
def upload_files(request):
    if request.method == 'POST':
        try:
            user = request.user
            user_id = request.POST.get('user_id')
            print("user_id", user_id)
            file = request.FILES.get('file')
            warnings = []
            period = request.POST.get('period')
            if period.startswith('M'):
                period = period[1:]
            FID = request.POST.get('file_id')

            if file and file.name.endswith('.json'):
                data = json.load(file)
                file_size = file.size
                file_size_hr = human_readable_size(file.size)

                upload_file = Upload_File.objects.create(
                    FID=FID,
                    fileName=file.name,
                    fileSize=file_size_hr,
                    path="uploadFiles/" + file.name,
                    insertDate=timezone.now(),
                    updateDate=timezone.now(),
                    period=period,
                    user_id=user_id,
                    status="Processing",
                    status_upload="Pending",
                    statussubmit="Pending",
                    FileType="json",
                    MID=user.memberinfo if hasattr(user, 'memberinfo') else None,
                    GID=user.user_group if hasattr(user, 'user_group') else None,
                    SType=user.stype if hasattr(user, 'stype') else None,
                    UType=user.upload_type if hasattr(user, 'upload_type') else None,
                )

                total_items = len(data)
                erroneous_items = 0

                for item in data:
                    try:
                        com_enterprise_code = item.get('com_enterprise_code', '')
                        lcicID = item.get('lcicID', '')  # ຮັກສາ lcicID ສຳລັບການເກັບຂໍ້ມູນ
                        LCIC_code = item.get('LCIC_code', '')  # ໃຊ້ LCIC_code ສຳລັບການກວດສອບ
                        LCIC_code_get = None
                        LCIC_code_error_status = '33'

                        if com_enterprise_code and LCIC_code:
                            enterprise_info_by_code = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first()
                            # ປ່ຽນການກວດສອບໃຊ້ LCIC_code ແທນ LCICID
                            enterprise_info_by_LCIC = EnterpriseInfo.objects.filter(LCIC_code=LCIC_code).first()
                            
                            if enterprise_info_by_code and enterprise_info_by_LCIC:
                                LCIC_code_error_status = '0'
                                data_edit.objects.create(
                                    lcicID=lcicID,  # ຍັງໃຊ້ lcicID ຈາກ JSON
                                    LCIC_code=LCIC_code,  # ໃຊ້ LCIC
                                    period=period,
                                    com_enterprise_code=com_enterprise_code,
                                    segmentType=item.get('segmentType', ''),
                                    bnk_code=item.get('bnk_code', ''),
                                    customer_id=item.get('customer_id', ''),
                                    branch_id=item.get('branch_id', ''),
                                    lon_sys_id=item.get('lon_sys_id', ''),
                                    loan_id=item.get('loan_id', ''),
                                    user_id=user_id,
                                    lon_open_date=item.get('lon_open_date', None),
                                    lon_exp_date=item.get('lon_exp_date', None),
                                    lon_ext_date=item.get('lon_ext_date', None),
                                    lon_int_rate=item.get('lon_int_rate', 0),
                                    lon_purpose_code=item.get('lon_purpose_code', ''),
                                    lon_credit_line=item.get('lon_credit_line', 0),
                                    lon_currency_code=item.get('lon_currency_code', ''),
                                    lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
                                    lon_account_no=item.get('lon_account_no', ''),
                                    lon_no_days_slow=item.get('lon_no_days_slow', 0),
                                    lon_class=item.get('lon_class', ''),
                                    lon_type=item.get('lon_type', ''),
                                    lon_term=item.get('lon_term', ''),
                                    lon_status=item.get('lon_status', ''),
                                    lon_insert_date=item.get('lon_insert_date', None),
                                    lon_update_date=item.get('lon_update_date', None),
                                    lon_applied_date=item.get('lon_applied_date', None),
                                    is_disputed=item.get('is_disputed', 0),
                                    id_file=FID
                                )
                                continue
                            else:
                                if enterprise_info_by_code:   # ມີ enterprise code ແຕ່ບໍ່ມີ LCIC_code ທີ່ກົງກັນ
                                    LCIC_code_get = enterprise_info_by_code.LCIC_code
                                    LCIC_code_error_status = '01'
                                elif enterprise_info_by_LCIC:  # ມີ LCIC_code ແຕ່ບໍ່ມີ enterprise code
                                    LCIC_code_get = enterprise_info_by_LCIC.EnterpriseID
                                    LCIC_code_error_status = '10'
                        elif com_enterprise_code:
                            enterprise_info_by_code = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first() # ມີ enterprise code ແຕ່ LCIC_code ຜິດ
                            if enterprise_info_by_code:
                                LCIC_code_get = enterprise_info_by_code.LCIC_code
                                LCIC_code_error_status = '31'
                            else:
                                LCIC_code_error_status = '31'
                        elif LCIC_code:
                            enterprise_info_by_LCIC = EnterpriseInfo.objects.filter(LCIC_code=LCIC_code).first() # ມີ LCIC_code ແຕ່ enterprise code ຜິດ
                            if enterprise_info_by_LCIC:
                                LCIC_code_get = enterprise_info_by_LCIC.EnterpriseID
                                LCIC_code_error_status = '13'
                            else:
                                LCIC_code_error_status = '13'

                        B_Data_is_damaged.objects.create(
                            lcicID=lcicID,  # ຍັງໃຊ້ lcicID ຈາກ JSON
                            
                            period=period,
                            user_id=user_id,
                            com_enterprise_code=com_enterprise_code,
                            product_type=item.get('product_type', ''),
                            segmentType=item.get('segmentType', ''),
                            bnk_code=item.get('bnk_code', ''),
                            customer_id=item.get('customer_id', ''),
                            branch_id=item.get('branch_id', ''),
                            lon_sys_id=item.get('lon_sys_id', ''),
                            loan_id=item.get('loan_id', ''),
                            lon_open_date=item.get('lon_open_date', None),
                            lon_exp_date=item.get('lon_exp_date', None),
                            lon_ext_date=item.get('lon_ext_date', None),
                            lon_int_rate=item.get('lon_int_rate', 0),
                            lon_purpose_code=item.get('lon_purpose_code', ''),
                            lon_credit_line=item.get('lon_credit_line', 0),
                            lon_currency_code=item.get('lon_currency_code', ''),
                            lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
                            lon_account_no=item.get('lon_account_no', ''),
                            lon_no_days_slow=item.get('lon_no_days_slow', 0),
                            lon_class=item.get('lon_class', ''),
                            lon_type=item.get('lon_type', ''),
                            lon_term=item.get('lon_term', ''),
                            lon_status=item.get('lon_status', ''),
                            lon_insert_date=item.get('lon_insert_date', None),
                            lon_update_date=item.get('lon_update_date', None),
                            lon_applied_date=item.get('lon_applied_date', None),
                            is_disputed=item.get('is_disputed', 0),
                            lcicID_error=LCIC_code_error_status,  # ໃຊ້ error status ຈາກ LCIC_code
                            lcicID_get=LCIC_code_get,  # ໃຊ້ LCIC_code_get ສຳລັບການກວດສອບ
                            LCIC_code=LCIC_code,  # ໃຊ້ LCIC_code ສຳລັບການກວດສອບ
                            id_file=FID
                        )

                        if LCIC_code_error_status != '0':
                            erroneous_items += 1

                    except Exception as e:
                        B_Data_is_damaged.objects.create(
                            lcicID=item.get('lcicID', ''),  # ຍັງໃຊ້ lcicID ຈາກ JSON
                            LCIC_code=item.get('LCIC_code', ''),  
                            period=period,
                            product_type=item.get('product_type', ''),
                            user_id=user_id,
                            com_enterprise_code=item.get('com_enterprise_code', ''),
                            segmentType=item.get('segmentType', ''),
                            bnk_code=item.get('bnk_code', ''),
                            customer_id=item.get('customer_id', ''),
                            branch_id=item.get('branch_id', ''),
                            lon_sys_id=item.get('lon_sys_id', ''),
                            loan_id=item.get('loan_id', ''),
                            lon_open_date=item.get('lon_open_date', None),
                            lon_exp_date=item.get('lon_exp_date', None),
                            lon_ext_date=item.get('lon_ext_date', None),
                            lon_int_rate=item.get('lon_int_rate', 0),
                            lon_purpose_code=item.get('lon_purpose_code', ''),
                            lon_credit_line=item.get('lon_credit_line', 0),
                            lon_currency_code=item.get('lon_currency_code', ''),
                            lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
                            lon_account_no=item.get('lon_account_no', ''),
                            lon_no_days_slow=item.get('lon_no_days_slow', 0),
                            lon_class=item.get('lon_class', ''),
                            lon_type=item.get('lon_type', ''),
                            lon_term=item.get('lon_term', ''),
                            lon_status=item.get('lon_status', ''),
                            lon_insert_date=item.get('lon_insert_date', None),
                            lon_update_date=item.get('lon_update_date', None),
                            lon_applied_date=item.get('lon_applied_date', None),
                            is_disputed=item.get('is_disputed', 0),
                            lcicID_error='33',
                            id_file=FID
                        )
                        erroneous_items += 1

                error_percentage = (erroneous_items / total_items) * 100 if total_items > 0 else 0

                upload_file.percentage = error_percentage
                upload_file.statussubmit = "2" if error_percentage > 15 else "1"
                upload_file.save()
                return JsonResponse({
                    'status': 'success',
                    'message': 'File uploaded and processed successfully',
                    'warnings': warnings,
                    'error_percentage': error_percentage
                }, status=200)

            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid file format'}, status=400)

        except Exception as e:
            logger.error(f"File upload failed: {str(e)}")
            return JsonResponse({'status': 'error', 'message': f'File upload failed: {str(e)}'}, status=500)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import json
# from .models import Upload_File, data_edit, B_Data_is_damaged, EnterpriseInfo
# from django.utils import timezone
# import logging

# logger = logging.getLogger(__name__)

# def human_readable_size(size):
   
#     for unit in ['B', 'KB', 'MB', 'GB']:
#         if size < 1024.0:
#             return f"{size:.2f} {unit}"
#         size /= 1024.0
#     return f"{size:.2f} TB"

# @csrf_exempt
# def upload_files(request):
#     if request.method == 'POST':
    
#         try:
#             user = request.user
#             user_id = request.POST.get('user_id')
#             print("user_id",user_id)
#             file = request.FILES.get('file')
#             warnings = []
#             period = request.POST.get('period')
#             if period.startswith('M'):
#                 period = period[1:]
#             FID = request.POST.get('file_id')
            

#             if file and file.name.endswith('.json'):
                
#                 data = json.load(file)
#                 file_size = file.size
#                 file_size_hr = human_readable_size(file.size)

#                 upload_file = Upload_File.objects.create(
#                     FID=FID,
                    
#                     fileName=file.name,
#                     fileSize=file_size_hr,
#                     path="uploadFiles/" + file.name,
#                     insertDate=timezone.now(),
#                     updateDate=timezone.now(),
#                     period=period,
#                     user_id=user_id,
#                     status="Processing",
#                     status_upload="Pending",
#                     statussubmit="Pending",
#                     FileType="json",
#                     MID=user.memberinfo if hasattr(user, 'memberinfo') else None,
#                     GID=user.user_group if hasattr(user, 'user_group') else None,
#                     SType=user.stype if hasattr(user, 'stype') else None,
#                     UType=user.upload_type if hasattr(user, 'upload_type') else None,
#                 )

#                 total_items = len(data)
#                 erroneous_items = 0

#                 for item in data:
#                     try:
#                         com_enterprise_code = item.get('com_enterprise_code', '')
#                         lcicID = item.get('lcicID', '')
#                         lcicID_get = None
#                         lcicID_error_status = '33'

#                         if com_enterprise_code and lcicID:
#                             enterprise_info_by_code = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first()
#                             enterprise_info_by_id = EnterpriseInfo.objects.filter(LCICID=lcicID).first()
                            
#                             if enterprise_info_by_code and enterprise_info_by_id:
#                                 lcicID_error_status = '0'
                               
#                                 data_edit.objects.create(
#                                     lcicID=lcicID,
#                                     period=period,
#                                     com_enterprise_code=com_enterprise_code,
#                                     segmentType=item.get('segmentType', ''),
#                                     bnk_code=item.get('bnk_code', ''),
#                                     customer_id=item.get('customer_id', ''),
#                                     branch_id=item.get('branch_id', ''),
#                                     lon_sys_id=item.get('lon_sys_id', ''),
#                                     loan_id=item.get('loan_id', ''),
#                                     user_id=user_id,
#                                     lon_open_date=item.get('lon_open_date', None),
#                                     lon_exp_date=item.get('lon_exp_date', None),
#                                     lon_ext_date=item.get('lon_ext_date', None),
#                                     lon_int_rate=item.get('lon_int_rate', 0),
#                                     lon_purpose_code=item.get('lon_purpose_code', ''),
#                                     lon_credit_line=item.get('lon_credit_line', 0),
#                                     lon_currency_code=item.get('lon_currency_code', ''),
#                                     lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                     lon_account_no=item.get('lon_account_no', ''),
#                                     lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                                     lon_class=item.get('lon_class', ''),
#                                     lon_type=item.get('lon_type', ''),
#                                     lon_term=item.get('lon_term', ''),
#                                     # user_id=item.get('user_id', ''),
#                                     lon_status=item.get('lon_status', ''),
#                                     lon_insert_date=item.get('lon_insert_date', None),
#                                     lon_update_date=item.get('lon_update_date', None),
#                                     lon_applied_date=item.get('lon_applied_date', None),
#                                     is_disputed=item.get('is_disputed', 0),
#                                     id_file=FID
#                                 )
#                                 continue
#                             else:
#                                 if enterprise_info_by_code:   #ມີ enterprise code ແຕ່ບໍ່ມີ lcicID 
#                                     lcicID_get = enterprise_info_by_code.LCICID
#                                     lcicID_error_status = '01'
#                                 elif enterprise_info_by_id:  #ມີ lcicID ແຕ່ບໍ່ມີ enterprise code
#                                     lcicID_get = enterprise_info_by_id.EnterpriseID
#                                     lcicID_error_status = '10'
#                         elif com_enterprise_code:
#                             enterprise_info_by_code = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first() #ມີ enterprise code ແຕ່ lcicID ຜິດ
#                             if enterprise_info_by_code:
#                                 lcicID_get = enterprise_info_by_code.LCICID
#                                 lcicID_error_status = '31'
#                             else:
#                                 lcicID_error_status = '31'
#                         elif lcicID:
#                             enterprise_info_by_id = EnterpriseInfo.objects.filter(LCICID=lcicID).first() #ມີ lcicID ແຕ່ enterprise code ຜິດ
#                             if enterprise_info_by_id:
#                                 lcicID_get = enterprise_info_by_id.EnterpriseID
#                                 lcicID_error_status = '13'
#                             else:
#                                 lcicID_error_status = '13'
                       
#                         # else:
#                         #     lcicID_error_status = '13'

#                         B_Data_is_damaged.objects.create(
#                             lcicID=lcicID,
#                             period=period,
#                             user_id=user_id,
#                             com_enterprise_code=com_enterprise_code,
#                             product_type=item.get('product_type', ''),  
#                             segmentType=item.get('segmentType', ''),
#                             bnk_code=item.get('bnk_code', ''),
#                             customer_id=item.get('customer_id', ''),
#                             branch_id=item.get('branch_id', ''),
#                             lon_sys_id=item.get('lon_sys_id', ''),
#                             loan_id=item.get('loan_id', ''),
#                             lon_open_date=item.get('lon_open_date', None),
#                             lon_exp_date=item.get('lon_exp_date', None),
#                             lon_ext_date=item.get('lon_ext_date', None),
#                             lon_int_rate=item.get('lon_int_rate', 0),
#                             lon_purpose_code=item.get('lon_purpose_code', ''),
#                             lon_credit_line=item.get('lon_credit_line', 0),
#                             lon_currency_code=item.get('lon_currency_code', ''),
#                             lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                             lon_account_no=item.get('lon_account_no', ''),
#                             lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                             lon_class=item.get('lon_class', ''),
#                             lon_type=item.get('lon_type', ''),
#                             lon_term=item.get('lon_term', ''),
#                             lon_status=item.get('lon_status', ''),
                            
#                             lon_insert_date=item.get('lon_insert_date', None),
#                             lon_update_date=item.get('lon_update_date', None),
#                             lon_applied_date=item.get('lon_applied_date', None),
#                             is_disputed=item.get('is_disputed', 0),
#                             lcicID_error=lcicID_error_status,
#                             lcicID_get=lcicID_get,
#                             id_file=FID
#                         )

#                         if lcicID_error_status != '0':
#                             erroneous_items += 1

#                     except Exception as e:
#                         B_Data_is_damaged.objects.create(
#                             lcicID=item.get('lcicID', ''),
#                             period=period,
#                             product_type=item.get('product_type', ''),
#                             user_id=user_id,
#                             com_enterprise_code=item.get('com_enterprise_code', ''),
#                             segmentType=item.get('segmentType', ''),
#                             bnk_code=item.get('bnk_code', ''),
#                             customer_id=item.get('customer_id', ''),
#                             branch_id=item.get('branch_id', ''),
#                             lon_sys_id=item.get('lon_sys_id', ''),
#                             loan_id=item.get('loan_id', ''),
#                             lon_open_date=item.get('lon_open_date', None),
#                             lon_exp_date=item.get('lon_exp_date', None),
#                             lon_ext_date=item.get('lon_ext_date', None),
#                             lon_int_rate=item.get('lon_int_rate', 0),
#                             lon_purpose_code=item.get('lon_purpose_code', ''),
#                             lon_credit_line=item.get('lon_credit_line', 0),
#                             lon_currency_code=item.get('lon_currency_code', ''),
#                             lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                             lon_account_no=item.get('lon_account_no', ''),
#                             lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                             lon_class=item.get('lon_class', ''),
#                             lon_type=item.get('lon_type', ''),
#                             lon_term=item.get('lon_term', ''),
                            
#                             lon_status=item.get('lon_status', ''),
#                             lon_insert_date=item.get('lon_insert_date', None),
#                             lon_update_date=item.get('lon_update_date', None),
#                             lon_applied_date=item.get('lon_applied_date', None),
#                             is_disputed=item.get('is_disputed', 0),
#                             lcicID_error='33',
#                             id_file=FID
#                         )
#                         erroneous_items += 1

#                 error_percentage = (erroneous_items / total_items) * 100 if total_items > 0 else 0

#                 upload_file.percentage = error_percentage
#                 upload_file.statussubmit = "2" if error_percentage > 15 else "1"
#                 upload_file.save()
#                 return JsonResponse({
#                     'status': 'success',
#                     'message': 'File uploaded and processed successfully',
#                     'warnings': warnings,
#                     'error_percentage': error_percentage
#                 }, status=200)

#             else:
#                 return JsonResponse({'status': 'error', 'message': 'Invalid file format'}, status=400)

#         except Exception as e:
#             logger.error(f"File upload failed: {str(e)}")
#             return JsonResponse({'status': 'error', 'message': f'File upload failed: {str(e)}'}, status=500)

#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)






from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Upload_File

@csrf_exempt
@require_POST
def update_statussubmit(request):
    print("update_statussubmit", request)
    try:
       
        FID = request.POST.get('FID')
        statussubmit = request.POST.get('statussubmit', '3')  
        if not FID or statussubmit not in ['3','0', '2' ]:
            return JsonResponse({'status': 'error', 'message': 'Invalid FID or statussubmit value'}, status=400)

        
        file = Upload_File.objects.get(FID=FID)
        
       
        file.statussubmit = statussubmit
        file.save()

        
        return JsonResponse({'status': 'success', 'message': 'statussubmit updated successfully'})

    except Upload_File.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'File not found'}, status=404)
    except Exception as e:
       
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
@csrf_exempt
@require_POST
def unload_statussubmit(request):
    print("update_statussubmit", request)
    try:
       
        FID = request.POST.get('FID')
        statussubmit = request.POST.get('statussubmit','4')  
        if not FID or statussubmit not in ['4','0', '2' ]:
            return JsonResponse({'status': 'error', 'message': 'Invalid FID or statussubmit value'}, status=400)

        
        file = Upload_File.objects.get(FID=FID)
        
       
        file.statussubmit = statussubmit
        file.save()

        
        return JsonResponse({'status': 'success', 'message': 'statussubmit updated successfully'})

    except Upload_File.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'File not found'}, status=404)
    except Exception as e:
       
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
@csrf_exempt
@require_POST
def error_statussubmit(request):
    print("update_statussubmit", request)
    try:
       
        FID = request.POST.get('FID')
        statussubmit = request.POST.get('statussubmit','0')  
        if not FID or statussubmit not in ['1','0', '2' ]:
            return JsonResponse({'status': 'error', 'message': 'Invalid FID or statussubmit value'}, status=400)

        
        file = Upload_File.objects.get(FID=FID)
        
       
        file.statussubmit = statussubmit
        file.save()

        
        return JsonResponse({'status': 'success', 'message': 'statussubmit updated successfully'})

    except Upload_File.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'File not found'}, status=404)
    except Exception as e:
       
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


# from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# @require_POST
# def update_statussubmit(request):
#     try:
#         FID = request.POST.get('FID')
#         file = Upload_File.objects.get(FID=FID)
#         file.statussubmit = "0"  
#         file.save()
#         return JsonResponse({'status': 'success', 'message': 'statussubmit updated successfully'})
#     except Upload_File.DoesNotExist:
#         return JsonResponse({'status': 'error', 'message': 'File not found'}, status=404)
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
@csrf_exempt
@require_POST
def update_statussubmitc(request):
    try:
        CID = request.POST.get('CID')
        file = Upload_File_C.objects.get(CID=CID)
        file.statussubmit = "3"  
        file.save()
        return JsonResponse({'status': 'success', 'message': 'statussubmit updated successfully'})
    except Upload_File_C.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'File not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
@csrf_exempt
@require_POST
def unload_statussubmitc(request):
    try:
        CID = request.POST.get('CID')
        file = Upload_File_C.objects.get(CID=CID)
        file.statussubmit = "4"  
        file.save()
        return JsonResponse({'status': 'success', 'message': 'statussubmit updated successfully'})
    except Upload_File_C.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'File not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


# from django.http import JsonResponse
# from django.views.decorators.http import require_POST   
# from django.views.decorators.csrf import csrf_exempt
# from .models import Upload_File, data_edit, B1, B1_Monthly

# @csrf_exempt
# @require_POST
# def confirm_upload(request):
#     try:
#         FID = request.POST.get('FID')
#         if not FID:
#             return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

#         data_edits = data_edit.objects.filter(id_file=FID)
#         if not data_edits.exists():
#             return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)

#         for item in data_edits:
#             try:
               
#                 B1_Monthly.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID
#                     }
#                 )

               
#                 B1.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID
#                     }
#                 )
#             except Exception as e:
#                 return JsonResponse({'status': 'error', 'message': f'Error while processing item with id {item.id}: {str(e)}'}, status=500)

#         return JsonResponse({'status': 'success', 'message': 'Data successfully confirmed and updated'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': f'Error in confirm_upload: {str(e)}'}, status=500)


from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Upload_File, data_edit, B1, B1_Monthly, disputes

def safe_parse_datetime(value):
    if isinstance(value, str):
        parsed_date = parse_datetime(value)
        return make_aware(parsed_date) if parsed_date else None
    elif isinstance(value, datetime):
        return make_aware(value) if value.tzinfo is None else value
    else:
        return None

# @csrf_exempt
# @require_POST
# def confirm_upload(request):
#     try:
#         FID = request.POST.get('FID')
#         if not FID:
#             return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

#         data_edits = data_edit.objects.filter(id_file=FID)
#         if not data_edits.exists():
#             return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)

#         for item in data_edits:
#             try:
#                 # Parsing dates safely
#                 item.lon_open_date = safe_parse_datetime(item.lon_open_date)
#                 item.lon_exp_date = safe_parse_datetime(item.lon_exp_date)
                
#                 # Check for existing records
#                 b1_monthly_record = B1_Monthly.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id
#                 ).first()

#                 b1_record = B1.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id
#                 ).first()

#                 # Check for mismatches and log disputes if needed
#                 if b1_monthly_record or b1_record:
#                     b1_monthly_mismatch = B1_Monthly.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     b1_mismatch = B1.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     if b1_monthly_mismatch or b1_mismatch:
#                         disputes.objects.create(
#                             id_file=FID,
#                             lcicID=item.lcicID,
#                             period=item.period,
#                             com_enterprise_code=item.com_enterprise_code,
#                             segmentType=item.segmentType,
#                             bnk_code=item.bnk_code,
#                             customer_id=item.customer_id,
#                             branch_id=item.branch_id,
#                             lon_sys_id=item.lon_sys_id,
#                             loan_id=item.loan_id,
#                             lon_open_date=item.lon_open_date,
#                             lon_exp_date=item.lon_exp_date,
#                             lon_ext_date=item.lon_ext_date,
#                             lon_int_rate=item.lon_int_rate,
#                             lon_purpose_code=item.lon_purpose_code,
#                             lon_credit_line=item.lon_credit_line,
#                             lon_currency_code=item.lon_currency_code,
#                             lon_outstanding_balance=item.lon_outstanding_balance,
#                             lon_account_no=item.lon_account_no,
#                             lon_no_days_slow=item.lon_no_days_slow,
#                             lon_class=item.lon_class,
#                             lon_type=item.lon_type,
#                             lon_term=item.lon_term,
#                             lon_status=item.lon_status,
#                             lon_insert_date=item.lon_insert_date,
#                             lon_update_date=item.lon_update_date,
#                             lon_applied_date=item.lon_applied_date,
#                             is_disputed=item.is_disputed
#                         )
#                         continue

#                 # Update or create records in B1_Monthly and B1
#                 B1_Monthly.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                     }
#                 )

#                 B1.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                     }
#                 )
#             except Exception as e:
#                 print(f"Error processing item with id {item.id}: {str(e)}")
#                 return JsonResponse({'status': 'error', 'message': f'Error while processing item with id {item.id}: {str(e)}'}, status=500)

#         return JsonResponse({'status': 'success', 'message': 'Data successfully confirmed and updated'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': f'Error in confirm_upload: {str(e)}'}, status=500)

# from django.http import JsonResponse
# from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt
# from .models import Upload_File, data_edit, B1, B1_Monthly, disputes

# @csrf_exempt
# @require_POST
# def confirm_upload(request):
#     try:
#         FID = request.POST.get('FID')
#         if not FID:
#             return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

#         data_edits = data_edit.objects.filter(id_file=FID)
#         if not data_edits.exists():
#             return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)

#         for item in data_edits:
#             try:
                  
#                 item_period_formatted = int(str(item.period)[:2] + str(item.period)[2:])
#                 print("file", item_period_formatted)

               
#                 last_record = B1.objects.filter(bnk_code=item.bnk_code).order_by('-period').first()
#                 if last_record:
#                     last_period_formatted = int(str(last_record.period)[:2] + str(last_record.period)[2:]) 
#                     print("B1",last_period_formatted)
#                 else:
#                     last_period_formatted = None

               
#                 if last_period_formatted is not None and item_period_formatted < last_period_formatted:
#                     continue

             
#                 b1_monthly, created = B1_Monthly.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'product_type': item.product_type,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                     }
#                 )
                
#                 b1, created = B1.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'user_id': item.user_id,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'period': item.period,
#                         'product_type': item.product_type,    
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                         'status_customer': '1' if created else '0'
#                     }
#                 )
#             except Exception as e:
#                 return JsonResponse({'status': 'error', 'message': f'Error while processing item with id {item.id}: {str(e)}'}, status=500)

#         return JsonResponse({'status': 'success', 'message': 'Data successfully confirmed and updated'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': f'Error in confirm_upload: {str(e)}'}, status=500)

# @csrf_exempt
# @require_POST
# def confirm_upload(request):
#     try:
#         FID = request.POST.get('FID')
#         if not FID:
#             return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

#         data_edits = data_edit.objects.filter(id_file=FID)
#         if not data_edits.exists():
#             return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)

#         for item in data_edits:
#             try:
               
#                 latest_b1 = B1.objects.filter(
#                     bnk_code=item.bnk_code,
                   
                    
                   
#                 ).order_by('-period').first()
#                 print("B1", latest_b1)
#                 print("item", item.period)

#                 if latest_b1 and item.period < latest_b1.period:
#                     Upload_File.objects.filter(FID=FID).update(statussubmit='2')
                   
#                     return JsonResponse({
#                         'status': 'error',
#                         'message': f'The uploaded period {item.period} is earlier than the latest period {latest_b1.period} in B1.'
#                     }, status=400)

                
#                 b1_monthly_match = B1_Monthly.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period
#                 ).exists()
                
#                 b1_match = B1.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period
#                 ).exists()

#                 if b1_monthly_match or b1_match:
#                     b1_monthly_mismatch = B1_Monthly.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id,
#                         period=item.period
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     b1_mismatch = B1.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id,
#                         period=item.period
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     if b1_monthly_mismatch or b1_mismatch:
#                         disputes.objects.create(
#                             id_file=FID,
#                             lcicID=item.lcicID,
#                             user_id=item.user_id,
#                             com_enterprise_code=item.com_enterprise_code,
#                             segmentType=item.segmentType,
#                             bnk_code=item.bnk_code,
#                             customer_id=item.customer_id,
#                             branch_id=item.branch_id,
#                             period=item.period,
#                             product_type=item.product_type,
#                             lon_sys_id=item.lon_sys_id,
#                             loan_id=item.loan_id,
#                             lon_open_date=item.lon_open_date,
#                             lon_exp_date=item.lon_exp_date,
#                             lon_ext_date=item.lon_ext_date,
#                             lon_int_rate=item.lon_int_rate,
#                             lon_purpose_code=item.lon_purpose_code,
#                             lon_credit_line=item.lon_credit_line,
#                             lon_currency_code=item.lon_currency_code,
#                             lon_outstanding_balance=item.lon_outstanding_balance,
#                             lon_account_no=item.lon_account_no,
#                             lon_no_days_slow=item.lon_no_days_slow,
#                             lon_class=item.lon_class,
#                             lon_type=item.lon_type,
#                             lon_term=item.lon_term,
#                             lon_status=item.lon_status,
#                             lon_insert_date=item.lon_insert_date,
#                             lon_update_date=item.lon_update_date,
#                             lon_applied_date=item.lon_applied_date,
#                             is_disputed=item.is_disputed,
#                             LCIC_code=item.LCIC_code
                            
#                         )
#                         continue  

#                 # ອັບເດດຕາຕະລາງ B1_Monthly ແລະ B1
#                 b1_monthly, created = B1_Monthly.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'product_type': item.product_type,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                         'LCIC_code': item.LCIC_code
#                     }
#                 )
                
#                 b1, created = B1.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'user_id': item.user_id,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'period': item.period,
#                         'product_type': item.product_type,    
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                         'LCIC_code': item.LCIC_code
#                     }
#                 )
                
#             except Exception as e:
#                 return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

#         return JsonResponse({'status': 'success', 'message': 'Data confirmed successfully'})
    
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
@csrf_exempt
@require_POST
# def confirm_upload(request):
#     try:
#         FID = request.POST.get('FID')
#         if not FID:
#             return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

#         data_edits = data_edit.objects.filter(id_file=FID)
#         if not data_edits.exists():
#             Upload_File.objects.filter(FID=FID).update(statussubmit='2')
#             return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)
        

#         for item in data_edits:
#             try:
#                 latest_b1 = B1.objects.filter(
#                     bnk_code=item.bnk_code,
#                 ).order_by('-period').first()
#                 print("B1", latest_b1)
#                 print("item", item.period)
#                 if latest_b1 and item.period < latest_b1.period:
#                     Upload_File.objects.filter(FID=FID).update(statussubmit='2')
#                     return JsonResponse({
#                         'status': 'error',
#                         'message': f'The uploaded period {item.period} is earlier than the latest period {latest_b1.period} in B1.'
#                     }, status=400)

#                 b1_monthly_match = B1_Monthly.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period
#                 ).exists()
                
#                 b1_match = B1.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period
#                 ).exists()

#                 if b1_monthly_match or b1_match:
#                     b1_monthly_mismatch = B1_Monthly.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id,
#                         period=item.period
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     b1_mismatch = B1.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id,
#                         period=item.period
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     if b1_monthly_mismatch or b1_mismatch:
#                         disputes.objects.create(
#                             id_file=FID,
#                             lcicID=item.lcicID,
#                             user_id=item.user_id,
#                             com_enterprise_code=item.com_enterprise_code,
#                             segmentType=item.segmentType,
#                             bnk_code=item.bnk_code,
#                             customer_id=item.customer_id,
#                             branch_id=item.branch_id,
#                             period=item.period,
#                             product_type=item.product_type,
#                             lon_sys_id=item.lon_sys_id,
#                             loan_id=item.loan_id,
#                             lon_open_date=item.lon_open_date,
#                             lon_exp_date=item.lon_exp_date,
#                             lon_ext_date=item.lon_ext_date,
#                             lon_int_rate=item.lon_int_rate,
#                             lon_purpose_code=item.lon_purpose_code,
#                             lon_credit_line=item.lon_credit_line,
#                             lon_currency_code=item.lon_currency_code,
#                             lon_outstanding_balance=item.lon_outstanding_balance,
#                             lon_account_no=item.lon_account_no,
#                             lon_no_days_slow=item.lon_no_days_slow,
#                             lon_class=item.lon_class,
#                             lon_type=item.lon_type,
#                             lon_term=item.lon_term,
#                             lon_status=item.lon_status,
#                             lon_insert_date=item.lon_insert_date,
#                             lon_update_date=item.lon_update_date,
#                             lon_applied_date=item.lon_applied_date,
#                             is_disputed=item.is_disputed,
#                             LCIC_code=item.LCIC_code
#                         )
#                         continue  

                
#                 existing_record = B1.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id
#                 ).exists()

               
#                 status_data_value = 'u' if existing_record else 'i'
#                 b1_monthly_exists = B1_Monthly.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id
#                 ).exists()
#                 b1_monthly_status_data = 'u' if b1_monthly_exists else 'i'

#                 b1_monthly, created = B1_Monthly.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'product_type': item.product_type,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                         'LCIC_code': item.LCIC_code,
#                         'status_data': b1_monthly_status_data
#                     }
#                 )
                
                
#                 B1.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id
#                 ).delete()
                
#                 B1.objects.create(
#                     lcicID=item.lcicID,
#                     com_enterprise_code=item.com_enterprise_code,
#                     segmentType=item.segmentType,
#                     bnk_code=item.bnk_code,
#                     user_id=item.user_id,
#                     customer_id=item.customer_id,
#                     branch_id=item.branch_id,
#                     lon_sys_id=item.lon_sys_id,
#                     loan_id=item.loan_id,
#                     period=item.period,
#                     product_type=item.product_type,    
#                     lon_open_date=item.lon_open_date,
#                     lon_exp_date=item.lon_exp_date,
#                     lon_ext_date=item.lon_ext_date,
#                     lon_int_rate=item.lon_int_rate,
#                     lon_purpose_code=item.lon_purpose_code,
#                     lon_credit_line=item.lon_credit_line,
#                     lon_currency_code=item.lon_currency_code,
#                     lon_outstanding_balance=item.lon_outstanding_balance,
#                     lon_account_no=item.lon_account_no,
#                     lon_no_days_slow=item.lon_no_days_slow,
#                     lon_class=item.lon_class,
#                     lon_type=item.lon_type,
#                     lon_term=item.lon_term,
#                     lon_status=item.lon_status,
#                     lon_insert_date=item.lon_insert_date,
#                     lon_update_date=item.lon_update_date,
#                     lon_applied_date=item.lon_applied_date,
#                     is_disputed=item.is_disputed,
#                     id_file=FID,
#                     LCIC_code=item.LCIC_code,
#                     status_data=status_data_value 
#                 )
                
#             except Exception as e:
#                 Upload_File.objects.filter(FID=FID).update(statussubmit='2')
#                 return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

#         Upload_File.objects.filter(FID=FID).update(statussubmit='0')

#         return JsonResponse({'status': 'success', 'message': 'Data confirmed successfully'})
    
#     except Exception as e:
#         Upload_File.objects.filter(FID=FID).update(statussubmit='2')
#         return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
def confirm_upload(request):
    try:
        FID = request.POST.get('FID')
        if not FID:
            return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

        data_edits = data_edit.objects.filter(id_file=FID)
        if not data_edits.exists():
            Upload_File.objects.filter(FID=FID).update(statussubmit='2')
            return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)
        
        for item in data_edits:
            try:
                latest_b1 = B1.objects.filter(
                    bnk_code=item.bnk_code,
                ).order_by('-period').first()
                print("B1", latest_b1)
                print("item", item.period)
                if latest_b1 and item.period < latest_b1.period:
                    Upload_File.objects.filter(FID=FID).update(statussubmit='2')
                    return JsonResponse({
                        'status': 'error',
                        'message': f'The uploaded period {item.period} is earlier than the latest period {latest_b1.period} in B1.'
                    }, status=400)

                b1_monthly_match = B1_Monthly.objects.filter(
                    bnk_code=item.bnk_code,
                    branch_id=item.branch_id,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id,
                    period=item.period
                ).exists()
                
                b1_match = B1.objects.filter(
                    bnk_code=item.bnk_code,
                    branch_id=item.branch_id,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id,
                    period=item.period
                ).exists()

                if b1_monthly_match or b1_match:
                    # ປ່ຽນການເຊັກຈາກ lcicID ມາເປັນ LCIC_code
                    b1_monthly_mismatch = B1_Monthly.objects.filter(
                        bnk_code=item.bnk_code,
                        branch_id=item.branch_id,
                        customer_id=item.customer_id,
                        loan_id=item.loan_id,
                        period=item.period
                    ).exclude(
                        com_enterprise_code=item.com_enterprise_code,
                        LCIC_code=item.LCIC_code  # ປ່ຽນຈາກ lcicID → LCIC_code
                    ).exists()

                    b1_mismatch = B1.objects.filter(
                        bnk_code=item.bnk_code,
                        branch_id=item.branch_id,
                        customer_id=item.customer_id,
                        loan_id=item.loan_id,
                        period=item.period
                    ).exclude(
                        com_enterprise_code=item.com_enterprise_code,
                        LCIC_code=item.LCIC_code  # ປ່ຽນຈາກ lcicID → LCIC_code
                    ).exists()

                    if b1_monthly_mismatch or b1_mismatch:
                        disputes.objects.create(
                            id_file=FID,
                            lcicID=item.lcicID,
                            user_id=item.user_id,
                            com_enterprise_code=item.com_enterprise_code,
                            segmentType=item.segmentType,
                            bnk_code=item.bnk_code,
                            customer_id=item.customer_id,
                            branch_id=item.branch_id,
                            period=item.period,
                            product_type=item.product_type,
                            lon_sys_id=item.lon_sys_id,
                            loan_id=item.loan_id,
                            lon_open_date=item.lon_open_date,
                            lon_exp_date=item.lon_exp_date,
                            lon_ext_date=item.lon_ext_date,
                            lon_int_rate=item.lon_int_rate,
                            lon_purpose_code=item.lon_purpose_code,
                            lon_credit_line=item.lon_credit_line,
                            lon_currency_code=item.lon_currency_code,
                            lon_outstanding_balance=item.lon_outstanding_balance,
                            lon_account_no=item.lon_account_no,
                            lon_no_days_slow=item.lon_no_days_slow,
                            lon_class=item.lon_class,
                            lon_type=item.lon_type,
                            lon_term=item.lon_term,
                            lon_status=item.lon_status,
                            lon_insert_date=item.lon_insert_date,
                            lon_update_date=item.lon_update_date,
                            lon_applied_date=item.lon_applied_date,
                            is_disputed=item.is_disputed,
                            LCIC_code=item.LCIC_code
                        )
                        continue  

                existing_record = B1.objects.filter(
                    bnk_code=item.bnk_code,
                    branch_id=item.branch_id,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id
                ).exists()

                status_data_value = 'u' if existing_record else 'i'
                b1_monthly_exists = B1_Monthly.objects.filter(
                    bnk_code=item.bnk_code,
                    branch_id=item.branch_id,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id
                ).exists()
                b1_monthly_status_data = 'u' if b1_monthly_exists else 'i'

                b1_monthly, created = B1_Monthly.objects.update_or_create(
                    bnk_code=item.bnk_code,
                    branch_id=item.branch_id,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id,
                    period=item.period,
                    defaults={
                        'lcicID': item.lcicID,
                        'com_enterprise_code': item.com_enterprise_code,
                        'segmentType': item.segmentType,
                        'bnk_code': item.bnk_code,
                        'customer_id': item.customer_id,
                        'branch_id': item.branch_id,
                        'user_id': item.user_id,
                        'period': item.period,
                        'product_type': item.product_type,
                        'lon_sys_id': item.lon_sys_id,
                        'loan_id': item.loan_id,
                        'lon_open_date': item.lon_open_date,
                        'lon_exp_date': item.lon_exp_date,
                        'lon_ext_date': item.lon_ext_date,
                        'lon_int_rate': item.lon_int_rate,
                        'lon_purpose_code': item.lon_purpose_code,
                        'lon_credit_line': item.lon_credit_line,
                        'lon_currency_code': item.lon_currency_code,
                        'lon_outstanding_balance': item.lon_outstanding_balance,
                        'lon_account_no': item.lon_account_no,
                        'lon_no_days_slow': item.lon_no_days_slow,
                        'lon_class': item.lon_class,
                        'lon_type': item.lon_type,
                        'lon_term': item.lon_term,
                        'lon_status': item.lon_status,
                        'lon_insert_date': item.lon_insert_date,
                        'lon_update_date': item.lon_update_date,
                        'lon_applied_date': item.lon_applied_date,
                        'is_disputed': item.is_disputed,
                        'id_file': FID,
                        'LCIC_code': item.LCIC_code,
                        'status_data': b1_monthly_status_data
                    }
                )
                
                B1.objects.filter(
                    bnk_code=item.bnk_code,
                    branch_id=item.branch_id,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id
                ).delete()
                
                B1.objects.create(
                    lcicID=item.lcicID,
                    com_enterprise_code=item.com_enterprise_code,
                    segmentType=item.segmentType,
                    bnk_code=item.bnk_code,
                    user_id=item.user_id,
                    customer_id=item.customer_id,
                    branch_id=item.branch_id,
                    lon_sys_id=item.lon_sys_id,
                    loan_id=item.loan_id,
                    period=item.period,
                    product_type=item.product_type,    
                    lon_open_date=item.lon_open_date,
                    lon_exp_date=item.lon_exp_date,
                    lon_ext_date=item.lon_ext_date,
                    lon_int_rate=item.lon_int_rate,
                    lon_purpose_code=item.lon_purpose_code,
                    lon_credit_line=item.lon_credit_line,
                    lon_currency_code=item.lon_currency_code,
                    lon_outstanding_balance=item.lon_outstanding_balance,
                    lon_account_no=item.lon_account_no,
                    lon_no_days_slow=item.lon_no_days_slow,
                    lon_class=item.lon_class,
                    lon_type=item.lon_type,
                    lon_term=item.lon_term,
                    lon_status=item.lon_status,
                    lon_insert_date=item.lon_insert_date,
                    lon_update_date=item.lon_update_date,
                    lon_applied_date=item.lon_applied_date,
                    is_disputed=item.is_disputed,
                    id_file=FID,
                    LCIC_code=item.LCIC_code,
                    status_data=status_data_value 
                )
                
            except Exception as e:
                Upload_File.objects.filter(FID=FID).update(statussubmit='2')
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

        Upload_File.objects.filter(FID=FID).update(statussubmit='0')

        return JsonResponse({'status': 'success', 'message': 'Data confirmed successfully'})
    
    except Exception as e:
        Upload_File.objects.filter(FID=FID).update(statussubmit='2')
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
@csrf_exempt
@require_POST
def unload_upload(request):
    try:
        FID = request.POST.get('FID')
        if not FID:
            Upload_File.objects.filter(FID=FID).update(statussubmit='1')
            return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

        
        upload_file = Upload_File.objects.filter(FID=FID).first()
        if not upload_file:
            Upload_File.objects.filter(FID=FID).update(statussubmit='1')
            return JsonResponse({'status': 'error', 'message': 'No upload file found for the given File ID'}, status=404)
        
        user_id = upload_file.user_id
        
        
        data_edits = data_edit.objects.filter(id_file=FID)
        if not data_edits.exists():
            Upload_File.objects.filter(FID=FID).update(statussubmit='1')
            return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)
        
        
        bank_codes = set(data_edits.values_list('bnk_code', flat=True))
        
       
        for bnk_code in bank_codes:
            
            max_period_in_b1 = B1.objects.filter(
                bnk_code=bnk_code
            ).exclude(id_file=FID).aggregate(Max('period'))['period__max']
            
            if max_period_in_b1 is not None:
                
                data_item_periods = data_edits.filter(bnk_code=bnk_code).values_list('period', flat=True)
                for period in data_item_periods:
                    if period <= max_period_in_b1:
                        Upload_File.objects.filter(FID=FID).update(statussubmit='1')
                        return JsonResponse({
                            'status': 'error', 
                            'message': f'Cannot upload data with period less than or equal to the maximum existing period for bank code {bnk_code}. Maximum existing period: {max_period_in_b1}, Upload period: {period}'
                        }, status=406)
        
        
        items_to_process = []
        for item in data_edits:
            
            b1_items = B1.objects.filter(
                bnk_code=item.bnk_code,
                customer_id=item.customer_id,
                loan_id=item.loan_id
            )
            
            status_data = None
            if b1_items.exists():
                status_data = b1_items.first().status_data
            
            items_to_process.append({
                'item': item,
                'status_data': status_data
            })
        
        
        for process_item in items_to_process:
            item = process_item['item']
            status_data = process_item['status_data']
            
            
            if status_data is None or status_data == 'i':
               
                B1.objects.filter(
                    id_file=FID,
                    bnk_code=item.bnk_code,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id
                ).delete()
                
                B1_Monthly.objects.filter(
                    id_file=FID,
                    bnk_code=item.bnk_code,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id
                ).delete()
                
            
            elif status_data == 'u':
                
                B1.objects.filter(
                    id_file=FID,
                    bnk_code=item.bnk_code,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id
                ).delete()
                
                B1_Monthly.objects.filter(
                    id_file=FID,
                    bnk_code=item.bnk_code,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id
                ).delete()
                
               
                latest_b1_monthly = B1_Monthly.objects.filter(
                    bnk_code=item.bnk_code,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id
                ).exclude(id_file=FID).order_by('-id').first()
                
                if latest_b1_monthly:
                   
                    B1.objects.create(
                        lcicID=latest_b1_monthly.lcicID,
                        com_enterprise_code=latest_b1_monthly.com_enterprise_code,
                        segmentType=latest_b1_monthly.segmentType,
                        bnk_code=latest_b1_monthly.bnk_code,
                        user_id=latest_b1_monthly.user_id,
                        customer_id=latest_b1_monthly.customer_id,
                        branch_id=latest_b1_monthly.branch_id,
                        lon_sys_id=latest_b1_monthly.lon_sys_id,
                        loan_id=latest_b1_monthly.loan_id,
                        period=latest_b1_monthly.period,
                        product_type=latest_b1_monthly.product_type,    
                        lon_open_date=latest_b1_monthly.lon_open_date,
                        lon_exp_date=latest_b1_monthly.lon_exp_date,
                        lon_ext_date=latest_b1_monthly.lon_ext_date,
                        lon_int_rate=latest_b1_monthly.lon_int_rate,
                        lon_purpose_code=latest_b1_monthly.lon_purpose_code,
                        lon_credit_line=latest_b1_monthly.lon_credit_line,
                        lon_currency_code=latest_b1_monthly.lon_currency_code,
                        lon_outstanding_balance=latest_b1_monthly.lon_outstanding_balance,
                        lon_account_no=latest_b1_monthly.lon_account_no,
                        lon_no_days_slow=latest_b1_monthly.lon_no_days_slow,
                        lon_class=latest_b1_monthly.lon_class,
                        lon_type=latest_b1_monthly.lon_type,
                        lon_term=latest_b1_monthly.lon_term,
                        lon_status=latest_b1_monthly.lon_status,
                        lon_insert_date=latest_b1_monthly.lon_insert_date,
                        lon_update_date=latest_b1_monthly.lon_update_date,
                        lon_applied_date=latest_b1_monthly.lon_applied_date,
                        is_disputed=latest_b1_monthly.is_disputed,
                        id_file=latest_b1_monthly.id_file,
                        LCIC_code=latest_b1_monthly.LCIC_code,
                        status_data=latest_b1_monthly.status_data if hasattr(latest_b1_monthly, 'status_data') else 'u'
                    )
        
    
        Upload_File.objects.filter(FID=FID).update(statussubmit='5')
        
        return JsonResponse({'status': 'success', 'message': 'Data unloaded successfully'})
    
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# @csrf_exempt
# @require_POST
# def unload_upload(request):
#     try:
#         FID = request.POST.get('FID')
#         if not FID:
#             return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

       
#         upload_file = Upload_File.objects.filter(FID=FID).first()
#         if not upload_file:
#             return JsonResponse({'status': 'error', 'message': 'No upload file found for the given File ID'}, status=404)
        
#         user_id = upload_file.user_id
        
        
#         data_edits = data_edit.objects.filter(id_file=FID)
#         if not data_edits.exists():
#             return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)
        
       
#         bank_codes = set(data_edits.values_list('bnk_code', flat=True))
        
        
#         B1.objects.filter(id_file=FID).delete()
#         B1_Monthly.objects.filter(id_file=FID).delete()
        
        
#         for item in data_edits:
#             try:
                
#                 previous_period = None
                
                
#                 b1_monthly_periods = B1_Monthly.objects.filter(
#                     bnk_code=item.bnk_code,
#                     user_id=user_id
#                 ).values_list('period', flat=True).distinct().order_by('-period')
                
               
#                 b1_periods = B1.objects.filter(
#                     bnk_code=item.bnk_code,
#                     user_id=user_id
#                 ).values_list('period', flat=True).distinct().order_by('-period')
                
                
#                 all_periods = list(b1_monthly_periods) + list(b1_periods)
#                 all_periods = sorted(set(all_periods), reverse=True)
                
                
#                 current_period = item.period
#                 for period in all_periods:
#                     if period < current_period:
#                         previous_period = period
#                         break
                
                
#                 B1_Monthly.objects.create(
#                     lcicID=item.lcicID,
#                     com_enterprise_code=item.com_enterprise_code,
#                     segmentType=item.segmentType,
#                     bnk_code=item.bnk_code,
#                     customer_id=item.customer_id,
#                     branch_id=item.branch_id,
#                     user_id=user_id,
#                     period=previous_period if previous_period else item.period,
#                     product_type=item.product_type,
#                     lon_sys_id=item.lon_sys_id,
#                     loan_id=item.loan_id,
#                     lon_open_date=item.lon_open_date,
#                     lon_exp_date=item.lon_exp_date,
#                     lon_ext_date=item.lon_ext_date,
#                     lon_int_rate=item.lon_int_rate,
#                     lon_purpose_code=item.lon_purpose_code,
#                     lon_credit_line=item.lon_credit_line,
#                     lon_currency_code=item.lon_currency_code,
#                     lon_outstanding_balance=item.lon_outstanding_balance,
#                     lon_account_no=item.lon_account_no,
#                     lon_no_days_slow=item.lon_no_days_slow,
#                     lon_class=item.lon_class,
#                     lon_type=item.lon_type,
#                     lon_term=item.lon_term,
#                     lon_status=item.lon_status,
#                     lon_insert_date=item.lon_insert_date,
#                     lon_update_date=item.lon_update_date,
#                     lon_applied_date=item.lon_applied_date,
#                     is_disputed=item.is_disputed,
#                     id_file=FID,
#                     LCIC_code=item.LCIC_code
#                 )
                
             
#                 B1.objects.create(
#                     lcicID=item.lcicID,
#                     com_enterprise_code=item.com_enterprise_code,
#                     segmentType=item.segmentType,
#                     bnk_code=item.bnk_code,
#                     user_id=user_id,
#                     customer_id=item.customer_id,
#                     branch_id=item.branch_id,
#                     lon_sys_id=item.lon_sys_id,
#                     loan_id=item.loan_id,
#                     period=previous_period if previous_period else item.period,
#                     product_type=item.product_type,    
#                     lon_open_date=item.lon_open_date,
#                     lon_exp_date=item.lon_exp_date,
#                     lon_ext_date=item.lon_ext_date,
#                     lon_int_rate=item.lon_int_rate,
#                     lon_purpose_code=item.lon_purpose_code,
#                     lon_credit_line=item.lon_credit_line,
#                     lon_currency_code=item.lon_currency_code,
#                     lon_outstanding_balance=item.lon_outstanding_balance,
#                     lon_account_no=item.lon_account_no,
#                     lon_no_days_slow=item.lon_no_days_slow,
#                     lon_class=item.lon_class,
#                     lon_type=item.lon_type,
#                     lon_term=item.lon_term,
#                     lon_status=item.lon_status,
#                     lon_insert_date=item.lon_insert_date,
#                     lon_update_date=item.lon_update_date,
#                     lon_applied_date=item.lon_applied_date,
#                     is_disputed=item.is_disputed,
#                     id_file=FID,
#                     LCIC_code=item.LCIC_code
#                 )
                
#             except Exception as e:
#                 return JsonResponse({'status': 'error', 'message': f'Error processing item: {str(e)}'}, status=500)

      
#         Upload_File.objects.filter(FID=FID).update(statussubmit='1')
        
#         return JsonResponse({'status': 'success', 'message': 'Data unloaded successfully'})
    
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
  
# from django.http import JsonResponse 
# from django.views.decorators.http import require_POST    
# from django.views.decorators.csrf import csrf_exempt
# from .models import Upload_File, data_edit, B1, B1_Monthly, disputes

# @csrf_exempt
# @require_POST
# def confirm_upload(request):
#     try:
#         FID = request.POST.get('FID')
#         if not FID:
#             return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

#         data_edits = data_edit.objects.filter(id_file=FID)
#         if not data_edits.exists():
#             return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)

#         for item in data_edits:
#             try:
#                 b1_monthly_match = B1_Monthly.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period
                    
#                 ).exists()
                
#                 b1_match = B1.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period
#                 ).exists()

#                 if b1_monthly_match or b1_match:
#                     b1_monthly_mismatch = B1_Monthly.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id,
#                         period=item.period
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     b1_mismatch = B1.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id,
#                         period=item.period
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     if b1_monthly_mismatch or b1_mismatch:
#                         disputes.objects.create(
#                             id_file=FID,
#                             lcicID=item.lcicID,
#                             user_id=item.user_id,
#                             com_enterprise_code=item.com_enterprise_code,
#                             segmentType=item.segmentType,
#                             bnk_code=item.bnk_code,
#                             customer_id=item.customer_id,
#                             branch_id=item.branch_id,
#                             period=item.period,
#                             product_type=item.product_type,
#                             lon_sys_id=item.lon_sys_id,
#                             loan_id=item.loan_id,
#                             lon_open_date=item.lon_open_date,
#                             lon_exp_date=item.lon_exp_date,
#                             lon_ext_date=item.lon_ext_date,
#                             lon_int_rate=item.lon_int_rate,
#                             lon_purpose_code=item.lon_purpose_code,
#                             lon_credit_line=item.lon_credit_line,
#                             lon_currency_code=item.lon_currency_code,
#                             lon_outstanding_balance=item.lon_outstanding_balance,
#                             lon_account_no=item.lon_account_no,
#                             lon_no_days_slow=item.lon_no_days_slow,
#                             lon_class=item.lon_class,
#                             lon_type=item.lon_type,
#                             lon_term=item.lon_term,
#                             lon_status=item.lon_status,
#                             lon_insert_date=item.lon_insert_date,
#                             lon_update_date=item.lon_update_date,
#                             lon_applied_date=item.lon_applied_date,
#                             is_disputed=item.is_disputed
#                         )
#                         continue  
#                 b1_monthly, created = B1_Monthly.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     period=item.period,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'user_id': item.user_id,
#                         'period': item.period,
#                         'product_type': item.product_type,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                     }
#                 )
                
#                 b1, created = B1.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'user_id': item.user_id,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'period': item.period,
#                         'product_type': item.product_type,    
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                         'status_customer': '1' if created else '0'
#                     }
#                 )
#             except Exception as e:
#                 return JsonResponse({'status': 'error', 'message': f'Error while processing item with id {item.id}: {str(e)}'}, status=500)

#         return JsonResponse({'status': 'success', 'message': 'Data successfully confirmed and updated'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': f'Error in confirm_upload: {str(e)}'}, status=500)


# from django.http import JsonResponse
# from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt
# from .models import Upload_File, data_edit, B1, B1_Monthly, disputes
# from django.utils import timezone

# @csrf_exempt
# @require_POST
# def confirm_upload(request):
#     try:
#         FID = request.POST.get('FID')
#         if not FID:
#             return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

#         data_edits = data_edit.objects.filter(id_file=FID)
#         if not data_edits.exists():
#             return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)

#         for item in data_edits:
#             try:
#                 b1_monthly_match = B1_Monthly.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id
#                 ).exists()
                
#                 b1_match = B1.objects.filter(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id
#                 ).exists()

#                 if b1_monthly_match or b1_match:
#                     b1_monthly_mismatch = B1_Monthly.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     b1_mismatch = B1.objects.filter(
#                         bnk_code=item.bnk_code,
#                         branch_id=item.branch_id,
#                         customer_id=item.customer_id,
#                         loan_id=item.loan_id
#                     ).exclude(
#                         com_enterprise_code=item.com_enterprise_code,
#                         lcicID=item.lcicID
#                     ).exists()

#                     if b1_monthly_mismatch or b1_mismatch:
#                         disputes.objects.create(
#                             id_file=FID,
#                             lcicID=item.lcicID,
                            
#                             com_enterprise_code=item.com_enterprise_code,
#                             segmentType=item.segmentType,
#                             bnk_code=item.bnk_code,
#                             customer_id=item.customer_id,
#                             branch_id=item.branch_id,
#                             period=item.period,
#                             lon_sys_id=item.lon_sys_id,
#                             loan_id=item.loan_id,
#                             lon_open_date=item.lon_open_date,
#                             lon_exp_date=item.lon_exp_date,
#                             lon_ext_date=item.lon_ext_date,
#                             lon_int_rate=item.lon_int_rate,
#                             lon_purpose_code=item.lon_purpose_code,
#                             lon_credit_line=item.lon_credit_line,
#                             lon_currency_code=item.lon_currency_code,
#                             lon_outstanding_balance=item.lon_outstanding_balance,
#                             lon_account_no=item.lon_account_no,
#                             lon_no_days_slow=item.lon_no_days_slow,
#                             lon_class=item.lon_class,
#                             lon_type=item.lon_type,
#                             lon_term=item.lon_term,
#                             lon_status=item.lon_status,
#                             lon_insert_date=item.lon_insert_date,
#                             lon_update_date=item.lon_update_date,
#                             lon_applied_date=item.lon_applied_date,
#                             is_disputed=item.is_disputed
#                         )
#                         continue  
#                 b1_monthly, created = B1_Monthly.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'period': item.period,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
#                         'id_file': FID,
#                     }
#                 )
                
#                 b1, created = B1.objects.update_or_create(
#                     bnk_code=item.bnk_code,
#                     branch_id=item.branch_id,
#                     customer_id=item.customer_id,
#                     loan_id=item.loan_id,
#                     defaults={
#                         'lcicID': item.lcicID,
#                         'com_enterprise_code': item.com_enterprise_code,
#                         'segmentType': item.segmentType,
#                         'bnk_code': item.bnk_code,
#                         'customer_id': item.customer_id,
#                         'branch_id': item.branch_id,
#                         'lon_sys_id': item.lon_sys_id,
#                         'loan_id': item.loan_id,
#                         'period': item.period,
#                         'lon_open_date': item.lon_open_date,
#                         'lon_exp_date': item.lon_exp_date,
#                         'lon_ext_date': item.lon_ext_date,
#                         'lon_int_rate': item.lon_int_rate,
#                         'lon_purpose_code': item.lon_purpose_code,
#                         'lon_credit_line': item.lon_credit_line,
#                         'lon_currency_code': item.lon_currency_code,
#                         'lon_outstanding_balance': item.lon_outstanding_balance,
#                         'lon_account_no': item.lon_account_no,
#                         'lon_no_days_slow': item.lon_no_days_slow,
#                         'lon_class': item.lon_class,
#                         'lon_type': item.lon_type,
#                         'lon_term': item.lon_term,
#                         'lon_status': item.lon_status,
#                         'lon_insert_date': item.lon_insert_date,
#                         'lon_update_date': item.lon_update_date,
#                         'lon_applied_date': item.lon_applied_date,
#                         'is_disputed': item.is_disputed,
                       
#                         'id_file': FID,
#                         # 'status_customer': '1' if created else '0'
#                     }
#                 )
#             except Exception as e:
#                 print(f"Error processing item with id {item.id}: {str(e)}")
#                 return JsonResponse({'status': 'error', 'message': f'Error while processing item with id {item.id}: {str(e)}'}, status=500)

#         return JsonResponse({'status': 'success', 'message': 'Data successfully confirmed and updated'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': f'Error in confirm_upload: {str(e)}'}, status=500)



# views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from .models import UploadedFile
# from .serializers import UploadedFileSerializer

# class FileUploadView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, format=None):
#         serializer = UploadedFileSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework.permissions import IsAuthenticated
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# # from .models import UploadedFile
# # from .serializers import UploadedFileSerializer

# class FileUploadView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         files = request.FILES.getlist('files')
#         uploaded_files = []

#         for file in files:
#             uploaded_file = UploadedFile(
#                 name=file.name,
#                 file=file,
#                 size=file.size,
#                 uploaded_by=request.user
#             )
#             uploaded_file.save()
#             uploaded_files.append(uploaded_file)

#         serializer = UploadedFileSerializer(uploaded_files, many=True)
#         return Response({
#             'message': 'Files successfully uploaded!',
#             'uploadedFiles': serializer.data
#         }, status=status.HTTP_201_CREATED)







from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class LoginView1(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response({"error": "ບັນຊີຜູ້ໃຊ້ຖືກປິດໃຊ້ງານ"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "ຂໍ້ມູນບໍ່ຖືກຕ້ອງ"}, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework import generics
# from .models import Upload_File
# from .serializers import UploadFileSerializer

# class UploadFileList(generics.ListAPIView):
#     queryset = Upload_File.objects.all()
#     serializer_class = UploadFileSerializer
# from rest_framework import generics, serializers
# from rest_framework.response import Response
# from rest_framework import status
# from django.db.models import Q
# from datetime import datetime
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Q  # ✅ import ຢູ່ເທິງສຸດ
import logging

logger = logging.getLogger(__name__)

class UploadFileList(generics.ListAPIView):
    serializer_class = UploadFileSerializer
    queryset = Upload_File.objects.all()
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        period = self.request.query_params.get('period')
        request_user_id = self.request.query_params.get('request_user_id')
        file_type = self.request.query_params.get('file_type')
        status_filter = self.request.query_params.get('status')
        
        queryset = Upload_File.objects.all()
        
        # Permission logic
        if request_user_id and request_user_id != "01":
            queryset = queryset.filter(user_id=request_user_id)
        elif request_user_id == "01" and user_id:
            queryset = queryset.filter(user_id=user_id)
        
        # Apply filters
        if period:
            queryset = queryset.filter(period=period)
        if file_type:
            queryset = queryset.filter(FileType=file_type)
        if status_filter:
            queryset = queryset.filter(statussubmit=status_filter)
            
        return queryset.order_by('-insertDate')
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
        
        
            stats = queryset.aggregate(
                total=Count('file_id'),
                json_count=Count('file_id', filter=Q(FileType='json')),
                xml_count=Count('file_id', filter=Q(FileType='xml')),
                status_0=Count('file_id', filter=Q(statussubmit='0')),
                status_1=Count('file_id', filter=Q(statussubmit='1')),
                status_2=Count('file_id', filter=Q(statussubmit='2')),
                status_3=Count('file_id', filter=Q(statussubmit='3')),
                status_4=Count('file_id', filter=Q(statussubmit='4')),
                status_5=Count('file_id', filter=Q(statussubmit='5')),
                status_pending=Count('file_id', filter=Q(statussubmit='Pending'))
            )
        
            serializer = self.get_serializer(queryset, many=True)
        
            response_data = {
                'count': stats['total'],
                'results': serializer.data,
                'summary': {
                    'total_files': stats['total'],
                    'json_files': stats['json_count'],
                    'xml_files': stats['xml_count'],
                    'status_breakdown': {
                        '0': stats['status_0'],
                        '1': stats['status_1'],
                        '2': stats['status_2'],
                        '3': stats['status_3'],
                        '4': stats['status_4'],
                        '5': stats['status_5'],
                        'Pending': stats['status_pending']
                    }
                },
                'filters_applied': {
                    'user_id': request.query_params.get('user_id'),
                    'period': request.query_params.get('period'),
                    'request_user_id': request.query_params.get('request_user_id'),
                    'file_type': request.query_params.get('file_type'),
                    'status': request.query_params.get('status')
                }
            }
        
            return Response(response_data, status=status.HTTP_200_OK)
        
        except Exception as e:
            logger.error(f"Error: {str(e)}", exc_info=True)
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )  # ✅ indentation ຖືກຕ້ອງ
            try:
                queryset = self.get_queryset()
            
            # ນັບທຸກຢ່າງໃນ query ດຽວ! ⚡
                stats = queryset.aggregate(
                    total=Count('id'),
                    json_count=Count('id', filter=Q(FileType='json')),
                    xml_count=Count('id', filter=Q(FileType='xml')),
                    status_0=Count('id', filter=Q(statussubmit='0')),
                    status_1=Count('id', filter=Q(statussubmit='1')),
                    status_2=Count('id', filter=Q(statussubmit='2')),
                    status_3=Count('id', filter=Q(statussubmit='3')),
                    status_4=Count('id', filter=Q(statussubmit='4')),
                    status_5=Count('id', filter=Q(statussubmit='5')),
                    status_pending=Count('id', filter=Q(statussubmit='Pending'))
                )
            
                serializer = self.get_serializer(queryset, many=True)
            
                response_data = {
                    'count': stats['total'],
                    'results': serializer.data,
                    'summary': {
                        'total_files': stats['total'],
                        'json_files': stats['json_count'],
                        'xml_files': stats['xml_count'],
                        'status_breakdown': {
                            '0': stats['status_0'],
                            '1': stats['status_1'],
                            '2': stats['status_2'],
                            '3': stats['status_3'],
                            '4': stats['status_4'],
                            '5': stats['status_5'],
                            'Pending': stats['status_pending']
                        }
                    },
                    'filters_applied': {
                        'user_id': request.query_params.get('user_id'),
                        'period': request.query_params.get('period'),
                        'request_user_id': request.query_params.get('request_user_id'),
                        'file_type': request.query_params.get('file_type'),
                        'status': request.query_params.get('status')
                    }
                }
            
                return Response(response_data, status=status.HTTP_200_OK)
            
            except Exception as e:
                logger.error(f"Error: {str(e)}", exc_info=True)
                return Response(
                    {'error': str(e)}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )



# class UploadFileList(generics.ListAPIView):
#     serializer_class = UploadFileSerializer
#     queryset = Upload_File.objects.all()  # ເພີ່ມບັນທັດນີ້ກ່ອນ
    
#     def get_queryset(self):  # ກວດ indentation ໃຫ້ດີ!
#         user_id = self.request.query_params.get('user_id')
#         period = self.request.query_params.get('period')
#         request_user_id = self.request.query_params.get('request_user_id')
#         file_type = self.request.query_params.get('file_type')
#         status_filter = self.request.query_params.get('status')
        
#         # ເລີ່ມຈາກ base queryset
#         queryset = Upload_File.objects.all()
        
#         # Permission logic
#         if request_user_id and request_user_id != "01":
#             queryset = queryset.filter(user_id=request_user_id)
#         elif request_user_id == "01" and user_id:
#             queryset = queryset.filter(user_id=user_id)
        
#         # Apply filters
#         if period:
#             queryset = queryset.filter(period=period)
#         if file_type:
#             queryset = queryset.filter(FileType=file_type)
#         if status_filter:
#             queryset = queryset.filter(statussubmit=status_filter)
            
#         return queryset.order_by('-insertdate')  # ກວດ field name ດ້ວຍ
    
#     def list(self, request, *args, **kwargs):
#         try:
#             queryset = self.get_queryset()
#             serializer = self.get_serializer(queryset, many=True)
            
#             total_files = queryset.count()
#             json_files = queryset.filter(FileType='json').count()
#             xml_files = queryset.filter(FileType='xml').count()
            
#             response_data = {
#                 'count': total_files,
#                 'results': serializer.data,
#                 'summary': {
#                     'total_files': total_files,
#                     'json_files': json_files,
#                     'xml_files': xml_files,
#                     'status_breakdown': self._get_status_breakdown(queryset)
#                 },
#                 'filters_applied': {
#                     'user_id': request.query_params.get('user_id'),
#                     'period': request.query_params.get('period'),
#                     'request_user_id': request.query_params.get('request_user_id'),
#                     'file_type': request.query_params.get('file_type'),
#                     'status': request.query_params.get('status')
#                 }
#             }
            
#             return Response(response_data, status=status.HTTP_200_OK)
            
#         except Exception as e:
#             logger.error(f"Error in UploadFileList: {str(e)}", exc_info=True)
#             return Response(
#                 {'error': f'ເກີດຂໍ້ຜິດພາດໃນການດຶງຂໍ້ມູນ: {str(e)}'}, 
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )
    
#     def _get_status_breakdown(self, queryset):
#         """ຄິດໄລ່ຈຳນວນຕາມສະຖານະ"""
#         status_map = ['0', '1', '2', '3', '4', '5', 'Pending']
#         breakdown = {}
#         for status_code in status_map:
#             breakdown[status_code] = queryset.filter(statussubmit=status_code).count()
#         return breakdown

# class UploadFileList(generics.ListAPIView):
#     serializer_class = UploadFileSerializer
    
#     def get_queryset(self):
       
#         user_id = self.request.query_params.get('user_id')
#         period = self.request.query_params.get('period')
#         request_user_id = self.request.query_params.get('request_user_id')
#         file_type = self.request.query_params.get('file_type')  # json, xml
#         status_filter = self.request.query_params.get('status')
        
       
#         queryset = Upload_File.objects.all()
        
       
#         if request_user_id and request_user_id != "01":
            
#             queryset = queryset.filter(user_id=request_user_id)
#         elif request_user_id == "01":
           
#             if user_id:
#                 queryset = queryset.filter(user_id=user_id)
        
      
#         if period:
#             queryset = queryset.filter(period=period)
            
     
#         if file_type:
#             queryset = queryset.filter(FileType=file_type)
            
       
#         if status_filter:
#             queryset = queryset.filter(statussubmit=status_filter)
            
#         return queryset.order_by('-insertDate')  
    
#     def list(self, request, *args, **kwargs):
#         """
#         Custom list method ພ້ອມການຈັດການ error ແລະ metadata
#         """
#         try:
#             queryset = self.get_queryset()
#             serializer = self.get_serializer(queryset, many=True)
            
        
#             total_files = queryset.count()
#             json_files = queryset.filter(FileType='json').count()
#             xml_files = queryset.filter(FileType='xml').count()
            
#             response_data = {
#                 'count': total_files,
#                 'results': serializer.data,
#                 'summary': {
#                     'total_files': total_files,
#                     'json_files': json_files,
#                     'xml_files': xml_files,
#                     'status_breakdown': self._get_status_breakdown(queryset)
#                 },
#                 'filters_applied': {
#                     'user_id': request.query_params.get('user_id'),
#                     'period': request.query_params.get('period'),
#                     'request_user_id': request.query_params.get('request_user_id'),
#                     'file_type': request.query_params.get('file_type'),
#                     'status': request.query_params.get('status')
#                 }
#             }
            
#             return Response(response_data, status=status.HTTP_200_OK)
            
#         except Exception as e:
#             return Response(
#                 {'error': f'ເກີດຂໍ້ຜິດພາດໃນການດຶງຂໍ້ມູນ: {str(e)}'}, 
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )
    
#     def _get_status_breakdown(self, queryset):
#         """ຄິດໄລ່ຈຳນວນຕາມສະຖານະ"""
#         status_map = ['0', '1', '2', '3', '4', '5', 'Pending']
#         breakdown = {}
#         for status_code in status_map:
#             breakdown[status_code] = queryset.filter(statussubmit=status_code).count()
#         return breakdown


class UploadFileSerializer(serializers.ModelSerializer):
    # ເພີ່ມ computed fields
    file_size_formatted = serializers.SerializerMethodField()
    upload_date_formatted = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()
    period_formatted = serializers.SerializerMethodField()
    days_since_upload = serializers.SerializerMethodField()
    
    class Meta:
        model = Upload_File
        fields = [
            'FID', 'user_id', 'file_id', 'fileName', 'fileUpload', 
            'fileSize', 'path', 'insertDate', 'updateDate', 'period',
            'status', 'statussubmit', 'status_upload', 'FileType', 
            'percentage', 'MID', 'GID', 'SType', 'UType',
            # Computed fields
            'file_size_formatted', 'upload_date_formatted', 
            'status_display', 'period_formatted', 'days_since_upload'
        ]
    
    def get_file_size_formatted(self, obj):
        """ຈັດຮູບແບບຂະໜາດຟາຍ"""
        if obj.fileSize:
            # ຖ້າ fileSize ເປັນ string ແລ້ວ (ເຊັ່ນ "4.49 KB")
            if isinstance(obj.fileSize, str):
                return obj.fileSize
            # ຖ້າເປັນ number ໃຫ້ແປງເປັນ KB/MB
            elif isinstance(obj.fileSize, (int, float)):
                if obj.fileSize < 1024:
                    return f"{obj.fileSize} B"
                elif obj.fileSize < 1024 * 1024:
                    return f"{round(obj.fileSize / 1024, 2)} KB"
                else:
                    return f"{round(obj.fileSize / (1024 * 1024), 2)} MB"
        return "0 B"
    
    def get_upload_date_formatted(self, obj):
        """ຈັດຮູບແບບວັນທີອັບໂຫຼດ"""
        if obj.insertDate:
            return obj.insertDate.strftime('%d/%m/%Y %H:%M')
        return None
    
    def get_status_display(self, obj):
        """ແປງ status code ເປັນຂໍ້ຄວາມພາສາລາວ"""
        status_map = {
            'Pending': 'ກຳລັງນຳສົ່ງຂໍ້ມູນ',
            '1': 'ນຳສົ່ງຂໍ້ມູນສຳເລັດ',
            '2': 'ປະຕິເສດ',
            '3': 'ນຳສົ່ງຂໍ້ມູນສຳເລັດ',
            '4': 'ຂໍ້ມູນຖືກອັນໂຫຼດ',
            '5': 'ຂໍ້ມູນຖືກອັນໂຫຼດ',
            '0': 'ສຳເລັດການໂຫຼດ'
        }
        return status_map.get(str(obj.statussubmit), 'ບໍ່ຮູ້ສະຖານະ')
    
    def get_period_formatted(self, obj):
        """ຈັດຮູບແບບ period (ເຊັ່ນ 201712 -> ທັນວາ 2017)"""
        if obj.period and len(str(obj.period)) == 6:
            year = str(obj.period)[:4]
            month = str(obj.period)[4:]
            
            month_names = {
                '01': 'ມັງກອນ', '02': 'ກຸມພາ', '03': 'ມີນາ',
                '04': 'ເມສາ', '05': 'ພຶດສະພາ', '06': 'ມິຖຸນາ',
                '07': 'ກໍລະກົດ', '08': 'ສິງຫາ', '09': 'ກັນຍາ',
                '10': 'ຕຸລາ', '11': 'ພະຈິກ', '12': 'ທັນວາ'
            }
            
            month_name = month_names.get(month, month)
            return f"{month_name} {year}"
        return obj.period
    
    def get_days_since_upload(self, obj):
        """ຄິດໄລ່ວັນທີ່ຜ່ານມາຕັ້ງແຕ່ອັບໂຫຼດ"""
        if obj.insertDate:
            from django.utils import timezone
            now = timezone.now()
            diff = now - obj.insertDate
            return diff.days
        return None


class AvailablePeriodsView(generics.ListAPIView):
    """API ສຳລັບດຶງລາຍການ periods ທີ່ມີໃນລະບົບ"""
    
    def get(self, request, *args, **kwargs):
        try:
            request_user_id = request.query_params.get('request_user_id')
            
            # ໃຊ້ logic ດຽວກັນກັບການກວດສອບສິດທິ່
            queryset = Upload_File.objects.all()
            if request_user_id and request_user_id != "01":
                queryset = queryset.filter(user_id=request_user_id)
            
            # ດຶງ periods ທີ່ແຕກຕ່າງກັນ
            periods = queryset.values_list('period', flat=True).distinct()
            periods = [p for p in periods if p]  # ກຳຈັດ null values
            
            # ຈັດຮູບແບບ periods
            formatted_periods = []
            for period in periods:
                if period and len(str(period)) == 6:
                    year = str(period)[:4]
                    month = str(period)[4:]
                    formatted_periods.append({
                        'value': period,
                        'display': f"{month}/{year}",
                        'year': year,
                        'month': month
                    })
                else:
                    formatted_periods.append({
                        'value': period,
                        'display': str(period),
                        'year': None,
                        'month': None
                    })
            
            # ຈັດຮຽງຕາມລຳດັບເວລາ
            formatted_periods.sort(key=lambda x: x['value'], reverse=True)
            
            return Response({
                'periods': formatted_periods,
                'count': len(formatted_periods)
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'ເກີດຂໍ້ຜິດພາດໃນການດຶງຂໍ້ມູນ period: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UploadFileStatsView(generics.GenericAPIView):
    """API ສຳລັບດຶງສະຖິຕິການອັບໂຫຼດ"""
    
    def get(self, request, *args, **kwargs):
        try:
            user_id = request.query_params.get('user_id')
            period = request.query_params.get('period')
            request_user_id = request.query_params.get('request_user_id')
            
            # ໃຊ້ logic ດຽວກັນກັບ UploadFileList ສຳລັບສິດທິ່
            queryset = Upload_File.objects.all()
            
            if request_user_id and request_user_id != "01":
                queryset = queryset.filter(user_id=request_user_id)
            elif request_user_id == "01" and user_id:
                queryset = queryset.filter(user_id=user_id)
            
            if period:
                queryset = queryset.filter(period=period)
            
            # ຄິດໄລ່ສະຖິຕິ
            total_files = queryset.count()
            successful_uploads = queryset.filter(statussubmit__in=['1', '3']).count()
            pending_uploads = queryset.filter(statussubmit='Pending').count()
            rejected_uploads = queryset.filter(statussubmit='2').count()
            uploaded_data = queryset.filter(statussubmit__in=['4', '5']).count()
            completed_loads = queryset.filter(statussubmit='0').count()
            
            # ສະຖິຕິຕາມປະເພດໄຟລ໌
            json_files = queryset.filter(FileType='json').count()
            xml_files = queryset.filter(FileType='xml').count()
            
            # ສະຖິຕິຕາມ user (ສຳລັບ admin ເທົ່ານັ້ນ)
            user_stats = {}
            if request_user_id == "01":
                user_counts = queryset.values('user_id').annotate(
                    count=models.Count('id')
                ).order_by('-count')
                user_stats = {item['user_id']: item['count'] for item in user_counts}
            
            stats = {
                'summary': {
                    'total_files': total_files,
                    'successful_uploads': successful_uploads,
                    'pending_uploads': pending_uploads,
                    'rejected_uploads': rejected_uploads,
                    'uploaded_data': uploaded_data,
                    'completed_loads': completed_loads,
                    'success_rate': round((successful_uploads / total_files * 100), 2) if total_files > 0 else 0
                },
                'file_types': {
                    'json_files': json_files,
                    'xml_files': xml_files
                },
                'user_breakdown': user_stats,
                'filters_applied': {
                    'user_id': user_id,
                    'period': period,
                    'request_user_id': request_user_id
                }
            }
            
            return Response(stats, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'ເກີດຂໍ້ຜິດພາດໃນການຄິດໄລ່ສະຖິຕິ: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
# from rest_framework import generics
# from .models import Upload_File
# from .serializers import UploadFileSerializer

# class UploadFileList(generics.ListAPIView):
#     serializer_class = UploadFileSerializer
    
#     def get_queryset(self):
#         user_id = self.request.query_params.get('user_id')
#         if user_id:
#             return Upload_File.objects.filter(user_id=user_id)
#         return Upload_File.objects.all()
    
class UploadFilecList(generics.ListAPIView):
    serializer_class = UploadFilecSerializer
    
    def get_queryset(self):
        # ດຶງ parameters ຈາກ request
        user_id = self.request.query_params.get('user_id')
        period = self.request.query_params.get('period')
        request_user_id = self.request.query_params.get('request_user_id')
        file_type = self.request.query_params.get('file_type')  # json, xml
        status_filter = self.request.query_params.get('status')
        
        # ເລີ່ມຕົ້ນດ້ວຍ queryset ທັງໝົດ
        queryset = Upload_File_C.objects.all()
        
        # ກວດສອບສິດທິ່ຜູ້ໃຊ້
        if request_user_id and request_user_id != "01":
            # ຖ້າບໍ່ແມ່ນ admin (01) ເຫັນໄດ້ແຕ່ຂອງຕົວເອງ
            queryset = queryset.filter(user_id=request_user_id)
        elif request_user_id == "01":
            # ຖ້າເປັນ admin (01) ສາມາດເຫັນທັງໝົດ
            # ຖ້າມີການລະບຸ user_id ໃຫ້ filter ຕາມນັ້ນ
            if user_id:
                queryset = queryset.filter(user_id=user_id)
        
        # Filter ຕາມ period ຖ້າມີ
        if period:
            queryset = queryset.filter(period=period)
            
        # Filter ຕາມປະເພດໄຟລ໌
        if file_type:
            queryset = queryset.filter(FileType=file_type)
            
        # Filter ຕາມສະຖານະ
        if status_filter:
            queryset = queryset.filter(statussubmit=status_filter)
            
        return queryset.order_by('-insertDate')  # ຈັດຮຽງຕາມວັນທີໃໝ່ສຸດ
    
    def list(self, request, *args, **kwargs):
        """
        Custom list method ພ້ອມການຈັດການ error ແລະ metadata
        """
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            
            # ຄິດໄລ່ສະຖິຕິເບື້ອງຕົ້ນ
            total_files = queryset.count()
            json_files = queryset.filter(FileType='json').count()
            xml_files = queryset.filter(FileType='xml').count()
            
            response_data = {
                'count': total_files,
                'results': serializer.data,
                'summary': {
                    'total_files': total_files,
                    'json_files': json_files,
                    'xml_files': xml_files,
                    'status_breakdown': self._get_status_breakdown(queryset)
                },
                'filters_applied': {
                    'user_id': request.query_params.get('user_id'),
                    'period': request.query_params.get('period'),
                    'request_user_id': request.query_params.get('request_user_id'),
                    'file_type': request.query_params.get('file_type'),
                    'status': request.query_params.get('status')
                }
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'ເກີດຂໍ້ຜິດພາດໃນການດຶງຂໍ້ມູນ: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def _get_status_breakdown(self, queryset):
        """ຄິດໄລ່ຈຳນວນຕາມສະຖານະ"""
        status_map = ['0', '1', '2', '3', '4', '5', 'Pending']
        breakdown = {}
        for status_code in status_map:
            breakdown[status_code] = queryset.filter(statussubmit=status_code).count()
        return breakdown
# class UploadFilecList(generics.ListAPIView):
#     serializer_class = UploadFilecSerializer
    
#     def get_queryset(self):
#         user_id = self.request.query_params.get('user_id')
#         if user_id:
#             return Upload_File_C.objects.filter(user_id=user_id)
#         return Upload_File_C.objects.all()


# from rest_framework import generics
# from .models import Upload_File_C
# from .serializers import UploadFilecSerializer

# class UploadFilecList(generics.ListAPIView):
#     queryset = Upload_File_C.objects.all()
#     serializer_class = UploadFilecSerializer


# kaftka



# from django.http import JsonResponse
# from .kafka_utils import send_message
# def send_kafka_message(request):
#     message = request.GET.get('message', 'Hello, Kafka!')
#     send_message('my_topic', {'message': message})
#     return JsonResponse({'status': 'message sent'})


# # views.py
from django.shortcuts import render, redirect
from .forms import uploadForm
from .models import UploadedJSONFile
import json
import os   

def upload_file(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_path = handle_uploaded_file(file)
            UploadedJSONFile.objects.create(   
                file_name=file.name,    
                file_path=file_path
            )
            return redirect('success')
    else:
        form = uploadForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    file_path = os.path.join('uploaded_files', f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path


# views.py
from .tasks import process_large_file

def upload_file(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_path = handle_uploaded_file(file)
            UploadedJSONFile.objects.create(
                file_name=file.name,
                file_path=file_path
            )
            # Call the processing function
            process_large_file(file_path)
            return redirect('success')
    else:
        form = uploadForm()
    return render(request, 'upload.html', {'form': form})




from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Upload_File
from .tasks import process_large_file

@csrf_exempt
def upload_file_view(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_path = os.path.join('uploads', file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        process_large_file.delay(file_path)

        return JsonResponse({'message': 'File uploaded successfully. Processing started.'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)


# import logging
# from rest_framework.decorators import api_view
# from django.http import JsonResponse
# from .models import B1_Monthly, B_Data_is_damaged, data_edit, B1
# from .serializers import B1MonthlySerializer, BDataIsDamagedSerializer, DataEditSerializer, B1Serializer

# logger = logging.getLogger(__name__)

# @api_view(['GET'])
# def get_data3(request):
#     try:
#         fid = request.GET.get('FID')
#         logger.debug(f"Received FID: {fid}")

#         if not fid:
#             return JsonResponse({'error': 'FID is required'}, status=400)

#         b1_monthly_data = B1_Monthly.objects.filter(id_file=fid)
#         b1_monthly_serializer = B1MonthlySerializer(b1_monthly_data, many=True)

#         b_data_is_damaged_data = B_Data_is_damaged.objects.filter(id_file=fid)
#         b_data_is_damaged_serializer = BDataIsDamagedSerializer(b_data_is_damaged_data, many=True)

#         data_edit_data = data_edit.objects.filter(id_file=fid)
#         data_edit_serializer = DataEditSerializer(data_edit_data, many=True)

#         b1_data = B1.objects.filter(id_file=fid)
#         b1_serializer = B1Serializer(b1_data, many=True)

#         data = {
#             'B1_Monthly': b1_monthly_serializer.data,
#             'B_Data_is_damaged': b_data_is_damaged_serializer.data,
#             'data_edit': data_edit_serializer.data,
#             'B1': b1_serializer.data,
#         }

#         return JsonResponse(data, safe=False)
#     except Exception as e:
#         logger.error(f"Error fetching data: {str(e)}")
#         return JsonResponse({'error': str(e)}, status=500) 


import logging
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import B1_Monthly, B_Data_is_damaged, data_edit, B1, disputes, Upload_File
from .serializers import B1MonthlySerializer, BDataIsDamagedSerializer, DataEditSerializer, B1Serializer, disputesSerializer, UploadFileSerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_data3(request):
    try:
        fid = request.GET.get('FID')

        logger.debug(f"Received FID: {fid}")

        if not fid:
            return JsonResponse({'error': 'FID is required'}, status=400)

        b1_monthly_data = B1_Monthly.objects.filter(id_file=fid)
        b1_monthly_serializer = B1MonthlySerializer(b1_monthly_data, many=True)

        b_data_is_damaged_data = B_Data_is_damaged.objects.filter(id_file=fid)
        b_data_is_damaged_serializer = BDataIsDamagedSerializer(b_data_is_damaged_data, many=True)

        data_edit_data = data_edit.objects.filter(id_file=fid)
        data_edit_serializer = DataEditSerializer(data_edit_data, many=True)

        b1_data = B1.objects.filter(id_file=fid, status_customer=1)
        b1_serializer = B1Serializer(b1_data, many=True)

        disputes_data = disputes.objects.filter(id_file=fid)
        disputes_serializer = disputesSerializer(disputes_data, many=True)

        uploadfile_data = Upload_File.objects.filter(FID=fid).first()
        uploadfile_serializer = UploadFileSerializer(uploadfile_data)

        data = {
            'B1_Monthly': b1_monthly_serializer.data,
            'B_Data_is_damaged': b_data_is_damaged_serializer.data,
            'data_edit': data_edit_serializer.data,
            'B1': b1_serializer.data,
            'disputes': disputes_serializer.data,
            'uploadfile': uploadfile_serializer.data
        }

        return JsonResponse(data)
    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)



import logging
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import  Upload_File_C, C1, C_error ,col_real_estates, col_money_mia, col_equipment_eqi , col_project_prj, col_vechicle_veh, col_guarantor_gua, col_goldsilver_gold,C_error
from .serializers import UploadFilecSerializer, C1Serializer, C_errorSerializer,col_real_estatesSerializer, col_money_miaSerializer, col_equipment_eqiSerializer, col_project_prjSerializer, col_vechicle_vehSerializer, col_guarantor_guaSerializer, col_goldsilver_goldSerializer,C_errorSerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_data4(request):
    try:
        cid = request.GET.get('CID')

        logger.debug(f"Received CID: {cid}")

        if not cid:
            return JsonResponse({'error': 'CID is required'}, status=400)

        c1_data = C1.objects.filter(id_file=cid)
        c1_serializer = C1Serializer( c1_data, many=True)

        c_error_data= C_error.objects.filter(id_file=cid)
        c_errorSerializer = C_errorSerializer(c_error_data, many=True)

        col_real_estates_data = col_real_estates.objects.filter(id_file=cid)
        col_real_estates_serializer = col_real_estatesSerializer(col_real_estates_data, many=True)

        col_money_data = col_money_mia.objects.filter(id_file=cid)
        col_money_serializer = col_money_miaSerializer(col_money_data, many=True)

        col_equipment_eqi_data = col_equipment_eqi.objects.filter(id_file=cid)
        col_equipment_eqi_serializer = col_equipment_eqiSerializer(col_equipment_eqi_data, many=True)

        col_project_prj_data = col_project_prj.objects.filter(id_file=cid)
        col_project_prj_serializer = col_project_prjSerializer(col_project_prj_data, many=True)

        col_vechicle_veh_data = col_vechicle_veh.objects.filter(id_file=cid)
        col_vechicle_veh_serializer = col_vechicle_vehSerializer(col_vechicle_veh_data, many=True)

        col_guarantor_gua_data = col_guarantor_gua.objects.filter(id_file=cid)
        col_guarantor_gua_serializer = col_guarantor_guaSerializer(col_guarantor_gua_data, many=True)

        col_goldsilver_gold_data = col_goldsilver_gold.objects.filter(id_file=cid)
        col_goldsilver_gold_serializer = col_goldsilver_goldSerializer(col_goldsilver_gold_data, many=True)

        c1_disptes = C1_disptes.objects.filter(id_file=cid)
        c1_disptes_serializer = C1Serializer(c1_disptes, many=True)

        uploadfilec_data = Upload_File_C.objects.filter(CID=cid)
        uploadfilec_serializer = UploadFilecSerializer(uploadfilec_data, many=True)




        data = {
            'C1': c1_serializer.data,
            'C_error': c_errorSerializer.data,
            'col_real_estates': col_real_estates_serializer.data,
            'col_money_mia': col_money_serializer.data,
            'col_equipment_eqi': col_equipment_eqi_serializer.data,
            'col_project_prj': col_project_prj_serializer.data,
            'col_vechicle_veh': col_vechicle_veh_serializer.data,
            'col_guarantor_gua': col_guarantor_gua_serializer.data,
            'col_goldsilver_gold': col_goldsilver_gold_serializer.data,
            'C1_disptes': c1_disptes_serializer.data,
            'uploadfile': uploadfilec_serializer.data
           
        }

        return JsonResponse(data)
    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)




# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import B1_Monthly, B_Data_is_damaged, data_edit, B1

def get_data_by_id_file(request, id_file):
    try:
        b1_monthly_data = B1_Monthly.objects.filter(id_file=id_file).values()
        b_data_damaged = B_Data_is_damaged.objects.filter(id_file=id_file).values()
        data_edit_data = data_edit.objects.filter(id_file=id_file).values()
        b1_data = B1.objects.filter(id_file=id_file).values()

        response = {
            'B1_Monthly': list(b1_monthly_data),
            'B_Data_is_damaged': list(b_data_damaged),
            'data_edit': list(data_edit_data),
            'B1': list(b1_data)
        }
        
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from .models import Collateral

# @csrf_exempt
# def upload_image(request):
#     if request.method == 'POST':
#         if 'image' not in request.FILES:
#             return JsonResponse({'status': 'error', 'message': 'No file provided'}, status=400)

#         file = request.FILES['image']

#         try:
            
#             file_path = default_storage.save(f'collaterals/{file.name}', ContentFile(file.read()))
            
            
#             collateral = Collateral(filename=file.name, pathfile=file_path)
            
#             collateral.save()
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': f'Error saving file: {str(e)}'}, status=500)

#         return JsonResponse({'status': 'success', 'message': 'File uploaded successfully', 'filename': file.name})
    
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Collateral


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Collateral

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'status': 'error', 'message': 'No file provided'}, status=400)

        file = request.FILES['image']
        
        # ຮັບຄ່າ user_mid_id ຈາກ Frontend
        user_mid_id = request.POST.get('user_mid_id')
        if not user_mid_id:
            return JsonResponse({'status': 'error', 'message': 'No user_mid_id provided'}, status=400)
        
        try:
            # ບັນທຶກໄຟລ໌ໄວ້ທີ່ directory
            file_path = default_storage.save(f'collaterals/{file.name}', ContentFile(file.read()))
            
            # ບັນທຶກເຂົ້າຖານຂໍ້ມູນ Collateral
            collateral = Collateral(filename=file.name, pathfile=file_path, user=user_mid_id , status= '1')
            collateral.save()
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error saving file: {str(e)}'}, status=500)

        return JsonResponse({'status': 'success', 'message': 'File uploaded successfully', 'filename': file.name})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)



# test upload image for profile 
@csrf_exempt
def upload_imageprofile(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'status': 'error', 'message': 'No file provided'}, status=400)

        file = request.FILES['image']
        
        # ຮັບຄ່າ user_mid_id ຈາກ Frontend
        user_mid_id = request.POST.get('user_mid_id')
        if not user_mid_id:
            return JsonResponse({'status': 'error', 'message': 'No user_mid_id provided'}, status=400)
        
        try:
            # ບັນທຶກໄຟລ໌ໄວ້ທີ່ directory
            file_path = default_storage.save(f'profile/{file.name}', ContentFile(file.read()))
            
            # ບັນທຶກເຂົ້າຖານຂໍ້ມູນ Login
            collateral = Login( profile_picture=file_path)
            collateral.save()
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error saving file: {str(e)}'}, status=500)

        return JsonResponse({'status': 'success', 'message': 'File uploaded successfully', 'filename': file.name})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)








from django.http import JsonResponse
from .models import Collateral

def get_collaterals(request):
    # ດຶງ current_user_id ຈາກ query parameter
    current_user = request.GET.get('current_user_id')
    
    # ຖ້າບໍ່ມີ current_user_id ໃຫ້ເອົາຈາກ authentication
    if not current_user:
        current_user = request.user.username  # ຫຼື request.user.id
    
   
    collaterals = Collateral.objects.all()
    
   
    if current_user != "01":
        collaterals = collaterals.filter(user=current_user)
    else:
       
        user_id = request.GET.get('user_id')
        if user_id:
            collaterals = collaterals.filter(user=user_id)
    
    
    year = request.GET.get('year')
    if year:
        collaterals = collaterals.filter(insertdate__year=year)
    
   
    month = request.GET.get('month')
    if month:
        collaterals = collaterals.filter(insertdate__month=month)
    
   
    day = request.GET.get('day')
    if day:
        collaterals = collaterals.filter(insertdate__day=day)
    
 
    start_date = request.GET.get('start_date') 
    end_date = request.GET.get('end_date')      
    
    if start_date and end_date:
        start_datetime = f"{start_date} 00:00:00"
        end_datetime = f"{end_date} 23:59:59"
        collaterals = collaterals.filter(
            insertdate__range=[start_datetime, end_datetime]
        )
    elif start_date:
        start_datetime = f"{start_date} 00:00:00"
        collaterals = collaterals.filter(insertdate__gte=start_datetime)
    elif end_date:
        end_datetime = f"{end_date} 23:59:59"
        collaterals = collaterals.filter(insertdate__lte=end_datetime)
    
  
    collaterals = collaterals.order_by('-id')
    
 
    print(f"Found {collaterals.count()} collaterals")
    
   
    result = collaterals.values()
    return JsonResponse(list(result), safe=False)
# def get_collaterals(request):
#     collaterals = Collateral.objects.exclude(status=0).values('id', 'filename', 'image', 'pathfile', 'status')
#     return JsonResponse(list(collaterals), safe=False)


<<<<<<< HEAD
=======
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import EnterpriseInfo
# from .serializers import EnterpriseInfoSerializer

# @api_view(['POST'])
# def create_enterprise_info(request):
#     if request.method == 'POST':
#         serializer = EnterpriseInfoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# views.py
>>>>>>> 3f3aa525c05a1cae5ef85613e6d2a6220f553f1f
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EnterpriseInfo
from .serializers import EnterpriseInfoSerializer
<<<<<<< HEAD

@api_view(['POST'])
def create_enterprise_info(request):
    if request.method == 'POST':
        serializer = EnterpriseInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

=======
from django.db import transaction, IntegrityError
from datetime import datetime
import random
import string
import traceback


def generate_lcic_code():
    """ສ້າງ LCIC_code ແບບ YYYYMMDDXXXX"""
    date_str = datetime.now().strftime('%Y%m%d')
    characters = string.ascii_uppercase + string.digits
    random_str = ''.join(random.choices(characters, k=4))
    lcic_code = f"{date_str}{random_str}"
    print(f"📝 Generated LCIC_code: {lcic_code}")
    return lcic_code


def generate_unique_lcic_code(max_attempts=100):
    """ສ້າງ LCIC_code ທີ່ບໍ່ຊ້ຳກັນ"""
    print(f"🔄 Generating unique LCIC_code...")
    
    for attempt in range(max_attempts):
        lcic_code = generate_lcic_code()
        
        # ກວດສອບວ່າມີໃນ DB ແລ້ວບໍ່
        exists = EnterpriseInfo.objects.filter(LCIC_code=lcic_code).exists()
        print(f"   Attempt {attempt + 1}: {lcic_code} - Exists: {exists}")
        
        if not exists:
            print(f"✅ Unique LCIC_code found: {lcic_code}")
            return lcic_code
        
        print(f"⚠️  Code exists, retrying...")
    
    raise Exception(f"ບໍ່ສາມາດສ້າງ LCIC_code ທີ່ບໍ່ຊ້ຳກັນໄດ້ຫຼັງຈາກ {max_attempts} ຄັ້ງ")


@api_view(['POST'])
def create_enterprise_info(request):
    """API endpoint ສຳລັບສ້າງຂໍ້ມູນວິສາຫະກິດ"""
    
    print("\n" + "="*70)
    print("🚀 CREATE ENTERPRISE INFO API CALLED")
    print("="*70)
    
    # 1. ດຶງ collateral_id
    collateral_id = request.data.get('collateral_id')
    print(f"\n[STEP 1] Collateral ID: {collateral_id}")
    
    if not collateral_id:
        print("❌ ERROR: collateral_id is missing!")
        return Response({
            'status': 'error',
            'message': 'ຕ້ອງມີ collateral_id'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # ແປງເປັນ int
    try:
        collateral_id = int(collateral_id)
        print(f"✅ Collateral ID validated: {collateral_id}")
    except (ValueError, TypeError):
        print(f"❌ ERROR: Invalid collateral_id type")
        return Response({
            'status': 'error',
            'message': 'collateral_id ຕ້ອງເປັນຕົວເລກ'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # 2. Validate data
    print(f"\n[STEP 2] Validating enterprise data...")
    serializer = EnterpriseInfoSerializer(data=request.data)
    
    if not serializer.is_valid():
        print(f"❌ Validation failed!")
        print(f"Errors: {serializer.errors}")
        return Response({
            'status': 'error',
            'message': 'ຂໍ້ມູນບໍ່ຖືກຕ້ອງ',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    print(f"✅ Validation passed!")
    
    # 3. ບັນທຶກຂໍ້ມູນ
    try:
        with transaction.atomic():
            print(f"\n[STEP 3] Saving enterprise...")
            
            # 3.1 ບັນທຶກ Enterprise ກ່ອນ
            enterprise = serializer.save()
            print(f"✅ Enterprise saved!")
            print(f"   LCICID: {enterprise.LCICID}")
            print(f"   EnterpriseID: {enterprise.EnterpriseID}")
            print(f"   LCIC_code (before): '{enterprise.LCIC_code}'")
            
            # 3.2 ສ້າງ LCIC_code
            print(f"\n[STEP 4] Generating LCIC_code...")
            try:
                lcic_code = generate_unique_lcic_code(max_attempts=50)
            except Exception as e:
                print(f"❌ Failed to generate LCIC_code: {str(e)}")
                raise
            
            # 3.3 ບັນທຶກ LCIC_code
            print(f"\n[STEP 5] Saving LCIC_code to enterprise...")
            enterprise.LCIC_code = lcic_code
            enterprise.save(update_fields=['LCIC_code'])
            print(f"✅ LCIC_code saved!")
            
            # 3.4 Verify
            enterprise.refresh_from_db()
            print(f"   LCIC_code (after): '{enterprise.LCIC_code}'")
            
            if enterprise.LCIC_code != lcic_code:
                print(f"❌ ERROR: LCIC_code not saved correctly!")
                print(f"   Expected: {lcic_code}")
                print(f"   Got: {enterprise.LCIC_code}")
                raise Exception("LCIC_code verification failed!")
            
            # 3.5 ອັບເດດ Collateral
            print(f"\n[STEP 6] Updating Collateral...")
            try:
                collateral = Collateral.objects.get(id=collateral_id)
                print(f"✅ Found Collateral:")
                print(f"   ID: {collateral.id}")
                print(f"   Filename: {collateral.filename}")
                print(f"   LCIC_reques (before): '{collateral.LCIC_reques}'")
                
                # ບັນທຶກ LCIC_code ໃສ່ Collateral
                collateral.LCIC_reques = lcic_code
                collateral.save(update_fields=['LCIC_reques'])
                
                # Verify
                collateral.refresh_from_db()
                print(f"   LCIC_reques (after): '{collateral.LCIC_reques}'")
                
                if collateral.LCIC_reques != lcic_code:
                    print(f"❌ ERROR: Collateral LCIC_reques not saved!")
                    raise Exception("Collateral update failed!")
                
                print(f"✅ Collateral updated successfully!")
                
            except Collateral.DoesNotExist:
                print(f"❌ ERROR: Collateral ID {collateral_id} not found!")
                raise Exception(f'ບໍ່ພົບຂໍ້ມູນ Collateral ID: {collateral_id}')
            
            # 3.6 Return success response
            print(f"\n[STEP 7] Preparing response...")
            print("="*70)
            print("✅✅✅ SUCCESS! ✅✅✅")
            print("="*70)
            print(f"Enterprise:")
            print(f"  - LCICID: {enterprise.LCICID}")
            print(f"  - LCIC_code: {enterprise.LCIC_code}")
            print(f"  - EnterpriseID: {enterprise.EnterpriseID}")
            print(f"\nCollateral:")
            print(f"  - ID: {collateral.id}")
            print(f"  - LCIC_reques: {collateral.LCIC_reques}")
            print("="*70 + "\n")
            
            return Response({
                'status': 'success',
                'message': 'ສ້າງຂໍ້ມູນວິສາຫະກິດສຳເລັດແລ້ວ',
                'data': {
                    'enterprise': {
                        'LCICID': enterprise.LCICID,
                        'LCIC_code': enterprise.LCIC_code,
                        'EnterpriseID': enterprise.EnterpriseID,
                        'enterpriseNameLao': enterprise.enterpriseNameLao,
                        'eneterpriseNameEnglish': enterprise.eneterpriseNameEnglish,
                        'investmentAmount': enterprise.investmentAmount,
                    },
                    'collateral': {
                        'id': collateral.id,
                        'filename': collateral.filename,
                        'LCIC_reques': collateral.LCIC_reques,
                        'status': collateral.status,
                    }
                }
            }, status=status.HTTP_201_CREATED)
            
    except Exception as e:
        print(f"\n{'='*70}")
        print(f"❌❌❌ ERROR! ❌❌❌")
        print(f"{'='*70}")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print(f"\nFull traceback:")
        traceback.print_exc()
        print(f"{'='*70}\n")
        
        return Response({
            'status': 'error',
            'message': f'ເກີດຂໍ້ຜິດພາດ: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
>>>>>>> 3f3aa525c05a1cae5ef85613e6d2a6220f553f1f
from django.http import JsonResponse
from .models import C1

def get_login3(request):
    c1_records = C1.objects.all().values()
    return JsonResponse(list(c1_records), safe=False)


# views.py
# from django.http import JsonResponse
# from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import login_required

# User = get_user_model()

# @login_required
# def get_login3(request):
#     user = request.user
#     data = {
#         "username": user.username,
#         "id": user.id,
#     }
#     return JsonResponse(data)
import logging

# class UserProfileView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         logging.info(f"Request Headers: {request.headers}")
#         logging.info(f"User: {request.user}")
#         user = request.user
#         serializer = LoginSerializer(user)
#         return Response(serializer.data)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=400)
        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({'error': 'Invalid username or password'}, status=400)
        if not user.check_password(password):
            return Response({'error': 'Invalid username or password'}, status=400)
        serializer = UserSerializer(user)
        return Response(serializer.data)


# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import EnterpriseInfo
# from .serializers import EnterpriseInfoSerializer

# @api_view(['POST'])
# def create_enterprise_info(request):
#     if request.method == 'POST':
#         serializer = EnterpriseInfoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print(serializer.errors)  
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EnterpriseInfo
from .serializers import EnterpriseInfoSerializer
from django.db.models import Max

# @api_view(['POST'])
# def create_enterprise_info(request):
#     if request.method == 'POST':
#         serializer = EnterpriseInfoSerializer(data=request.data)
#         if serializer.is_valid():
            
#             max_lcicid = EnterpriseInfo.objects.aggregate(max_lcicid=Max('LCICID'))['max_lcicid']
            
            
#             if max_lcicid is not None:
#                 new_lcicid = max_lcicid + 1
#             else:
#                 new_lcicid = 1  

            
#             serializer.validated_data['LCICID'] = new_lcicid
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def create_enterprise_info(request):
#     if request.method == 'POST':
#         serializer = EnterpriseInfoSerializer(data=request.data)
#         if serializer.is_valid():
            
#             max_lcicid = EnterpriseInfo.objects.aggregate(max_lcicid=Max('LCICID'))['max_lcicid']
            
#             if max_lcicid is not None:
#                 new_lcicid = max_lcicid + 1
#             else:
#                 new_lcicid = 1  

#             serializer.validated_data['LCICID'] = new_lcicid
#             serializer.save()

            
#             # Collateral.objects.filter(status='1').update(status='0')

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EnterpriseInfo

@api_view(['GET'])
def get_last_lcicid(request):
    last_lcicid = EnterpriseInfo.objects.latest('LCICID').LCICID
    return Response({'last_lcicid': last_lcicid})


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Collateral

# @csrf_exempt
# def confirm_image(request, id):
#     if request.method == 'POST':
#         try:
#             collateral = Collateral.objects.get(id=id)
#             collateral.status = 0
#             collateral.save()
#             return JsonResponse({'status': 'success', 'message': 'Image confirmed successfully'})
#         except Collateral.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Image not found'}, status=404)

#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

import logging
logger = logging.getLogger(__name__)

@csrf_exempt
def confirm_image(request, id):
    if request.method == 'POST':
        try:
            logger.info(f"Confirming image with id: {id}")
            collateral = Collateral.objects.get(id=id)
            collateral.status = 0
            collateral.save()
            logger.info(f"Image with id {id} confirmed successfully")
            return JsonResponse({'status': 'success', 'message': 'Image confirmed successfully'})
        except Collateral.DoesNotExist:
            logger.error(f"Image with id {id} not found")
            return JsonResponse({'status': 'error', 'message': 'Image not found'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


from django.middleware.csrf import get_token
from django.http import JsonResponse

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            
            print("User_info: ", user)
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            
            user_data = UserLoginSerializer(user).data
            
            return Response({
                'detail': 'Successfully logged in.',
                'access': str(access_token),
                'refresh': str(refresh),
                'user':user_data,
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Paylay Pherm
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Login, User_Group, memberInfo
# from .serializers import LoginSerializer
# from django.contrib.auth.hashers import make_password
# import logging
# logger = logging.getLogger(__name__)


# class UserManagementView(APIView):
#     parser_classes = [MultiPartParser, FormParser]
    
#     def post(self, request):
#         # Your code here to handle POST request
#         data = request.data.copy()
#         if 'profile_image' in request.FILES:
#             data['profile_image'] = request.FILES['profile_image']

#         serializer = LoginSerializer(data=request.data)
        
#         if serializer.is_valid():
#             user = serializer.save()

#             return Response({
#                 'success': 'User created successfully',
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
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

class UserManagementView(APIView):
    """
    Clean and secure user management view with proper error handling
    """
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [IsAuthenticated]  # Add authentication

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """
        Create new user with bank code validation and comprehensive error handling
        """
        try:
            # Fix field name mismatch - handle both profile_image and profile_image_url
            data = request.data.copy()
            
            # If profile_image_url is provided instead of profile_image, fix it
            if 'profile_image_url' in request.FILES and 'profile_image' not in request.FILES:
                data['profile_image'] = request.FILES['profile_image_url']
            
            serializer = LoginSerializer(data=data)
            
            if serializer.is_valid():
                user = serializer.save()
                
                # Log successful creation
                logger.info(f'User created successfully: {user.username} by {request.user.username}')
                
                return Response({
                    'success': True,
                    'message': 'User created successfully',
                    'data': {
                        'UID': user.UID,
                        'username': user.username,
                        'nameL': user.nameL,
                        'surnameL': user.surnameL,
                        'nameE': user.nameE,
                        'surnameE': user.surnameE,
                        'bnk_code': user.bnk_code,
                        'branch_id': user.branch_id,
                        'GID': user.GID.GID if user.GID else None,
                        'MID': user.MID.pk if user.MID else None,
                        'profile_image_url': f'/{user.profile_image.name}' if user.profile_image else None,
                        'is_active': user.is_active,
                        'created_at': user.insertDate.isoformat()
                    }
                }, status=status.HTTP_201_CREATED)
            
            # Handle validation errors
            return Response({
                'success': False,
                'message': 'Validation failed',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
        except ValidationError as e:
            logger.error(f'Validation error creating user: {str(e)}')
            return Response({
                'success': False,
                'message': 'Validation error',
                'errors': {'non_field_errors': [str(e)]}
            }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            logger.error(f'Unexpected error creating user: {str(e)}')
            return Response({
                'success': False,
                'message': 'Internal server error',
                'errors': {'non_field_errors': ['An unexpected error occurred']}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        """
        Get user details or list users (optional enhancement)
        """
        try:
            user_id = request.query_params.get('uid')
            
            if user_id:
                # Get specific user
                try:
                    user = Login.objects.select_related('MID', 'GID').get(UID=user_id)
                    serializer = LoginSerializer(user)
                    return Response({
                        'success': True,
                        'data': serializer.data
                    })
                except Login.DoesNotExist:
                    return Response({
                        'success': False,
                        'message': 'User not found'
                    }, status=status.HTTP_404_NOT_FOUND)
            
            # List users (with pagination in real implementation)
            users = Login.objects.select_related('MID', 'GID').filter(is_active=True)[:20]
            serializer = LoginSerializer(users, many=True)
            
            return Response({
                'success': True,
                'data': serializer.data,
                'count': users.count()
            })
            
        except Exception as e:
            logger.error(f'Error retrieving user(s): {str(e)}')
            return Response({
                'success': False,
                'message': 'Error retrieving user data'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EnterpriseInfo, B1_Yearly, InvestorInfo, B1_Monthly, C1, request_charge
from django.forms.models import model_to_dict
from .serializers import EnterpriseInfoSerializer, B1_YearlySerializer, InvestorInfoSerializer, B1Serializer, RequestChargeSerializer
from datetime import date, timedelta
from django.db.models import Q

class FCR_reportView(APIView):    
    def get(self, request):
        enterprise_id = request.GET.get('EnterpriseID')
        lcic_id = request.GET.get('LCIC_code')

        print(enterprise_id)
        print("test print",lcic_id)

        status_inactive = "INACTIVE"
        status_active = "ACTIVE"

        # --- Get dynamic years from catalog ---
        year_record = Main_catalog_cat.objects.filter(ct_type="FRY").first()
        inactive_years = int(year_record.cat_value) if year_record else 3  # fallback 3 years
        cutoff_date = date.today() - timedelta(days=inactive_years * 365)
        
        # --- Apply loan filters ---
        loan_info = B1.objects.filter(
            com_enterprise_code=enterprise_id
        ).exclude(
            Q(lon_status="INACTIVE") & Q(lon_exp_date__lt=cutoff_date)
        ).order_by('lon_status')
        # -------------------------------------
        
        try:
           
            ent_info = EnterpriseInfo.objects.filter(EnterpriseID=enterprise_id, LCIC_code=lcic_id)
            loan_info = B1.objects.filter(
            com_enterprise_code=enterprise_id
                ).exclude(
                    Q(lon_status="INACTIVE") & Q(lon_exp_date__lt=cutoff_date)
                ).order_by('lon_status')
            inves_info = InvestorInfo.objects.filter(EnterpriseID=enterprise_id)
            search_history = request_charge.objects.filter(LCIC_code=lcic_id)
            
            
            
         

            if not ent_info.exists():
                return Response({"detail": "Enterprise information not found."}, status=status.HTTP_404_NOT_FOUND)

            loan_info_list_active = []   

            
            col_type_to_model = {
                'C2.1': col_real_estates,
                'C2.2': col_money_mia,
                'C2.3': col_equipment_eqi,
                'C2.4': col_project_prj,
                'C2.5': col_vechicle_veh,
                'C2.6': col_guarantor_gua,
                'C2.7': col_goldsilver_gold,
            }
            
            for loan in loan_info:
                    lon_class_history = B1_Monthly.objects.filter(
                        com_enterprise_code=enterprise_id,
                        bnk_code=loan.bnk_code,
                        customer_id=loan.customer_id,
                        branch_id=loan.branch_id,
                        loan_id=loan.loan_id,
                    ).order_by('-period')[:12]
                    
                  
                    
                    lon_class_history_list = list(lon_class_history.values())

                    
                    colleteral_list = C1.objects.filter(
                        com_enterprise_code=enterprise_id,
                        bnk_code=loan.bnk_code,
                        branch_id_code=loan.branch_id,
                        bank_customer_ID=loan.customer_id,
                        loan_id=loan.loan_id,
                    )
                    print("Colleteral ---------------> : ", colleteral_list)
                    
                    
                    collateral_history_list = []
                    for collateral in colleteral_list:
                        col_id = collateral.col_id
                        col_type = collateral.col_type

                       
                        

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

                               
                                collateral_history_list.append({
                                    "col_id": col_id,
                                    "col_type": col_type,
                                    "collateral_info": collateral_dict, #C1
                                    "related_record": related_record_dict, #C2.n
                                })
                        else:
                            print(f"Unrecognized col_type: {col_type} for collateral ID {col_id}")
                    
                    lon_purpose_detail = (
                        Main_catalog_cat.objects.filter(ct_type="LPR", cat_value=loan.lon_purpose_code)
                        .first()
                    )

                    lon_purpose_detail = lon_purpose_detail.cat_lao_name if lon_purpose_detail else None
                        
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
                        # "lon_purpose_code": loan.lon_purpose_code,
                        "lon_purpose_code": lon_purpose_detail,
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
                    
            # Exclude bnk_code=01 directly in query
            search_history = request_charge.objects.filter(
                LCIC_code=lcic_id
            ).exclude(bnk_code="01")

            lon_search_history_list = []
            for lon_search in search_history:
                print(lon_search.lon_purpose)
                lon_purpose_detail = Main_catalog_cat.objects.filter(cat_value=lon_search.lon_purpose)
                
                for lon_pur_code in lon_purpose_detail:
                    print("Loan_purpose:-->", lon_pur_code.cat_lao_name)

                search_data = {
                    "id": lon_search.insert_date,
                    "bnk_code": lon_search.bnk_code,
                    "lon_purpose": lon_pur_code.cat_lao_name if lon_purpose_detail.exists() else None
                }
                lon_search_history_list.append(search_data)

            ent_info_serializer = EnterpriseInfoSerializer(ent_info, many=True)
            loan_info_serializer = B1Serializer(loan_info, many=True)
            inves_info_serializer = InvestorInfoSerializer(inves_info, many=True)
            request_charge_serializer = RequestChargeSerializer(search_history, many=True)
            print("---> FCR Report View: ", request_charge_serializer)
            
            
            response_data = {
                'enterprise_info': ent_info_serializer.data,
                'loan_info': loan_info_serializer.data,
                'inves_info': inves_info_serializer.data,
                'active_loans': loan_info_list_active,
                # 'search_history': request_charge_serializer.data
                'search_history':lon_search_history_list
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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer,UserLoginSerializer
from django.contrib.auth import login
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta


# ............................................................................//...................................................................................



# class UserLoginView(APIView):
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.validated_data['user']
#             # print("User_info: ", user)
            
#             # Generate JWT tokens
#             refresh = RefreshToken.for_user(user)
#             access_token = refresh.access_token

#             # user_role = user.GID
#             user_data = UserLoginSerializer(user).data
#             print("user_data: ", user_data)
            
#             return Response({
#                 'detail': 'Successfully logged in.',
#                 'access': str(access_token),
#                 'refresh': str(refresh),
#                 'user':user_data,
#             }, status=status.HTTP_200_OK)
     
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import LoginSerializer,UserLoginSerializer
# from django.contrib.auth import login
# from django.shortcuts import redirect
# from rest_framework.authtoken.models import Token
# from .models import UserLoginLog, Login
# from django.utils import timezone
# from datetime import timedelta
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.tokens import RefreshToken
# class UserLoginView(APIView):
#     permission_classes = [AllowAny]  # Ensure login is open to unauthenticated users

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         # Authenticate user based on your custom model
#         try:
#             user = Login.objects.get(username=username)
#             if not user.check_password(password):
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
#             # Generate JWT token
#             refresh = RefreshToken.for_user(user)
            
#             # login_time = Login(
#             #     last_login = datetime.now()
#             # )
#             # login_time.save()
            
#             # login_time.save()            
#             print("----> Login were added Here ")
            
#             return Response({
#                 'detail': 'Successfully logged in.',
#                 'access': str(refresh.access_token),
#                 'refresh': str(refresh),
#                 'user': {
#                     'UID': user.UID,
#                     'MID': {
#                         'id': user.MID.bnk_code if user.MID else None,
#                         'code': user.MID.code if user.MID else None
#                     },
#                     'GID': {
#                         'GID': user.GID.GID if user.GID else None,
#                         'nameL': user.GID.nameL if user.GID else None
#                     },
#                     'username': user.username,
#                     'nameL': user.nameL,
#                     'nameE': user.nameE,
#                     'surnameL': user.surnameL,
#                     'surnameE': user.surnameE,
#                     'is_active': user.is_active,
#                     'last_login': user.last_login,
#                     'is_staff': user.is_staff,
#                     'is_superuser': user.is_superuser
#                 }
#             }, status=status.HTTP_200_OK)
#         except Login.DoesNotExist:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Login
class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = Login.objects.get(username=username)
            if not user.check_password(password):
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            # Update last_login
            user.last_login = datetime.now()
            user.save(update_fields=['last_login'])

            # Create tokens
            refresh = RefreshToken.for_user(user)

            # Return only the path under MEDIA_ROOT, e.g. "/profile_images/foo.png"
            profile_path = f"/{user.profile_image.name}" if user.profile_image else None

            return Response({
                'detail': 'Successfully logged in.',
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': {
                    'UID': user.UID,
                    'MID': {
                        'id': user.MID.bnk_code if user.MID else None,
                        'code': user.MID.code if user.MID else None,
                    },
                    'GID': {
                        'GID': user.GID.GID if user.GID else None,
                        'nameL': user.GID.nameL if user.GID else None,
                    },
                    'username': user.username,
                    'nameL': user.nameL,
                    'nameE': user.nameE,
                    'surnameL': user.surnameL,
                    'surnameE': user.surnameE,
                    'profile_image': profile_path,
                    'is_active': user.is_active,
                    'last_login': user.last_login,
                    'is_staff': user.is_staff,
                    'is_superuser': user.is_superuser,
                }
            }, status=status.HTTP_200_OK)

        except Login.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



# from django.db.models import IntegerField
# from django.db.models.functions import Cast
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import memberInfo  # Make sure to import your model
# from .serializers import MemberInfoSerializer  # Make sure to import your serializer

# class memberinfolistView(APIView):
#     def get(self, request):
        
#         member_info = memberInfo.objects.annotate(
#             bnk_code_as_int=Cast('bnk_code', IntegerField())
#         ).order_by('bnk_code_as_int')
        
#         serializer = MemberInfoSerializer(member_info, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework import viewsets
from .models import User_Group
from .serializers import UserGroupSerializer

class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = User_Group.objects.all().order_by('GID')
    serializer_class = UserGroupSerializer


from django.db.models import IntegerField
from django.db.models.functions import Cast
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import memberInfo  # Make sure to import your model
from .serializers import MemberInfoSerializer  # Make sure to import your serializer

class memberinfolistView(APIView):
    def get(self, request):
        # Exclude records where bnk_code is '01' and cast bnk_code as integer
        member_info = memberInfo.objects.annotate(
            bnk_code_as_int=Cast('bnk_code', IntegerField())
        ).order_by('bnk_code_as_int')
        
        serializer = MemberInfoSerializer(member_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from .serializers import SidebarItemSerializer
from .models import SidebarItem, Role


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
        


from .serializers import RoleSerializer, SidebarItemSerializer, SidebarSubItemSerializer
class RoleListView(APIView):
    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SidebarItemListView(APIView):
    def get(self, request):
        sidebar_items = SidebarItem.objects.all().order_by('id')
        serializer = SidebarItemSerializer(sidebar_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SidebarSubItemListView(APIView):
    def get(self, request):
        sidebar_sub_items = SidebarSubItem.objects.all()
        serializer = SidebarSubItemSerializer(sidebar_sub_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SidebarCreateView(APIView):
    def post(self, request):
        # Determine whether creating SidebarItem or SidebarSubItem
        item_type = request.data.get('item_type')

        if item_type == 'sidebar_item':
            serializer = SidebarItemSerializer(data=request.data)
        elif item_type == 'sidebar_sub_item':
            serializer = SidebarSubItemSerializer(data=request.data)
        else:
            return Response({"error": "Invalid item_type specified."}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """Update SidebarItem or SidebarSubItem by ID"""
        item_type = request.data.get('item_type')

        if item_type == 'sidebar_item':
            try:
                instance = SidebarItem.objects.get(pk=pk)
            except SidebarItem.DoesNotExist:
                return Response({"error": "SidebarItem not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = SidebarItemSerializer(instance, data=request.data)
        
        elif item_type == 'sidebar_sub_item':
            try:
                instance = SidebarSubItem.objects.get(pk=pk)
            except SidebarSubItem.DoesNotExist:
                return Response({"error": "SidebarSubItem not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = SidebarSubItemSerializer(instance, data=request.data)
        
        else:
            return Response({"error": "Invalid item_type specified."}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete SidebarItem or SidebarSubItem by ID"""
        item_type = request.query_params.get('item_type')

        if item_type == 'sidebar_item':
            try:
                instance = SidebarItem.objects.get(pk=pk)
                instance.delete()
                return Response({"success": "SidebarItem deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            except SidebarItem.DoesNotExist:
                return Response({"error": "SidebarItem not found."}, status=status.HTTP_404_NOT_FOUND)

        elif item_type == 'sidebar_sub_item':
            try:
                instance = SidebarSubItem.objects.get(pk=pk)
                instance.delete()
                return Response({"success": "SidebarSubItem deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            except SidebarSubItem.DoesNotExist:
                return Response({"error": "SidebarSubItem not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": "Invalid item_type specified."}, status=status.HTTP_400_BAD_REQUEST) 

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
        
    
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import pytz  # Import pytz to handle timezone conversion

class ManageUserView(APIView):

    def get(self, request, format=None):
        # Define the timezone (e.g., Asia/Bangkok)
        target_timezone = pytz.timezone('Asia/Bangkok')
        
        # Fetch all users and order by 'UID', including related 'memberInfo' (MID)
        all_users = Login.objects.select_related('MID').order_by('UID')

        custom_user_data = []

        # Loop through all users and extract necessary fields, including memberInfo (bank) fields
        for user in all_users:
            if user.MID:  # Ensure that the user has a related MID
                bank_info = user.MID  # Access the related memberInfo (MID) directly

                # Convert last_login to the target timezone
                last_login_local = user.last_login.astimezone(target_timezone) if user.last_login else None
                formatted_last_login_local = last_login_local.strftime('%Y-%m-%d %H:%M:%S') if last_login_local else None
                custom_user_data.append({
                    "UID": user.UID,
                    "bnk_code": bank_info.bnk_code if bank_info else None,  # Access bank code from memberInfo
                    "bnk_name": bank_info.nameL if bank_info else None,  # Access bank name from memberInfo
                    "Permission": user.GID.nameL if user.GID else None,  # Handle case where GID may be null
                    "username": user.username,
                    "nameL": user.nameL,
                    "nameE": user.nameE,
                    "surnameL": user.surnameL,
                    "surnameE": user.surnameE,
                    "last_login": formatted_last_login_local,  # Use the converted last_login
                    "is_active": user.is_active,
                })
                
        # Prepare the combined response
        combined_data = {
            'all_user': custom_user_data,
        }
        
        return Response(combined_data, status=status.HTTP_200_OK)

    
    
    def post(self, request, format=None):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(data['password']))
            return Response(LoginSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    



# from .serializers import SearchLogSerializer

# class searchlog_reportView(APIView):
#     # permission_classes = [IsAuthenticated]
    
#     def get(self, request):
#         searchlog_report = searchLog.objects.all()
#         serializer = SearchLogSerializer(searchlog_report, many=True)  # many=True because it's a queryset
        
#         return Response({
#             'logged': serializer.data
#         }, status=status.HTTP_200_OK)


# from .models import searchLog,memberInfo
# from .serializers import SearchLogSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class searchlog_reportView(APIView):
#     # permission_classes = [IsAuthenticated]

#        def get(self, request, bnk_code=None):                
#         try:
#             # Get query parameters
#             bank = request.query_params.get('bank', bnk_code)
#             month = request.query_params.get('month')
#             year = request.query_params.get('year')
#             from_date = request.query_params.get('fromDate')
#             to_date = request.query_params.get('toDate')


#             # Start with the searchLog queryset
#             search_log_queryset = searchLog.objects.all()

#             # Apply filters based on query parameters
#             if bank:
#                 search_log_queryset = search_log_queryset.filter(bnk_code=bank)
#             if year:
#                 search_log_queryset = search_log_queryset.filter(inquiry_date__year=year)
#                 if month:
#                     search_log_queryset = search_log_queryset.filter(inquiry_date__month=month)
#             elif month:
#                 # If month is provided without year, return an error
#                 return Response({
#                     'error': 'Year is required when filtering by month.'
#                 }, status=status.HTTP_400_BAD_REQUEST)
#             if from_date and to_date:
#                 search_log_queryset = search_log_queryset.filter(inquiry_date__range=[from_date, to_date])
#             elif from_date:
#                 search_log_queryset = search_log_queryset.filter(inquiry_date__gte=from_date)
#             elif to_date:
#                 search_log_queryset = search_log_queryset.filter(inquiry_date__lte=to_date)
                        
#             # Annotate the counts from both models
#             bank_info = memberInfo.objects.filter(bnk_code=bank)
            
#             results = (
#                 search_log_queryset
#                 .values('bnk_code')
#                 .annotate(
#                     searchlog_count=Count('search_ID', filter=Q(rec_enquiry_type='')),  # Count search_ID where rec_enquiry_type is '1'
#                     request_charge_count=Count('request_charge__chg_amount')
#                 )
#                 .order_by(Cast('bnk_code', IntegerField()))  # Order by bnk_code as Integer
#             )

#             # Prepare the response data
#             response_data = list(results)
            

#             return Response(response_data, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({
#                 'error': str(e)
#             }, status=status.HTTP_400_BAD_REQUEST)


from django.db.models import Count, IntegerField, Q
from django.db.models.functions import Cast
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import searchLog, request_charge, memberInfo
from .serializers import SearchLogSerializer

class searchlog_reportView(APIView):
    
    def get(self, request, bnk_code=None):
        try:
            # Get query parameters
            bank = request.query_params.get('bank', bnk_code)
            month = request.query_params.get('month')
            year = request.query_params.get('year')
            from_date = request.query_params.get('fromDate')
            to_date = request.query_params.get('toDate')
            
            search_log_queryset = searchLog.objects.exclude(bnk_code='01')
            if bank:
                search_log_queryset = search_log_queryset.filter(bnk_code=bank)
            
            if year:
                search_log_queryset = search_log_queryset.filter(inquiry_date__year=year)
                if month:
                    search_log_queryset = search_log_queryset.filter(inquiry_date__month=month)
            elif month:
                return Response({'error': 'Year is required when filtering by month.'}, status=status.HTTP_400_BAD_REQUEST)
            
            if from_date:
                from_date = datetime.strptime(from_date, '%Y-%m-%d')  # Parse fromDate as a date
            if to_date:
                to_date = datetime.strptime(to_date, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)  # End of the day

            if from_date and to_date:
                search_log_queryset = search_log_queryset.filter(inquiry_date__range=[from_date, to_date])
            elif from_date:
                search_log_queryset = search_log_queryset.filter(inquiry_date__gte=from_date)
            elif to_date:
                search_log_queryset = search_log_queryset.filter(inquiry_date__lte=to_date)

            # Annotate counts for search logs and request charges
            results = (
                search_log_queryset
                .values('bnk_code')
                .annotate(
                    searchlog_count=Count('search_ID', filter=Q(rec_enquiry_type='')),  # Count where rec_enquiry_type='1'
                    request_charge_count=Count('request_charge__chg_amount')  # Count related request_charge entries
                )
                .order_by(Cast('bnk_code', IntegerField()))
            )
            # bnk_code_loop = result['bnk_code']
            
            # print("--------L Bank_Code_Loop : ", bnk_code_loop)
            # Prepare the custom response with bank info
            response_data = []
            for result in results:
                bnk_code = result.get('bnk_code')  # Access bnk_code from each dictionary
                
                # Retrieve the bank information based on bnk_code
                bank_info_data = memberInfo.objects.filter(bnk_code=bnk_code).first()
                bank_info_name = bank_info_data.nameL if bank_info_data else "N/A"
                bank_short_form = bank_info_data.code if bank_info_data else "N/A"

                # Append the result with bank details
                response_data.append({
                    "bnk_code": bnk_code,
                    "Bank_short_form": f"{bank_short_form}-{bank_info_name}",
                    "searchlog_count": result.get('searchlog_count', 0),
                    "request_log": result.get('request_charge_count', 0)
                })

            return Response({"charge_report": response_data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
from .models import searchLog, request_charge, memberInfo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

class SearchlogReportDetailView(APIView):
    def get(self, request):
        # Retrieve query parameters
        bank = request.query_params.get('bank')
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        from_date = request.query_params.get('fromDate')
        to_date = request.query_params.get('toDate')

        # Initial queryset for SearchLog with rec_enquiry_type='1' and bnk_code not '01'
        searchlog_queryset = searchLog.objects.filter(rec_enquiry_type='').exclude(bnk_code='01')

        # Apply filtering based on query parameters
        if bank:
            searchlog_queryset = searchlog_queryset.filter(bnk_code=bank)
        
        if year:
            searchlog_queryset = searchlog_queryset.filter(inquiry_date__year=year)
            if month:
                searchlog_queryset = searchlog_queryset.filter(inquiry_date__month=month)
        elif month:
            return Response({'error': 'Year is required when filtering by month.'}, status=status.HTTP_400_BAD_REQUEST)

        if from_date:
                from_date = datetime.strptime(from_date, '%Y-%m-%d')  # Parse fromDate as a date
        if to_date:
                to_date = datetime.strptime(to_date, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)  # End of the day
                
        if from_date and to_date:
            searchlog_queryset = searchlog_queryset.filter(inquiry_date__range=[from_date, to_date])
        elif from_date:
            searchlog_queryset = searchlog_queryset.filter(inquiry_date_gte=from_date)
        elif to_date:
            searchlog_queryset = searchlog_queryset.filter(inquiry_date__lte=to_date)

        # Check if there are records
        if not searchlog_queryset.exists():
            return Response({'detail': 'No records found for the provided filters.'}, status=status.HTTP_404_NOT_FOUND)

        # Prepare separate lists for SearchLog and request_charge details
        searchlog_details = []
        request_charge_details = []

        # Iterate over each SearchLog record
        for log in searchlog_queryset:
            # Fetch related bank info
            bank_info = memberInfo.objects.filter(bnk_code=log.bnk_code).first()
            bank_name = bank_info.nameL if bank_info else None
            bank_short_form = bank_info.code if bank_info else None
            
            en_data = EnterpriseInfo.objects.filter(LCICID=log.LCIC_ID).first()
                
                
            # Populate searchlog details
            log_data = {
                "search_ID": log.search_ID,
                "sys_usr": log.sys_usr,
                "bnk_code": f"{log.bnk_code} - {bank_short_form}",
                "bank_name": bank_name,
                "lcic_id": en_data.enterpriseNameLao,
                "insert_date": log.inquiry_date,

            }
            searchlog_details.append(log_data)

            # Retrieve related request_charge records for this SearchLog entry
        related_request_charges = request_charge.objects.filter(bnk_code=log.bnk_code)

            # Apply the same date filters to request_charge queryset
        if year:
            related_request_charges = related_request_charges.filter(rec_insert_date__year=year)
            if month:
                related_request_charges = related_request_charges.filter(rec_insert_date__month=month)
                
        # if from_date:
        #         from_date = datetime.strptime(from_date, '%Y-%m-%d')  # Parse fromDate as a date
        # if to_date:
        #         to_date = datetime.strptime(to_date, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)  # End of the day
                
        if from_date and to_date:
            related_request_charges = related_request_charges.filter(rec_insert_date__range=[from_date, to_date])
        elif from_date:
            related_request_charges = related_request_charges.filter(rec_insert_date__gte=from_date)
        elif to_date:
            related_request_charges = related_request_charges.filter(rec_insert_date__lte=to_date)

            # Add each filtered request_charge record to the request_charge_details list
        for charge in related_request_charges:
            charge_data = {
                "rec_charge_ID": charge.rec_charge_ID,
                "bnk_code": f"{log.bnk_code} - {bank_short_form}",
                "sys_usr": charge.user_sys_id,
                "bank_name": bank_name,
                "lcic_id": en_data.enterpriseNameLao,
                "rec_insert_date": charge.rec_insert_date,
            }
            request_charge_details.append(charge_data)

        # Structure the response to include separate lists
        response_data = {
            'searchlog': searchlog_details,
            'request_charge': request_charge_details
        }
        return Response(response_data, status=status.HTTP_200_OK)

# from .serializers import ChargeSerializer
# class charge_reportView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, bnk_code=None):
#         try:
#             # Filter the charge records by bnk_code if provided
#             if bnk_code:
#                 charge_report = request_charge.objects.filter(bnk_code=bnk_code)
#             else:
#                 charge_report = request_charge.objects.all().order_by('insert_date')

#             # If no records are found, return an appropriate message
#             if not charge_report.exists():
#                 return Response({
#                     'detail': 'No charges found for the provided bnk_code.'
#                 }, status=status.HTTP_404_NOT_FOUND)

#             # Serialize the data
#             serializer = ChargeSerializer(charge_report, many=True)
            
#             return Response({
#                 'charge': serializer.data
#             }, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({
#                 'error': str(e)
#             }, status=status.HTTP_400_BAD_REQUEST)


# from .serializers import ChargeSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import request_charge  # Assuming this is your model
# from django.db.models import Q  # To handle complex queries

# class charge_reportView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, bnk_code=None):
#         try:
#             # Get query parameters
#             bank = request.query_params.get('bank', bnk_code)  # Can come from URL or query param
#             month = request.query_params.get('month')
#             year = request.query_params.get('year')
#             from_date = request.query_params.get('fromDate')  # New: fromDate filter
#             to_date = request.query_params.get('toDate')      # New: toDate filter

#             # Start with all records or filter by bank if provided
#             charge_report = request_charge.objects.all().order_by('-rec_charge_ID')
            
#             charge_report_list = []       
#             for charge_field in charge_report:
#                 # print(charge_field)
                    
#                 enterprise_data = EnterpriseInfo.objects.filter         (LCICID=charge_field.LCIC_ID)

#                 lon_purpose_data = Main_catalog_cat.objects.filter(cat_value=charge_field.lon_purpose)
#                 # print(lon_purpose_data)
                
#                 bank_info = memberInfo.objects.filter
            
#                 # for bank_data in 
                
#                 for lon_list in lon_purpose_data:
#                     print("Loan_purpose: ",lon_list.cat_name)
            
#                 # print("====> Enterprise_Data LCICID : ",enterprise_data)
#                 for enter_data in enterprise_data:
#                     print("-=---->",enter_data.enterpriseNameLao)
            
#             charge_data_list = {
#                 "rec_charge_ID": charge_field.rec_charge_ID,
#                 "bnk_code": charge_field.bnk_code,
#                 "bnk_type": charge_field.bnk_type,
#                 "chg_amount": charge_field.chg_amount,
#                 "chg_code": charge_field.chg_code,
#                 "status": charge_field.status,
#                 "insert_date": charge_field.insert_date,
#                 "update_date": charge_field.update_date,
#                 "rtp_code": charge_field.rtp_code,
#                 "lon_purpose": lon_list.cat_name,
#                 "chg_unit": charge_field.chg_unit,
#                 "user_sys_id": charge_field.user_sys_id,
#                 "LCIC_ID": enter_data.enterpriseNameLao,
#                 "cusType": charge_field.cusType,
#                 "user_session_id": "",
#                 "rec_reference_code": charge_field.rec_reference_code,
#                 "rec_insert_date": charge_field.rec_insert_date,
#                 "search_log": charge_field.search_log.search_ID
#             }
#             charge_report_list.append(charge_data_list)
            
                
                
            
#             # Filter by bank code if provided
#             if bank:
#                 charge_report = charge_report.filter(bnk_code=bank)

#             # Filter by year and month if provided
#             if year:
#                 charge_report = charge_report.filter(insert_date__year=year)

#                 if month:
#                     charge_report = charge_report.filter(insert_date__month=month)

#             elif month:
#                 # If month is provided without year, return an error
#                 return Response({
#                     'error': 'Year is required when filtering by month.'
#                 }, status=status.HTTP_400_BAD_REQUEST)

#             # Apply date range filter if both fromDate and toDate are provided
#             if from_date and to_date:
#                 charge_report = charge_report.filter(insert_date__range=[from_date, to_date])
#             elif from_date:
#                 charge_report = charge_report.filter(insert_date__gte=from_date)
#             elif to_date:
#                 charge_report = charge_report.filter(insert_date__lte=to_date)

#             # If no records are found, return an appropriate message
#             if not charge_report.exists():
#                 return Response({
#                     'detail': 'No charges found for the provided filters.'
#                 }, status=status.HTTP_404_NOT_FOUND)

#             # Serialize the data
#             serializer = ChargeSerializer(charge_report, many=True)
            
#             # return Response({
#             #     'charge': serializer.data
#             # }, status=status.HTTP_200_OK)
            
#             response_data = {
#                 'charge': charge_report_list
#             }
#             return Response(response_data, status=status.HTTP_200_OK)


#         except Exception as e:
#             return Response({
#                 'error': str(e)
#             }, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count
from datetime import datetime, timedelta
from .models import request_charge, memberInfo

class ChargeReportSummary(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Retrieve query parameters
            bank = request.query_params.get('bank')
            month = request.query_params.get('month')
            year = request.query_params.get('year')
            from_date = request.query_params.get('fromDate')
            to_date = request.query_params.get('toDate')

            # Start with all records
            charge_report = request_charge.objects.all()

            # Filter by bank code if provided
            if bank:
                charge_report = charge_report.filter(bnk_code=bank)

            # Filter by year/month
            if year:
                charge_report = charge_report.filter(insert_date__year=year)
                if month:
                    charge_report = charge_report.filter(insert_date__month=month)
            elif month:
                return Response({
                    'error': 'Year is required when filtering by month.'
                }, status=status.HTTP_400_BAD_REQUEST)

            # Date range filtering
            if from_date:
                from_date = datetime.strptime(from_date, '%Y-%m-%d')
            if to_date:
                to_date = datetime.strptime(to_date, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)

            if from_date and to_date:
                charge_report = charge_report.filter(insert_date__range=[from_date, to_date])
            elif from_date:
                charge_report = charge_report.filter(insert_date__gte=from_date)
            elif to_date:
                charge_report = charge_report.filter(insert_date__lte=to_date)

            # Group by bank code and aggregate
            summary_data = (
                charge_report.values('bnk_code')
                .annotate(
                    total_records=Count('rec_charge_ID'),
                    total_chg_amount=Sum('chg_amount')
                )
                .order_by('bnk_code')
            )

            # Build response with bank names
            response_data = []
            for data in summary_data:
                bank_info = memberInfo.objects.filter(bnk_code=data['bnk_code']).first()
                # Adjust these fields based on your model
                bank_code = bank_info.bnk_code if bank_info else 'Unknown'
                bank_name = getattr(bank_info, 'bnk_name', 'Unknown Bank')
                bank_nameL = getattr(bank_info, 'nameL', 'Unknown Lao Name')

                response_data.append({
                    'bnk_code': data['bnk_code'],
                    'bank_name': f"{bank_name} - {bank_nameL}",
                    'total_records': data['total_records'],
                    'total_chg_amount': data['total_chg_amount'] or 0
                })

            return Response({'summary': response_data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            
            
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count
from datetime import datetime, timedelta
from .models import request_charge, memberInfo

class ChargeReportSummary(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Retrieve query parameters
            bank = request.query_params.get('bank')
            month = request.query_params.get('month')
            year = request.query_params.get('year')
            from_date = request.query_params.get('fromDate')
            to_date = request.query_params.get('toDate')

            # Start with all records
            charge_report = request_charge.objects.all()

            # Filter by bank code if provided
            if bank:
                charge_report = charge_report.filter(bnk_code=bank)

            # Filter by year/month
            if year:
                charge_report = charge_report.filter(insert_date__year=year)
                if month:
                    charge_report = charge_report.filter(insert_date__month=month)
            elif month:
                return Response({
                    'error': 'Year is required when filtering by month.'
                }, status=status.HTTP_400_BAD_REQUEST)

            # Date range filtering
            if from_date:
                from_date = datetime.strptime(from_date, '%Y-%m-%d')
            if to_date:
                to_date = datetime.strptime(to_date, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)

            if from_date and to_date:
                charge_report = charge_report.filter(insert_date__range=[from_date, to_date])
            elif from_date:
                charge_report = charge_report.filter(insert_date__gte=from_date)
            elif to_date:
                charge_report = charge_report.filter(insert_date__lte=to_date)

            # Group by bank code and aggregate
            summary_data = (
                charge_report.values('bnk_code')
                .annotate(
                    total_records=Count('rec_charge_ID'),
                    total_chg_amount=Sum('chg_amount')
                )
                .order_by('bnk_code')
            )

            # Build response with bank names
            response_data = []
            for data in summary_data:
                bank_info = memberInfo.objects.filter(bnk_code=data['bnk_code']).first()
                # Adjust these fields based on your model
                bank_code = bank_info.bnk_code if bank_info else 'Unknown'
                bank_name = getattr(bank_info, 'bnk_name', 'Unknown Bank')
                bank_nameL = getattr(bank_info, 'nameL', 'Unknown Lao Name')

                response_data.append({
                    'bnk_code': data['bnk_code'],
                    'bank_name': f"{bank_name} - {bank_nameL}",
                    'total_records': data['total_records'],
                    'total_chg_amount': data['total_chg_amount'] or 0
                })

            return Response({'summary': response_data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


            
# from django.db.models import Count
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from django.db.models.functions import TruncMonth
# from .models import searchLog  # Assuming you are working with the searchLog model

# class SearchLogChartView(APIView):
#     def get(self, request):
#         try:
#             # Truncate rec_insert_date to month (YYYY-MM) and aggregate the count of bnk_code
#             searchlog_data = (
#                 request_charge.objects
#                 .annotate(month=TruncMonth('rec_insert_date'))  # Truncate rec_insert_date to month
#                 .values('bnk_code', 'month')  # Group by bnk_code and month
#                 .annotate(total_logs=Count('bnk_code'))  # Count total logs for each bnk_code and month
#                 .order_by('-total_logs')  # Order by total logs (descending)
#             )

#             # If no data is found, return a 404 response
#             if not searchlog_data.exists():
#                 return Response({'detail': 'No search log data available.'}, status=status.HTTP_404_NOT_FOUND)

#             # Prepare the chart data
#             chart_data = [
#                 {
#                     "bnk_code": entry['bnk_code'],
#                     entry['month'].strftime('%Y-%m'): entry['total_logs']  # Format month as YYYY-MM
#                 }
#                 for entry in searchlog_data
#             ]

#             # Return the aggregated data as a response
#             return Response({
#                 'chart_data': chart_data
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({
#                 'error': str(e)
#             }, status=status.HTTP_400_BAD_REQUEST)
            
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models.functions import TruncMonth
from .models import searchLog, memberInfo,request_charge  

class SearchLogChartView(APIView):
    def get(self, request):
        try:
            # Truncate rec_insert_date to month (YYYY-MM) and aggregate the count of bnk_code
            searchlog_data = (
                searchLog.objects
                .filter(rec_enquiry_type='1')  # Filter where rec_enquiry_type is empty
                .exclude(bnk_code='01')  # Exclude where bnk_code is '01'
                .annotate(month=TruncMonth('inquiry_date'))  # Truncate inquiry_date to month
                .values('bnk_code', 'month')  # Group by bnk_code and month
                .annotate(total_logs=Count('bnk_code'))  # Count total logs for each bnk_code and month
                .order_by('-total_logs')  # Order by total logs (descending)
            )


            # If no data is found, return a 404 response
            if not searchlog_data.exists():
                return Response({'detail': 'No search log data available.'}, status=status.HTTP_404_NOT_FOUND)

            # Prepare the chart data with bank names from MemberInfo
            chart_data = []
            for entry in searchlog_data:
                bnk_code = entry['bnk_code']

                # Fetch the bank name from MemberInfo based on bnk_code
                member_info = memberInfo.objects.filter(bnk_code=bnk_code).first()

                # If bank information exists, use the bank_name, otherwise use a default value
                bank_name = member_info.code if member_info else "Unknown Bank"

                # Append the formatted data to chart_data
                chart_data.append({
                    "bnk_code": bnk_code,
                    "bank_name": bank_name,  # Add bank name to the response
                    entry['month'].strftime('%Y-%m'): entry['total_logs']  # Format month as YYYY-MM
                })

            # Return the aggregated data as a response
            return Response({
                'chart_data': chart_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

            
# class SearchLogChart_MonthView(APIView):
#      def get(self, request, inquiry_month):
#         try:
#             # Filter search logs by the provided inquiry_month
#             searchlog_data = (
#                 searchLog.objects
#                 .filter(inquiry_month=inquiry_month)  # Filter by inquiry_month
#                 .values('bnk_code', 'inquiry_month')
#                 .annotate(total_logs=Count('bnk_code'))  # Count total logs for each bnk_code
#                 .order_by('-total_logs')
#             )

#             # If no data is found for the given month, return a 404
#             if not searchlog_data:
#                 return Response({'detail': f'No search log data available for {inquiry_month}.'}, status=status.HTTP_404_NOT_FOUND)

#             # Prepare the response data in the required format
#             chart_data = [
#                 {
#                     "bnk_code": entry['bnk_code'],
#                     entry['inquiry_month']: entry['total_logs']
#                 }
#                 for entry in searchlog_data
#             ]

#             # Return the filtered and formatted data
#             return Response({
#                 'chart_data': chart_data
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({
#                 'error': str(e)
#             }, status=status.HTTP_400_BAD_REQUEST)

class SearchLogChart_MonthView(APIView):
    def get(self, request, month_year=None):
        try:
            # If month_year is not provided, use the current month and year
            if not month_year:
                current_date = datetime.now()
                month_year = current_date.strftime("%Y-%m")
            
            # Extract year and month from month_year string
            filter_month_year = datetime.strptime(month_year, "%Y-%m")
            filter_month = filter_month_year.month
            filter_year = filter_month_year.year
            
            # Filter search logs by the provided or current month_year
            searchlog_data = (
                searchLog.objects
                .filter(inquiry_date__month=filter_month, inquiry_date__year=filter_year)  # Use inquiry_date
                .values('bnk_code')
                .annotate(total_logs=Count('bnk_code'))  # Count total logs for each bnk_code
                .order_by('-total_logs')
            )

            # If no data is found for the given month, return a 404
            if not searchlog_data:
                return Response({'detail': f'No search log data available for {month_year}.'}, status=404)

            # Prepare the response data in the required format
            chart_data = [
                {
                    "bnk_code": entry['bnk_code'],
                    month_year: entry['total_logs']
                }
                for entry in searchlog_data
            ]

            # Return the filtered and formatted data
            return Response({
                'chart_data': chart_data
            }, status=200)

        except ValueError:
            return Response({
                'error': 'Invalid month-year format. Please use YYYY-MM format.'
            }, status=400)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=400)

# PerHour AS Date Today
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.utils import timezone
# from .models import request_charge
# from django.db.models import Count
# from django.db.models.functions import ExtractHour
# from datetime import timedelta

# class ChargeCountByHourView(APIView):
#     def get(self, request):
#         # Get the start and end of the current day
#         now = timezone.now()
#         start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
#         end_of_day = start_of_day + timedelta(days=1)

#         # Initialize a dictionary with all hours set to zero
#         hour_counts = {hour: 0 for hour in range(24)}

#         # Query to count rec_charge_ID by hour for the current day
#         hourly_counts = (
#             request_charge.objects
#             .filter(insert_date__range=(start_of_day, end_of_day))
#             .annotate(hour=ExtractHour('insert_date'))  # Extract the hour from insert_date
#             .values('hour')  # Group by hour
#             .annotate(total=Count('rec_charge_ID'))  # Count rec_charge_ID
#             .order_by('hour')  # Order by hour
#         )

#         # Populate the hour_counts dictionary with actual counts
#         for hour in hourly_counts:
#             hour_counts[hour['hour']] = hour['total']

#         # Convert the hour counts to a standard response format
#         formatted_result = {str(hour): hour_counts[hour] for hour in range(24)}

#         return Response(formatted_result, status=status.HTTP_200_OK)
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.utils import timezone
# from .models import request_charge
# from django.db.models import Count
# from django.db.models.functions import ExtractHour
# from datetime import timedelta

# class ChargeCountByHourView(APIView):
#     def get(self, request):
#         # Get the start and end of the current day
#         now = timezone.now()
#         start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
#         end_of_day = start_of_day + timedelta(days=1)

#         # Initialize a dictionary with all hours set to zero
#         hour_counts = {hour: 0 for hour in range(24)}

#         # Query to count rec_charge_ID by hour for the current day
#         hourly_counts = (
#             request_charge.objects
#             .filter(insert_date__range=(start_of_day, end_of_day))
#             .annotate(hour=ExtractHour('insert_date'))  # Extract the hour from insert_date
#             .values('hour')  # Group by hour
#             .annotate(total=Count('rec_charge_ID'))  # Count rec_charge_ID
#             .order_by('hour')  # Order by hour
#         )

#         # Populate the hour_counts dictionary with actual counts
#         for hour in hourly_counts:
#             hour_counts[hour['hour']] = hour['total']

#         # Format the output to reflect the correct hours with counts in 24-hour format
#         formatted_result = {}
#         for hour in range(24):
#             formatted_result[str(hour)] = hour_counts[hour]  # Use 24-hour format directly

#         return Response(formatted_result, status=status.HTTP_200_OK)




from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import ExtractHour, ExtractDay
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
#sone updated code 13/1/2025
class ChargeCountByHourView(APIView):
    def get(self, request):
        
        now = timezone.now()  
        
        
        
        now_system_local = datetime.now()  
        

        
        now_utc = timezone.now()  
        now_local = timezone.localtime(now_utc)  
        
        
        
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = start_of_day + timedelta(days=1)

        
        start_of_week = now - timedelta(days=now.weekday())
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_week = start_of_week + timedelta(days=7)

        
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        next_month = start_of_month + timedelta(days=32)
        start_of_next_month = next_month.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        end_of_month = start_of_next_month

       
        hour_counts_day = {hour: 0 for hour in range(24)}
        day_counts_week = {day: 0 for day in range(7)}
        day_counts_month = {day: 0 for day in range(1, 32)}

       
        hourly_counts_day = (
            request_charge.objects
            .filter(insert_date__range=(start_of_day, end_of_day))
            .annotate(hour=ExtractHour('insert_date'))  
            .values('hour')  
            .annotate(total=Count('rec_charge_ID'))  
            .order_by('hour')  
        )

        
        daily_counts_week = (
            request_charge.objects
            .filter(insert_date__range=(start_of_week, end_of_week))
            .annotate(day=ExtractDay('insert_date'))  
            .values('day')  
            .annotate(total=Count('rec_charge_ID'))  
            .order_by('day')  
        )
        print("week ",daily_counts_week)

        
        daily_counts_month = (
            request_charge.objects
            .filter(insert_date__range=(start_of_month, end_of_month))
            .annotate(day=ExtractDay('insert_date'))  
            .values('day')  
            .annotate(total=Count('rec_charge_ID')) 
            .order_by('day')  
        )

        
        for hour in hourly_counts_day:
            hour_counts_day[hour['hour']] = hour['total']

        for day in daily_counts_week:
            day_counts_week[day['day'] - 1] = day['total']  
            print("day ",day['day'],day['total'])
            print("day ",day_counts_week)

        for day in daily_counts_month:
            day_counts_month[day['day']] = day['total']

       
        formatted_result_day = {}
        formatted_result_week = {}
        formatted_result_month = {}

        for hour in range(24):
            
            if hour == 0:
                formatted_hour = "12 AM"  
            elif hour < 12:
                formatted_hour = f"{hour} AM"  
            elif hour == 12:
                formatted_hour = "12 PM"  
            else:
                formatted_hour = f"{hour - 12} PM"  

            formatted_result_day[formatted_hour] = hour_counts_day[hour]

        
        days_of_week = ["ວັນເສົາ", "ວັນທິດ","ວັນຈັນ", "ວັນອັງຄານ", "ວັນພຸດ", "ວັນພະຫັດ", "ວັນສຸກ"]
        for day in range(7):
            formatted_result_week[days_of_week[day]] = day_counts_week.get(day, 0)
            

        
        for day in range(1, 32):
            formatted_result_month[f"ວັນທີ {day}"] = day_counts_month.get(day, 0)

        return Response({
            'day': formatted_result_day,
            'week': formatted_result_week,
            'month': formatted_result_month
        }, status=status.HTTP_200_OK)
# class ChargeCountByHourView(APIView):
#     def get(self, request):
        
#         # Use Django's timezone aware current time
#         now = timezone.now()  # Default DJANGO time
#         print(f"Django Timezone now: {now}")
        
#         # System local time using datetime.now()
#         now_system_local = datetime.now()  # Local Default
#         print(f"System Local Time (datetime.now()): {now_system_local}")

#         # Localized time (converted from UTC)
#         now_utc = timezone.now()  # UTC time in Django
#         now_local = timezone.localtime(now_utc)  # Convert to local time
#         print(f"Local Time (Converted to Django TIME_ZONE): {now_local}")
        
#         # Define start and end of the current day in the local timezone
#         start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
#         end_of_day = start_of_day + timedelta(days=1)

#         # Initialize a dictionary with all hours set to zero
#         hour_counts = {hour: 0 for hour in range(24)}

#         # Query to count `rec_charge_ID` by hour for the current day
#         hourly_counts = (
#             request_charge.objects
#             .filter(insert_date__range=(start_of_day, end_of_day))
#             .annotate(hour=ExtractHour('insert_date'))  # Extract the hour from insert_date
#             .values('hour')  # Group by hour
#             .annotate(total=Count('rec_charge_ID'))  # Count rec_charge_ID
#             .order_by('hour')  # Order by hour
#         )

#         # Populate the hour_counts dictionary with actual counts
#         for hour in hourly_counts:
#             hour_counts[hour['hour']] = hour['total']

#         # Format the output to reflect the correct hours with counts in 12-hour format
#         formatted_result = {}
#         for hour in range(24):
#             # Convert hour to 12-hour format with AM/PM
#             if hour == 0:
#                 formatted_hour = "12 AM"  # Midnight
#             elif hour < 12:
#                 formatted_hour = f"{hour} AM"  # Morning hours
#             elif hour == 12:
#                 formatted_hour = "12 PM"  # Noon
#             else:
#                 formatted_hour = f"{hour - 12} PM"  # Afternoon/Evening hours

#             formatted_result[formatted_hour] = hour_counts[hour]

#         return Response(formatted_result, status=status.HTTP_200_OK)



class SearchLogChartByDateView(APIView):
    def get(self, request, inquiry_date):
        try:
            # Convert the date string to a datetime object for comparison
            filter_date = datetime.strptime(inquiry_date, "%d-%m-%Y").date()

            # Filter the search logs by the given inquiry date
            searchlog_data = (
                searchLog.objects
                .filter(inquiry_date__date=filter_date)  # Filter by date
                .values('bnk_code')
                .annotate(total_logs=Count('bnk_code'))
                .order_by('-total_logs')
            )

            # If no data is found, return a 404
            if not searchlog_data.exists():
                return Response({'detail': f'No search log data available for {inquiry_date}.'}, status=status.HTTP_404_NOT_FOUND)

            # Prepare data for the chart
            chart_data = [
                {
                    'bnk_code': entry['bnk_code'],
                    inquiry_date: entry['total_logs'],
                }
                for entry in searchlog_data
            ]

            # Return the data formatted for the chart
            return Response({'chart_data': chart_data}, status=status.HTTP_200_OK)

        except ValueError:
            # Return a 400 error if the date format is invalid
            return Response({
                'error': 'Invalid date format. Please use DD-MM-YYYY format.'
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
            
from django.db.models import Count
from django.db.models.functions import TruncHour
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from .models import searchLog  # Adjust if needed

class SearchLogChargePerDayView(APIView):
    def get(self, request):
        try:
            # Get the current date in UTC
            current_datetime = timezone.now()
            current_day = current_datetime.date()

            # Print the current day for debugging
            print(f"Current Day: {current_day}")
            print(f"Current DateTime: {current_datetime}")
            
             # Count all logs for today (current date)
            total_logs_today = searchLog.objects.filter(inquiry_time__date=current_day).count()
            
            print(total_logs_today)
            
            # Filter logs for the current day (assuming timestamps are stored in UTC)
            hourly_data = (
                searchLog.objects
                .filter(inquiry_time__date=current_day)  # Filter by today's date using inquiry_time (in UTC)
                .annotate(hour=TruncHour('inquiry_time'))  # Group by the hour (in UTC)
                .values('hour')  # Extract the hour
                .annotate(total_logs=Count('search_ID'))  # Count the logs for each hour
                .order_by('hour')  # Order by hour
            )

            # Debugging: Print the query for debugging purposes
            print(f"Hourly Data Query: {hourly_data.query}")
            print(f"Hourly Data Result: {list(hourly_data)}")

            # Create a list for 24 hours initialized with 0 logs
            chart_data = [{'hour': i, 'total_logs': 0} for i in range(24)]

            # Populate the data with actual logs for each hour
            for entry in hourly_data:
                if entry['hour'] is not None:  # Make sure there is valid data
                    hour = entry['hour'].hour  # Extract the hour (0-23)
                    chart_data[hour]['total_logs'] = entry['total_logs']  # Assign log count

            # Return the data with today's date
            return Response({
                'date': current_day.strftime('%Y-%m-%d'),  # Return the current date in YYYY-MM-DD format
                'total_logs_today': total_logs_today,  # Total count of logs for today
                'chart_data': chart_data  # List containing 24 entries (one for each hour)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)




            
class SearchLogChartByBankCodeView(APIView):
    def get(self, request, bnk_code):
        try:
            
            searchlog_data = (
                searchLog.objects
                .filter(bnk_code=bnk_code) 
                
                .values('bnk_code', 'inquiry_month')
                .annotate(total_logs=Count('bnk_code'))  
                .order_by('-total_logs')
            ) 
            
            if not searchlog_data:
                return Response({'detail': f'No search log data available for bank code {bnk_code}.'}, status=status.HTTP_404_NOT_FOUND)

            chart_data = [
                {
                    "inquiry_month": entry['inquiry_month'],
                    entry['inquiry_month']: entry['total_logs']
                }
                for entry in searchlog_data
            ]

            return Response({
                'chart_data': chart_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
class ChargeChartView(APIView):
    
    def get(self, request, bnk_code=None):
        try:
            # Filter the charge records by bnk_code if provided
            if bnk_code:
                charge_report = request_charge.objects.filter(bnk_code=bnk_code)
            else:
                charge_report = request_charge.objects.all()

            # If no records are found, return an appropriate message
            if not charge_report.exists():
                return Response({
                    'detail': 'No charges found for the provided bnk_code.'
                }, status=status.HTTP_404_NOT_FOUND)

            # Prepare the data by extracting month and year
            monthly_charges = charge_report.annotate(
                month=ExtractMonth('rec_insert_date'),  # Extract month from date
                year=ExtractYear('rec_insert_date')     # Extract year from date
            ).values('bnk_code', 'month', 'year').annotate(
                total_amount=Sum('chg_amount')
            ).order_by('bnk_code', 'year', 'month')

            # Structure the data for the table
            result = {}
            for entry in monthly_charges:
                bnk_code = entry['bnk_code']
                month_year = f"{entry['month']:02d}-{entry['year']}"  # Format as MM-YYYY
                total_amount = entry['total_amount']

                if bnk_code not in result:
                    result[bnk_code] = {}
                
                result[bnk_code][month_year] = total_amount

            # Convert the result dict to a list for easier consumption in the frontend
            chart_data = [
                {'bnk_code': bnk, **amounts}
                for bnk, amounts in result.items()
            ]

            return Response({
                'chart_data': chart_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
            
class ChargeChartByDateView(APIView):

    def get(self, request, charge_date):
        try:
            # Parse the charge_date string into a datetime object
            filter_date = datetime.strptime(charge_date, "%d-%m-%Y").date()

            # Filter the charge records by the exact date
            charge_report = request_charge.objects.filter(rec_insert_date__date=filter_date)

            # If no records are found, return a 404
            if not charge_report.exists():
                return Response({
                    'detail': f'No charges found for the provided date: {charge_date}.'
                }, status=status.HTTP_404_NOT_FOUND)

            # Prepare the data by extracting month and year and summing the charge amounts
            monthly_charges = charge_report.annotate(
                month=ExtractMonth('rec_insert_date'),  # Extract month
                year=ExtractYear('rec_insert_date')     # Extract year
            ).values('bnk_code', 'month', 'year').annotate(
                total_amount=Sum('chg_amount')
            ).order_by('bnk_code', 'year', 'month')

            # Structure the data
            result = {}
            for entry in monthly_charges:
                bnk_code = entry['bnk_code']
                month_year = f"{entry['month']:02d}-{entry['year']}"  # Format as MM-YYYY
                total_amount = entry['total_amount']

                if bnk_code not in result:
                    result[bnk_code] = {}
                
                result[bnk_code][month_year] = total_amount

            # Convert the result dict to a list for easier consumption in the frontend
            chart_data = [
                {'bnk_code': bnk, **amounts}
                for bnk, amounts in result.items()
            ]

            return Response({
                'chart_data': chart_data
            }, status=status.HTTP_200_OK)

        except ValueError:
            return Response({
                'error': 'Invalid date format. Please use DD-MM-YYYY format.'
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
            
class ChargeChartMonthView(APIView):

    def get(self, request, month_year=None):  # Make 'month_year' optional with default None
        try:
            # If month_year is not provided, default to the current month and year
            if not month_year:
                now = timezone.now()
                filter_month = now.month
                filter_year = now.year
                month_year = now.strftime("%m-%Y")  # Format the current month and year as 'MM-YYYY'
            else:
                # Parse the month_year string (e.g., '10-2024') into month and year
                filter_month_year = datetime.strptime(month_year, "%m-%Y")
                filter_month = filter_month_year.month
                filter_year = filter_month_year.year
            
            # print("date-now",month_year)
            charge_report = request_charge.objects.filter(
                rec_insert_date__month=filter_month,
                rec_insert_date__year=filter_year
            )

            # If no records are found, return a 404
            if not charge_report.exists():
                return Response({
                    'detail': f'No charges found for the provided month and year: {month_year}.'
                }, status=status.HTTP_404_NOT_FOUND)

            # Aggregate the charge data by bank code and sum the charge amounts
            monthly_charges = charge_report.values('bnk_code').annotate(
                total_amount=Sum('chg_amount')
            ).order_by('bnk_code')

            # Structure the data for the frontend
            chart_data = [
                {
                    'bnk_code': entry['bnk_code'],
                    month_year: entry['total_amount']
                }
                for entry in monthly_charges
            ]

            return Response({
                'chart_data': chart_data
            }, status=status.HTTP_200_OK)

        except ValueError:
            return Response({
                'error': 'Invalid month-year format. Please use MM-YYYY format.'
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
            
class ChargeChartByBankView(APIView):

    def get(self, request, bnk_code):
        try:
            # Filter the charge records by the provided bnk_code
            charge_report = request_charge.objects.filter(bnk_code=bnk_code)

            # If no records are found, return a 404
            if not charge_report.exists():
                return Response({
                    'detail': f'No charges found for bank code: {bnk_code}.'
                }, status=status.HTTP_404_NOT_FOUND)

            # Aggregate the charge data by month and year, and sum the charge amounts
            monthly_charges = charge_report.annotate(
                month=ExtractMonth('rec_insert_date'),  # Extract month from date
                year=ExtractYear('rec_insert_date')     # Extract year from date
            ).values('month', 'year').annotate(
                total_amount=Sum('chg_amount')
            ).order_by('year', 'month')

            # Structure the data for the frontend
            chart_data = [
                {
                    'bnk_code': bnk_code,
                    f"{entry['month']:02d}-{entry['year']}": entry['total_amount']
                }
                for entry in monthly_charges
            ]

            return Response({
                'chart_data': chart_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
            
            
from .models import Main_catalog_cat  # Assuming this is your model
from .serializers import MainCatalogCatSerializer  # Serializer for your model

class CatalogCatListView(APIView):
    def get(self, request):
        cats = Main_catalog_cat.objects.all()
        serializer = MainCatalogCatSerializer(cats, many=True)
        return Response(serializer.data)



from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Q,F 
class TotalSearchLogByBankTypeView(APIView):
    def get(self, request):
        try:
            # Get all bank codes for banks and MFIs
            bank_data = memberInfo.objects.filter(bnk_type__in=['1', '2']).values('bnk_code', 'bnk_type')

            # Prepare a list to hold the final results
            result = []


            for bank in bank_data:
                # Count search logs for each bank code
                total_search_logs = searchLog.objects.filter(bnk_code=bank['bnk_code']).count()
                
                institution_type = "Bank" if bank['bnk_type'] == 1 else "MFI"

                result.append({
                    'Bank_Code': bank['bnk_code'],
                    'Institution_Type': institution_type,
                    'Total_Search_Logs': total_search_logs
                })

            # Return the filtered and formatted data
            return Response({'data': result}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=400)

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Sum, Q, F

class SumTotalByBankType(APIView):
    def get(self, request):
        try:
            # Get the bank types and their corresponding bank codes
            bank_data = memberInfo.objects.filter(bnk_type__in=['1', '2']).values('bnk_code', 'bnk_type')

            # Prepare a dictionary to hold the results grouped by bank type
            result = {
                'Bank': 0,
                'MFI': 0,
                'Total': 0
            }

            # Count search logs for each bank code
            for bank in bank_data:
                total_search_logs = searchLog.objects.filter(bnk_code=bank['bnk_code']).count()
                
                # Check the bank type and accumulate totals
                if bank['bnk_type'] == 1:
                    result['Bank'] += total_search_logs
                elif bank['bnk_type'] == 2:
                    result['MFI'] += total_search_logs
                    
                result['Total'] = result['Bank'] + result['MFI']
            # Return the aggregated data
            return Response({'data': result}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=400)

    
class MemberCountView(APIView):
    def get(self, request):
        try:
            # Count the number of members for each memberType_id
            member_count = memberInfo.objects.values('memberType_id').annotate(count=Count('id')).filter(memberType_id__in=[1, 2, 3, 4, 5, 6, 7])

            # Calculate the total number of members across all memberType_id
            total_count = memberInfo.objects.filter(memberType_id__in=[1, 2, 3, 4, 5, 6, 7]).count()

            # Add the total count to the response
            result = {
                'member_count': list(member_count),  # Convert QuerySet to a list for the response
                'total_count': total_count  # Total number of members across all types
            }

            return Response(result, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BankTypeCountView(APIView):
    def get(self, request):
        try:
            # Count the number of members for each memberType_id
            member_count = memberInfo.objects.values('bnk_type').annotate(count=Count('id')).filter(memberType_id__in=[1, 2])
            
            return Response(member_count, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class SumTotalByBankTypeMonth(APIView):
    def get(self, request):
        try:
            # Get the bank types and their corresponding bank codes
            bank_data = memberInfo.objects.filter(bnk_type__in=['1', '2']).values('bnk_code', 'bnk_type')

            # Prepare a dictionary to hold the results grouped by month and bank type
            result = {}

            # Iterate through each bank and group search logs by inquiry_month and bank type
            for bank in bank_data:
                # Group by inquiry_month and count logs for each bank
                search_logs_by_month = (
                    searchLog.objects.filter(bnk_code=bank['bnk_code'])
                    .values('inquiry_month')  # Use the 'inquiry_month' field to group by month
                    .annotate(total=Count('search_ID'))  # Count the logs for each month
                    .order_by('inquiry_month')
                )

                # Add the logs to the result dictionary by month and bank type
                for log in search_logs_by_month:
                    month = log['inquiry_month']  # Already in 'yyyy-mm' format
                    if month not in result:
                        result[month] = {'Bank': 0, 'MFI': 0}

                    if bank['bnk_type'] == 1:  # Bank
                        result[month]['Bank'] += log['total']
                    elif bank['bnk_type'] == 2:  # MFI
                        result[month]['MFI'] += log['total']

            # Add total sums for each month
            for month_data in result.values():
                month_data['Total'] = month_data['Bank'] + month_data['MFI']

            # Return the aggregated data
            return Response({'data': result}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=400)

class SumTotalByBankTypeYear(APIView):
    def get(self, request):
        try:
            # Get the bank types and their corresponding bank codes
            bank_data = memberInfo.objects.filter(bnk_type__in=['1', '2']).values('bnk_code', 'bnk_type')

            # Prepare dictionaries to hold the results grouped by month and year
            result_monthly = {}
            result_yearly = {}

            # Iterate through each bank and group search logs by inquiry_month and bank type
            for bank in bank_data:
                # Group by inquiry_month and count logs for each bank
                search_logs_by_month = (
                    searchLog.objects.filter(bnk_code=bank['bnk_code'])
                    .values('inquiry_month')  # Use the 'inquiry_month' field to group by month
                    .annotate(total=Count('search_ID'))  # Count the logs for each month
                    .order_by('inquiry_month')
                )

                # Add the logs to the result dictionary by month and year
                for log in search_logs_by_month:
                    month = log['inquiry_month']  # Already in 'yyyy-mm' format
                    year = month.split('-')[0]  # Extract the year from 'yyyy-mm'

                    # Monthly results
                    # if month not in result_monthly:
                    #     result_monthly[month] = {'Bank': 0, 'MFI': 0}

                    # if bank['bnk_type'] == 1:  # Bank
                    #     result_monthly[month]['Bank'] += log['total']
                    # elif bank['bnk_type'] == 2:  # MFI
                    #     result_monthly[month]['MFI'] += log['total']

                    # Yearly results
                    if year not in result_yearly:
                        result_yearly[year] = {'Bank': 0, 'MFI': 0}

                    if bank['bnk_type'] == 1:  
                        result_yearly[year]['Bank'] += log['total']
                    elif bank['bnk_type'] == 2:  
                        result_yearly[year]['MFI'] += log['total']

            # Add total sums for each month and year
            for month_data in result_monthly.values():
                month_data['Total'] = month_data['Bank'] + month_data['MFI']

            for year_data in result_yearly.values():
                year_data['Total'] = year_data['Bank'] + year_data['MFI']

            # Return the aggregated data
            return Response({'monthly_data': result_monthly, 'yearly_data': result_yearly}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=400)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Sum

# class SumTotalChgAmountByBankType(APIView):
#     def get(self, request):
#         try:
#             # Aggregate the sum of chg_amount for banks and MFIs by joining on bnk_code
#             total_chg_amount = (
#                 request_charge.objects.filter(bnk_code__isnull=False)  # Ensure that there is a valid bnk_code
#                 .values('bnk_code')  # Group by bnk_code
#                 .annotate(total_chg_amount=Sum('chg_amount'))  # Sum chg_amount
#                 .values('bnk_code', 'total_chg_amount')  # Select bnk_code and the calculated sum
#             )

#             # Initialize sum variables for Bank and MFI
#             bank_total_chg_amount = 0
#             mfi_total_chg_amount = 0
#             overall_total_chg_amount = 0

#             # Get all banks and MFIs from memberInfo with their bnk_type
#             bank_data = memberInfo.objects.filter(bnk_type__in=['1', '2']).values('bnk_code', 'bnk_type')

#             # Create a dictionary for easy lookup of bnk_type by bnk_code
#             bank_type_lookup = {bank['bnk_code']: bank['bnk_type'] for bank in bank_data}

#             # Iterate through the aggregated total_chg_amount and sum based on the bank type
#             for charge in total_chg_amount:
#                 bnk_code = charge['bnk_code']
#                 total_chg_amount = charge['total_chg_amount']

#                 # Determine the bank type using the lookup dictionary
#                 if bnk_code in bank_type_lookup:
#                     if bank_type_lookup[bnk_code] == 1:
#                         bank_total_chg_amount += total_chg_amount
#                     elif bank_type_lookup[bnk_code] == 2:
#                         mfi_total_chg_amount += total_chg_amount
#                 overall_total_chg_amount = bank_total_chg_amount + mfi_total_chg_amount 
#             # Prepare the response
#             result = {
#                 'Bank_TotalChgAmount': bank_total_chg_amount,
#                 'MFI_TotalChgAmount': mfi_total_chg_amount,
#                 'Overall_TotalChgAmount': overall_total_chg_amount  # Bank + MFI
#             }

#             return Response({'data': result}, status=200)

#         except Exception as e:
#             return Response({'error': str(e)}, status=400)

from datetime import datetime
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import request_charge, memberInfo

class SumTotalChgAmountByBankType(APIView):
    def get(self, request, month_year=None):
        try:
            # If no month_year is provided, default to the current month and year
            if not month_year:
                current_date = datetime.now()
                month_year = current_date.strftime("%Y-%m")
            
            # Parse month_year to extract the month and year
            try:
                filter_month_year = datetime.strptime(month_year, "%Y-%m")
                filter_month = filter_month_year.month
                filter_year = filter_month_year.year
            except ValueError:
                return Response({'error': 'Invalid month-year format. Please use YYYY-MM format.'}, status=400)

            # Filter charges by the extracted month and year
            total_chg_amount = (
                request_charge.objects.filter(
                    bnk_code__isnull=False,  # Ensure that there is a valid bnk_code
                    rec_insert_date__year=filter_year,  # Filter by year
                    rec_insert_date__month=filter_month  # Filter by month
                )
                .values('bnk_code')  # Group by bnk_code
                .annotate(total_chg_amount=Sum('chg_amount'))  # Sum chg_amount
                .values('bnk_code', 'total_chg_amount')  # Select bnk_code and the calculated sum
            )

            # Initialize sum variables for Bank and MFI
            bank_total_chg_amount = 0
            mfi_total_chg_amount = 0
            overall_total_chg_amount = 0

            # Get all banks and MFIs from memberInfo with their bnk_type
            bank_data = memberInfo.objects.filter(bnk_type__in=['1', '2']).values('bnk_code', 'bnk_type')

            # Create a dictionary for easy lookup of bnk_type by bnk_code
            bank_type_lookup = {bank['bnk_code']: bank['bnk_type'] for bank in bank_data}

            # Iterate through the aggregated total_chg_amount and sum based on the bank type
            for charge in total_chg_amount:
                bnk_code = charge['bnk_code']
                total_chg_amount = charge['total_chg_amount']

                # Determine the bank type using the lookup dictionary
                if bnk_code in bank_type_lookup:
                    if bank_type_lookup[bnk_code] == 1:  # Bank type 1
                        bank_total_chg_amount += total_chg_amount
                    elif bank_type_lookup[bnk_code] == 2:  # Bank type 2 (MFI)
                        mfi_total_chg_amount += total_chg_amount

            # Calculate overall total
            overall_total_chg_amount = bank_total_chg_amount + mfi_total_chg_amount 

            # Prepare the response
            result = {
                'Bank_TotalChgAmount': bank_total_chg_amount,
                'MFI_TotalChgAmount': mfi_total_chg_amount,
                'Overall_TotalChgAmount': overall_total_chg_amount  # Bank + MFI
            }

            return Response({'data': result}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SumTotalByBankTypeEveryMonth(APIView):
    def get(self, request):
        try:
            # Get the current year
            current_year = datetime.now().year

            # Initialize a result dictionary to store the total charge amounts grouped by month and bank type
            result = {}

            # Get all banks and MFIs from memberInfo with their bnk_type
            bank_data = memberInfo.objects.filter(bnk_type__in=['1', '2']).values('bnk_code', 'bnk_type')

            # Create a dictionary for easy lookup of bnk_type by bnk_code
            bank_type_lookup = {bank['bnk_code']: bank['bnk_type'] for bank in bank_data}

            # Iterate through each month (from 1 to 12)
            for month in range(1, 13):
                # Filter charges for the current month and year
                monthly_charges = (
                    request_charge.objects.filter(
                        rec_insert_date__year=current_year, 
                        rec_insert_date__month=month
                    )
                    .values('bnk_code')
                    .annotate(total_chg_amount=Sum('chg_amount'))  # Sum the charge amount for each bnk_code
                )

                # Initialize totals for the current month
                bank_total_chg_amount = 0
                mfi_total_chg_amount = 0

                # Iterate through the monthly charges and sum based on the bank type
                for charge in monthly_charges:
                    bnk_code = charge['bnk_code']
                    total_chg_amount = charge['total_chg_amount']

                    # Determine the bank type using the lookup dictionary
                    if bnk_code in bank_type_lookup:
                        if bank_type_lookup[bnk_code] == 1:  # Bank
                            bank_total_chg_amount += total_chg_amount
                        elif bank_type_lookup[bnk_code] == 2:  # MFI
                            mfi_total_chg_amount += total_chg_amount

                # Store the totals in the result dictionary for the current month
                month_key = f"{current_year}-{str(month).zfill(2)}"  # Format month as 'YYYY-MM'
                result[month_key] = {
                    'Bank_TotalChgAmount': bank_total_chg_amount,
                    'MFI_TotalChgAmount': mfi_total_chg_amount,
                    'Overall_TotalChgAmount': bank_total_chg_amount + mfi_total_chg_amount
                }

            # Return the aggregated data by month
            return Response({'data': result}, status=200)

        except Exception as e:
            return Response({'error': str(e)}, status=400)


from .serializers import ProvinceSerializer, DistrictSerializer, VillageSerializer

class LocationView(APIView):
    def get(self, request):
        provinces = Province.objects.all()
        districts = District.objects.all()
        villages = Village.objects.all()

        # Serialize the data
        province_serializer = ProvinceSerializer(provinces, many=True)
        district_serializer = DistrictSerializer(districts, many=True)
        village_serializer = VillageSerializer(villages, many=True)

        # Prepare the response data
        data = {
            'provinces': province_serializer.data,
            'districts': district_serializer.data,
            'villages': village_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)
    
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Village
# from django.db.models import Q

# def filter_villages(request):

#     village_name = request.GET.get('village_name', '')  
#     province_id = request.GET.get('province_id', None)   
#     district_id = request.GET.get('district_id', None)   


#     query = Village.objects.filter(Village_Name__icontains=village_name)


#     if province_id:
#         query = query.filter(Prov_ID=province_id)


#     if district_id:
#         query = query.filter(Dstr_ID=district_id)


#     village_data = list(query.values('ID', 'Prov_ID', 'Dstr_ID', 'Vill_ID', 'Village_Name'))

#     return JsonResponse(village_data, safe=False)

from django.shortcuts import render
from django.http import JsonResponse
from .models import Village, Province, District
from django.db.models import Q

def filter_villages(request):
    """
    Simple but fast village filter - ແກ້ບັນຫາ performance ໂດຍບໍ່ໃຊ້ raw SQL
    """
    village_name = request.GET.get('village_name', '')  
    province_id = request.GET.get('province_id', None)  
    district_id = request.GET.get('district_id', None)  

    # ໃຊ້ values() ເພື່ອດືງແຕ່ຂໍ້ມູນທີ່ຕ້ອງການ - ໄວກວ່າການສ້າງ objects
    # ໃຊ້ pk ເພື່ອໃຫ້ Django auto ເລືອກ primary key
    query = Village.objects.values(
        'pk', 'Prov_ID', 'Dstr_ID', 'Vill_ID', 'Village_Name'
    )
    
    # ເພີ່ມ filters
    if village_name:
        query = query.filter(Village_Name__icontains=village_name)
    if province_id:
        query = query.filter(Prov_ID=province_id)
    if district_id:
        query = query.filter(Dstr_ID=district_id)

    # ດຶງຂໍ້ມູນ villages ກ່ອນ
    villages = list(query)
    
    if not villages:
        return JsonResponse([], safe=False)
    
    # ເກັບ province_ids ແລະ district_ids ທີ່ບໍ່ຊ້ໍາກັນ
    prov_ids = set(v['Prov_ID'] for v in villages)
    dstr_keys = set((v['Dstr_ID'], v['Prov_ID']) for v in villages)
    
    # ດຶງ provinces ທັງໝົດໃນຄັ້ງດຽວ (bulk query)
    provinces = {
        p['Prov_ID']: p['Province_Name'] 
        for p in Province.objects.filter(
            Prov_ID__in=prov_ids
        ).values('Prov_ID', 'Province_Name')
    }
    
    # ດຶງ districts ທັງໝົດໃນຄັ້ງດຽວ (bulk query)
    district_filters = Q()
    for dstr_id, prov_id in dstr_keys:
        district_filters |= (Q(Dstr_ID=dstr_id) & Q(Prov_ID=prov_id))
    
    districts = {}
    if district_filters:
        districts = {
            (d['Dstr_ID'], d['Prov_ID']): d['District_Name'] 
            for d in District.objects.filter(
                district_filters
            ).values('Dstr_ID', 'Prov_ID', 'District_Name')
        }
    
    # ລວມຂໍ້ມູນ
    village_data = []
    for village in villages:
        village_data.append({
            'ID': village['pk'],  # ໃຊ້ pk ແທນ ID
            'Prov_ID': village['Prov_ID'],
            'Province_Name': provinces.get(village['Prov_ID']),
            'Dstr_ID': village['Dstr_ID'], 
            'District_Name': districts.get((village['Dstr_ID'], village['Prov_ID'])),
            'Vill_ID': village['Vill_ID'],
            'Village_Name': village['Village_Name']
        })
    
    return JsonResponse(village_data, safe=False)


# ຖ້າທ່ານຢາກໃຊ້ caching ເພີ່ມເຕີມ
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # Cache 5 minutes
def filter_villages_cached(request):
    """
    Version ມີ caching - ໃຊ້ເມື່ອຂໍ້ມູນບໍ່ຄ່ອຍປ່ຽນ
    """
    return filter_villages(request)


from .models import ReportCatalog
from .serializers import ReportCatalogSerializer
# class ReportCatalogView(APIView):
    
#     def get(self, request):
#         report_catalogs = ReportCatalog.objects.all()  # Retrieve all entries
#         serializer = ReportCatalogSerializer(report_catalogs, many=True)  # Serialize the data
#         return Response(serializer.data, status=status.HTTP_200_OK)

class ReportCatalogView(APIView):
    def get(self, request):

        report_catalogs = ReportCatalog.objects.all()  
        serializer = ReportCatalogSerializer(report_catalogs, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = ReportCatalogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    def put(self, request, pk):

        try:
            report_catalog = ReportCatalog.objects.get(pk=pk)
        except ReportCatalog.DoesNotExist:
            return Response({"error": "ReportCatalog not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReportCatalogSerializer(report_catalog, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# from django.utils import timezone
# from django.db.models import Count
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class SumTotalSearchByBankTypeByDate(APIView):
#     def get(self, request):
#         try:
#             # Get today's date (without time)
#             today = timezone.now().date()

#             # Prepare a dictionary to hold the results separated by bank type
#             result = {
#                 'Bank': 0,  
#                 'MFI': 0,
#                 'Total': 0
#             }

#             # Get search logs for today and separate them by bnk_type
#             search_logs_today = searchLog.objects.filter(inquiry_date__date=today)
            
#             print("saerch_log :", search_logs_today)
            
#             # Annotate and count the logs by bnk_type
#             search_logs_by_type = search_logs_today.values('bnk_code').annotate(total=Count('search_ID')).order_by('bnk_code')

#             # Iterate through each log and accumulate the counts based on bank type
#             for log in search_logs_by_type:
#                 bnk_code = log['bnk_code']
#                 bank_type = memberInfo.objects.filter(bnk_code=bnk_code).values('bnk_type').first()

#                 if bank_type:
#                     if bank_type['bnk_type'] == 1: 
#                         result['Bank'] += log['total']
#                     elif bank_type['bnk_type'] == 2:
#                         result['MFI'] += log['total']

#             # Calculate total searches for today
#             result['Total'] = result['Bank'] + result['MFI']

#             # Return the results
#             return Response({'data': result}, status=200)

#         except Exception as e:
#             return Response({'error': str(e)}, status=400)





from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import EnterpriseInfo, Search_batfile, SearchResult

# @csrf_exempt
# def upload_json(request):
#     if request.method == 'POST':
#         file = request.FILES.get('file')
#         user_id = request.POST.get('user_id')
#         UID = request.POST.get('UID')
        
#         print('user_id', user_id)
#         if not file:
#             return JsonResponse({"error": "No file provided"}, status=400)

#         search_batfile = Search_batfile(
#             fileName=file.name,
#             fileUpload=file,
#             fileSize=f"{file.size} bytes",
#             path=f"searchfile/{file.name}",
#             status="Uploaded",
#             FileType="json",
#             user_id=user_id,
#             UID=UID
#         )
#         search_batfile.save()

#         try:
#             file.seek(0)
#             data = json.load(file)
#             print(data)
#         except json.JSONDecodeError as e:
#             return JsonResponse({"error": f"Invalid JSON file: {str(e)}"}, status=400)

#         results = []
#         found_count = 0  
#         not_found_count = 0 

#         for record in data:
#             lcic_id = record.get('lcicID') or "" 
#             com_code = record.get('com_enterprise_code') or "" 
            
#             enterprise = None
#             search_criteria = "" 

#             if lcic_id and com_code:
#                 enterprise = EnterpriseInfo.objects.filter(
#                     LCICID=lcic_id, 
#                     EnterpriseID=com_code
#                 ).first()
#                 search_criteria = "both"
#             elif lcic_id:
#                 enterprise = EnterpriseInfo.objects.filter(
#                     LCICID=lcic_id
#                 ).first()
#                 search_criteria = "lcic_only"
#             elif com_code:
#                 enterprise = EnterpriseInfo.objects.filter(
#                     EnterpriseID=com_code
#                 ).first()
#                 search_criteria = "com_code_only"
            
#             result_data = {
#                 "lcicID": lcic_id,  
#                 "com_enterprise_code": com_code, 
#                 "search_criteria": search_criteria,  
#                 "status": "Found" if enterprise else "Not Found",
#                 "enterpriseNameLao": enterprise.enterpriseNameLao if enterprise else None,
#                 "investmentCurrency": enterprise.investmentCurrency if enterprise else None
#             }
            
#             if result_data["status"] == "Found":
#                 found_count += 1
#             else:
#                 not_found_count += 1
            
#             search_result = SearchResult.objects.create(
#                 bank_code=user_id,
#                 UID=UID,
#                 search_batch=search_batfile,
#                 lcicID=lcic_id,
#                 com_enterprise_code=com_code,
#                 status=result_data["status"],
#                 enterpriseNameLao=result_data["enterpriseNameLao"],
#                 investmentCurrency=result_data["investmentCurrency"]
#             )
           
#             results.append({
#                 "id": search_result.id,
#                 "lcicID": search_result.lcicID,
#                 "com_enterprise_code": search_result.com_enterprise_code,
#                 "status": search_result.status,
#                 "enterpriseNameLao": search_result.enterpriseNameLao,
#                 "investmentCurrency": search_result.investmentCurrency,
#                 "created_at": search_result.created_at,
#                 "bank_code": search_result.bank_code,
#                 "UID": search_result.UID
#             })

#         search_batfile.searchtrue = found_count
#         search_batfile.searchfals = not_found_count
#         search_batfile.save()


#         return JsonResponse({"results": results, "search_batfile_id": search_batfile.id}, status=200)

#     return JsonResponse({"error": "Invalid request method"}, status=405)
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Search_batfile, SearchResult, EnterpriseInfo
import json
from collections import Counter
from datetime import date
import os

@csrf_exempt
@csrf_exempt
def upload_json(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        user_id = request.POST.get('user_id')
        UID = request.POST.get('UID')
        token = request.POST.get('token')  
        
        if not file:
            return JsonResponse({"error": "No file provided"}, status=400)

        
        def generate_filename(original_filename):
            
            name_without_ext = os.path.splitext(original_filename)[0]
            extension = os.path.splitext(original_filename)[1]
            
            
            today = date.today().strftime("%Y%m%d")
            
            # ຄົ້ນຫາໄຟລ໌ທີ່ມີຊື່ຄ້າຍກັນໃນມື້ນີ້
            today_files = Search_batfile.objects.filter(
                fileName__startswith=f"{name_without_ext}-{today}-",
                insertDate__date=date.today()
            ).count()
            
            # ກຳນົດລຳດັບໃຫມ່
            sequence = today_files + 1
            sequence_str = f"{sequence:03d}"  # ແປງເປັນ 3 ໂຕເລກ 001, 002, 003...
            
            # ສ້າງຊື່ໄຟລ໌ໃຫມ່
            new_filename = f"{name_without_ext}-{today}-{sequence_str}{extension}"
            return new_filename

        # ສ້າງຊື່ໄຟລ໌ໃຫມ່
        new_filename = generate_filename(file.name)

        search_batfile = Search_batfile(
            fileName=new_filename,  # ໃຊ້ຊື່ໄຟລ໌ໃຫມ່
            fileUpload=file,
            fileSize=f"{file.size} bytes",
            path=f"searchfile/{new_filename}",  # path ກໍໃຊ້ຊື່ໃຫມ່ເຊັ່ນກັນ
            status="Uploaded",
            FileType="json",
            user_id=user_id,
            UID=UID
        )
        search_batfile.save()

        try:
            file.seek(0)
            data = json.load(file)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": f"Invalid JSON file: {str(e)}"}, status=400)

        unique_records = set()
        results = []
        found_count = 0  
        not_found_count = 0 

        record_counter = Counter()

        for record in data:
            lcic_id = record.get('LCIC_code') or "" 
            com_code = record.get('com_enterprise_code') or "" 
            
            unique_key = (lcic_id, com_code)
            record_counter[unique_key] += 1

            if unique_key in unique_records:
                continue
            
            unique_records.add(unique_key)

            enterprise = None
            search_criteria = ""
            final_lcic_id = lcic_id  # ເກັບຄ່າສຸດທ້າຍທີ່ຈະບັນທຶກ
            final_com_code = com_code  # ເກັບຄ່າສຸດທ້າຍທີ່ຈະບັນທຶກ

            if lcic_id and com_code:
                # ລອງຄົ້ນຫາດ້ວຍທັງສອງຄ່າກ່ອນ
                enterprise = EnterpriseInfo.objects.filter(
                    LCIC_code=lcic_id, 
                    EnterpriseID=com_code
                ).first()
                search_criteria = "both"
                
                # ຖ້າບໍ່ເຈົ້າ, ລອງຄົ້ນຫາແຍກ ແລະດຶງຄ່າທີ່ຂາດໄປ
                if not enterprise:
                    # ລອງຄົ້ນຫາດ້ວຍ LCIC_code ກ່ອນ
                    enterprise_by_lcic = EnterpriseInfo.objects.filter(LCIC_code=lcic_id).first()
                    if enterprise_by_lcic:
                        enterprise = enterprise_by_lcic
                        final_com_code = enterprise_by_lcic.EnterpriseID  # ດຶງ com_code ທີ່ຖືກຈາກ DB
                        search_criteria = "found_by_lcic_updated_com_code"
                    else:
                        # ຖ້າບໍ່ເຈົ້າດ້ວຍ LCIC, ລອງຄົ້ນຫາດ້ວຍ com_code
                        enterprise_by_com = EnterpriseInfo.objects.filter(EnterpriseID=com_code).first()
                        if enterprise_by_com:
                            enterprise = enterprise_by_com
                            final_lcic_id = enterprise_by_com.LCIC_code  # ດຶງ LCIC_code ທີ່ຖືກຈາກ DB
                            search_criteria = "found_by_com_code_updated_lcic"
                        
            elif lcic_id:
                enterprise = EnterpriseInfo.objects.filter(
                    LCIC_code=lcic_id
                ).first()
                if enterprise:
                    final_com_code = enterprise.EnterpriseID  
                search_criteria = "lcic_only"
            elif com_code:
                enterprise = EnterpriseInfo.objects.filter(
                    EnterpriseID=com_code
                ).first()
                if enterprise:
                    final_lcic_id = enterprise.LCIC_code 
                search_criteria = "com_code_only"
            
            result_data = {
                "LCIC_code": final_lcic_id,  
                "com_enterprise_code": final_com_code,  
                "search_criteria": search_criteria,  
                "status": "Found" if enterprise else "Not Found",
                "enterpriseNameLao": enterprise.enterpriseNameLao if enterprise else None,
                "investmentCurrency": enterprise.investmentCurrency if enterprise else None
            }
            
            if result_data["status"] == "Found":
                found_count += 1
            else:
                not_found_count += 1
            
            search_result = SearchResult.objects.create(
                bank_code=user_id,
                UID=UID,
                search_batch=search_batfile,
                LCIC_code=final_lcic_id,  
                com_enterprise_code=final_com_code,  
                status=result_data["status"],
                enterpriseNameLao=result_data["enterpriseNameLao"],
                investmentCurrency=result_data["investmentCurrency"],
                duplicates=json.dumps({
                    "original_LCIC_code": lcic_id,  
                    "original_com_enterprise_code": com_code,  
                    "final_LCIC_code": final_lcic_id, 
                    "final_com_enterprise_code": final_com_code,  
                    "total": record_counter[unique_key]
                })  
            )
           
            results.append({
                "id": search_result.id,
                "LCIC_code": search_result.LCIC_code,
                "com_enterprise_code": search_result.com_enterprise_code,
                "status": search_result.status,
                "enterpriseNameLao": search_result.enterpriseNameLao,
                "investmentCurrency": search_result.investmentCurrency,
                "created_at": search_result.created_at,
                "bank_code": search_result.bank_code,
                "UID": search_result.UID
            })

        search_batfile.searchtrue = found_count
        search_batfile.searchfals = not_found_count
        search_batfile.save()

        duplicates = {f"{key[0]}-{key[1]}": count for key, count in record_counter.items() if count > 1}
        duplicate_counts = list(duplicates.values())
        total_duplicates = sum(duplicate_counts)
        print("duplicates", duplicates)
        print("total_duplicates", total_duplicates)
        search_batfile.duplicates = json.dumps(duplicate_counts)  
        search_batfile.duplicates_false = json.dumps(list(duplicates.keys()))  
        search_batfile.count_duplicates = total_duplicates
        search_batfile.save()

        return JsonResponse({
            "results": results, 
            "search_batfile_id": search_batfile.id, 
            "duplicates": total_duplicates,
            "filename": new_filename  
        }, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=405)
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import SearchResult
@csrf_exempt
@require_http_methods(["PATCH"])
def update_multiple_search_results_status(request):
  
    try:
        # ອ່ານ JSON data
        data = json.loads(request.body)
        ids = data.get('ids', [])
        
        if not ids or not isinstance(ids, list):
            return JsonResponse({
                'success': False,
                'message': 'IDs list is required and must be an array'
            }, status=400)
        
        
        search_results = SearchResult.objects.filter(id__in=ids)
        found_ids = list(search_results.values_list('id', flat=True))
        not_found_ids = [id for id in ids if id not in found_ids]
        
        # ອັບເດດ status ເປັນ 'Found'
        updated_count = search_results.update(status='Not Found')
        
        # ດຶງຂໍ້ມູນທີ່ອັບເດດແລ້ວ
        updated_results = list(search_results.values(
            'id', 'status', 'lcicID', 'LCIC_code', 
            'com_enterprise_code', 'enterpriseNameLao'
        ))
        
        return JsonResponse({
            'success': True,
            'message': f'Successfully updated {updated_count} records',
            'data': {
                'updated_count': updated_count,
                'updated_results': updated_results,
                'requested_ids': ids,
                'found_ids': found_ids,
                'not_found_ids': not_found_ids
            }
        }, status=200)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON format'
        }, status=400)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error updating status: {str(e)}'
        }, status=500)
from .models import ChargeMatrix, B1



class InsertSearchLogView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        bank = user.MID
        bank_info = memberInfo.objects.get(bnk_code=bank.bnk_code)
        charge_bank_type = bank_info.bnk_type
        if charge_bank_type == 1:
            chargeType = ChargeMatrix.objects.get(chg_sys_id=2)                    
        else:
            chargeType = ChargeMatrix.objects.get(chg_sys_id=5)
        charge_amount_com = chargeType.chg_amount
        EnterpriseID = request.data.get('EnterpriseID')
        LCIC_code = request.data.get('LCIC_code')
        # search_loan = B1.objects.filter(LCIC_code=LCIC_code or EnterpriseID=EnterpriseID)
        search_loan = B1.objects.filter(Q(LCIC_code=LCIC_code) | Q(com_enterprise_code=EnterpriseID))
        print("LCIC_code: =-=============================>", LCIC_code)
        print("EnterpriseID: =-=============================>", EnterpriseID)
        
        for loan_log in search_loan:
         sys_usr = f"{str(user.UID)}-{str(bank.bnk_code)}"
        if EnterpriseID and LCIC_code:
            try:
                inquiry_month = datetime(year=2024, month=10, day=1).strftime('%Y-%m')
                inquiry_month_charge = datetime(year=2024, month=10, day=1).strftime('%d%m%Y')
                search_log = searchLog.objects.create(
                    enterprise_ID=EnterpriseID,
                    LCIC_code=LCIC_code,
                    bnk_code=bank_info.bnk_code,
                    bnk_type=bank_info.bnk_type,
                    branch=loan_log.branch_id,
                    cus_ID=loan_log.customer_id,
                    cusType=loan_log.segmentType,
                    credit_type=chargeType.chg_code,
                    inquiry_month=inquiry_month,
                    com_tel='',
                    com_location='',
                    rec_loan_amount=0.0,
                    rec_loan_amount_currency='LAK',
                    rec_loan_purpose=loan_log.lon_purpose_code,
                    rec_enquiry_type='1',
                    sys_usr=sys_usr  
                )
               
                charge = request_charge.objects.create(
                    bnk_code=bank_info.bnk_code,
                    bnk_type=bank_info.bnk_type,
                    chg_amount=charge_amount_com,
                    chg_code=chargeType.chg_code,
                    status='pending',  
                    rtp_code='1',
                    lon_purpose=loan_log.lon_purpose_code,
                    chg_unit=chargeType.chg_unit,
                    user_sys_id=sys_usr,
                    LCIC_code=LCIC_code,
                    cusType=loan_log.segmentType,
                    user_session_id='',
                    rec_reference_code='',
                    search_log=search_log
                )
                charge.rec_reference_code = f"{chargeType.chg_code}-{charge.rtp_code}-{charge.bnk_code}-{inquiry_month_charge}-{charge.rec_charge_ID}"
                charge.save()
               
                return Response({'success': 'Search log inserted'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                import traceback
                error_details = traceback.format_exc()
                return Response({
        'error': str(e),
        'details': error_details
    }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'EnterpriseID and LCIC_code are required'}, status=status.HTTP_400_BAD_REQUEST)
       
        
        
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Search_batfile
# from .serializers import SearchBatfileSerializer

# class SearchBatfileAPIView(APIView):
#     def get(self, request):
#         user_id = request.query_params.get('user_id')
#         filter_user_id = request.query_params.get('filter_user_id')  
        
#         if not user_id:
#             return Response(
#                 {"error": "user_id parameter is required"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
        
#         if user_id == "01":
           
#             if filter_user_id:
#                 files = Search_batfile.objects.filter(user_id=filter_user_id)
#             else:
              
#                 files = Search_batfile.objects.all()
#         else:
            
#             files = Search_batfile.objects.filter(user_id=user_id)
        
#         serializer = SearchBatfileSerializer(files, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Search_batfile
from .serializers import SearchBatfileSerializer
from django.db.models import Q
from datetime import datetime, date

class SearchBatfileAPIView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        filter_user_id = request.query_params.get('filter_user_id')
        
        # Date filtering parameters
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        day = request.query_params.get('day')
        start_date = request.query_params.get('start_date')  # YYYY-MM-DD
        end_date = request.query_params.get('end_date')      # YYYY-MM-DD
        
        if not user_id:
            return Response(
                {"error": "user_id parameter is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # ຖ້າເປັນ admin user (01)
        if user_id == "01":
            if filter_user_id:
                files = Search_batfile.objects.filter(user_id=filter_user_id)
            else:
                files = Search_batfile.objects.all()
        else:
            files = Search_batfile.objects.filter(user_id=user_id)
        
        # Apply date filters
        try:
            # Filter by year
            if year:
                files = files.filter(insertDate__year=int(year))
            
            # Filter by month (requires year or will filter all records with that month)
            if month:
                files = files.filter(insertDate__month=int(month))
            
            # Filter by day (requires year and month or will filter all records with that day)
            if day:
                files = files.filter(insertDate__day=int(day))
            
            # Filter by date range
            if start_date:
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
                files = files.filter(insertDate__date__gte=start_date_obj)
            
            if end_date:
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
                files = files.filter(insertDate__date__lte=end_date_obj)
                
        except (ValueError, TypeError) as e:
            return Response(
                {"error": "Invalid date format. Use YYYY for year, MM for month, DD for day, YYYY-MM-DD for dates"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = SearchBatfileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from .models import Search_batfile, SearchResult

def get_search_results(request, id):
    search_batch = get_object_or_404(Search_batfile, id=id)
    search_results = SearchResult.objects.filter(search_batch=search_batch)
    results_data = [
        {
            "id": result.id,
            "LCIC_code": result.LCIC_code,
            "com_enterprise_code": result.com_enterprise_code,
            "status": result.status,
            "enterpriseNameLao": result.enterpriseNameLao,
            "investmentCurrency": result.investmentCurrency,
            "created_at": result.created_at,
            "duplicates": result.duplicates,
        }
        for result in search_results
    ]
    return JsonResponse({"results": results_data})


@csrf_exempt
def update_searchlog_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        search_result_id = data.get('id')
        status = data.get('status')

        try:
            search_result = SearchResult.objects.get(id=search_result_id)
            search_result.status = status
            search_result.save()
            return JsonResponse({"success": "Status updated"}, status=200)
        except SearchResult.DoesNotExist:
            return JsonResponse({"error": "SearchResult not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=405)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EnterpriseInfo, UploadFile_enterpriseinfo
from django.utils.dateparse import parse_datetime
import json

@csrf_exempt
def upload_enterprise_info(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        user_id = request.POST.get('user_id')
        if not file:
            return JsonResponse({"error": "No file provided"}, status=400)

        try:
            data = json.load(file)
            if isinstance(data, dict):
                data = [data]
        except json.JSONDecodeError as e:
            return JsonResponse({"error": f"Invalid JSON file: {str(e)}"}, status=400)

        updated_count = 0
        created_count = 0
        updated_records = []
        created_records = []

        
        upload_file = UploadFile_enterpriseinfo.objects.create(
            user_id=user_id,
            file_name=file.name,
            path=f"searchfile/{file.name}",
            fileUpload=file,
            status='Processing'
        )

        for record in data:
            enterprise_id = record.get('EnterpriseID')
            lcic_id = record.get('LCICID')
            if not enterprise_id or not lcic_id:
                print(f"Missing EnterpriseID or LCICID in record: {record}")
                continue

            print(f"Processing record for EnterpriseID: {enterprise_id}, LCICID: {lcic_id}")

            regis_date = record.get('regisDate')
            if regis_date and isinstance(regis_date, str):
                regis_date = parse_datetime(regis_date)

            last_update = record.get('LastUpdate')
            if last_update and isinstance(last_update, str):
                last_update = parse_datetime(last_update)

            cancellation_date = record.get('CancellationDate')
            if cancellation_date and isinstance(cancellation_date, str):
                cancellation_date = parse_datetime(cancellation_date)

            update_date = record.get('UpdateDate')
            if update_date and isinstance(update_date, str):
                update_date = parse_datetime(update_date)

            enterprise, created = EnterpriseInfo.objects.update_or_create(
                EnterpriseID=enterprise_id,
                LCICID=lcic_id,
                defaults={
                    'enterpriseNameLao': record.get('enterpriseNameLao'),
                    'eneterpriseNameEnglish': record.get('enterpriseNameEnglish'),
                    'regisCertificateNumber': record.get('regisCertificateNumber'),
                    'regisDate': regis_date,
                    'enLocation': record.get('enLocation'),
                    'regisStrationOfficeType': record.get('regisStrationOfficeType'),
                    'regisStationOfficeCode': record.get('regisStationOfficeCode'),
                    'enLegalStrature': record.get('enLegalStrature'),
                    'foreigninvestorFlag': record.get('foreignInvestorFlag'),
                    'investmentAmount': record.get('investmentAmount'),
                    'investmentCurrency': record.get('investmentCurrency'),
                    'representativeNationality': record.get('representativeNationality'),
                    'LastUpdate': last_update,
                    'CancellationDate': cancellation_date,
                    'UpdateDate': update_date,
                    'id_file': upload_file,
                }
            )
            
            
            enterprise.status = 1 if created else 2
            enterprise.save()

            if created:
                created_count += 1
                created_records.append(enterprise.EnterpriseID)
                print(f"Created new record: {enterprise.EnterpriseID}")
            else:
                updated_count += 1
                updated_records.append(enterprise.EnterpriseID)
                print(f"Updated record: {enterprise.EnterpriseID}")

       
        upload_file.status = 'Completed'
        upload_file.updatedate = updated_count
        upload_file.crete = created_count
        upload_file.save()

        response_data = {
            'updated_count': updated_count,
            'created_count': created_count,
            'updated_records': updated_records,
            'created_records': created_records,
        }
        
        return JsonResponse(response_data, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
@csrf_exempt
def get_enterprise_info(request):
    if request.method == 'GET':
        id_file = request.GET.get('id_file')
        status = request.GET.get('status')
        limit = int(request.GET.get('limit', 100))
        page = int(request.GET.get('page', 1))

        if id_file and status:
            enterprises = EnterpriseInfo.objects.filter(id_file=id_file, status=status)
        elif id_file:
            enterprises = EnterpriseInfo.objects.filter(id_file=id_file)
        elif status:
            enterprises = EnterpriseInfo.objects.filter(status=status)
        else:
            enterprises = EnterpriseInfo.objects.all()

        start = (page - 1) * limit
        end = start + limit
        enterprise_list = list(enterprises.values()[start:end])
        return JsonResponse(enterprise_list, safe=False, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
@csrf_exempt
def get_all_enterprise(request):
    if request.method == 'GET':
        id_file = request.GET.get('id_file')
        status = request.GET.get('status')

        if id_file and status:
            enterprises = EnterpriseInfo.objects.filter(id_file=id_file, status=status)
        elif id_file:
            enterprises = EnterpriseInfo.objects.filter(id_file=id_file)
        elif status:
            enterprises = EnterpriseInfo.objects.filter(status=status)
        else:
            enterprises = EnterpriseInfo.objects.all()

        enterprise_list = list(enterprises.values())
        return JsonResponse(enterprise_list, safe=False, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
@csrf_exempt
def get_all_upload_files(request):
    if request.method == 'GET':
        files = UploadFile_enterpriseinfo.objects.all().order_by('-insertdate')
        file_list = list(files.values())
        return JsonResponse(file_list, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
# perm paylay
from collections import defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import pytz  # Import pytz to handle timezone conversion

class UserListbyBank(APIView):
    def get(self, request, format=None):
        # Define the timezone (e.g., Asia/Bangkok)
        target_timezone = pytz.timezone('Asia/Bangkok')
        
        # Fetch all users and order by 'UID', including related 'memberInfo' (MID)
        all_users = Login.objects.select_related('MID').order_by('UID')

        custom_user_data = []
        bnk_code_counts = defaultdict(int)  # To keep track of user counts per bnk_code

        # Loop through all users and extract necessary fields, including memberInfo (bank) fields
        for user in all_users:
            if user.MID:  # Ensure that the user has a related MID
                bank_info = user.MID  # Access the related memberInfo (MID) directly

                # Convert last_login to the target timezone
                last_login_local = user.last_login.astimezone(target_timezone) if user.last_login else None
                formatted_last_login_local = last_login_local.strftime('%Y-%m-%d %H:%M:%S') if last_login_local else None
                
                # Add user data to the list
                custom_user_data.append({
                    "UID": user.UID,
                    "bnk_code": bank_info.bnk_code if bank_info else None,  # Access bank code from memberInfo
                    "bnk_name": bank_info.nameL if bank_info else None,  # Access bank name from memberInfo
                    "Permission": user.GID.nameL if user.GID else None,  # Handle case where GID may be null
                    "username": user.username,
                    "nameL": user.nameL,
                    "nameE": user.nameE,
                    "surnameL": user.surnameL,
                    "surnameE": user.surnameE,
                    "last_login": formatted_last_login_local,  # Use the converted last_login
                    "is_active": user.is_active,
                })
                
                # Increment the count for the user's bnk_code
                if bank_info.bnk_code:
                    bnk_code_counts[bank_info.bnk_code] += 1

        # Prepare the combined response
        combined_data = {
            # 'all_user': custom_user_data,
            'sum_by_bnk_code': dict(bnk_code_counts),  # Convert defaultdict to a regular dictionary for JSON response
        }
        
        return Response(combined_data, status=status.HTTP_200_OK)
from .models import DataSubmitUtility
from .serializers import DataSubmitUtilitySerializer
class DataSubmitUtilityView(APIView):
    def get(self, request):

        report_catalogs = DataSubmitUtility.objects.all()  # Retrieve all report catalog entries
        serializer = DataSubmitUtilitySerializer(report_catalogs, many=True)  # Serialize them
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        try:
            utility = DataSubmitUtility.objects.get(pk=pk)  # Retrieve the record by primary key (pk)
        except DataSubmitUtility.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DataSubmitUtilitySerializer(utility, data=request.data, partial=True)  # Partial update
        if serializer.is_valid():
            serializer.save()  # Save the updated record
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            utility = DataSubmitUtility.objects.get(pk=pk)  # Retrieve the record by primary key (pk)
        except DataSubmitUtility.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DataSubmitUtilitySerializer(utility, data=request.data)  # Full update (all fields required)
        if serializer.is_valid():
            serializer.save()  # Save the updated record
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DataUtility
from datetime import datetime
import json

class UploadUtilityView(APIView):
    def post(self, request):
        try:
            # Ensure a file is provided in the request
            if "file" not in request.FILES:
                return Response({"status": "error", "message": "No file uploaded."}, status=400)
            
            # Parse the JSON file
            json_file = request.FILES["file"]
            data = json.load(json_file)

            # Validate JSON structure
            if not isinstance(data, list):
                return Response({"status": "error", "message": "Invalid JSON structure: Expected a list."}, status=400)

            # Insert records into the database
            for record in data:
                DataUtility.objects.create(  # Ensure this matches your model name
                    no=record.get("NO"),
                    customer_id=record.get("CUSTOMER_ID"),
                    supply_type=record.get("SUPPLY_TYPE"),
                    outstanding=record.get("OUTSTANDING"),
                    basic_tax=record.get("BASIC+TAX"),
                    bill_amount=record.get("BILL_AMOUNT"),
                    bill_of_month=record.get("BILL_OF_MONTH"),
                    date_of_issue=record.get("DATE_OF_ISSUE"),
                    dis_id=record.get("DIS_ID"),
                    pro_id=record.get("PRO_ID"),
                    zone=record.get("ZONE"),
                    pay_amount=record.get("PAY_AMOUNT"),
                    payment_id=record.get("PAYMENT_ID"),
                    pay_type=record.get("PAY_TYPE"),
                    payment_date=record.get("PAYMENT_DATE"),
                )
            
            return Response({"status": "success", "message": "Data inserted successfully."})
        
        except json.JSONDecodeError:
            return Response({"status": "error", "message": "Invalid JSON file."}, status=400)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=500)
        
class AddMemberAPIView(APIView):
    def post(self, request):
        serializer = MemberInfoSerializer(data=request.data)
        if serializer.is_valid():
            member = serializer.save()
            return Response({
                "success": True,
                "message": "Member added successfully!",
                "data": MemberInfoSerializer(member).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import memberInfo, bank_branch
# from django.db.models import OuterRef, Subquery, F, Count
from django.db.models import F, Count, OuterRef, Subquery, Q
from pytz import timezone


class DistinctBankCodeView(APIView):
    def get(self, request):
        try:
            # Get query parameters
            bnk_code = request.GET.get('bnk_code', None)
            branch_id = request.GET.get('branch_id', None)
            sort_by = request.GET.get('sort_by', 'user_count')  # Default sort by `user_count`
            
            
            target_timezone = pytz.timezone('Asia/Bangkok')
            # Validate `sort_by` parameter
            valid_sort_fields = ['user_count', '-user_count', 'bnk_code', '-bnk_code', 'branch_id', '-branch_id']
            if sort_by not in valid_sort_fields:
                return Response(
                    {"detail": f"Invalid sort field: {sort_by}. Valid fields are {valid_sort_fields}."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if bnk_code and branch_id:
                # Fetch users matching both bnk_code and branch_id
                # user_count = Login.objects.filter(bnk_code=bnk_code, branch_id=branch_id)
                user_count = Login.objects.filter(
                    bnk_code=bnk_code
                ).filter(
                    Q(branch_id=branch_id) | Q(branch_id__isnull=True)
                )
                # Serialize detailed user data
                # serializer = LoginSerializer(user_count, many=True)
                # result = serializer.data
                
                custom_user_data = []

                for user in user_count:
                    # Convert `last_login` to the target timezone
                    last_login_local = user.last_login.astimezone(target_timezone) if user.last_login else None
                    formatted_last_login_local = last_login_local.strftime('%Y-%m-%d %H:%M:%S') if last_login_local else None
                    
                    # Extract related `memberInfo` (MID) fields
                    bank_info = user.MID if user.MID else None

                    # Append custom user data
                    custom_user_data.append({
                        "UID": user.UID,
                        "bnk_form": bank_info.code,
                        "bnk_code": bank_info.bnk_code if bank_info else None,  # Bank code from `memberInfo`
                        "bnk_name": bank_info.nameL if bank_info else None,    # Bank name from `memberInfo`
                        "Permission": user.GID.nameL if user.GID else None,    # Permission from `GID`
                        "username": user.username,
                        "nameL": user.nameL,
                        "nameE": user.nameE,
                        "surnameL": user.surnameL,
                        "surnameE": user.surnameE,
                        "last_login": formatted_last_login_local,             # Formatted last login
                        "is_active": user.is_active,
                    })

                # Use the custom data list as the result
                result = custom_user_data

            elif bnk_code:
                # Prepare a subquery to fetch branch_name from bank_branch
                branch_name_subquery = bank_branch.objects.filter(
                    bnk_code=OuterRef('bnk_code'),
                    branch_id=OuterRef('branch_id')
                ).values('branch_name')[:1]

                # If `bnk_code` is provided, group by `bnk_code` and `branch_id`
                user_count = (
                    Login.objects.filter(bnk_code=bnk_code)
                    .values('bnk_code', 'branch_id')
                    .annotate(
                        user_count=Count('UID'),               # Count the users
                        member_code=F('MID__code'),            # Get `code` from `memberInfo`
                        member_nameL=F('MID__nameL'),          # Get `nameL` from `memberInfo`
                        branch_name=Subquery(branch_name_subquery)  # Fetch branch_name from `bank_branch`
                    )
                    .order_by(sort_by)  # Dynamic sorting
                )

                # Convert queryset to a list for JSON response
                result = list(user_count)

            else:
                # If `bnk_code` is not provided, group only by `bnk_code` with additional join on memberInfo
                user_count = (
                    Login.objects.values('bnk_code')
                    .annotate(
                        user_count=Count('UID'),
                        member_code=F('MID__code'),  # Referencing the related field `code` from memberInfo
                        member_nameL=F('MID__nameL')  # Referencing the related field `nameL` from memberInfo
                    )
                    .order_by(sort_by)  # Dynamic sorting
                )

                # No need to use serializer for aggregated results
                result = list(user_count)

            # If no records are found, return a 404 error
            if not result:
                return Response({"detail": "No users found."}, status=status.HTTP_404_NOT_FOUND)

            # Return the result
            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle exceptions and return a 500 error if something goes wrong
            return Response(
                {"detail": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import bank_branch
from .serializers import BankBranchSerializer

class BankBranchListView(APIView):
    def get(self, request):
        bnk_code = request.GET.get('bnk_code')  # Get the bank code from query parameters
        if not bnk_code:
            return Response({"detail": "Bank code is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        branches = bank_branch.objects.filter(bnk_code=bnk_code)  # Filter branches by bank code
        if not branches.exists():
            return Response({"detail": "No branches found for this bank code."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BankBranchSerializer(branches, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
		
class CreateMemberView(APIView):
    def post(self, request):
        serializer = MemberInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import pytz

class UserByBankCodeView(APIView):
    def get(self, request, bnk_code, format=None):
        # Define the timezone (e.g., Asia/Bangkok)
        target_timezone = pytz.timezone('Asia/Bangkok')
        
        # Fetch users with the specified bnk_code
        users_by_bnk_code = Login.objects.select_related('MID').filter(MID__bnk_code=bnk_code).order_by('UID')
        
        custom_user_data = []

        for user in users_by_bnk_code:
            if user.MID:  # Ensure that the user has a related MID
                bank_info = user.MID

                # Convert last_login to the target timezone
                last_login_local = user.last_login.astimezone(target_timezone) if user.last_login else None
                formatted_last_login_local = last_login_local.strftime('%Y-%m-%d %H:%M:%S') if last_login_local else None
                
                # Add user data to the list
                custom_user_data.append({
                    "UID": user.UID,
                    "bnk_code": bank_info.bnk_code if bank_info else None,
                    "bnk_name": bank_info.nameL if bank_info else None,
                    "Permission": user.GID.nameL if user.GID else None,
                    "username": user.username,
                    "nameL": user.nameL,
                    "nameE": user.nameE,
                    "surnameL": user.surnameL,
                    "surnameE": user.surnameE,
                    "last_login": formatted_last_login_local,
                    "is_active": user.is_active,
                })
        
        # Prepare the response
        return Response({"users": custom_user_data}, status=status.HTTP_200_OK)
class BankUsersView(APIView):
    def get(self, request):
        # Get the 'bnk_code' parameter from the request
        bnk_code = request.GET.get('bnk_code', None)

        # Check if 'bnk_code' is provided
        if not bnk_code:
            return Response(
                {"error": "bnk_code parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Filter users by 'bnk_code' and count them
        user_count = Login.objects.filter(bnk_code=bnk_code).count()

        # Return the count in the response
        return Response(
            {"bnk_code": bnk_code, "user_count": user_count},
            status=status.HTTP_200_OK
        )
        
# from django.db.models import Count
# from django.db.models.functions import ExtractYear, ExtractMonth
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import B1  

# class LoanCountByMonthAPIView(APIView):
    
#     def get(self, request, *args, **kwargs):
        
#         bnk_code = request.GET.get('bnk_code', None)
#         year = request.GET.get('year', None)
        
#         queryset = B1.objects.filter(
#             bnk_code=bnk_code,
#             lon_insert_date__year=year
#         )

#         # Annotate the queryset with year and month, then group by them
#         monthly_counts = queryset.annotate(
#             year=ExtractYear('lon_insert_date'),
#             month=ExtractMonth('lon_insert_date')
#         ).values('year', 'month').annotate(
#             loan_count=Count('loan_id')
#         ).order_by('year', 'month')

#         # Format the result as a list of dictionaries
#         result = [
#             {
#                 'year_month': f"{item['year']}-{str(item['month']).zfill(2)}",
#                 'loan_count': item['loan_count']
#             }
#             for item in monthly_counts
#         ]

#         return Response(result, status=status.HTTP_200_OK)

from django.db.models import Count
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay, ExtractHour
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import B1  # Your Django model

class LoanCountByDate(APIView):
    
    # def get(self, request, *args, **kwargs):
    #     bnk_code = request.GET.get("bnk_code")
    #     year = request.GET.get("year")
    #     month = request.GET.get("month")
    #     day = request.GET.get("day")

    #     if not bnk_code:
    #         return Response({"error": "bnk_code is required"}, status=status.HTTP_400_BAD_REQUEST)

    #     # Initial queryset filter
    #     queryset = B1.objects.filter(bnk_code=bnk_code)

    #     # Determine grouping based on provided parameters
    #     if year and month and day:
    #         # Group by Hour of the Day
    #         grouped_queryset = queryset.filter(lon_insert_date__year=year, lon_insert_date__month=month, lon_insert_date__day=day) \
    #             .annotate(hour=ExtractHour("lon_insert_date")) \
    #             .values("hour") \
    #             .annotate(loan_count=Count("loan_id")) \
    #             .order_by("hour")

    #         result = [{"hour_of_day": str(item["hour"]).zfill(2), "loan_count": item["loan_count"]} for item in grouped_queryset]

    #     elif year and month:
    #         # Group by Day of the Month
    #         grouped_queryset = queryset.filter(lon_insert_date__year=year, lon_insert_date__month=month) \
    #             .annotate(day=ExtractDay("lon_insert_date")) \
    #             .values("day") \
    #             .annotate(loan_count=Count("loan_id")) \
    #             .order_by("day")

    #         result = [{"day_of_month": str(item["day"]).zfill(2), "loan_count": item["loan_count"]} for item in grouped_queryset]

    #     elif year:
    #         # Group by Month of the Year
    #         grouped_queryset = queryset.filter(lon_insert_date__year=year) \
    #             .annotate(month=ExtractMonth("lon_insert_date")) \
    #             .values("month") \
    #             .annotate(loan_count=Count("loan_id")) \
    #             .order_by("month")

    #         result = [{"year_month": f"{year}-{str(item['month']).zfill(2)}", "loan_count": item["loan_count"]} for item in grouped_queryset]

    #     else:
    #         # Group by Year when no date filters are provided
    #         grouped_queryset = queryset.annotate(year=ExtractYear("lon_insert_date")) \
    #             .values("year") \
    #             .annotate(loan_count=Count("loan_id")) \
    #             .order_by("year")

    #         result = [{"year": str(item["year"]), "loan_count": item["loan_count"]} for item in grouped_queryset]

    #     return Response(result, status=status.HTTP_200_OK)
    
        
    # def get(self, request, *args, **kwargs):
    #     bnk_code = request.GET.get("bnk_code")
    #     year = request.GET.get("year")
    #     month = request.GET.get("month")

    #     if not bnk_code:
    #         return Response({"error": "bnk_code is required"}, status=status.HTTP_400_BAD_REQUEST)

    #     # Initial queryset filter
    #     queryset = B1_Monthly.objects.filter(bnk_code=bnk_code)

    #     # Build the period string based on year and month
    #     if year and month:
    #         period = f"{year}{month.zfill(2)}"  # Format: YYYYMM
    #     elif year:
    #         period = f"{year}"  # Format: YYYY
    #     else:
    #         period = None

    #     # Determine grouping based on provided parameters
    #     if year and month:
    #         # Group by Day of the Month
    #         queryset = queryset.filter(period__startswith=period)  # Filter by YYYYMM
    #         grouped_queryset = queryset.values("period") \
    #             .annotate(loan_count=Count("loan_id")) \
    #             .order_by("period")

    #         result = [{"day_of_month": item["period"][-2:], "loan_count": item["loan_count"]} for item in grouped_queryset]

    #     elif year:
    #         # Group by Month of the Year
    #         queryset = queryset.filter(period__startswith=year)  # Filter by YYYY
    #         grouped_queryset = queryset.values("period") \
    #             .annotate(loan_count=Count("loan_id")) \
    #             .order_by("period")

    #         result = [{"year_month": f"{item['period'][:4]}-{item['period'][4:]}", "loan_count": item["loan_count"]} for item in grouped_queryset]

    #     else:
    #         # Group by Year when no year or month is provided
    #         grouped_queryset = queryset.values("period") \
    #             .annotate(loan_count=Count("loan_id")) \
    #             .order_by("period")

    #         result = [{"year": item["period"][:4], "loan_count": item["loan_count"]} for item in grouped_queryset]

    #     return Response(result, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        bnk_code = request.GET.get("bnk_code")
        year = request.GET.get("year")
        month = request.GET.get("month")

        if not bnk_code:
            return Response({"error": "bnk_code is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Initial queryset filter
        queryset = B1_Monthly.objects.filter(bnk_code=bnk_code)

        # Determine grouping based on provided parameters
        if year and month:
            # Group by Day of the Month (YYYYMM)
            period_prefix = f"{year}{month.zfill(2)}"
            queryset = queryset.filter(period__startswith=period_prefix)
            grouped_queryset = queryset.values("period") \
                .annotate(loan_count=Count("loan_id")) \
                .order_by("period")

            result = [{"day_of_month": item["period"][-2:], "loan_count": item["loan_count"]} for item in grouped_queryset]

        elif year:
            # Group by Month of the Year (YYYY)
            period_prefix = f"{year}"
            queryset = queryset.filter(period__startswith=period_prefix)
            grouped_queryset = queryset.values("period") \
                .annotate(loan_count=Count("loan_id")) \
                .order_by("period")

            result = [{"year_month": f"{item['period'][:4]}-{item['period'][4:]}", "loan_count": item["loan_count"]} for item in grouped_queryset]

        else:
            # Group by Year when no year or month is provided
            grouped_queryset = queryset.values("period") \
                .annotate(loan_count=Count("loan_id")) \
                .order_by("period")

            result = []
            for item in grouped_queryset:
                year_str = item["period"][:4]  # Extract first 4 digits as year
                found = next((r for r in result if r["year"] == year_str), None)
                if found:
                    found["loan_count"] += item["loan_count"]
                else:
                    result.append({"year": year_str, "loan_count": item["loan_count"]})

        return Response(result, status=status.HTTP_200_OK)

class CountSearchLogbyDate(APIView):
    def get(self, request, *args, **kwargs):
        bnk_code = request.GET.get("bnk_code")
        year = request.GET.get("year")
        month = request.GET.get("month")
        day = request.GET.get("day")

        if not bnk_code:
            return Response({"error": "bnk_code is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Initial queryset filter
        queryset = searchLog.objects.filter(bnk_code=bnk_code)

        # If no year, month, or day is provided → Group by Year
        if not year:
            grouped_queryset = queryset.annotate(year=ExtractYear("inquiry_date")) \
                .values("year") \
                .annotate(search_count=Count("search_ID")) \
                .order_by("year")

            result = [{"year": item["year"], "search_count": item["search_count"]} for item in grouped_queryset]

        # If year, month, and day are provided → Group by Hour
        elif year and month and day:
            grouped_queryset = queryset.filter(inquiry_date__year=year, inquiry_date__month=month, inquiry_date__day=day) \
                .annotate(hour=ExtractHour("inquiry_date")) \
                .values("hour") \
                .annotate(search_count=Count("search_ID")) \
                .order_by("hour")

            result = [{"hour_of_day": str(item["hour"]).zfill(2), "search_count": item["search_count"]} for item in grouped_queryset]

        # If year and month are provided → Group by Day
        elif year and month:
            grouped_queryset = queryset.filter(inquiry_date__year=year, inquiry_date__month=month) \
                .annotate(day=ExtractDay("inquiry_date")) \
                .values("day") \
                .annotate(search_count=Count("search_ID")) \
                .order_by("day")

            result = [{"day_of_month": str(item["day"]).zfill(2), "search_count": item["search_count"]} for item in grouped_queryset]

        # If only year is provided → Group by Month
        else:
            grouped_queryset = queryset.filter(inquiry_date__year=year) \
                .annotate(month=ExtractMonth("inquiry_date")) \
                .values("month") \
                .annotate(search_count=Count("search_ID")) \
                .order_by("month")

            result = [{"year_month": f"{year}-{str(item['month']).zfill(2)}", "search_count": item["search_count"]} for item in grouped_queryset]

        return Response(result, status=status.HTTP_200_OK)
    
class CountFeebyDate(APIView):
    
    def get(self, request, *args, **kwargs):
        bnk_code = request.GET.get("bnk_code")
        year = request.GET.get("year")  
        month = request.GET.get("month")
        day = request.GET.get("day")

        if not bnk_code:
            return Response({"error": "bnk_code is required"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = request_charge.objects.filter(bnk_code=bnk_code)

        # If no year, month, or day is provided → Group by Year
        if not year and not month and not day:
            grouped_queryset = queryset.annotate(year=ExtractYear("rec_insert_date")) \
                .values("year") \
                .annotate(total_fee=Sum("chg_amount")) \
                .order_by("year")

            result = [{"year": item["year"], "total_fee": float(item["total_fee"] or 0)} for item in grouped_queryset]

        # If only year is provided → Group by Month
        elif year and not month and not day:
            queryset = queryset.filter(rec_insert_date__year=year)
            grouped_queryset = queryset.annotate(month=ExtractMonth("rec_insert_date")) \
                .values("month") \
                .annotate(total_fee=Sum("chg_amount")) \
                .order_by("month")

            result = [{"year_month": f"{year}-{str(item['month']).zfill(2)}", "total_fee": float(item["total_fee"] or 0)} for item in grouped_queryset]

        # If year and month are provided → Group by Day
        elif year and month and not day:
            queryset = queryset.filter(rec_insert_date__year=year, rec_insert_date__month=month)
            grouped_queryset = queryset.annotate(day=ExtractDay("rec_insert_date")) \
                .values("day") \
                .annotate(total_fee=Sum("chg_amount")) \
                .order_by("day")

            result = [{"day_of_month": str(item["day"]).zfill(2), "total_fee": float(item["total_fee"] or 0)} for item in grouped_queryset]

        # If year, month, and day are provided → Group by Hour
        elif year and month and day:
            queryset = queryset.filter(rec_insert_date__year=year, rec_insert_date__month=month, rec_insert_date__day=day)
            grouped_queryset = queryset.annotate(hour=ExtractHour("rec_insert_date")) \
                .values("hour") \
                .annotate(total_fee=Sum("chg_amount")) \
                .order_by("hour")

            result = [{"hour_of_day": str(item["hour"]).zfill(2), "total_fee": float(item["total_fee"] or 0)} for item in grouped_queryset]

        return Response(result, status=status.HTTP_200_OK)
    
# class LoanStatsView(APIView):
#     def get(self, request):
#         # Get the bnk_code from query parameters (default to None)
#         bnk_code = request.GET.get("bnk_code")

#         if not bnk_code:
#             return Response({"error": "bnk_code is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Total loan counts grouped by year
#         total_counts = (
#             B1.objects
#             .annotate(year=ExtractYear("lon_open_date"))
#             .values("year")
#             .annotate(total_count=Count("id"))  # Count all records per year
#         )

#         # Loan counts for the given bnk_code grouped by year
#         filtered_counts = (
#             B1.objects
#             .filter(bnk_code=bnk_code)
#             .annotate(year=ExtractYear("lon_open_date"))
#             .values("year")
#             .annotate(loan_count=Count("id"))  # Count only filtered records per year
#         )

#         # Convert queryset results to dictionaries for easy lookup
#         total_counts_dict = {entry["year"]: entry["total_count"] for entry in total_counts}
#         filtered_counts_dict = {entry["year"]: entry["loan_count"] for entry in filtered_counts}

#         # Construct the final response data
#         result = []
#         for year, total_count in total_counts_dict.items():
#             loan_count = filtered_counts_dict.get(year, 0)  # Get count for bnk_code or 0
#             percentage = round((loan_count * 100.0) / total_count, 2) if total_count > 0 else 0
#             result.append({
#                 "year": year,
#                 "loan_count": loan_count,
#                 "total_count": total_count,
#                 "percentage": percentage
#             })

#         return Response(result, status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import B1
from django.db.models import Count
from django.db.models.functions import ExtractHour, ExtractDay, ExtractMonth, ExtractYear

class LoanStatsView(APIView):
    def get(self, request):
        # Get query parameters
        bnk_code = request.GET.get("bnk_code")
        year = request.GET.get("year")
        month = request.GET.get("month")
        day = request.GET.get("day")
        
        bnk_shortform = memberInfo.objects.get(bnk_code=bnk_code)
        print(bnk_shortform.code, "<----------")
        
        bnk_form = bnk_shortform.code
        
        if not bnk_code:
            return Response({"error": "bnk_code is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Base queryset
        queryset = B1.objects.all()
        filtered_queryset = B1.objects.filter(bnk_code=bnk_code)

        # Determine grouping
        if year and month and day:
            # Group by hour
            group_by = "hour"
            total_counts = queryset.annotate(hour=ExtractHour("lon_open_date")).values("hour").annotate(total_count=Count("id")).order_by("hour")
            filtered_counts = filtered_queryset.filter(lon_open_date__year=year, lon_open_date__month=month, lon_open_date__day=day).annotate(hour=ExtractHour("lon_open_date")).values("hour").annotate(loan_count=Count("id"))
        elif year and month:
            # Group by day
            group_by = "day"
            total_counts = queryset.annotate(day=ExtractDay("lon_open_date")).values("day").annotate(total_count=Count("id")).order_by("day")
            filtered_counts = filtered_queryset.filter(lon_open_date__year=year, lon_open_date__month=month).annotate(day=ExtractDay("lon_open_date")).values("day").annotate(loan_count=Count("id"))
        elif year:
            # Group by month
            group_by = "month"
            total_counts = queryset.annotate(month=ExtractMonth("lon_open_date")).values("month").annotate(total_count=Count("id")).order_by("month")
            filtered_counts = filtered_queryset.filter(lon_open_date__year=year).annotate(month=ExtractMonth("lon_open_date")).values("month").annotate(loan_count=Count("id"))
        else:
            # Group by year (default case)
            group_by = "year"
            total_counts = queryset.annotate(year=ExtractYear("lon_open_date")).values("year").annotate(total_count=Count("id")).order_by("year")
            filtered_counts = filtered_queryset.annotate(year=ExtractYear("lon_open_date")).values("year").annotate(loan_count=Count("id"))

        # Convert results to dictionaries for easy lookup
        total_counts_dict = {entry[group_by]: entry["total_count"] for entry in total_counts}
        filtered_counts_dict = {entry[group_by]: entry["loan_count"] for entry in filtered_counts}

        # Construct response
        result = []
        sumtotals = {"loan_count": 0, "total_count": 0}  # Initialize sumtotals

        for group_value, total_count in total_counts_dict.items():
            loan_count = filtered_counts_dict.get(group_value, 0)
            percentage = round((loan_count * 100.0) / total_count, 2) if total_count > 0 else 0
            result.append({
                group_by: group_value,
                f"{bnk_form}": loan_count,
                "total_count": total_count,
                "percentage": percentage,
            })
            sumtotals["loan_count"] += loan_count
            sumtotals["total_count"] += total_count

        # Add sumtotals to the response
        result.append({
            "sumtotals": {
                f"{bnk_form}": sumtotals["loan_count"],
                "total_count": sumtotals["total_count"]
                },
            "percentage": round((sumtotals["loan_count"] * 100.0) / sumtotals["total_count"], 2) if sumtotals["total_count"] > 0 else 0,
        })

        return Response(result, status=status.HTTP_200_OK)

# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Utility_Bill
# import json
# from datetime import datetime

# class UtilityUploadView(APIView):
#     # Use MultiPartParser to handle file uploads
#     parser_classes = [MultiPartParser]

#     def post(self, request, *args, **kwargs):
#         # Check if a file is included in the request
#         file = request.FILES.get('file')
#         if not file:
#             return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             # Read and parse the JSON file
#             file_content = file.read().decode('utf-8')
#             json_data = json.loads(file_content)

#             # Validate the JSON structure
#             if json_data.get('status') != 200 or 'message' not in json_data:
#                 return Response({'error': 'Invalid JSON structure'}, status=status.HTTP_400_BAD_REQUEST)

#             # Process each payment record
#             for record in json_data['message']:
#                 # Convert date strings to Django DateField format
#                 date_of_issue = datetime.strptime(record['DATE_OF_ISSUE'], '%d/%m/%Y').date()
#                 payment_date = datetime.strptime(record['PAYMENT_DATE'], '%d/%m/%Y').date()

#                 # Create and save the PaymentRecord instance
#                 Utility_Bill.objects.create(
#                     no=record['NO'],
#                     customer_id=record['CUSTOMER_ID'],
#                     supply_type=record['SUPPLY_TYPE'],
#                     outstanding=record['OUTSTANDING'],
#                     basic_tax=record['BASIC+TAX'],
#                     bill_amount=record['BILL_AMOUNT'],
#                     bill_of_month=record['BILL_OF_MONTH'],
#                     date_of_issue=record['DATE_OF_ISSUE'],
#                     dis_id=record['DIS_ID'],
#                     pro_id=record['PRO_ID'],
#                     zone=record['ZONE'],
#                     pay_amount=record['PAY_AMOUNT'],
#                     payment_id=record['PAYMENT_ID'],
#                     pay_type=record['PAY_TYPE'],
#                     payment_date=['PAYMENT_DATE'],
#                     userid='unknown'
#                 )

#             return Response({'message': 'Data processed and saved successfully'}, status=status.HTTP_200_OK)

#         except json.JSONDecodeError:
#             return Response({'error': 'Invalid JSON file'}, status=status.HTTP_400_BAD_REQUEST)
#         except KeyError as e:
#             return Response({'error': f'Missing key in JSON data: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import Utility_Bill
import json
from datetime import datetime

class UtilityUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            file_content = file.read().decode('utf-8')
            json_data = json.loads(file_content)

            if json_data.get('status') != 200 or 'message' not in json_data:
                return Response({'error': 'Invalid JSON structure'}, status=status.HTTP_400_BAD_REQUEST)

            # Process each record
            for record in json_data['message']:
                try:
                    # Convert date fields to string if they are required as CharFields
                    date_of_issue = record.get('DATE_OF_ISSUE', '')
                    payment_date = record.get('PAYMENT_DATE', '')

                    Utility_Bill.objects.using('utility').create(
                        Customer_ID=record['CUSTOMER_ID'],
                        InvoiceNo=record['NO'],  # Mapping NO -> InvoiceNo
                        TypeOfPro=record['SUPPLY_TYPE'], 
                        Outstanding=record['OUTSTANDING'],
                        Basic_Tax=record['BASIC+TAX'],
                        Bill_Amount=record['BILL_AMOUNT'],
                        Debt_Amount=record['PAY_AMOUNT'],  # Mapping PAY_AMOUNT -> Debt_Amount
                        Payment_ID=record['PAYMENT_ID'],
                        PaymentType=record['PAY_TYPE'],
                        Payment_Date=payment_date,  # Payment_Date is a CharField
                        InvoiceMonth=record['BILL_OF_MONTH'],
                        InvoiceDate=date_of_issue,  # InvoiceDate is a CharField
                        DisID=record['DIS_ID'],
                        ProID=record['PRO_ID'],
                        UserID='unknown'  # Default UserID if not provided
                    )
                except KeyError as e:
                    return Response({'error': f'Missing key in record: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Data processed and saved successfully'}, status=status.HTTP_200_OK)

        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON file'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EnterpriseInfo

@csrf_exempt
def search_enterprise_view(request):
    EnterpriseID = request.POST.get('q', '')
    
    try:
        enterprise = EnterpriseInfo.objects.get(EnterpriseID=EnterpriseID)
        return JsonResponse({
            'status': 200,
            'enterprise_id': enterprise.EnterpriseID,
            'name': enterprise.enterpriseNameLao
        })
    except EnterpriseInfo.DoesNotExist:
        return JsonResponse({
            'status': 400,
            'message': 'ບໍ່ພົບຂໍ້ມູນ'
        })
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import EnterpriseInfo

@csrf_exempt
def search_enterprise_by_id(request, enterprise_id):
    if request.method == "POST":
        try:
            enterprise = EnterpriseInfo.objects.get(EnterpriseID=enterprise_id)
            return JsonResponse({'enterprise': enterprise.EnterpriseID}, status=200)
        except EnterpriseInfo.DoesNotExist:
            return JsonResponse({'error': 'Enterprise not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Utility_Bill
# import json
# from datetime import datetime
# import os

# class UtilityUploadView(APIView):
#     parser_classes = [MultiPartParser]

#     def post(self, request, *args, **kwargs):
#         file = request.FILES.get('file')
#         if not file:
#             return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             file_path = f"temp_uploads/{file.name}"
#             os.makedirs("temp_uploads", exist_ok=True)

#             # Save file temporarily
#             with open(file_path, 'wb+') as destination:
#                 for chunk in file.chunks():
#                     destination.write(chunk)

#             # Read the JSON file
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 json_data = json.load(f)

#             if json_data.get('status') != 200 or 'message' not in json_data:
#                 return Response({'error': 'Invalid JSON structure'}, status=status.HTTP_400_BAD_REQUEST)

#             # Process each record in the JSON file
#             for record in json_data['message']:
#                 Utility_Bill.objects.create(
#                     Customer_ID=record['CUSTOMER_ID'],
#                     InvoiceNo=record['NO'],
#                     TypeOfPro=record['SUPPLY_TYPE'],
#                     Outstanding=record['OUTSTANDING'],
#                     Basic_Tax=record['BASIC+TAX'],
#                     Bill_Amount=record['BILL_AMOUNT'],
#                     Debt_Amount=record['PAY_AMOUNT'],
#                     Payment_ID=record['PAYMENT_ID'],
#                     PaymentType=record['PAY_TYPE'],
#                     Payment_Date=datetime.strptime(record['PAYMENT_DATE'], '%d/%m/%Y').date(),
#                     InvoiceMonth=record['BILL_OF_MONTH'],
#                     InvoiceDate=datetime.strptime(record['DATE_OF_ISSUE'], '%d/%m/%Y').date(),
#                     DisID=record['DIS_ID'],
#                     ProID=record['PRO_ID'],
#                     UserID="unknown"
#                 )

#             # Delete temporary file after processing
#             os.remove(file_path)

#             return Response({'message': 'Data processed and saved successfully'}, status=status.HTTP_200_OK)

#         except json.JSONDecodeError:
#             return Response({'error': 'Invalid JSON file'}, status=status.HTTP_400_BAD_REQUEST)
#         except KeyError as e:
#             return Response({'error': f'Missing key in JSON data: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser
# from rest_framework.response import Response
# from rest_framework import status
# from utility.models import JsonfileWater
# from .tasks import process_json_file  # Celery task

# class JSONFileUploadView(APIView):
#     parser_classes = [MultiPartParser]

#     def post(self, request, *args, **kwargs):
#         file = request.FILES.get('file')
#         if not file:
#             return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

#         json_file = JsonfileWater.objects.using('utility').create(file=file)

#         # Trigger Celery task asynchronously
#         process_json_file.delay(json_file.id)

#         return Response({"message": "File uploaded successfully, processing started"}, status=status.HTTP_201_CREATED)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from utility.models import JsonfileWater, UploadJsonFiles
from utility.serializers import JsonfileWaterSerializer

class JsonFileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_obj = request.FILES.get('file_path')  # Get uploaded file

        if not file_obj:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        # Save file details
        json_file = UploadJsonFiles.objects.create(
            file_name=file_obj.name,
            file_path=file_obj,
            status='Pending'
        )

        serializer = JsonfileWaterSerializer(json_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        files = JsonfileWater.objects.all()
        serializer = JsonfileWaterSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utility.models import FileDetail, Utility_Bill, File_Electric, Electric_Bill
from .serializers import FileDetailSerializer
from django.http import Http404
from django.http import HttpResponse
import json
import os
from celery import shared_task
from django.conf import settings
from django.http import StreamingHttpResponse
import time
import threading

# backend/django_app/views.py
class FileUploadView(APIView):
    def get(self, request):
        files = FileDetail.objects.all()
        serializer = FileDetailSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request):
        file_obj = request.FILES.get('file_path')
        user_upload = request.data.get('user_upload', 'anonymous')
        
        if not file_obj or not file_obj.name.endswith('.json'):
            return Response(
                {'error': 'Please upload a valid JSON file'},
                status=status.HTTP_400_BAD_REQUEST
            )

        file_detail = FileDetail(
            name=file_obj.name,
            file_path=file_obj,
            status='Pending' 
        )
        file_detail.save()

        serializer = FileDetailSerializer(file_detail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Add PATCH method for status update
    def patch(self, request, pk):
        try:
            file = FileDetail.objects.get(pk=pk)
            serializer = FileDetailSerializer(file, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except FileDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk):
        try:
            file = FileDetail.objects.get(pk=pk)
            file.file_path.delete()  # Delete the file from storage
            file.delete()  # Delete the database record
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FileDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class FileDeleteView(APIView):
    def delete(self, request, pk):
        try:
            file = FileDetail.objects.get(pk=pk)
            file.file_path.delete()  # Delete the file from storage
            file.delete()  # Delete the database record
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FileDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# # backend/django_app/views.py
# class FileDetailView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 file = FileDetail.objects.get(pk=pk)
#                 serializer = FileDetailSerializer(file)
#                 return Response(serializer.data)
#             except FileDetail.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         files = FileDetail.objects.all()
#         serializer = FileDetailSerializer(files, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         file_obj = request.FILES.get('file_path')
#         user_upload = request.data.get('user_upload', 'anonymous')
        
#         if not file_obj or not file_obj.name.endswith('.json'):
#             return Response({'error': 'Please upload a valid JSON file'}, status=status.HTTP_400_BAD_REQUEST)

#         file_detail = FileDetail(name=file_obj.name, file_path=file_obj, status='Pending')
#         file_detail.save()
#         serializer = FileDetailSerializer(file_detail)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def patch(self, request, pk):
#         try:
#             file = FileDetail.objects.get(pk=pk)
#             serializer = FileDetailSerializer(file, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 print(f"File {pk} status updated to: {serializer.data['status']}")
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except FileDetail.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk):
#         try:
#             file = FileDetail.objects.get(pk=pk)
#             file.file_path.delete()
#             file.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except FileDetail.DoesNotExist:
#             return Response(status=status.HTTP_204_NO_CONTENT)
        
# def truncate(value, max_length):
#     return str(value)[:max_length] if value else ''
# def progress_view(request, pk):
#     try:
#         file = FileDetail.objects.get(pk=pk)
#         if file.status != 'Approved':
#             print(f"File {pk} not approved, returning 0 progress")
#             return HttpResponse(json.dumps({'progress': 0, 'total': 0}), content_type='application/json', status=200)

#         file_path = os.path.join(settings.MEDIA_ROOT, file.file_path.name)
#         print(f"Opening file: {file_path}")
#         with open(file_path, 'r') as f:
#             data = json.load(f)
        
#         records = data.get('message', [])
#         total_items = len(records)
#         processed_items = file.processed_items
#         print(f"Total items: {total_items}, Processed items: {processed_items}")

#         if processed_items < total_items:
#             batch_size = 1000
#             print(f"Processing batch from {processed_items} to {min(processed_items + batch_size, total_items)}")
#             batch = []
#             for i, item in enumerate(records[processed_items:processed_items + batch_size], start=processed_items + 1):
#                 payment_id = item.get('PAYMENT_ID', '')  # No truncate for Payment_ID
#                 print(f"Adding record {i} with Payment_ID: {payment_id}")
#                 batch.append(Utility_Bill(
#                     Customer_ID=truncate(item.get('CUSTOMER_ID', ''), 100),
#                     InvoiceNo=truncate(item.get('PAYMENT_ID', ''), 100),
#                     TypeOfPro=truncate(item.get('SUPPLY_TYPE', ''), 100),
#                     Outstanding=item.get('OUTSTANDING', 0.00),
#                     Basic_Tax=item.get('BASIC+TAX', 0.00),
#                     Bill_Amount=item.get('BILL_AMOUNT', 0.00),
#                     Debt_Amount=0.00,
#                     Payment_ID=payment_id,  # Full value, no truncation
#                     PaymentType=truncate(item.get('PAY_TYPE', ''), 255),
#                     Payment_Date=truncate(item.get('PAYMENT_DATE', ''), 255),
#                     InvoiceMonth=truncate(item.get('BILL_OF_MONTH', ''), 50),
#                     InvoiceDate=truncate(item.get('DATE_OF_ISSUE', ''), 100),
#                     DisID=truncate(item.get('DIS_ID', ''), 100),
#                     ProID=truncate(item.get('PRO_ID', ''), 100),
#                     UserID=None
#                 ))
#             if batch:
#                 try:
#                     print(f"Attempting to bulk create {len(batch)} records")
#                     Utility_Bill.objects.bulk_create(batch)
#                     file.processed_items += len(batch)
#                     file.save()
#                     print(f"Processed {file.processed_items}/{total_items}")
#                 except Exception as e:
#                     print(f"Bulk create failed at {processed_items}: {str(e)}")
#                     return HttpResponse(
#                         json.dumps({'error': f"Bulk create failed: {str(e)}"}),
#                         content_type='application/json',
#                         status=500
#                     )

#         progress = (file.processed_items / total_items) * 100 if total_items > 0 else 0
#         print(f"Progress view: {file.processed_items}/{total_items} = {progress}%")
#         return HttpResponse(
#             json.dumps({'progress': progress, 'total': total_items}),
#             content_type='application/json',
#             status=200
#         )
#     except FileDetail.DoesNotExist:
#         return HttpResponse(
#             json.dumps({'error': 'File not found'}),
#             content_type='application/json',
#             status=404
#         )
#     except Exception as e:
#         print(f"Error in progress view for file {pk}: {str(e)}")
#         return HttpResponse(
#             json.dumps({'error': str(e)}),
#             content_type='application/json',
#             status=500
#         )

class FileDetailView(APIView):
    # def get(self, request, pk=None):
    #     if pk:
    #         try:
    #             file = FileDetail.objects.get(pk=pk)
    #             serializer = FileDetailSerializer(file)
    #             return Response(serializer.data)
    #         except FileDetail.DoesNotExist:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #     files = FileDetail.objects.all()
    #     serializer = FileDetailSerializer(files, many=True)
    #     return Response(serializer.data)
    def get(self, request, pk=None):
        # If a PK is provided, just return that single object
        if pk is not None:
            try:
                file = FileDetail.objects.get(pk=pk)
            except FileDetail.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = FileDetail(file)
            return Response(serializer.data)

        # Otherwise, build a queryset and apply filters
        qs = FileDetail.objects.all()

        # 1) filter by name substring (case‐insensitive)
        name = request.GET.get("name")
        if name:
            qs = qs.filter(name__icontains=name)

        # 2) filter by exact status
        status_param = request.GET.get("status")
        if status_param:
            qs = qs.filter(status=status_param)

        # 3) filter by the YYYYMM chunk in the filename
        date = request.GET.get("date")  # e.g. "202503"
        if date:
            # matches any name containing "-YYYYMM"
            qs = qs.filter(name__contains=f"-{date}")

        serializer = FileDetailSerializer(qs, many=True)
        return Response(serializer.data)


    def post(self, request):
        file_obj = request.FILES.get('file_path')
        user_upload = request.data.get('user_upload', 'anonymous')
        
        if not file_obj or not file_obj.name.endswith('.json'):
            return Response({'error': 'Please upload a valid JSON file'}, status=status.HTTP_400_BAD_REQUEST)

        file_detail = FileDetail(name=file_obj.name, file_path=file_obj, status='Pending')
        file_detail.save()
        serializer = FileDetailSerializer(file_detail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        try:
            file = FileDetail.objects.get(pk=pk)
            serializer = FileDetailSerializer(file, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                print(f"Water File {pk} status updated to: {serializer.data['status']}")
                if serializer.data['status'] == 'Approved':
                    print(f"Starting background processing for water file {pk}")
                    threading.Thread(target=process_water_file, args=(pk,), daemon=True).start()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except FileDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            file = FileDetail.objects.get(pk=pk)
            file.file_path.delete()
            file.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FileDetail.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

class FileElectricView(APIView):
    # def get(self, request, pk=None):
    #     if pk:
    #         try:
    #             file = File_Electric.objects.get(pk=pk)
    #             serializer = FileDetailSerializer(file)
    #             return Response(serializer.data)
    #         except File_Electric.DoesNotExist:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #     files = File_Electric.objects.all()
    #     serializer = FileDetailSerializer(files, many=True)
    #     return Response(serializer.data)
    def get(self, request, pk=None):
        # If a PK is provided, just return that single object
        if pk is not None:
            try:
                file = File_Electric.objects.get(pk=pk)
            except File_Electric.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = FileElectricSerializer(file)
            return Response(serializer.data)

        # Otherwise, build a queryset and apply filters
        qs = File_Electric.objects.all()

        # 1) filter by name substring (case‐insensitive)
        name = request.GET.get("name")
        if name:
            qs = qs.filter(name__icontains=name)

        # 2) filter by exact status
        status_param = request.GET.get("status")
        if status_param:
            qs = qs.filter(status=status_param)

        # 3) filter by the YYYYMM chunk in the filename
        date = request.GET.get("date")  # e.g. "202503"
        if date:
            # matches any name containing "-YYYYMM"
            qs = qs.filter(name__contains=f"-{date}")

        serializer = FileElectricSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        file_obj = request.FILES.get('file_path')
        user_upload = request.data.get('user_upload', 'anonymous')
        
        if not file_obj or not file_obj.name.endswith('.json'):
            return Response({'error': 'Please upload a valid JSON file'}, status=status.HTTP_400_BAD_REQUEST)

        file_electric = File_Electric(name=file_obj.name, file_path=file_obj, status='Pending')
        file_electric.save()
        serializer = FileDetailSerializer(file_electric)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        try:
            file = File_Electric.objects.get(pk=pk)
            serializer = FileDetailSerializer(file, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                print(f"Electric File {pk} status updated to: {serializer.data['status']}")
                if serializer.data['status'] == 'Approved':
                    print(f"Starting background processing for electric file {pk}")
                    threading.Thread(target=process_electric_file, args=(pk,), daemon=True).start()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except File_Electric.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            file = File_Electric.objects.get(pk=pk)
            file.file_path.delete()
            file.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except File_Electric.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

def truncate(value, max_length):
    return str(value)[:max_length] if value else ''

def process_water_file(file_id):
    try:
        file = FileDetail.objects.get(pk=file_id)
        file_path = os.path.join(settings.MEDIA_ROOT, file.file_path.name)
        print(f"Water background thread opening file: {file_path}")
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        records = data.get('message', [])
        total_items = len(records)
        processed_items = file.processed_items

        batch = []
        for i, item in enumerate(records[processed_items:], start=processed_items + 1):
            payment_id = item.get('PAYMENT_ID', '')
            print(f"Water background thread adding record {i} with Payment_ID: {payment_id}")
            batch.append(Utility_Bill(
                Customer_ID=truncate(item.get('CUSTOMER_ID', ''), 100),
                InvoiceNo=truncate(item.get('NO', ''), 100),
                TypeOfPro=truncate(item.get('SUPPLY_TYPE', ''), 100),
                Outstanding=item.get('OUTSTANDING', 0.00),
                Basic_Tax=item.get('BASIC+TAX', 0.00),
                Bill_Amount=item.get('BILL_AMOUNT', 0.00),
                Debt_Amount=0.00,
                Payment_ID=payment_id,
                PaymentType=truncate(item.get('PAY_TYPE', ''), 255),
                Payment_Date=truncate(item.get('PAYMENT_DATE', ''), 255),
                InvoiceMonth=truncate(item.get('BILL_OF_MONTH', ''), 50),
                InvoiceDate=truncate(item.get('DATE_OF_ISSUE', ''), 100),
                DisID=truncate(item.get('DIS_ID', ''), 100),
                ProID=truncate(item.get('PRO_ID', ''), 100),
                UserID=None
            ))
            if len(batch) >= 1000:
                Utility_Bill.objects.bulk_create(batch)
                file.processed_items += len(batch)
                file.save()
                print(f"Water background thread processed {file.processed_items}/{total_items}")
                batch = []
        if batch:
            Utility_Bill.objects.bulk_create(batch)
            file.processed_items += len(batch)
            file.save()
            print(f"Water background thread processed {file.processed_items}/{total_items} - Completed")
    except Exception as e:
        print(f"Error in water background thread for file {file_id}: {str(e)}")

def process_electric_file(file_id):
    try:
        file = File_Electric.objects.get(pk=file_id)
        file_path = os.path.join(settings.MEDIA_ROOT, file.file_path.name)
        print(f"Electric background thread opening file: {file_path}")
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Updated to match electric-bill.json structure
        records = data.get('data', {}).get('paymentHistory', [])
        total_items = len(records)
        processed_items = file.processed_items

        batch = []
        for i, item in enumerate(records[processed_items:], start=processed_items + 1):
            payment_id = item.get('PAYMENT_ID', '')
            print(f"Electric background thread adding record {i} with Payment_ID: {payment_id}")
            batch.append(Electric_Bill(
                Customer_ID=truncate(item.get('MASTER_BILL_ID', ''), 255),
                InvoiceNo=truncate(item.get('INDEX_NO', ''), 255),
                TypeOfPro=truncate(item.get('SUPPLY_TYPE', ''), 100),
                Outstanding=item.get('OUTSTANDING', 0.00),
                Basic_Tax=item.get('FACT_TOTAL', 0.00),
                Bill_Amount=item.get('BILL_AMOUNT', 0.00),
                Debt_Amount=0.00,
                Payment_ID=payment_id,
                PaymentType=item.get('PAYMENT_WAY', ''),
                Payment_Date=item.get('PAYMENTDAY', ''),
                InvoiceMonth=truncate(item.get('INVM', ''), 50),
                InvoiceDate=truncate(item.get('INVD', ''), 100),
                DisID=truncate(item.get('DIS_ID', ''), 100),
                ProID=truncate(item.get('PROVINCE_CODE', ''), 100),
                UserID=None
            ))
            if len(batch) >= 1000:
                Electric_Bill.objects.bulk_create(batch)
                file.processed_items += len(batch)
                file.save()
                print(f"Electric background thread processed {file.processed_items}/{total_items}")
                batch = []
        if batch:
            Electric_Bill.objects.bulk_create(batch)
            file.processed_items += len(batch)
            file.save()
            print(f"Electric background thread processed {file.processed_items}/{total_items} - Completed")
    except Exception as e:
        print(f"Error in electric background thread for file {file_id}: {str(e)}")

def water_progress_view(request, pk):
    try:
        file = FileDetail.objects.get(pk=pk)
        if file.status != 'Approved':
            print(f"Water File {pk} not approved, returning 0 progress")
            return HttpResponse(json.dumps({'progress': 0, 'total': 0, 'completed': False}), content_type='application/json', status=200)

        file_path = os.path.join(settings.MEDIA_ROOT, file.file_path.name)
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        records = data.get('message', [])
        total_items = len(records)
        processed_items = file.processed_items

        progress = (processed_items / total_items) * 100 if total_items > 0 else 0
        completed = processed_items >= total_items
        print(f"Water Progress view: {processed_items}/{total_items} = {progress}%{' - Completed' if completed else ''}")
        return HttpResponse(
            json.dumps({'progress': progress, 'total': total_items, 'completed': completed}),
            content_type='application/json',
            status=200
        )
    except FileDetail.DoesNotExist:
        return HttpResponse(
            json.dumps({'error': 'File not found'}),
            content_type='application/json',
            status=404
        )
    except Exception as e:
        print(f"Error in water progress view for file {pk}: {str(e)}")
        return HttpResponse(
            json.dumps({'error': str(e)}),
            content_type='application/json',
            status=500
        )

def electric_progress_view(request, pk):
    try:
        file = File_Electric.objects.get(pk=pk)
        if file.status != 'Approved':
            print(f"Electric File {pk} not approved, returning 0 progress")
            return HttpResponse(json.dumps({'progress': 0, 'total': 0, 'completed': False}), content_type='application/json', status=200)

        file_path = os.path.join(settings.MEDIA_ROOT, file.file_path.name)
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Updated to match electric-bill.json structure
        records = data.get('data', {}).get('paymentHistory', [])
        total_items = len(records)
        processed_items = file.processed_items

        progress = (processed_items / total_items) * 100 if total_items > 0 else 0
        completed = processed_items >= total_items
        print(f"Electric Progress view: {processed_items}/{total_items} = {progress}%{' - Completed' if completed else ''}")
        return HttpResponse(
            json.dumps({'progress': progress, 'total': total_items, 'completed': completed}),
            content_type='application/json',
            status=200
        )
    except File_Electric.DoesNotExist:
        return HttpResponse(
            json.dumps({'error': 'File not found'}),
            content_type='application/json',
            status=404
        )
    except Exception as e:
        print(f"Error in electric progress view for file {pk}: {str(e)}")
        return HttpResponse(
            json.dumps({'error': str(e)}),
            content_type='application/json',
            status=500
        )
        
        
        
from utility.models import w_customer_info, Utility_Bill, searchlog_utility, request_charge_utility
from .serializers import WaterCustomerSerializer, UtilityBillSerializer, SearchLogUtilitySerializer
import uuid
import re
import logging
from datetime import datetime
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)


class SafeUtilityBillSerializer(UtilityBillSerializer):
    """Custom serializer that safely handles problematic date fields"""
    
    def to_representation(self, instance):
        try:
            # Get the original representation
            data = super().to_representation(instance)
            
            # List of date fields that might have year 1 issues
            problematic_date_fields = ['created_at', 'updated_at', 'created', 'modified']
            
            for field_name in problematic_date_fields:
                if field_name in data:
                    try:
                        field_value = getattr(instance, field_name, None)
                        if field_value and hasattr(field_value, 'year'):
                            # Check for problematic years (year 1, year 0, negative years)
                            if field_value.year <= 1900:
                                data[field_name] = None  # Set problematic dates to None
                            else:
                                data[field_name] = field_value.isoformat() if hasattr(field_value, 'isoformat') else str(field_value)
                    except Exception as e:
                        logger.warning(f"Error processing date field {field_name}: {str(e)}")
                        data[field_name] = None
            
            return data
            
        except Exception as e:
            logger.error(f"Error in SafeUtilityBillSerializer: {str(e)}")
            # Return basic bill data even if serialization fails
            return {
                'id': getattr(instance, 'id', None),
                'Customer_ID': getattr(instance, 'Customer_ID', None),
                'InvoiceMonth': getattr(instance, 'InvoiceMonth', None),
                'Total_amount': getattr(instance, 'Total_amount', 0),
                'Water_rate': getattr(instance, 'Water_rate', 0),
                'Service_charge': getattr(instance, 'Service_charge', 0),
                'Paid_amount': getattr(instance, 'Paid_amount', 0)
            }

class UtilityReportAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def serialize_bills_safely(self, bills):
        """Serialize bills one by one, skipping any that fail"""
        serialized_bills = []
        
        for bill in bills:
            try:
                # Try normal serialization first
                serializer = UtilityBillSerializer(bill)
                bill_data = serializer.data
                serialized_bills.append(bill_data)
                
            except Exception as e:
                # If normal serialization fails, create manual safe data
                logger.warning(f"Serialization failed for bill {bill.BillID}: {str(e)}")
                
                # Create safe manual data without problematic fields
                safe_bill_data = {
                    'BillID': bill.BillID,
                    'Customer_ID': bill.Customer_ID,
                    'InvoiceNo': bill.InvoiceNo or '',
                    'TypeOfPro': bill.TypeOfPro or '',
                    'Outstanding': float(bill.Outstanding or 0),
                    'Basic_Tax': float(bill.Basic_Tax or 0),
                    'Bill_Amount': float(bill.Bill_Amount or 0),
                    'Debt_Amount': float(bill.Debt_Amount or 0),
                    'Payment_ID': bill.Payment_ID or '',
                    'PaymentType': bill.PaymentType or '',
                    'Payment_Date': bill.Payment_Date or '',
                    'InvoiceMonth': bill.InvoiceMonth or '',
                    'InvoiceDate': bill.InvoiceDate or '',
                    'DisID': bill.DisID or '',
                    'ProID': bill.ProID or '',
                    'UserID': bill.UserID or '',
                    # Skip InsertDate and UpdateDate - these cause the error
                    'InsertDate': None,  
                    'UpdateDate': None
                }
                serialized_bills.append(safe_bill_data)
        
        return serialized_bills

    def get(self, request):
        try:
            # Input validation
            customer_id = request.query_params.get('water')
            if not customer_id:
                return Response({"error": "water parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

            user = request.user
            bank = user.MID
            sys_usr = f"{str(user.UID)}-{str(bank.bnk_code)}"

            # Get bank info
            bank_info = memberInfo.objects.get(bnk_code=bank.bnk_code)
            charge_bank_type = bank_info.bnk_type
            if charge_bank_type == 1:
                chargeType = ChargeMatrix.objects.get(chg_sys_id=9)
            else:
                chargeType = ChargeMatrix.objects.get(chg_sys_id=10)
            charge_amount_com = chargeType.chg_amount

            # Get customer
            customer = w_customer_info.objects.get(Customer_ID=customer_id)

            # Get bills - focus only on InvoiceMonth validation (which is fine)
            bills = Utility_Bill.objects.filter(Customer_ID=customer_id).exclude(
                InvoiceMonth__isnull=True
            ).exclude(
                InvoiceMonth=""
            )

            # Sort by InvoiceMonth manually (since your format is MM-YYYY)
            bills_list = list(bills)
            def sort_key(bill):
                try:
                    invoice_month = bill.InvoiceMonth
                    if invoice_month and re.match(r'^(0[1-9]|1[0-2])-(\d{4})$', invoice_month):
                        month, year = invoice_month.split('-')
                        return f"{year}-{month.zfill(2)}"
                    return "0000-00"  # Put invalid dates at the end
                except:
                    return "0000-00"
            
            bills_list.sort(key=sort_key, reverse=True)  # Most recent first

            # Log the search
            search_log = searchlog_utility.objects.create(
                bnk_code=bank.bnk_code,
                sys_usr=sys_usr,
                wt_cusid=customer_id,
                edl_cusid='',
                tel_cusid='',
                proID_edl='',
                proID_wt='',
                proID_tel='',
                credittype='water',
                inquiry_date=timezone.now(),
                inquiry_time=timezone.now()
            )

            # Get current timestamp for rec_insert_date
            rec_insert_date = timezone.now()
            date_str = rec_insert_date.strftime('%d%m%Y')
            report_date = rec_insert_date.strftime('%d-%m-%Y')
            rec_reference_code = f"{chargeType.chg_code}-0-{bank.bnk_code}-{date_str}-{search_log.search_id}"
            rec_reference_code = rec_reference_code[:100]

            # Log the charge request
            request_charge_utility.objects.create(
                usr_session_id=str(uuid.uuid4()),
                search_id=search_log,
                bnk_code=bank.bnk_code,
                chg_code=chargeType.chg_code,
                chg_amount=charge_amount_com,
                chg_unit='LAK',
                sys_usr=sys_usr,
                credit_type='water',
                wt_cusid=customer_id,
                edl_cusid='',
                tel_cusid='',
                proID_edl='',
                proID_wt='',
                proID_tel='',
                rec_reference_code=rec_reference_code
            )

            # Serialize safely
            customer_serializer = WaterCustomerSerializer(customer)
            bill_data = self.serialize_bills_safely(bills_list)
            search_log_serializer = SearchLogUtilitySerializer(search_log)

            # Construct reference_data
            reference_data = [
                rec_reference_code,
                customer_id,
                report_date,
                search_log_serializer.data,
                rec_insert_date.isoformat()
            ]

            logger.info(f"Successfully returning {len(bill_data)} bills for customer {customer_id}")

            return Response({
                "reference_data": reference_data,
                "customer": [customer_serializer.data],
                "bill": bill_data
            }, status=status.HTTP_200_OK)

        except w_customer_info.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        except memberInfo.DoesNotExist:
            return Response({"error": "Bank information not found"}, status=status.HTTP_400_BAD_REQUEST)
        except ChargeMatrix.DoesNotExist:
            return Response({"error": "Charge configuration not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Optional: Database cleanup function to fix the year 1 dates
def fix_problematic_dates():
    """
    Run this to fix the problematic InsertDate and UpdateDate fields
    WARNING: This will update database records
    """
    from django.utils import timezone
    
    current_time = timezone.now()
    
    # Fix bills with year 1 dates - using your actual model field names
    problematic_bills = Utility_Bill.objects.filter(
        Q(InsertDate__year=1) | Q(UpdateDate__year=1)
    )
    
    count = 0
    total_bills = problematic_bills.count()
    print(f"Found {total_bills} bills with problematic dates")
    
    for bill in problematic_bills:
        try:
            updated = False
            if hasattr(bill, 'InsertDate') and bill.InsertDate and bill.InsertDate.year == 1:
                bill.InsertDate = current_time
                updated = True
                print(f"Fixed InsertDate for bill {bill.BillID}")
            
            if hasattr(bill, 'UpdateDate') and bill.UpdateDate and bill.UpdateDate.year == 1:
                bill.UpdateDate = current_time
                updated = True
                print(f"Fixed UpdateDate for bill {bill.BillID}")
            
            if updated:
                bill.save(update_fields=['InsertDate', 'UpdateDate'])
                count += 1
                
        except Exception as e:
            logger.error(f"Error fixing bill {bill.BillID}: {e}")
            print(f"Error fixing bill {bill.BillID}: {e}")
    
    print(f"Successfully fixed {count} bills with problematic dates")
    return count

# from utility.models import w_customer_info, Utility_Bill, searchlog_utility, request_charge_utility
# from .serializers import WaterCustomerSerializer, UtilityBillSerializer, SearchLogUtilitySerializer
# import uuid
# from django.db.models import Func, F, Value

# class UtilityReportAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         try:
#             customer_id = request.query_params.get('water')
#             if not customer_id:
#                 return Response({"error": "water parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

#             user = request.user
#             bank = user.MID
#             sys_usr = f"{str(user.UID)}-{str(bank.bnk_code)}"

#             bank_info = memberInfo.objects.get(bnk_code=bank.bnk_code)
#             charge_bank_type = bank_info.bnk_type
#             if charge_bank_type == 1:
#                 chargeType = ChargeMatrix.objects.get(chg_sys_id=9)
#             else:
#                 chargeType = ChargeMatrix.objects.get(chg_sys_id=10)
#             charge_amount_com = chargeType.chg_amount

#             customer = w_customer_info.objects.get(Customer_ID=customer_id)

#             # Custom function to convert MM-YYYY to YYYY-MM for sorting (PostgreSQL)
#             class ReorderMonthYear(Func):
#                 function = "TO_CHAR"
#                 template = (
#                     "CASE WHEN LENGTH(%(expressions)s) = 7 THEN "
#                     "SUBSTRING(%(expressions)s FROM 4 FOR 4) || '-' || SUBSTRING(%(expressions)s FROM 1 FOR 2) "
#                     "ELSE NULL END"
#                 )

#             # Filter and validate bills
#             bills = Utility_Bill.objects.filter(Customer_ID=customer_id).exclude(
#                 InvoiceMonth__isnull=True
#             ).exclude(
#                 InvoiceMonth=""
#             ).annotate(
#                 year_month=ReorderMonthYear(F('InvoiceMonth'))
#             ).order_by('-year_month')

#             # Log the search
#             search_log = searchlog_utility.objects.create(
#                 bnk_code=bank.bnk_code,
#                 sys_usr=sys_usr,
#                 wt_cusid=customer_id,
#                 edl_cusid='',
#                 tel_cusid='',
#                 proID_edl='',
#                 proID_wt='',
#                 proID_tel='',
#                 credittype='water',
#                 inquiry_date=timezone.now(),
#                 inquiry_time=timezone.now()
#             )

#             # Get current timestamp for rec_insert_date
#             rec_insert_date = timezone.now()
#             date_str = rec_insert_date.strftime('%d%m%Y')
#             report_date = rec_insert_date.strftime('%d-%m-%Y')
#             rec_reference_code = f"{chargeType.chg_code}-0-{bank.bnk_code}-{date_str}-{search_log.search_id}"
#             rec_reference_code = rec_reference_code[:100]

#             # Log the charge request
#             request_charge_utility.objects.create(
#                 usr_session_id=str(uuid.uuid4()),
#                 search_id=search_log,
#                 bnk_code=bank.bnk_code,
#                 chg_code=chargeType.chg_code,
#                 chg_amount=charge_amount_com,
#                 chg_unit='LAK',
#                 sys_usr=sys_usr,
#                 credit_type='water',
#                 wt_cusid=customer_id,
#                 edl_cusid='',
#                 tel_cusid='',
#                 proID_edl='',
#                 proID_wt='',
#                 proID_tel='',
#                 rec_reference_code=rec_reference_code
#             )

#             customer_serializer = WaterCustomerSerializer(customer)
#             bill_serializer = UtilityBillSerializer(bills, many=True)
#             search_log_serializer = SearchLogUtilitySerializer(search_log)

#             # Construct reference_data as a tuple
#             reference_data = (
#                 rec_reference_code,
#                 customer_id,
#                 report_date,
#                 search_log_serializer.data,
#                 rec_insert_date.isoformat()
#             )

#             # Return response with reference_data as a list (JSON-compatible)
#             return Response({
#                 "reference_data": reference_data,
#                 "customer": [customer_serializer.data],
#                 "bill": bill_serializer.data
#             }, status=status.HTTP_200_OK)

#         except w_customer_info.DoesNotExist:
#             return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
#         except memberInfo.DoesNotExist:
#             return Response({"error": "Bank information not found"}, status=status.HTTP_400_BAD_REQUEST)
#         except ChargeMatrix.DoesNotExist:
#             return Response({"error": "Charge configuration not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
      
from utility.models import edl_customer_info, Electric_Bill, searchlog_utility, request_charge_utility
from .serializers import EDLCustomerSerializer, ElectricBillSerializer, SearchLogUtilitySerializer
import uuid
from django.db.models import Func, F, Value

class ElectricReportAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            customer_id = request.query_params.get('edl')
            if not customer_id:
                return Response({"error": "water parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

            user = request.user
            bank = user.MID
            sys_usr = f"{str(user.UID)}-{str(bank.bnk_code)}"

            bank_info = memberInfo.objects.get(bnk_code=bank.bnk_code)
            charge_bank_type = bank_info.bnk_type
            if charge_bank_type == 1:
                chargeType = ChargeMatrix.objects.get(chg_sys_id=9)
            else:
                chargeType = ChargeMatrix.objects.get(chg_sys_id=10)
            charge_amount_com = chargeType.chg_amount

            customer = edl_customer_info.objects.get(Customer_ID=customer_id)

            # edl = edl_customer_info.objects.get(Customer_ID=customer_id)
            # Custom function to convert MM-YYYY to YYYY-MM for sorting (PostgreSQL)
            class ReorderMonthYear(Func):
                function = "TO_CHAR"
                template = "SUBSTRING(%(expressions)s FROM 4 FOR 4) || '-' || SUBSTRING(%(expressions)s FROM 1 FOR 2)"

            # Sort bills by InvoiceMonth in descending order
            bills = Electric_Bill.objects.filter(Customer_ID=customer_id).annotate(
                year_month=ReorderMonthYear(F('InvoiceMonth'))
            ).order_by('-year_month')

            # edl_bill = Electric_Bill.objects.filter(Customer_ID=customer_id_2).annotate(
            #     year_month=ReorderMonthYear(F('InvoiceMonth'))
            # ).order_by('-year_month')
            
            # Log the search
            search_log = searchlog_utility.objects.create(
                bnk_code=bank.bnk_code,
                sys_usr=sys_usr,
                wt_cusid=customer_id,
                edl_cusid='',
                tel_cusid='',
                proID_edl='',
                proID_wt='',
                proID_tel='',
                credittype='edl',
                inquiry_date=timezone.now(),
                inquiry_time=timezone.now()
            )

            # Get current timestamp for rec_insert_date
            rec_insert_date = timezone.now()
            date_str = rec_insert_date.strftime('%d%m%Y')
            report_date = rec_insert_date.strftime('%d-%m-%Y')
            rec_reference_code = f"{chargeType.chg_code}-0-{bank.bnk_code}-{date_str}-{search_log.search_id}"
            rec_reference_code = rec_reference_code[:100]

            # Log the charge request
            request_charge_utility.objects.create(
                usr_session_id=str(uuid.uuid4()),
                search_id=search_log,
                bnk_code=bank.bnk_code,
                chg_code=chargeType.chg_code,
                chg_amount=charge_amount_com,
                chg_unit='LAK',
                sys_usr=sys_usr,
                credit_type='edl',
                wt_cusid=customer_id,
                edl_cusid='',
                tel_cusid='',
                proID_edl='',
                proID_wt='',
                proID_tel='',
                rec_reference_code=rec_reference_code
            )

            customer_serializer = EDLCustomerSerializer(customer)
            bill_serializer = ElectricBillSerializer(bills, many=True)
            search_log_serializer = SearchLogUtilitySerializer(search_log)

            # Construct reference_data as a tuple
            reference_data = (
                rec_reference_code,
                customer_id,
                report_date,
                search_log_serializer.data,  # Serialized search_log
                rec_insert_date.isoformat()  # Convert datetime to ISO string
            )

            # Return response with reference_data as a list (JSON-compatible)
            return Response({
                "reference_data": reference_data,
                "customer": [customer_serializer.data],
                "bill": bill_serializer.data
            }, status=status.HTTP_200_OK)

        except w_customer_info.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        except memberInfo.DoesNotExist:
            return Response({"error": "Bank information not found"}, status=status.HTTP_400_BAD_REQUEST)
        except ChargeMatrix.DoesNotExist:
            return Response({"error": "Charge configuration not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
from .models import ChargeMatrix
from .serializers import ChargeMatrixSerializer

class ChargeMatrixViewSet(viewsets.ModelViewSet):
    queryset = ChargeMatrix.objects.all()
    serializer_class = ChargeMatrixSerializer
# class CreditReportAPIView(APIView):
#     def get(self, request, customer_id=None):
#         try:
#             # If no customer_id provided in URL, check query params
#             if not customer_id:
#                 customer_id = request.query_params.get('customer_id')
            
#             if not customer_id:
#                 return Response(
#                     {"error": "Customer_ID is required"},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # Get customer data
#             try:
#                 customer = w_customer_info.objects.get(Customer_ID=customer_id)
#                 customer_serializer = WaterCustomerSerializer(customer)
#             except w_customer_info.DoesNotExist:
#                 return Response(
#                     {"error": "Customer not found"},
#                     status=status.HTTP_404_NOT_FOUND
#                 )

#             # Get bills for the customer, ordered by InvoiceMonth descending
#             bills = Utility_Bill.objects.filter(
#                 Customer_ID=customer_id
#             ).order_by('-InvoiceMonth')
            
#             bill_serializer = UtilityBillSerializer(bills, many=True)

#             # Construct the response
#             response_data = {
#                 "customer": [customer_serializer.data],  # Array with single customer
#                 "bill": bill_serializer.data            # Array of bills
#             }

#             return Response(response_data, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response(
#                 {"error": str(e)},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )        
#             )       

class EDLProvinceAPIView(APIView):
    def get(self, request):
        try:
            provinces = edl_province_code.objects.all()
            serializer = ProvinceSerializer(provinces, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EDLProvinceDetailAPIView(APIView):
    def get(self, request):
        try:
            # Get all provinces and districts
            provinces = edl_province_code.objects.all()
            districts = edl_district_code.objects.all()

            # Manual join (Python-side join)
            result = []
            for province in provinces:
                matching_districts = [d for d in districts if d.pro_id == province.pro_id]
                for district in matching_districts:
                    result.append({
                        'pro_id': province.pro_id,
                        'pro_name': province.pro_name,
                        'dis_id': district.dis_id,
                        'dis_name': district.dis_name
                    })

            # Sort result if needed
            result.sort(key=lambda x: (x['pro_id'], x['dis_id']))

            serializer = ProvinceDistrictSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProvinceDistrictAPIView(APIView):
    def get(self, request, pro_id=None):
        try:
            # Get the province
            province = edl_province_code.objects.get(pro_id=pro_id)
            
            # Get all districts for this province
            districts = edl_district_code.objects.filter(pro_id=pro_id)
            
            # Serialize the data
            province_serializer = ProvinceSerializer(province)
            districts_serializer = DistrictSerializer(districts, many=True)
            
            # Combine the response
            response_data = {
                'province': province_serializer.data,
                'districts': districts_serializer.data
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except edl_province_code.DoesNotExist:
            return Response(
                {'error': f'Province with pro_id {pro_id} not found'},
                status=status.HTTP_404_NOT_FOUND
            )
            
            
# class EDLUploaded_DetailView(APIView):  
#     def post(self, request, pro_id=None):
#         try:
            
#             return Response(, status=status.HTTP_200_OK)
            
#         except edl_province_code.DoesNotExist:
#             return Response(
#                 {'error': f'Province with pro_id {pro_id} not found'},
#                 status=status.HTTP_404_NOT_FOUND
#             )
        
    
    
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LCICSystemUser
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist

# Import the custom token generation function
from .utils import get_tokens_for_user  # Adjust the import path if needed

class SysUserLogin(APIView):
    def post(self, request):
        try:
            # Extract username and password from request
            username = request.data.get('username')
            password = request.data.get('password')

            print(f"Username: {username}, Password: {password}")
            
            # Validate input
            if not username or not password:
                return Response(
                    {'error': 'Username and password are required'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Query the LCICSystemUser model for the user
            try:
                user = LCICSystemUser.objects.get(username=username)
            except ObjectDoesNotExist:
                return Response(
                    {'error': 'Invalid credentials'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Verify password
            if not check_password(password, user.password):
                return Response(
                    {'error': 'Invalid credentials'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Check if the user is active
            if not user.is_active:
                return Response(
                    {'error': 'Account is deactivated'},
                    status=status.HTTP_403_FORBIDDEN
                )

            # Update last login timestamp
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])

            # Generate JWT tokens using the custom function
            try:
                tokens = get_tokens_for_user(user)
            except Exception as token_error:
                print(f"Token generation error: {str(token_error)}")
                return Response(
                    {
                        'error': 'Failed to generate token',
                        'details': str(token_error)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            # Prepare user data for response
            user_data = {
                'id': user.id,
                'username': user.username,
                'bnk_code': user.bnk_code,
                'branch_code': user.branch_code,
                'roles': user.roles,
                'nameL': user.nameL,
                'nameE': user.nameE,
                'surnameL': user.surnameL,
                'surnameE': user.surnameE,
                'profile_image_url': user.profile_image.url if user.profile_image else None,
                'last_login': user.last_login,
                'insertDate': user.insertDate,
                'updateDate': user.updateDate,
                'is_active': user.is_active,
            }

            return Response({
                'message': 'Login successful',
                'user': user_data,
                'tokens': tokens
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Login error: {str(e)}")
            return Response(
                {
                    'error': 'An unexpected error occurred',
                    'details': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
# Optional: Add a token refresh view
from rest_framework_simplejwt.views import TokenRefreshView

class SysUserTokenRefresh(TokenRefreshView):
    pass
            
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import LCICSystemUser  # Assuming LCICSystemUser is in models.py

class AddLCICSystemUser(APIView):
    def post(self, request):
        try:
            # Extract required fields from request data
            required_fields = [
                'bnk_code', 'branch_code', 'username', 'password', 'roles',
                'nameL', 'nameE', 'surnameL', 'surnameE'
            ]
            
            # Check if all required fields are present
            missing_fields = [field for field in required_fields if field not in request.data]
            if missing_fields:
                return Response(
                    {'error': f'Missing required fields: {", ".join(missing_fields)}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Check if username already exists
            if LCICSystemUser.objects.filter(username=request.data['username']).exists():
                return Response(
                    {'error': 'Username already exists'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Create new user with hashed password
            user = LCICSystemUser(
                bnk_code=request.data['bnk_code'],
                branch_code=request.data['branch_code'],
                username=request.data['username'],
                password=make_password(request.data['password']),  # Explicitly hash password
                roles=request.data['roles'],
                nameL=request.data['nameL'],
                nameE=request.data['nameE'],
                surnameL=request.data['surnameL'],
                surnameE=request.data['surnameE'],
                is_active=True,
                insertDate=timezone.now(),
            )

            # Handle optional profile image if provided
            if 'profile_image' in request.FILES:
                user.profile_image = request.FILES['profile_image']

            # Save user
            user.save()

            # Prepare response data (excluding password)
            user_data = {
                'username': user.username,
                'bnk_code': user.bnk_code,
                'branch_code': user.branch_code,
                'roles': user.roles,
                'nameL': user.nameL,
                'nameE': user.nameE,
                'surnameL': user.surnameL,
                'surnameE': user.surnameE,
                'insertDate': user.insertDate,
                'is_active': user.is_active,
            }

            return Response(
                {
                    'message': 'User created successfully',
                    'user': user_data
                },
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                {'error': f'An error occurred: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LCICSystemUserListView(APIView):
    def get(self, request):
        users = LCICSystemUser.objects.all()
        
        serializer = LCICSystemUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LCICSystemUserDetailView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(LCICSystemUser, pk=pk)
        serializer = LCICSystemUserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        print('Request.FILES:', request.FILES)  # Debug: Check if file is received
        print('Request.data:', request.data)   # Debug: Check all data
        user = get_object_or_404(LCICSystemUser, pk=pk)
        serializer = LCICSystemUserSerializer(user, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            print('Validated data:', serializer.validated_data)  # Debug: Check validated data
            user = serializer.save()
            print('Updated user profile_image:', user.profile_image)  # Debug: Check saved image
            return Response(serializer.data, status=status.HTTP_200_OK)
        print('Serializer errors:', serializer.errors)  # Debug: Check validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(LCICSystemUser, pk=pk)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import bank_bnk
from .serializers import BankSerializer

class BankListCreateView(APIView):
    def get(self, request):
        banks = bank_bnk.objects.all()
        serializer = BankSerializer(banks, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print('Request.FILES:', request.FILES)  # Debug
        print('Request.data:', request.data)   # Debug

        # Check for duplicate bnk_code
        bnk_code = request.data.get('bnk_code')
        if bnk_code and bank_bnk.objects.filter(bnk_code=bnk_code).exists():
            return Response(
                {'error': f'A bank with bnk_code "{bnk_code}" already exists. Skipping creation.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BankSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            print('Validated data:', serializer.validated_data)  # Debug
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('Serializer errors:', serializer.errors)  # Debug
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankDetailView(APIView):
    def get(self, request, pk):
        bank = get_object_or_404(bank_bnk, pk=pk)
        serializer = BankSerializer(bank, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        print('Request.FILES:', request.FILES)  
        print('Request.data:', request.data)   
        bank = get_object_or_404(bank_bnk, pk=pk)
        serializer = BankSerializer(bank, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            print('Validated data:', serializer.validated_data)  
            bank = serializer.save()
            print('Updated bank bnk_images:', bank.bnk_images)  
            return Response(serializer.data, status=status.HTTP_200_OK)
        print('Serializer errors:', serializer.errors)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bank = get_object_or_404(bank_bnk, pk=pk)
        bank.delete()
        return Response({'message': 'Bank deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
# views.py
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework.parsers import MultiPartParser, FormParser
# from .models import memberInfo
# from .serializers import MemberInfoSerializer

# class MemberInfoViewSet(viewsets.ModelViewSet):
#     queryset = memberInfo.objects.all()
#     serializer_class = MemberInfoSerializer
#     parser_classes = (MultiPartParser, FormParser)
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @action(detail=False, methods=['get'])
#     def published(self, request):
#         members = memberInfo.objects.filter(published=True)
#         serializer = self.get_serializer(members, many=True)
#         return Response(serializer.data)
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import IntegerField
from django.db.models.functions import Cast


class MemberInfoViewSet(viewsets.ModelViewSet):
    queryset = memberInfo.objects.all()  # ຈຳເປັນສຳລັບ Router
    serializer_class = MemberInfoSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def get_queryset(self):
        """
        ກຳນົດ queryset ທີ່ຈັດລຽງຕາມ bnk_code ແຕ່ນ້ອຍຫາໃຫຍ່
        ແປງ bnk_code ເປັນ integer ກ່ອນຈັດລຽງເພື່ອໃຫ້ຖືກຕ້ອງ
        """
        return memberInfo.objects.annotate(
            bnk_code_int=Cast('bnk_code', IntegerField())
        ).order_by('bnk_code_int')
    
    def create(self, request, *args, **kwargs):
        """
        ສ້າງສະມາຊິກໃໝ່
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        """
        ອັບເດດຂໍ້ມູນສະມາຊິກ
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def published(self, request):
        """
        ດຶງສະມາຊິກທີ່ published ເທົ່ານັ້ນ ແລະຈັດລຽງຕາມ bnk_code
        """
        members = self.get_queryset().filter(published=True)
        serializer = self.get_serializer(members, many=True)
        return Response(serializer.data)
def get_all_provinces(request):
    provinces = Province.objects.all().order_by('Province_Name')
    data = [{'id': province.Prov_ID, 'name': province.Province_Name} for province in provinces]
    return JsonResponse(data, safe=False)


def get_districts_by_province(request):
    province_id = request.GET.get('province_id')
    if not province_id:
        return JsonResponse([], safe=False)
    
    districts = District.objects.filter(Prov_ID=province_id).order_by('District_Name')
    data = [{'id': district.Dstr_ID, 'name': district.District_Name} for district in districts]
    return JsonResponse(data, safe=False)


def get_villages_by_district(request):
    district_id = request.GET.get('district_id')
    province_id = request.GET.get('province_id')
    if not district_id or not province_id:
        return JsonResponse([], safe=False)
    
    villages = Village.objects.filter(Prov_ID=province_id, Dstr_ID=district_id).order_by('Village_Name')
    data = [{'id': village.Vill_ID, 'name': village.Village_Name} for village in villages]
    return JsonResponse(data, safe=False)


def location_form(request):
    provinces = Province.objects.all().order_by('Province_Name')
    context = {
        'provinces': provinces
    }
    return render(request, 'location_form.html', context)

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Q
from django.db.models.expressions import RawSQL

class FileElectricListAPIView(APIView):
    """
    GET params:
      - name:   substring to match in `name`
      - date:   exact 'YYYYMM' to match in the filename
      - status: one of Pending, Approved, Rejected
    Response:
      {
        "results": […],
        "counts_by_month": [
           {"file_month":"202503","cnt": 5},
           …
        ]
      }
    """
    def get(self, request, *args, **kwargs):
        qs = File_Electric.objects.all()

        
        name = request.GET.get("name")
        if name:
            qs = qs.filter(name__icontains=name)

        
        status = request.GET.get("status")
        if status:
            qs = qs.filter(status=status)

       
        date = request.GET.get("date")  
        if date:
            
            qs = qs.filter(name__contains=f"-{date}")

        
        files_data = FileElectricSerializer(qs, many=True).data

        
        counts_qs = (
            qs
            .annotate(
               
                file_month=RawSQL(
                    "SUBSTRING(name FROM '-([0-9]{6})')",
                    []
                )
            )
            .values("file_month")
            .annotate(cnt=Count("id"))
            .order_by("file_month")
        )

        return Response({
            "results": files_data,
            "counts_by_month": list(counts_qs)
        })

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import json

class InvestorInfoService:
    """ບໍລິການສຳລັບຈັດການຂໍ້ມູນນັກລົງທຶນ"""
    
    @staticmethod
    def get_all_investors(page=None, per_page=None):
        """ດຶງຂໍ້ມູນນັກລົງທຶນທັງໝົດ (ແບບແບ່ງໜ້າຫຼືທັງໝົດ)"""
        try:
            investors = InvestorInfo.objects.all().order_by('-InsertDate')
            
            # ຖ້າບໍ່ມີການແບ່ງໜ້າ ດຶງທັງໝົດ
            if page is None or per_page is None:
                data = []
                for investor in investors:
                    data.append({
                        'id': investor.ID,
                        'enterprise_id': investor.EnterpriseID,
                        'name': investor.investorName,
                        'ownership_percentage': investor.investorOwnerPercentage,
                        'nationality': investor.investorNationality,
                        'card_number': investor.investorcardNumber,
                        'mobile': investor.investorMobile,
                        'insert_date': investor.InsertDate.strftime('%Y-%m-%d %H:%M:%S') if investor.InsertDate else None,
                        'update_date': investor.UpdateDate.strftime('%Y-%m-%d %H:%M:%S') if investor.UpdateDate else None,
                    })
                
                return {
                    'success': True,
                    'data': data,
                    'total_items': investors.count(),
                }
            
            # ແບ່ງໜ້າ - ຕັ້ງຄ່າເລີ່ມຕົ້ນຖ້າເປັນ None
            page = 1 if page is None else page
            per_page = 10 if per_page is None else per_page
            
            paginator = Paginator(investors, per_page)
            page_obj = paginator.get_page(page)
            
            data = []
            for investor in page_obj:
                data.append({
                    'id': investor.ID,
                    'enterprise_id': investor.EnterpriseID,
                    'name': investor.investorName,
                    'ownership_percentage': investor.investorOwnerPercentage,
                    'nationality': investor.investorNationality,
                    'card_number': investor.investorcardNumber,
                    'mobile': investor.investorMobile,
                    'insert_date': investor.InsertDate.strftime('%Y-%m-%d %H:%M:%S') if investor.InsertDate else None,
                    'update_date': investor.UpdateDate.strftime('%Y-%m-%d %H:%M:%S') if investor.UpdateDate else None,
                })
            
            return {
                'success': True,
                'data': data,
                'pagination': {
                    'current_page': page_obj.number,
                    'total_pages': paginator.num_pages,
                    'total_items': paginator.count,
                    'has_next': page_obj.has_next(),
                    'has_previous': page_obj.has_previous(),
                }
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def get_investor_by_id(investor_id):
        """ດຶງຂໍ້ມູນນັກລົງທຶນຕາມ ID"""
        try:
            # ກວດສອບວ່າ investor_id ມີຄ່າແລະສາມາດແປງເປັນ int ໄດ້
            if investor_id is None:
                return {'success': False, 'error': 'Investor ID is required'}
            
            # ພະຍາຍາມແປງເປັນ int
            try:
                investor_id = int(investor_id)
            except (ValueError, TypeError):
                return {'success': False, 'error': 'Invalid Investor ID format'}
            
            investor = InvestorInfo.objects.get(ID=investor_id)
            return {
                'success': True,
                'data': {
                    'id': investor.ID,
                    'enterprise_id': investor.EnterpriseID,
                    'name': investor.investorName,
                    'ownership_percentage': investor.investorOwnerPercentage,
                    'nationality': investor.investorNationality,
                    'card_number': investor.investorcardNumber,
                    'mobile': investor.investorMobile,
                    'insert_date': investor.InsertDate.strftime('%Y-%m-%d %H:%M:%S') if investor.InsertDate else None,
                    'update_date': investor.UpdateDate.strftime('%Y-%m-%d %H:%M:%S') if investor.UpdateDate else None,
                }
            }
        except ObjectDoesNotExist:
            return {'success': False, 'error': 'ບໍ່ພົບຂໍ້ມູນນັກລົງທຶນ'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def get_investors_by_enterprise(enterprise_id, page=None, per_page=None):
        """ດຶງຂໍ້ມູນນັກລົງທຶນຕາມ Enterprise ID"""
        try:
            investors = InvestorInfo.objects.filter(
                EnterpriseID=enterprise_id
            ).order_by('-InsertDate')
            
            # ຖ້າບໍ່ມີການແບ່ງໜ້າ ດຶງທັງໝົດ
            if page is None or per_page is None:
                data = []
                for investor in investors:
                    data.append({
                        'id': investor.ID,
                        'enterprise_id': investor.EnterpriseID,
                        'name': investor.investorName,
                        'ownership_percentage': investor.investorOwnerPercentage,
                        'nationality': investor.investorNationality,
                        'card_number': investor.investorcardNumber,
                        'mobile': investor.investorMobile,
                        'insert_date': investor.InsertDate.strftime('%Y-%m-%d %H:%M:%S') if investor.InsertDate else None,
                        'update_date': investor.UpdateDate.strftime('%Y-%m-%d %H:%M:%S') if investor.UpdateDate else None,
                    })
                
                return {
                    'success': True,
                    'data': data,
                    'total_items': investors.count(),
                }
            
            # ແບ່ງໜ້າ - ຕັ້ງຄ່າເລີ່ມຕົ້ນຖ້າເປັນ None
            page = 1 if page is None else page
            per_page = 10 if per_page is None else per_page
            
            paginator = Paginator(investors, per_page)
            page_obj = paginator.get_page(page)
            
            data = []
            for investor in page_obj:
                data.append({
                    'id': investor.ID,
                    'enterprise_id': investor.EnterpriseID,
                    'name': investor.investorName,
                    'ownership_percentage': investor.investorOwnerPercentage,
                    'nationality': investor.investorNationality,
                    'card_number': investor.investorcardNumber,
                    'mobile': investor.investorMobile,
                    'insert_date': investor.InsertDate.strftime('%Y-%m-%d %H:%M:%S') if investor.InsertDate else None,
                    'update_date': investor.UpdateDate.strftime('%Y-%m-%d %H:%M:%S') if investor.UpdateDate else None,
                })
            
            return {
                'success': True,
                'data': data,
                'pagination': {
                    'current_page': page_obj.number,
                    'total_pages': paginator.num_pages,
                    'total_items': paginator.count,
                    'has_next': page_obj.has_next(),
                    'has_previous': page_obj.has_previous(),
                }
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def search_investors(search_term, page=None, per_page=None):
        """ຄົ້ນຫານັກລົງທຶນຕາມຊື່, ເບີໂທ, ຫຼືບັດປະຊາຊົນ"""
        try:
            investors = InvestorInfo.objects.filter(
                Q(investorName__icontains=search_term) |
                Q(investorMobile__icontains=search_term) |
                Q(investorcardNumber__icontains=search_term) |
                Q(investorNationality__icontains=search_term) |
                Q(EnterpriseID__icontains=search_term)
            ).order_by('-InsertDate')
            
            # ຖ້າບໍ່ມີການແບ່ງໜ້າ ດຶງທັງໝົດ
            if page is None or per_page is None:
                data = []
                for investor in investors:
                    data.append({
                        'id': investor.ID,
                        'enterprise_id': investor.EnterpriseID,
                        'name': investor.investorName,
                        'ownership_percentage': investor.investorOwnerPercentage,
                        'nationality': investor.investorNationality,
                        'card_number': investor.investorcardNumber,
                        'mobile': investor.investorMobile,
                        'insert_date': investor.InsertDate.strftime('%Y-%m-%d %H:%M:%S') if investor.InsertDate else None,
                        'update_date': investor.UpdateDate.strftime('%Y-%m-%d %H:%M:%S') if investor.UpdateDate else None,
                    })
                
                return {
                    'success': True,
                    'data': data,
                    'total_items': investors.count(),
                    'search_term': search_term
                }
            
            # ແບ່ງໜ້າ - ຕັ້ງຄ່າເລີ່ມຕົ້ນຖ້າເປັນ None
            page = 1 if page is None else page
            per_page = 10 if per_page is None else per_page
            
            paginator = Paginator(investors, per_page)
            page_obj = paginator.get_page(page)
            
            data = []
            for investor in page_obj:
                data.append({
                    'id': investor.ID,
                    'enterprise_id': investor.EnterpriseID,
                    'name': investor.investorName,
                    'ownership_percentage': investor.investorOwnerPercentage,
                    'nationality': investor.investorNationality,
                    'card_number': investor.investorcardNumber,
                    'mobile': investor.investorMobile,
                    'insert_date': investor.InsertDate.strftime('%Y-%m-%d %H:%M:%S') if investor.InsertDate else None,
                    'update_date': investor.UpdateDate.strftime('%Y-%m-%d %H:%M:%S') if investor.UpdateDate else None,
                })
            
            return {
                'success': True,
                'data': data,
                'pagination': {
                    'current_page': page_obj.number,
                    'total_pages': paginator.num_pages,
                    'total_items': paginator.count,
                    'has_next': page_obj.has_next(),
                    'has_previous': page_obj.has_previous(),
                },
                'search_term': search_term
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def get_investors_by_nationality(nationality, page=None, per_page=None):
        """ດຶງຂໍ້ມູນນັກລົງທຶນຕາມສັນຊາດ"""
        try:
            investors = InvestorInfo.objects.filter(
                investorNationality__icontains=nationality
            ).order_by('-InsertDate')
            
            # ຖ້າບໍ່ມີການແບ່ງໜ້າ ດຶງທັງໝົດ
            if page is None or per_page is None:
                data = []
                for investor in investors:
                    data.append({
                        'id': investor.ID,
                        'enterprise_id': investor.EnterpriseID,
                        'name': investor.investorName,
                        'ownership_percentage': investor.investorOwnerPercentage,
                        'nationality': investor.investorNationality,
                        'card_number': investor.investorcardNumber,
                        'mobile': investor.investorMobile,
                        'insert_date': investor.InsertDate.strftime('%Y-%m-%d %H:%M:%S') if investor.InsertDate else None,
                        'update_date': investor.UpdateDate.strftime('%Y-%m-%d %H:%M:%S') if investor.UpdateDate else None,
                    })
                
                return {
                    'success': True,
                    'data': data,
                    'total_items': investors.count(),
                }
            
            # ແບ່ງໜ້າ - ຕັ້ງຄ່າເລີ່ມຕົ້ນຖ້າເປັນ None
            page = 1 if page is None else page
            per_page = 10 if per_page is None else per_page
            
            paginator = Paginator(investors, per_page)
            page_obj = paginator.get_page(page)
            
            data = []
            for investor in page_obj:
                data.append({
                    'id': investor.ID,
                    'enterprise_id': investor.EnterpriseID,
                    'name': investor.investorName,
                    'ownership_percentage': investor.investorOwnerPercentage,
                    'nationality': investor.investorNationality,
                    'card_number': investor.investorcardNumber,
                    'mobile': investor.investorMobile,
                    'insert_date': investor.InsertDate.strftime('%Y-%m-%d %H:%M:%S') if investor.InsertDate else None,
                    'update_date': investor.UpdateDate.strftime('%Y-%m-%d %H:%M:%S') if investor.UpdateDate else None,
                })
            
            return {
                'success': True,
                'data': data,
                'pagination': {
                    'current_page': page_obj.number,
                    'total_pages': paginator.num_pages,
                    'total_items': paginator.count,
                    'has_next': page_obj.has_next(),
                    'has_previous': page_obj.has_previous(),
                }
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def get_investor_statistics():
        """ສະຖິຕິຂອງນັກລົງທຶນ"""
        try:
            total_investors = InvestorInfo.objects.count()
            
            # ນັບຕາມສັນຊາດ
            nationality_stats = InvestorInfo.objects.values('investorNationality').annotate(
                count=models.Count('investorNationality')
            ).order_by('-count')
            
            # ນັກລົງທຶນໃໝ່ໃນເດືອນນີ້
            current_month = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            new_investors_this_month = InvestorInfo.objects.filter(
                InsertDate__gte=current_month
            ).count()
            
            # ວິສາຫະກິດທີ່ມີນັກລົງທຶນ
            enterprises_with_investors = InvestorInfo.objects.values('EnterpriseID').distinct().count()
            
            return {
                'success': True,
                'data': {
                    'total_investors': total_investors,
                    'new_investors_this_month': new_investors_this_month,
                    'enterprises_with_investors': enterprises_with_investors,
                    'nationality_distribution': list(nationality_stats),
                }
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}

# Django Views ສຳລັບ API
def get_investors_by_enterprise_api(request, enterprise_id):
    """API endpoint ສຳລັບດຶງຂໍ້ມູນນັກລົງທຶນຕາມວິສາຫະກິດ"""
    page = request.GET.get('page')
    per_page = request.GET.get('per_page')
    
    # ແປງເປັນ integer ຖ້າມີຄ່າ
    if page is not None:
        try:
            page = int(page)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid page parameter'})
    
    if per_page is not None:
        try:
            per_page = int(per_page)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid per_page parameter'})
    
    result = InvestorInfoService.get_investors_by_enterprise(enterprise_id, page=page, per_page=per_page)
    return JsonResponse(result)

def get_investors_by_nationality_api(request, nationality):
    """API endpoint ສຳລັບດຶງຂໍ້ມູນນັກລົງທຶນຕາມສັນຊາດ"""
    page = request.GET.get('page')
    per_page = request.GET.get('per_page')
    
    # ແປງເປັນ integer ຖ້າມີຄ່າ
    if page is not None:
        try:
            page = int(page)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid page parameter'})
    
    if per_page is not None:
        try:
            per_page = int(per_page)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid per_page parameter'})
    
    result = InvestorInfoService.get_investors_by_nationality(nationality, page=page, per_page=per_page)
    return JsonResponse(result)

def get_all_investors_api(request):
    """API endpoint ສຳລັບດຶງຂໍ້ມູນນັກລົງທຶນທັງໝົດ"""
    page = request.GET.get('page')
    per_page = request.GET.get('per_page')
    
    
    if page is not None:
        try:
            page = int(page)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid page parameter'})
    
    if per_page is not None:
        try:
            per_page = int(per_page)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid per_page parameter'})
    
    result = InvestorInfoService.get_all_investors(page=page, per_page=per_page)
    return JsonResponse(result)

def get_investor_by_id_api(request, investor_id):
    """API endpoint ສຳລັບດຶງຂໍ້ມູນນັກລົງທຶນຕາມ ID"""
    # ກວດສອບວ່າ investor_id ມີຄ່າ
    if investor_id is None:
        return JsonResponse({'success': False, 'error': 'Investor ID is required'})
    
    result = InvestorInfoService.get_investor_by_id(investor_id)
    return JsonResponse(result)

def search_investors_api(request):
    """API endpoint ສຳລັບຄົ້ນຫານັກລົງທຶນ"""
    search_term = request.GET.get('q', '')
    page = request.GET.get('page')
    per_page = request.GET.get('per_page')
    
    if not search_term:
        return JsonResponse({'success': False, 'error': 'Search term is required'})
    
    # ແປງເປັນ integer ຖ້າມີຄ່າ
    if page is not None:
        try:
            page = int(page)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid page parameter'})
    
    if per_page is not None:
        try:
            per_page = int(per_page)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid per_page parameter'})
    
    result = InvestorInfoService.search_investors(search_term, page=page, per_page=per_page)
    return JsonResponse(result)

def get_investor_statistics_api(request):
    """API endpoint ສຳລັບສະຖິຕິນັກລົງທຶນ"""
    result = InvestorInfoService.get_investor_statistics()
    return JsonResponse(result)    
from django.core.exceptions import ValidationError

# ຟັງຊັ້ນຫຼັກ (ໃສ່ໃນ views.py)
def filter_data_by_criteria(id_file, **kwargs):
    """
    ດຶງຂໍ້ມູນຈາກທຸກຕາຕະລາງຕາມ id_file ແລະເງື່ອນໄຂເພີ່ມເຕີມ
    """
    result = {}
    try:
        # ສ້າງ filter criteria ທີ່ລວມ id_file
        filter_criteria = {'id_file': id_file}
        filter_criteria.update(kwargs)
        
        result['b1_data'] = B1.objects.filter(**filter_criteria)
        result['data_edit'] = data_edit.objects.filter(**filter_criteria)
        result['disputes'] = disputes.objects.filter(**filter_criteria)
        result['b_data_damaged'] = B_Data_is_damaged.objects.filter(**filter_criteria)
        result['b1_monthly'] = B1_Monthly.objects.filter(**filter_criteria)
        
    except Exception as e:
        print(f"Error in filter_data_by_criteria: {str(e)}")
        return None
    
    return result


def get_data_api(request):
    """
    API ສຳລັບດຶງຂໍ້ມູນ
    URL: /api/data/?id_file=10&bnk_code=001&period=202401
    """
    # ດຶງ id_file
    id_file = request.GET.get('id_file')
    if not id_file:
        return JsonResponse({
            'error': 'id_file parameter is required',
            'example': '/api/data/?id_file=10'
        }, status=400)
    
   
    filter_params = {}
    allowed_filters = ['bnk_code', 'period', 'customer_id', 'loan_id', 'branch_id', 
                      'segmentType', 'com_enterprise_code', 'product_type', 'lcicID']
    
    for key in allowed_filters:
        if request.GET.get(key):
            filter_params[key] = request.GET.get(key)
    
    # ດຶງຂໍ້ມູນ
    data = filter_data_by_criteria(id_file, **filter_params)
    
    if data is None:
        return JsonResponse({
            'error': 'ເກີດຂໍ້ຜິດພາດໃນການດຶງຂໍ້ມູນ'
        }, status=500)
    
    # ສ້າງ response
    response_data = {
        'id_file': id_file,
        'filters': filter_params,
        'counts': {
            'b1': data['b1_data'].count(),
            'data_edit': data['data_edit'].count(),
            'disputes': data['disputes'].count(),
            'b_data_damaged': data['b_data_damaged'].count(),
            'b1_monthly': data['b1_monthly'].count()
        },
        'total_records': (
            data['b1_data'].count() + 
            data['data_edit'].count() + 
            data['disputes'].count() + 
            data['b_data_damaged'].count() + 
            data['b1_monthly'].count()
        ),
        'data': {
            'b1': list(data['b1_data'].values()),
            'data_edit': list(data['data_edit'].values()),
            'disputes': list(data['disputes'].values()),
            'b_data_damaged': list(data['b_data_damaged'].values()),
            'b1_monthly': list(data['b1_monthly'].values())
        }
    }
    
    return JsonResponse(response_data, safe=False)


# API Tracking Edl ----------------------------------


import requests
import json
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, Count, Sum, Avg
from django.core.paginator import Paginator
from datetime import datetime
from django.conf import settings
import logging
from django.db import transaction
from utility.models import UploadDataTracking, UploadLog
from utility.models import Electric_Bill
from utility.models import edl_province_code, edl_district_code, edl_customer_info 
from .serializers import (
    UploadTrackingSerializer, 
    UploadTrackingDetailSerializer,
    ProvinceSerializer,
    DistrictSerializer
)

logger = logging.getLogger(__name__)

class ProvinceListAPIView(APIView):
    """Get list of provinces from edl_province_code model"""
    
    def get(self, request):
        try:
            provinces = edl_province_code.objects.all().order_by('pro_id')
            serializer = ProvinceSerializer(provinces, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching provinces: {str(e)}")
            return Response(
                {"error": "Failed to fetch provinces"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class DistrictListAPIView(APIView):
    """Get districts for a specific province from edl_district_code model"""
    
    def get(self, request):
        province_id = request.GET.get('province_id')
        if not province_id:
            return Response(
                {"error": "province_id parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Get province info
            try:
                province = edl_province_code.objects.get(pro_id=province_id)
            except edl_province_code.DoesNotExist:
                return Response(
                    {"error": f"Province with ID {province_id} not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Get districts for this province
            districts = edl_district_code.objects.filter(
                pro_id=province_id
            ).order_by('dis_id')
            
            if not districts.exists():
                return Response(
                    {"error": f"No districts found for province {province_id}"},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Add province name to each district
            result = []
            for district in districts:
                result.append({
                    'pro_id': district.pro_id,
                    'pro_name': province.pro_name,
                    'dis_id': district.dis_id,
                    'dis_name': district.dis_name
                })
            
            return Response(result, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error fetching districts: {str(e)}")
            return Response(
                {"error": "Failed to fetch districts"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UploadTrackingListAPIView(APIView):
    """List tracking records for specific province and month"""
    
    def get(self, request):
        try:        
            month = request.GET.get('month', timezone.now().strftime('%Y%m'))
            province_id = request.GET.get('province_id')
            
            if not province_id:
                return Response(
                    {"error": "province_id parameter is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validate month format
            try:
                datetime.strptime(month, '%Y%m')
            except ValueError:
                return Response(
                    {"error": "Invalid month format. Use YYYYMM (e.g., 202509)"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Get tracking records for the specific province and month
            queryset = UploadDataTracking.objects.filter(
                upload_month=month,
                pro_id=province_id
            ).order_by('dis_id')
            
            # Serialize data
            serialized_data = []
            for item in queryset:
                data = UploadTrackingSerializer(item).data
                data['success_rate_formatted'] = f"{item.success_rates:.1f}" if item.success_rates else "0.0"
                data['formatted_size'] = self.format_file_size(item.data_size_mb)
                data['upload_duration'] = self.format_duration(item.upload_duration) if item.upload_duration else None
                serialized_data.append(data)
            
            # Get statistics
            stats = self.get_statistics(month, province_id)
            
            return Response({
                'data': serialized_data,
                'statistics': stats
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Failed to fetch tracking data: {str(e)}")
            return Response(
                {"error": "Failed to fetch tracking data"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def get_statistics(self, month, province_id):
        """Calculate statistics for the dashboard"""
        try:
            queryset = UploadDataTracking.objects.filter(
                upload_month=month,
                pro_id=province_id
            )
            
            total_count = queryset.count()
            if total_count == 0:
                return {
                    'total_locations': 0,
                    'status_breakdown': {},
                    'total_data_size_mb': 0.0,
                    'average_records': 0
                }
            
            # Status breakdown
            status_data = queryset.values('status').annotate(count=Count('id'))
            status_counts = {item['status']: item['count'] for item in status_data}
            
            # Aggregated data
            aggregated = queryset.aggregate(
                total_size=Sum('data_size_mb'),
                avg_records=Avg('total_records')
            )
            
            return {
                'total_locations': total_count,
                'status_breakdown': status_counts,
                'total_data_size_mb': round(float(aggregated['total_size'] or 0), 2),
                'average_records': round(float(aggregated['avg_records'] or 0))
            }
            
        except Exception as e:
            logger.error(f"Error in get_statistics: {str(e)}")
            return {
                'total_locations': 0,
                'status_breakdown': {},
                'total_data_size_mb': 0.0,
                'average_records': 0
            }
    
    def format_file_size(self, size_mb):
        """Format file size for display"""
        if not size_mb or size_mb < 1:
            return f"{(size_mb or 0) * 1024:.1f} KB"
        elif size_mb < 1024:
            return f"{size_mb:.1f} MB"
        else:
            return f"{size_mb / 1024:.1f} GB"
    
    def format_duration(self, seconds):
        """Format duration for display"""
        if not seconds:
            return None
        if seconds < 60:
            return f"{seconds:.0f}s"
        elif seconds < 3600:
            return f"{seconds / 60:.1f}m"
        else:
            return f"{seconds / 3600:.1f}h"

from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

class InitializeDistrictsAPIView(APIView):
    """Initialize tracking records for districts in a specific province"""
    parser_classes = [JSONParser, FormParser, MultiPartParser]  
    
    def post(self, request):
        try:
            # Force JSON parsing if content type is application/json
            if request.content_type == 'application/json' and not request.data:
                import json
                data = json.loads(request.body.decode('utf-8'))
            else:
                data = request.data
            
            month = data.get('month', timezone.now().strftime('%Y%m'))
            province_id = data.get('province_id')
            username = data.get('username', 'system')
            
            if not province_id:
                return Response(
                    {
                        "error": "province_id is required",
                        "received_data": dict(data) if hasattr(data, 'items') else str(data),
                        "debug_info": {
                            "request_data": dict(request.data) if hasattr(request.data, 'items') else str(request.data),
                            "content_type": request.content_type,
                            "body": request.body.decode('utf-8') if request.body else None
                        }
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            if not month:
                return Response(
                    {"error": "month is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            if not username:
                return Response(
                    {"error": "username is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validate month format
            try:
                datetime.strptime(month, '%Y%m')
            except ValueError:
                return Response(
                    {"error": "Invalid month format. Use YYYYMM (e.g., 202509)"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Get province info
            try:
                province = edl_province_code.objects.get(pro_id=province_id)
            except edl_province_code.DoesNotExist:
                return Response(
                    {"error": f"Province with ID {province_id} not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Get districts for this province
            districts = edl_district_code.objects.filter(pro_id=province_id)
            
            if not districts.exists():
                return Response(
                    {"error": f"No districts found for province {province_id}"},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            created_count = 0
            
            # Create tracking records for each district
            for district in districts:
                tracking, created = UploadDataTracking.objects.get_or_create(
                    pro_id=district.pro_id,
                    dis_id=district.dis_id,
                    upload_month=month,
                    defaults={
                        'pro_name': province.pro_name,
                        'dis_name': district.dis_name,
                        'status': 'pending',
                        'user_upload': username
                    }
                )
                if created:
                    created_count += 1
            
            return Response({
                'message': f'Initialized {created_count} districts for {province.pro_name} - {month}',
                'total_districts': districts.count(),
                'created_count': created_count
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Initialization failed: {str(e)}")
            return Response({
                'error': f'Initialization failed: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UploadDataAPIView(APIView):
    """Handle individual district data upload"""
    
    def post(self, request):
        try:
            # Extract parameters
            province_code = request.data.get('province_code')
            district_code = request.data.get('district_code')
            date_request = request.data.get('dateRequest')
            username = request.data.get('username', 'system')
            
            if not all([province_code, district_code, date_request]):
                return Response({
                    'error': 'Missing required parameters: province_code, district_code, dateRequest'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Validate date format
            try:
                datetime.strptime(date_request, '%Y%m')
            except ValueError:
                return Response(
                    {"error": "Invalid dateRequest format. Use YYYYMM (e.g., 202509)"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validate province and district exist in our models
            try:
                province = edl_province_code.objects.get(pro_id=province_code)
            except edl_province_code.DoesNotExist:
                return Response({
                    'error': f'Province with ID {province_code} not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Handle district_code format - try exact match first, then with padding
            district = None
            try:
                district = edl_district_code.objects.get(
                    pro_id=province_code, 
                    dis_id=district_code
                )
            except edl_district_code.DoesNotExist:
                # Try with leading zero padding (01 -> 0101)
                padded_district_code = f"{province_code}{district_code.zfill(2)}"
                try:
                    district = edl_district_code.objects.get(
                        pro_id=province_code, 
                        dis_id=padded_district_code
                    )
                    district_code = padded_district_code  # Update to use the correct format
                except edl_district_code.DoesNotExist:
                    return Response({
                        'error': f'District with ID {district_code} not found in province {province_code}. Available districts: {list(edl_district_code.objects.filter(pro_id=province_code).values_list("dis_id", flat=True))}'
                    }, status=status.HTTP_404_NOT_FOUND)
            
            # Get tracking record
            try:
                tracking = UploadDataTracking.objects.get(
                    pro_id=province_code,
                    dis_id=district_code,
                    upload_month=date_request
                )
            except UploadDataTracking.DoesNotExist:
                return Response({
                    'error': 'Tracking record not found. Please initialize districts first.'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Check if already completed
            if tracking.status == 'completed':
                return Response({
                    'message': 'Data already uploaded successfully',
                    'tracking_id': tracking.id,
                    'total_records': tracking.total_records,
                    'processed_records': tracking.processed_records
                }, status=status.HTTP_200_OK)
            
            # Update status to in_progress
            tracking.status = 'in_progress'
            tracking.upload_started = timezone.now()
            tracking.user_upload = username
            tracking.save()
            
            # Log start
            UploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Upload started by {username} for {province.pro_name} - {district.dis_name}'
            )
            
            # Fetch and process data
            result = self.fetch_and_process_data(tracking)
            
            return Response(result, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Upload failed: {str(e)}")
            return Response({
                'error': f'Upload failed: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            

    def fetch_and_process_data(self, tracking):
        """Fetch data from EDL API and insert into Electric_Bill and Customer tables"""
        try:
            # EDL API endpoints
            payment_api_url = "https://edl-inside-api.edl.com.la/api_v1/wattmonitor-bol/billing-svc/billing/getpaymenthistory"
            customer_api_url = "https://edl-inside-api.edl.com.la/api_v1/wattmonitor-bol/billing-svc/billing/getCustomerInfo"
            page = 1
            limit = 100000
            
            params = {
                'province_code': tracking.pro_id,
                'district_code': tracking.dis_id,
                'dateRequest': tracking.upload_month,
                'page': page,
                'limit': limit
            }
            
            # ========== Fetch Payment History ==========
            UploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Fetching payment data from EDL API'
            )
            
            payment_response = requests.get(payment_api_url, params=params, timeout=300)
            tracking.api_response_code = payment_response.status_code
            tracking.save()
            
            if payment_response.status_code != 200:
                raise Exception(f'Payment API failed with status {payment_response.status_code}')
            
            payment_data = payment_response.json()
            payment_records = []
            
            if isinstance(payment_data, dict) and 'data' in payment_data:
                data_section = payment_data['data']
                if isinstance(data_section, dict) and 'paymentHistory' in data_section:
                    payment_records = data_section['paymentHistory']
            
            UploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Received {len(payment_records)} payment records'
            )
            
            # ========== Fetch Customer Info with Better Error Handling ==========
            UploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Fetching customer data from EDL API'
            )
            
            customer_records = []
            customer_error = None
            
            try:
                # Increase timeout to 5 minutes for customer API
                customer_response = requests.get(customer_api_url, params=params, timeout=300)
                
                if customer_response.status_code != 200:
                    customer_error = f'Customer API returned status {customer_response.status_code}'
                    UploadLog.objects.create(
                        tracking=tracking,
                        log_level='WARNING',
                        message=customer_error
                    )
                else:
                    customer_data = customer_response.json()
                    
                    if isinstance(customer_data, dict) and 'data' in customer_data:
                        data_section = customer_data['data']
                        if isinstance(data_section, dict) and 'customerInfo' in data_section:
                            customer_records = data_section['customerInfo']
                        elif isinstance(data_section, list):
                            customer_records = data_section
                    
                    UploadLog.objects.create(
                        tracking=tracking,
                        log_level='INFO',
                        message=f'Received {len(customer_records)} customer records'
                    )
            
            except requests.exceptions.Timeout:
                customer_error = 'Customer API request timed out after 5 minutes'
                UploadLog.objects.create(
                    tracking=tracking,
                    log_level='ERROR',
                    message=customer_error
                )
            
            except requests.exceptions.RequestException as e:
                customer_error = f'Customer API request failed: {str(e)}'
                UploadLog.objects.create(
                    tracking=tracking,
                    log_level='ERROR',
                    message=customer_error
                )
            
            except Exception as e:
                customer_error = f'Unexpected error fetching customer data: {str(e)}'
                UploadLog.objects.create(
                    tracking=tracking,
                    log_level='ERROR',
                    message=customer_error
                )
            
            # ========== Process Data ==========
            payment_processed = 0
            payment_failed = 0
            customer_processed = 0
            customer_failed = 0
            
            # Always process payment records
            if payment_records:
                UploadLog.objects.create(
                    tracking=tracking,
                    log_level='INFO',
                    message=f'Processing {len(payment_records)} payment records'
                )
                payment_processed, payment_failed = self.insert_electric_bill_data(
                    payment_records, tracking
                )
            
            # Process customer records only if available
            if customer_records:
                UploadLog.objects.create(
                    tracking=tracking,
                    log_level='INFO',
                    message=f'Processing {len(customer_records)} customer records'
                )
                customer_processed, customer_failed = self.insert_customer_info_data(
                    customer_records, tracking
                )
            elif customer_error:
                UploadLog.objects.create(
                    tracking=tracking,
                    log_level='WARNING',
                    message=f'Skipping customer data processing due to error: {customer_error}'
                )
            
            # Calculate total data size
            total_size = len(json.dumps({
                'payment': payment_records,
                'customer': customer_records
            }).encode('utf-8')) / (1024 * 1024)
            
            # Update tracking
            total_records = len(payment_records) + len(customer_records)
            total_processed = payment_processed + customer_processed
            total_failed = payment_failed + customer_failed
            
            # Determine status: completed if no failures, partial if customer failed but payment succeeded
            if total_failed == 0 and not customer_error:
                final_status = 'completed'
            elif payment_processed > 0 and customer_error:
                final_status = 'partial'
            elif total_failed > 0:
                final_status = 'partial'
            else:
                final_status = 'failed'
            
            tracking.status = final_status
            tracking.upload_completed = timezone.now()
            tracking.total_records = total_records
            tracking.processed_records = total_processed
            tracking.failed_records = total_failed
            tracking.data_size_mb = round(total_size, 2)
            tracking.success_rates = (total_processed / total_records * 100) if total_records > 0 else 0
            tracking.save()
            
            # Calculate upload duration after save
            duration = None
            if tracking.upload_started and tracking.upload_completed:
                duration = (tracking.upload_completed - tracking.upload_started).total_seconds()
            
            message = f'Upload completed - Payment: {payment_processed}/{len(payment_records)}, Customer: {customer_processed}/{len(customer_records)}'
            if customer_error:
                message += f' (Customer API Error: {customer_error})'
            
            UploadLog.objects.create(
                tracking=tracking,
                log_level='INFO' if final_status == 'completed' else 'WARNING',
                message=message
            )
            
            return {
                'message': 'Data upload completed' + (' with warnings' if customer_error else ' successfully'),
                'tracking_id': tracking.id,
                'status': final_status,
                'payment_records': {
                    'total': len(payment_records),
                    'processed': payment_processed,
                    'failed': payment_failed
                },
                'customer_records': {
                    'total': len(customer_records),
                    'processed': customer_processed,
                    'failed': customer_failed,
                    'error': customer_error
                },
                'data_size_mb': tracking.data_size_mb,
                'success_rate': tracking.success_rates,
                'upload_duration': duration
            }
            
        except Exception as e:
            tracking.status = 'failed'
            tracking.error_message = str(e)
            tracking.upload_completed = timezone.now()
            tracking.save()
            
            UploadLog.objects.create(
                tracking=tracking,
                log_level='ERROR',
                message=f'Upload failed: {str(e)}'
            )
            
            return {
                'error': f'Failed to fetch and process data: {str(e)}',
                'tracking_id': tracking.id,
                'status': 'failed'
            }


    def insert_electric_bill_data(self, records, tracking):
        """Insert records into Electric_Bill table"""
        processed_count = 0
        failed_count = 0
        batch_size = 1000
        
        try:
            UploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Starting to insert {len(records)} records into Electric_Bill table'
            )
            
            with transaction.atomic():
                batch = []
                
                for i, item in enumerate(records):
                    try:
                        # Validate that item is a dictionary
                        if not isinstance(item, dict):
                            UploadLog.objects.create(
                                tracking=tracking,
                                log_level='ERROR',
                                message=f'Record {i} is not a dictionary: {type(item)} - {str(item)[:100]}'
                            )
                            failed_count += 1
                            continue
                        
                        # Helper function to safely get values
                        def safe_get(key, default=''):
                            value = item.get(key, default)
                            return value if value is not None else default
                        
                        # Create Electric_Bill object according to your mapping
                        bill = Electric_Bill(
                            Customer_ID=self.truncate(safe_get('MASTER_BILL_ID', ''), 255),
                            InvoiceNo=self.truncate(safe_get('INDEX_NO', ''), 255),
                            TypeOfPro=self.truncate(safe_get('SUPPLY_TYPE', ''), 100),
                            Outstanding=self.safe_decimal(safe_get('OUTSTANDING', 0)),
                            Basic_Tax=self.safe_decimal(safe_get('FACT_TOTAL', 0)),
                            Bill_Amount=self.safe_decimal(safe_get('BILL_AMOUNT', 0)),
                            Debt_Amount=0.00,
                            Payment_ID=safe_get('PAYMENT_ID', ''),
                            PaymentType=safe_get('PAYMENT_WAY', ''),
                            Payment_Date=safe_get('PAYMENTDAY', ''),
                            InvoiceMonth=self.truncate(safe_get('INVM', ''), 50),
                            InvoiceDate=self.truncate(safe_get('INVD', ''), 100),
                            DisID=self.truncate(safe_get('DIS_ID', ''), 100),
                            ProID=self.truncate(safe_get('PROVINCE_CODE', ''), 100),
                            UserID=tracking.user_upload
                        )
                        
                        batch.append(bill)
                        
                        # Bulk insert when batch is full
                        if len(batch) >= batch_size:
                            Electric_Bill.objects.bulk_create(batch, ignore_conflicts=True)
                            processed_count += len(batch)
                            batch = []
                            
                            # Log progress
                            UploadLog.objects.create(
                                tracking=tracking,
                                log_level='INFO',
                                message=f'Inserted batch: {processed_count}/{len(records)} records processed'
                            )
                    
                    except Exception as e:
                        failed_count += 1
                        UploadLog.objects.create(
                            tracking=tracking,
                            log_level='ERROR',
                            message=f'Failed to process record {i}: {str(e)} - Record: {str(item)[:200] if isinstance(item, dict) else str(type(item))}'
                        )
                        continue
                
                # Insert remaining batch
                if batch:
                    Electric_Bill.objects.bulk_create(batch, ignore_conflicts=True)
                    processed_count += len(batch)
            
            UploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Data insertion completed. Processed: {processed_count}, Failed: {failed_count}'
            )
            
            return processed_count, failed_count
            
        except Exception as e:
            UploadLog.objects.create(
                tracking=tracking,
                log_level='ERROR',
                message=f'Bulk insert failed: {str(e)}'
            )
            raise e


    def insert_customer_info_data(self, records, tracking):
        """Insert or update customer records in edl_customer_info table"""
        processed_count = 0
        failed_count = 0
        
        try:
            UploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Starting to process {len(records)} customer records'
            )
            
            # Use batch processing for better performance
            batch_size = 500
            for i in range(0, len(records), batch_size):
                batch = records[i:i + batch_size]
                
                for j, item in enumerate(batch):
                    try:
                        if not isinstance(item, dict):
                            failed_count += 1
                            continue
                        
                        def safe_get(key, default=''):
                            value = item.get(key, default)
                            return value if value is not None else default
                        
                        # Use update_or_create for upsert logic
                        customer_id = self.truncate(safe_get('CUSTOMER_ID', ''), 100)
                        
                        if not customer_id:  # Skip if no customer ID
                            failed_count += 1
                            continue
                        
                        customer, created = edl_customer_info.objects.update_or_create(
                            Customer_ID=customer_id,
                            defaults={
                                'No': self.truncate(safe_get('INDEX_NO', ''), 100),
                                'Company_name': self.truncate(safe_get('COMPANY_NAME', ''), 100),
                                'Name': self.truncate(safe_get('GIVEN_NAME', ''), 100),
                                'Surname': self.truncate(safe_get('FAMILY_NAME', ''), 100),
                                'National_ID': self.truncate(safe_get('ID_NO', ''), 100),
                                'Passport': self.truncate(safe_get('PASSPORT_NO', ''), 100),
                                'Address': self.truncate(safe_get('FORW_ADDRESS', ''), 100),
                                'Dustrict_ID': self.truncate(safe_get('DIS_ID', ''), 100),
                                'Province_ID': self.truncate(safe_get('PRO_ID', ''), 100),
                                'Tel': self.truncate(safe_get('TEL_NO', ''), 100),
                                'Email': self.truncate(safe_get('EMAIL_NO', ''), 100),
                                'Cus_type': self.truncate(safe_get('SUPPLY_TYPE', ''), 100),
                                'Regis_date': self.truncate(safe_get('REGIT_D', ''), 100)
                            }
                        )
                        
                        processed_count += 1
                    
                    except Exception as e:
                        failed_count += 1
                        if failed_count <= 10:  # Log only first 10 errors
                            UploadLog.objects.create(
                                tracking=tracking,
                                log_level='ERROR',
                                message=f'Failed to process customer record {i+j}: {str(e)}'
                            )
                        continue
                
                # Log progress after each batch
                if (i + batch_size) % 1000 == 0 or (i + batch_size) >= len(records):
                    UploadLog.objects.create(
                        tracking=tracking,
                        log_level='INFO',
                        message=f'Customer records progress: {min(i + batch_size, len(records))}/{len(records)} processed'
                    )
            
            UploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Customer data processing completed. Processed: {processed_count}, Failed: {failed_count}'
            )
            
            return processed_count, failed_count
            
        except Exception as e:
            UploadLog.objects.create(
                tracking=tracking,
                log_level='ERROR',
                message=f'Customer data insert failed: {str(e)}'
            )
            raise e


    def truncate(self, value, max_length):
        """Safely truncate string to max length"""
        if value is None:
            return ''
        return str(value)[:max_length]


    def safe_decimal(self, value):
        """Safely convert to decimal"""
        try:
            return float(value or 0)
        except (ValueError, TypeError):
            return 0.0

class UploadTrackingDetailAPIView(APIView):
    """Get detailed tracking information with logs"""
    
    def get(self, request, tracking_id):
        try:
            tracking = UploadDataTracking.objects.get(id=tracking_id)
            serializer = UploadTrackingDetailSerializer(tracking)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UploadDataTracking.DoesNotExist:
            return Response(
                {'error': 'Tracking record not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

class InitializeTrackingAPIView(APIView):
    """Initialize tracking records for a month"""
    
    def post(self, request):
        try:
            month = request.data.get('month', timezone.now().strftime('%Y%m'))
            username = request.data.get('username', 'system')
            
            # Validate month format
            try:
                datetime.strptime(month, '%Y%m')
            except ValueError:
                return Response(
                    {"error": "Invalid month format. Use YYYYMM (e.g., 202509)"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Get provinces and districts from external API
            # api_url = getattr(settings, 'PROVINCE_API_URL', 'http://192.169.45.56:8000/api/province-edldetail/')
            api_url = f"{request.scheme}://{request.get_host()}/api/province-edldetail/"
            
            try:
                response = requests.get(api_url, timeout=30)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch province/district data: {str(e)}")
                return Response({
                    'error': 'Failed to fetch province/district data'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            province_districts = response.json()
            created_count = 0
            
            # Create tracking records
            for item in province_districts:
                tracking, created = UploadDataTracking.objects.get_or_create(
                    pro_id=item['pro_id'],
                    dis_id=item['dis_id'],
                    upload_month=month,
                    defaults={
                        'pro_name': item['pro_name'],
                        'dis_name': item['dis_name'],
                        'status': 'pending',
                        'user_upload': username
                    }
                )
                if created:
                    created_count += 1
            
            return Response({
                'message': f'Initialized {created_count} tracking records for month {month}',
                'total_locations': len(province_districts),
                'created_count': created_count
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Initialization failed: {str(e)}")
            return Response({
                'error': f'Initialization failed: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
# End API Tracking Edl ----------------------------------           
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class InitializeDistrictsAlternativeView(View):
    """Alternative implementation that should work with any JSON request"""
    
    def post(self, request):
        try:
            # Parse JSON manually to ensure it works
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
            else:
                # Fallback for form data
                data = request.POST.dict()
            
            print(f"Parsed data: {data}")  # Debug print
            
            month = data.get('month', timezone.now().strftime('%Y%m'))
            province_id = data.get('province_id')
            username = data.get('username', 'system')
            
            if not province_id:
                return JsonResponse({
                    'error': 'province_id is required',
                    'received_data': data,
                    'content_type': request.content_type
                }, status=400)
            
            # Validate month format
            try:
                datetime.strptime(month, '%Y%m')
            except ValueError:
                return JsonResponse({
                    'error': 'Invalid month format. Use YYYYMM (e.g., 202509)'
                }, status=400)
            
            # Get province info
            try:
                province = edl_province_code.objects.get(pro_id=province_id)
            except edl_province_code.DoesNotExist:
                return JsonResponse({
                    'error': f'Province with ID {province_id} not found'
                }, status=404)
            
            # Get districts for this province
            districts = edl_district_code.objects.filter(pro_id=province_id)
            
            if not districts.exists():
                return JsonResponse({
                    'error': f'No districts found for province {province_id}'
                }, status=404)
            
            created_count = 0
            
            # Create tracking records for each district
            for district in districts:
                tracking, created = UploadDataTracking.objects.get_or_create(
                    pro_id=district.pro_id,
                    dis_id=district.dis_id,
                    upload_month=month,
                    defaults={
                        'pro_name': province.pro_name,
                        'dis_name': district.dis_name,
                        'status': 'pending',
                        'user_upload': username
                    }
                )
                if created:
                    created_count += 1
            
            return JsonResponse({
                'message': f'Initialized {created_count} districts for {province.pro_name} - {month}',
                'total_districts': districts.count(),
                'created_count': created_count
            })
            
        except Exception as e:
            return JsonResponse({
                'error': f'Initialization failed: {str(e)}'
            }, status=500)

# Function-based alternative
@csrf_exempt
@require_http_methods(["POST"])
def initialize_districts_function(request):
    """Function-based view alternative"""
    try:
        # Parse JSON data
        data = json.loads(request.body.decode('utf-8'))
        
        month = data.get('month', timezone.now().strftime('%Y%m'))
        province_id = data.get('province_id')
        username = data.get('username', 'system')
        
        if not province_id:
            return JsonResponse({
                'error': 'province_id is required',
                'received_data': data
            }, status=400)
        
        # Rest of the logic same as above...
        # Get province
        try:
            province = edl_province_code.objects.get(pro_id=province_id)
        except edl_province_code.DoesNotExist:
            return JsonResponse({
                'error': f'Province with ID {province_id} not found'
            }, status=404)
        
        # Get districts and create tracking records
        districts = edl_district_code.objects.filter(pro_id=province_id)
        created_count = 0
        
        for district in districts:
            tracking, created = UploadDataTracking.objects.get_or_create(
                pro_id=district.pro_id,
                dis_id=district.dis_id,
                upload_month=month,
                defaults={
                    'pro_name': province.pro_name,
                    'dis_name': district.dis_name,
                    'status': 'pending',
                    'user_upload': username
                }
            )
            if created:
                created_count += 1
        
        return JsonResponse({
            'message': f'Initialized {created_count} districts for {province.pro_name} - {month}',
            'total_districts': districts.count(),
            'created_count': created_count
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Initialization failed: {str(e)}'}, status=500)
# Endf Point Test EDL ----------------------------------


from django.http import JsonResponse
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utility.models import UploadDataTracking, UploadLog

class DebugAPIView(APIView):
    """Debug view to check database state and models"""
    
    def get(self, request):
        debug_info = {}
        
        try:
            # Check if table exists
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT name FROM sqlite_master 
                    WHERE type='table' AND name='upload_data_tracking';
                """)
                table_exists = cursor.fetchone() is not None
                debug_info['table_exists'] = table_exists
                
                if table_exists:
                    # Get table structure
                    cursor.execute("PRAGMA table_info(upload_data_tracking);")
                    columns = cursor.fetchall()
                    debug_info['table_columns'] = [col[1] for col in columns]
                    
                    # Get record count
                    cursor.execute("SELECT COUNT(*) FROM upload_data_tracking;")
                    record_count = cursor.fetchone()[0]
                    debug_info['record_count'] = record_count
        
        except Exception as e:
            debug_info['table_error'] = str(e)
        
        try:
            # Test model query
            tracking_count = UploadDataTracking.objects.count()
            debug_info['model_count'] = tracking_count
            
            # Get sample records
            sample_records = UploadDataTracking.objects.all()[:3]
            debug_info['sample_records'] = [
                {
                    'id': record.id,
                    'pro_id': record.pro_id,
                    'pro_name': record.pro_name,
                    'dis_id': record.dis_id,
                    'dis_name': record.dis_name,
                    'upload_month': record.upload_month,
                    'status': record.status
                }
                for record in sample_records
            ]
            
        except Exception as e:
            debug_info['model_error'] = str(e)
        
        # Check current month format
        from django.utils import timezone
        current_month = timezone.now().strftime('%Y%m')
        debug_info['current_month'] = current_month
        
        # Check request parameters
        debug_info['request_params'] = dict(request.GET)
        
        return Response({
            'debug_info': debug_info,
            'status': 'debug_complete'
        })

class InitializeTestDataAPIView(APIView):
    """Create some test tracking records for debugging"""
    
    def post(self, request):
        try:
            month = request.data.get('month', '202509')
            
            # Sample test data
            test_districts = [
                {'pro_id': '01', 'pro_name': 'Vientiane Capital', 'dis_id': '01', 'dis_name': 'Chanthabouly'},
                {'pro_id': '01', 'pro_name': 'Vientiane Capital', 'dis_id': '02', 'dis_name': 'Sikhottabong'},
                {'pro_id': '01', 'pro_name': 'Vientiane Capital', 'dis_id': '03', 'dis_name': 'Xaysettha'},
                {'pro_id': '02', 'pro_name': 'Phongsaly', 'dis_id': '01', 'dis_name': 'Phongsaly'},
                {'pro_id': '02', 'pro_name': 'Phongsaly', 'dis_id': '02', 'dis_name': 'May'},
            ]
            
            created_count = 0
            for district_data in test_districts:
                tracking, created = UploadDataTracking.objects.get_or_create(
                    pro_id=district_data['pro_id'],
                    dis_id=district_data['dis_id'],
                    upload_month=month,
                    defaults={
                        'pro_name': district_data['pro_name'],
                        'dis_name': district_data['dis_name'],
                        'status': 'pending',
                        'user_upload': 'test_user',
                        'total_records': 0,
                        'processed_records': 0,
                        'failed_records': 0,
                        'data_size_mb': 0.0
                    }
                )
                if created:
                    created_count += 1
            
            return Response({
                'message': f'Created {created_count} test tracking records for month {month}',
                'total_records': UploadDataTracking.objects.filter(upload_month=month).count()
            })
            
        except Exception as e:
            return Response({
                'error': f'Failed to create test data: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestRealUploadAPIView(APIView):
    """Test real upload with EDL API"""
    
    def post(self, request):
        try:
            username = request.data.get('username', 'test_user')
            
            # Use the first test record for testing
            test_record = UploadDataTracking.objects.filter(status='pending').first()
            
            if not test_record:
                return Response({
                    'error': 'No pending test records found. Create test data first.'
                }, status=400)
            
            print(f"DEBUG: Testing upload for {test_record.pro_name} - {test_record.dis_name}")
            
            # Update status to in_progress
            test_record.status = 'in_progress'
            test_record.upload_started = timezone.now()
            test_record.user_upload = username
            test_record.save()
            
            # Log start
            UploadLog.objects.create(
                tracking=test_record,
                log_level='INFO',
                message=f'Test upload started by {username}'
            )
            
            # Test the real EDL API call
            result = self.test_edl_api_call(test_record, username)
            
            return Response(result)
            
        except Exception as e:
            return Response({
                'error': f'Test upload failed: {str(e)}'
            }, status=500)
    
    def test_edl_api_call(self, tracking, username):
        """Test actual EDL API call with real parameters"""
        try:
            import requests
            
            # Real EDL API endpoint
            api_url = "https://edl-inside-api.edl.com.la/api_v1/wattmonitor-bol/billing-svc/billing/getpaymenthistory"
            
            params = {
                'province_code': tracking.pro_id,
                'district_code': tracking.dis_id,
                'dateRequest': tracking.upload_month,
                'page': 1,
                'limit': 100  # Small limit for testing
            }
            
            print(f"DEBUG: Calling EDL API with params: {params}")
            
            # Make the actual API call
            response = requests.get(api_url, params=params, timeout=60)
            tracking.api_response_code = response.status_code
            
            print(f"DEBUG: EDL API Response Status: {response.status_code}")
            print(f"DEBUG: Response size: {len(response.text)} characters")
            
            if response.status_code == 200:
                data = response.json()
                
                # Log the response structure
                print(f"DEBUG: Response keys: {list(data.keys()) if isinstance(data, dict) else type(data)}")
                
                # Calculate data size
                data_size_mb = len(json.dumps(data).encode('utf-8')) / (1024 * 1024)
                
                # Extract records with flexible structure handling
                records = []
                if isinstance(data, dict):
                    if 'data' in data and 'paymentHistory' in data['data']:
                        records = data['data']['paymentHistory']
                    elif 'data' in data and isinstance(data['data'], list):
                        records = data['data']
                    elif 'paymentHistory' in data:
                        records = data['paymentHistory']
                    elif isinstance(data.get('data'), list):
                        records = data['data']
                elif isinstance(data, list):
                    records = data
                
                total_records = len(records)
                print(f"DEBUG: Extracted {total_records} records")
                
                # Log sample record structure if available
                if records and len(records) > 0:
                    sample_record = records[0]
                    print(f"DEBUG: Sample record keys: {list(sample_record.keys()) if isinstance(sample_record, dict) else type(sample_record)}")
                
                # Update tracking
                tracking.total_records = total_records
                tracking.data_size_mb = round(data_size_mb, 2)
                tracking.upload_completed = timezone.now()
                
                if total_records > 0:
                    tracking.status = 'completed'
                    # For testing, we'll simulate processing without actually saving to Electric_Bill
                    tracking.processed_records = min(total_records, 10)  # Simulate processing first 10 records
                    tracking.failed_records = 0
                    
                    message = f'Test completed successfully. Found {total_records} records, simulated processing of {tracking.processed_records} records'
                else:
                    tracking.status = 'completed'
                    tracking.processed_records = 0
                    tracking.failed_records = 0
                    message = 'Test completed - No records found for this location/month'
                
                tracking.save()
                
                # Log completion
                UploadLog.objects.create(
                    tracking=tracking,
                    log_level='INFO',
                    message=message
                )
                
                return {
                    'success': True,
                    'message': message,
                    'api_response': {
                        'status_code': response.status_code,
                        'total_records': total_records,
                        'data_size_mb': tracking.data_size_mb,
                        'response_structure': self.analyze_response_structure(data),
                        'sample_record_fields': list(records[0].keys()) if records else []
                    },
                    'tracking_info': {
                        'id': tracking.id,
                        'province': tracking.pro_name,
                        'district': tracking.dis_name,
                        'month': tracking.upload_month,
                        'duration_seconds': tracking.upload_duration
                    }
                }
            
            else:
                # Handle API errors
                tracking.status = 'failed'
                error_text = response.text[:500] if response.text else 'No response text'
                tracking.error_message = f'API returned status {response.status_code}: {error_text}'
                tracking.upload_completed = timezone.now()
                tracking.save()
                
                UploadLog.objects.create(
                    tracking=tracking,
                    log_level='ERROR',
                    message=f'API test failed: {response.status_code} - {error_text}'
                )
                
                return {
                    'success': False,
                    'error': f'EDL API returned status {response.status_code}',
                    'api_response': {
                        'status_code': response.status_code,
                        'error_text': error_text
                    }
                }
        
        except requests.exceptions.Timeout:
            tracking.status = 'failed'
            tracking.error_message = 'API request timeout'
            tracking.upload_completed = timezone.now()
            tracking.save()
            
            return {
                'success': False,
                'error': 'API request timeout after 60 seconds'
            }
            
        except requests.exceptions.ConnectionError:
            tracking.status = 'failed'
            tracking.error_message = 'Cannot connect to EDL API'
            tracking.upload_completed = timezone.now()
            tracking.save()
            
            return {
                'success': False,
                'error': 'Cannot connect to EDL API server'
            }
            
        except Exception as e:
            tracking.status = 'failed'
            tracking.error_message = f'Processing error: {str(e)}'
            tracking.upload_completed = timezone.now()
            tracking.save()
            
            UploadLog.objects.create(
                tracking=tracking,
                log_level='ERROR',
                message=f'Processing exception: {str(e)}'
            )
            
            return {
                'success': False,
                'error': f'Processing error: {str(e)}'
            }
    
    def analyze_response_structure(self, data):
        """Analyze and return the structure of API response"""
        if isinstance(data, dict):
            structure = {}
            for key, value in data.items():
                if isinstance(value, list) and len(value) > 0:
                    structure[key] = f"array[{len(value)}] of {type(value[0]).__name__}"
                elif isinstance(value, dict):
                    structure[key] = f"object with {len(value)} keys"
                else:
                    structure[key] = type(value).__name__
            return structure
        elif isinstance(data, list):
            return f"array[{len(data)}] of {type(data[0]).__name__ if data else 'unknown'}"
        else:
            return type(data).__name__
@csrf_exempt
def debug_edl_api(request):
    """Debug endpoint to test EDL API response parsing"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST method required'}, status=405)
    
    try:
        data = json.loads(request.body.decode('utf-8'))
        province_code = data.get('province_code')
        district_code = data.get('district_code') 
        date_request = data.get('dateRequest')
        
        if not all([province_code, district_code, date_request]):
            return JsonResponse({
                'error': 'Missing required parameters: province_code, district_code, dateRequest'
            }, status=400)
        
        # Make API call
        api_url = "https://edl-inside-api.edl.com.la/api_v1/wattmonitor-bol/billing-svc/billing/getpaymenthistory"
        params = {
            'province_code': province_code,
            'district_code': district_code,
            'dateRequest': date_request,
            'page': 1,
            'limit': 5  # Just get first 5 records for testing
        }
        
        response = requests.get(api_url, params=params, timeout=60)
        
        if response.status_code != 200:
            return JsonResponse({
                'error': f'API request failed with status {response.status_code}',
                'response_text': response.text
            }, status=response.status_code)
        
        # Parse response
        api_data = response.json()
        
        # Extract records using the new logic
        records = []
        if isinstance(api_data, dict):
            data_section = api_data.get('data', {})
            if isinstance(data_section, dict) and 'paymentHistory' in data_section:
                records = data_section.get('paymentHistory', [])
        
        # Get sample record info
        sample_record = records[0] if records else None
        sample_keys = list(sample_record.keys()) if sample_record else []
        
        return JsonResponse({
            'success': True,
            'api_status_code': response.status_code,
            'response_structure': {
                'type': str(type(api_data)),
                'top_level_keys': list(api_data.keys()) if isinstance(api_data, dict) else 'not a dict',
                'data_section_type': str(type(data_section)) if 'data_section' in locals() else 'not found',
                'data_section_keys': list(data_section.keys()) if isinstance(data_section, dict) else 'not a dict'
            },
            'records_info': {
                'total_found': len(records),
                'sample_record_keys': sample_keys,
                'sample_record': sample_record
            },
            'extraction_path': 'api_response["data"]["paymentHistory"]',
            'parameters_sent': params
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Debug failed: {str(e)}'}, status=500)


# EDL API Summarize Endpoint ----------------------------------

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, Count, Avg, Max, Min, Q
from django.db.models.functions import TruncMonth, TruncYear
from datetime import datetime, timedelta
from django.utils import timezone
import calendar
from utility.models import UploadDataTracking
from utility.models import Electric_Bill
from utility.models import edl_province_code, edl_district_code
import logging

logger = logging.getLogger(__name__)

class EDLSummaryOverviewAPIView(APIView):
    """Get overall EDL summary statistics"""
    
    def get(self, request):
        try:
            # Get query parameters
            start_month = request.GET.get('start_month')  # YYYYMM format
            end_month = request.GET.get('end_month')      # YYYYMM format
            province_id = request.GET.get('province_id')
            district_id = request.GET.get('district_id')
            
            # Build base queryset
            queryset = UploadDataTracking.objects.all()
            
            # Apply filters
            if start_month and end_month:
                queryset = queryset.filter(upload_month__gte=start_month, upload_month__lte=end_month)
            elif start_month:
                queryset = queryset.filter(upload_month__gte=start_month)
            elif end_month:
                queryset = queryset.filter(upload_month__lte=end_month)
            
            if province_id:
                queryset = queryset.filter(pro_id=province_id)
            
            if district_id:
                queryset = queryset.filter(dis_id=district_id)
            
            # Overall statistics
            overall_stats = queryset.aggregate(
                total_uploads=Count('id'),
                total_records=Sum('total_records'),
                total_processed=Sum('processed_records'),
                total_failed=Sum('failed_records'),
                total_data_size=Sum('data_size_mb'),
                avg_success_rate=Avg('success_rates'),
                completed_uploads=Count('id', filter=Q(status='completed')),
                failed_uploads=Count('id', filter=Q(status='failed')),
                in_progress_uploads=Count('id', filter=Q(status='in_progress'))
            )
            
            # Calculate derived metrics
            success_rate = (overall_stats['total_processed'] / overall_stats['total_records'] * 100) if overall_stats['total_records'] else 0
            completion_rate = (overall_stats['completed_uploads'] / overall_stats['total_uploads'] * 100) if overall_stats['total_uploads'] else 0
            
            # Monthly trends (last 12 months)
            monthly_trends = self.get_monthly_trends(queryset)
            
            # Province breakdown
            province_breakdown = self.get_province_breakdown(queryset)
            
            # Recent activity
            recent_activity = self.get_recent_activity()
            
            return Response({
                'overview': {
                    'total_uploads': overall_stats['total_uploads'] or 0,
                    'total_records': overall_stats['total_records'] or 0,
                    'total_processed': overall_stats['total_processed'] or 0,
                    'total_failed': overall_stats['total_failed'] or 0,
                    'total_data_size_mb': round(overall_stats['total_data_size'] or 0, 2),
                    'overall_success_rate': round(success_rate, 2),
                    'completion_rate': round(completion_rate, 2),
                    'completed_uploads': overall_stats['completed_uploads'] or 0,
                    'failed_uploads': overall_stats['failed_uploads'] or 0,
                    'in_progress_uploads': overall_stats['in_progress_uploads'] or 0
                },
                'monthly_trends': monthly_trends,
                'province_breakdown': province_breakdown,
                'recent_activity': recent_activity
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in EDL summary overview: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_monthly_trends(self, base_queryset):
        """Get monthly upload trends for the last 12 months"""
        try:
            # Get last 12 months
            end_date = datetime.now()
            start_date = end_date - timedelta(days=365)
            
            monthly_data = []
            for i in range(12):
                month_date = end_date - timedelta(days=30 * i)
                month_str = month_date.strftime('%Y%m')
                
                month_stats = base_queryset.filter(upload_month=month_str).aggregate(
                    total_records=Sum('total_records'),
                    total_processed=Sum('processed_records'),
                    total_uploads=Count('id'),
                    total_data_size=Sum('data_size_mb')
                )
                
                monthly_data.append({
                    'month': month_str,
                    'month_name': month_date.strftime('%b %Y'),
                    'total_records': month_stats['total_records'] or 0,
                    'total_processed': month_stats['total_processed'] or 0,
                    'total_uploads': month_stats['total_uploads'] or 0,
                    'total_data_size_mb': round(month_stats['total_data_size'] or 0, 2)
                })
            
            return list(reversed(monthly_data))
        except Exception as e:
            logger.error(f"Error getting monthly trends: {str(e)}")
            return []
    
    def get_province_breakdown(self, base_queryset):
        """Get breakdown by province"""
        try:
            province_stats = base_queryset.values('pro_id', 'pro_name').annotate(
                total_records=Sum('total_records'),
                total_processed=Sum('processed_records'),
                total_uploads=Count('id'),
                total_data_size=Sum('data_size_mb'),
                avg_success_rate=Avg('success_rates'),
                completed_uploads=Count('id', filter=Q(status='completed'))
            ).order_by('-total_records')
            
            return [
                {
                    'pro_id': item['pro_id'],
                    'pro_name': item['pro_name'],
                    'total_records': item['total_records'] or 0,
                    'total_processed': item['total_processed'] or 0,
                    'total_uploads': item['total_uploads'] or 0,
                    'total_data_size_mb': round(item['total_data_size'] or 0, 2),
                    'avg_success_rate': round(item['avg_success_rate'] or 0, 2),
                    'completed_uploads': item['completed_uploads'] or 0
                }
                for item in province_stats
            ]
        except Exception as e:
            logger.error(f"Error getting province breakdown: {str(e)}")
            return []
    
    def get_recent_activity(self):
        """Get recent upload activity"""
        try:
            recent_uploads = UploadDataTracking.objects.filter(
                upload_completed__isnull=False
            ).order_by('-upload_completed')[:10]
            
            return [
                {
                    'id': upload.id,
                    'pro_name': upload.pro_name,
                    'dis_name': upload.dis_name,
                    'upload_month': upload.upload_month,
                    'total_records': upload.total_records,
                    'status': upload.status,
                    'upload_completed': upload.upload_completed.isoformat() if upload.upload_completed else None,
                    'data_size_mb': round(upload.data_size_mb, 2),
                    'success_rate': round(upload.success_rates, 2) if upload.success_rates else 0
                }
                for upload in recent_uploads
            ]
        except Exception as e:
            logger.error(f"Error getting recent activity: {str(e)}")
            return []

class EDLSummaryByProvinceAPIView(APIView):
    """Get detailed summary by province"""
    
    def get(self, request):
        try:
            province_id = request.GET.get('province_id')
            start_month = request.GET.get('start_month')
            end_month = request.GET.get('end_month')
            
            if not province_id:
                return Response({'error': 'province_id is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Get province info
            try:
                province = edl_province_code.objects.get(pro_id=province_id)
            except edl_province_code.DoesNotExist:
                return Response({'error': 'Province not found'}, status=status.HTTP_404_NOT_FOUND)
            
            # Build queryset
            queryset = UploadDataTracking.objects.filter(pro_id=province_id)
            
            if start_month and end_month:
                queryset = queryset.filter(upload_month__gte=start_month, upload_month__lte=end_month)
            
            # Province summary
            province_summary = queryset.aggregate(
                total_uploads=Count('id'),
                total_records=Sum('total_records'),
                total_processed=Sum('processed_records'),
                total_failed=Sum('failed_records'),
                total_data_size=Sum('data_size_mb'),
                avg_success_rate=Avg('success_rates')
            )
            
            # District breakdown
            district_breakdown = queryset.values('dis_id', 'dis_name').annotate(
                total_records=Sum('total_records'),
                total_processed=Sum('processed_records'),
                total_uploads=Count('id'),
                total_data_size=Sum('data_size_mb'),
                avg_success_rate=Avg('success_rates'),
                completed_uploads=Count('id', filter=Q(status='completed'))
            ).order_by('-total_records')
            
            # Monthly breakdown for this province
            monthly_breakdown = self.get_province_monthly_data(queryset)
            
            return Response({
                'province_info': {
                    'pro_id': province.pro_id,
                    'pro_name': province.pro_name
                },
                'summary': {
                    'total_uploads': province_summary['total_uploads'] or 0,
                    'total_records': province_summary['total_records'] or 0,
                    'total_processed': province_summary['total_processed'] or 0,
                    'total_failed': province_summary['total_failed'] or 0,
                    'total_data_size_mb': round(province_summary['total_data_size'] or 0, 2),
                    'avg_success_rate': round(province_summary['avg_success_rate'] or 0, 2)
                },
                'district_breakdown': [
                    {
                        'dis_id': item['dis_id'],
                        'dis_name': item['dis_name'],
                        'total_records': item['total_records'] or 0,
                        'total_processed': item['total_processed'] or 0,
                        'total_uploads': item['total_uploads'] or 0,
                        'total_data_size_mb': round(item['total_data_size'] or 0, 2),
                        'avg_success_rate': round(item['avg_success_rate'] or 0, 2),
                        'completed_uploads': item['completed_uploads'] or 0
                    }
                    for item in district_breakdown
                ],
                'monthly_breakdown': monthly_breakdown
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in province summary: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_province_monthly_data(self, queryset):
        """Get monthly data for a specific province"""
        try:
            monthly_data = queryset.values('upload_month').annotate(
                total_records=Sum('total_records'),
                total_processed=Sum('processed_records'),
                total_uploads=Count('id'),
                total_data_size=Sum('data_size_mb')
            ).order_by('upload_month')
            
            return [
                {
                    'month': item['upload_month'],
                    'month_name': self.format_month_name(item['upload_month']),
                    'total_records': item['total_records'] or 0,
                    'total_processed': item['total_processed'] or 0,
                    'total_uploads': item['total_uploads'] or 0,
                    'total_data_size_mb': round(item['total_data_size'] or 0, 2)
                }
                for item in monthly_data
            ]
        except Exception as e:
            logger.error(f"Error getting province monthly data: {str(e)}")
            return []
    
    def format_month_name(self, month_str):
        """Convert YYYYMM to readable format"""
        try:
            if len(month_str) == 6:
                year = int(month_str[:4])
                month = int(month_str[4:6])
                return f"{calendar.month_abbr[month]} {year}"
        except:
            pass
        return month_str

class EDLSummaryByDistrictAPIView(APIView):
    """Get detailed summary by district"""
    
    def get(self, request):
        try:
            province_id = request.GET.get('province_id')
            district_id = request.GET.get('district_id')
            start_month = request.GET.get('start_month')
            end_month = request.GET.get('end_month')
            
            if not district_id:
                return Response({'error': 'district_id is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Debug logging
            logger.info(f"District summary request: district_id={district_id}, province_id={province_id}")
            
            # Get district info - MUST use both pro_id and dis_id for unique identification
            district = None
            try:
                if province_id:
                    # Use both province_id and district_id for unique identification
                    district = edl_district_code.objects.get(pro_id=province_id, dis_id=district_id)
                    logger.info(f"Found district by pro_id+dis_id: {district.dis_name}")
                else:
                    # If no province_id provided, we can't uniquely identify the district
                    return Response({
                        'error': 'province_id is required when district_id is provided',
                        'reason': f'District ID "{district_id}" exists in multiple provinces. Need province_id for unique identification.'
                    }, status=status.HTTP_400_BAD_REQUEST)
                    
            except edl_district_code.DoesNotExist:
                # Get available districts for this province for debugging
                available_districts = list(edl_district_code.objects.filter(
                    pro_id=province_id
                ).values_list('dis_id', 'dis_name'))
                
                return Response({
                    'error': f'District with ID "{district_id}" not found in province "{province_id}"',
                    'debug_info': {
                        'requested_district_id': district_id,
                        'requested_province_id': province_id,
                        'available_districts_in_province': available_districts
                    }
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Build queryset for tracking data using BOTH pro_id and dis_id
            queryset = UploadDataTracking.objects.filter(
                pro_id=province_id,
                dis_id=district_id
            )
            
            if start_month and end_month:
                queryset = queryset.filter(upload_month__gte=start_month, upload_month__lte=end_month)
            elif start_month:
                queryset = queryset.filter(upload_month__gte=start_month)
            elif end_month:
                queryset = queryset.filter(upload_month__lte=end_month)
            
            logger.info(f"Queryset count: {queryset.count()} records found for pro_id={province_id}, dis_id={district_id}")
            
            # District summary
            district_summary = queryset.aggregate(
                total_uploads=Count('id'),
                total_records=Sum('total_records'),
                total_processed=Sum('processed_records'),
                total_failed=Sum('failed_records'),
                total_data_size=Sum('data_size_mb'),
                avg_success_rate=Avg('success_rates')
            )
            
            # Monthly breakdown for this district
            monthly_breakdown = queryset.values('upload_month').annotate(
                total_records=Sum('total_records'),
                total_processed=Sum('processed_records'),
                total_uploads=Count('id'),
                total_data_size=Sum('data_size_mb'),
                success_rate=Avg('success_rates')
            ).order_by('upload_month')
            
            # Upload history
            upload_history = queryset.order_by('-upload_completed')[:20]
            
            return Response({
                'district_info': {
                    'dis_id': district.dis_id,
                    'dis_name': district.dis_name,
                    'pro_id': district.pro_id
                },
                'summary': {
                    'total_uploads': district_summary['total_uploads'] or 0,
                    'total_records': district_summary['total_records'] or 0,
                    'total_processed': district_summary['total_processed'] or 0,
                    'total_failed': district_summary['total_failed'] or 0,
                    'total_data_size_mb': round(district_summary['total_data_size'] or 0, 2),
                    'avg_success_rate': round(district_summary['avg_success_rate'] or 0, 2)
                },
                'monthly_breakdown': [
                    {
                        'month': item['upload_month'],
                        'month_name': EDLSummaryByProvinceAPIView().format_month_name(item['upload_month']),
                        'total_records': item['total_records'] or 0,
                        'total_processed': item['total_processed'] or 0,
                        'total_uploads': item['total_uploads'] or 0,
                        'total_data_size_mb': round(item['total_data_size'] or 0, 2),
                        'success_rate': round(item['success_rate'] or 0, 2)
                    }
                    for item in monthly_breakdown
                ],
                'upload_history': [
                    {
                        'id': upload.id,
                        'upload_month': upload.upload_month,
                        'total_records': upload.total_records,
                        'processed_records': upload.processed_records,
                        'status': upload.status,
                        'upload_completed': upload.upload_completed.isoformat() if upload.upload_completed else None,
                        'data_size_mb': round(upload.data_size_mb, 2),
                        'success_rate': round(upload.success_rates, 2) if upload.success_rates else 0,
                        'user_upload': upload.user_upload
                    }
                    for upload in upload_history
                ]
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in district summary: {str(e)}", exc_info=True)
            return Response({
                'error': f'Internal server error: {str(e)}',
                'debug_info': {
                    'district_id': request.GET.get('district_id'),
                    'province_id': request.GET.get('province_id'),
                    'error_type': type(e).__name__
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EDLExportSummaryAPIView(APIView):
    """Export summary data to different formats"""
    
    def post(self, request):
        try:
            export_type = request.data.get('export_type', 'overview')  # overview, province, district
            format_type = request.data.get('format', 'json')  # json, csv
            filters = request.data.get('filters', {})
            
            if export_type == 'overview':
                overview_view = EDLSummaryOverviewAPIView()
                mock_request = type('MockRequest', (), {'GET': filters})()
                response_data = overview_view.get(mock_request).data
            elif export_type == 'province':
                province_view = EDLSummaryByProvinceAPIView()
                mock_request = type('MockRequest', (), {'GET': filters})()
                response_data = province_view.get(mock_request).data
            elif export_type == 'district':
                district_view = EDLSummaryByDistrictAPIView()
                mock_request = type('MockRequest', (), {'GET': filters})()
                response_data = district_view.get(mock_request).data
            else:
                return Response({'error': 'Invalid export_type'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Add metadata
            export_data = {
                'export_info': {
                    'export_type': export_type,
                    'exported_at': timezone.now().isoformat(),
                    'filters_applied': filters
                },
                'data': response_data
            }
            
            return Response(export_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in export summary: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
# water supply data load tracking views ----------------------------------
import requests
import json
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, Count, Sum, Avg
from django.core.paginator import Paginator
from datetime import datetime
from django.conf import settings
import logging
from django.db import transaction
from utility.models import WaterUploadDataTracking, WaterUploadLog
from utility.models import Utility_Bill
from .serializers import (
    WaterUploadTrackingSerializer, 
    WaterUploadTrackingDetailSerializer,
)
import threading
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class WaterUploadTrackingListAPIView(APIView):
    """List water supply tracking records for specific month"""
    
    def get(self, request):
        try:        
            month = request.GET.get('month', timezone.now().strftime('%m%Y'))
            
            # Validate month format (MMYYYY)
            try:
                datetime.strptime(month, '%m%Y')
            except ValueError:
                return Response(
                    {"error": "Invalid month format. Use MMYYYY (e.g., 122024)"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Get tracking records for the specific month
            queryset = WaterUploadDataTracking.objects.filter(
                upload_month=month
            ).order_by('-created_at')
            
            # Serialize data
            serialized_data = []
            for item in queryset:
                data = WaterUploadTrackingSerializer(item).data
                data['success_rate_formatted'] = f"{item.success_rates:.1f}" if item.success_rates else "0.0"
                data['formatted_size'] = self.format_file_size(item.data_size_mb)
                data['upload_duration'] = self.format_duration(item.upload_duration) if item.upload_duration else None
                serialized_data.append(data)
            
            # Get statistics
            stats = self.get_statistics(month)
            
            return Response({
                'data': serialized_data,
                'statistics': stats
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Failed to fetch water tracking data: {str(e)}")
            return Response(
                {"error": "Failed to fetch water tracking data"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def get_statistics(self, month):
        """Calculate statistics for the dashboard"""
        try:
            queryset = WaterUploadDataTracking.objects.filter(upload_month=month)
            
            total_count = queryset.count()
            if total_count == 0:
                return {
                    'total_uploads': 0,
                    'status_breakdown': {},
                    'total_data_size_mb': 0.0,
                    'total_records': 0
                }
            
            # Status breakdown
            status_data = queryset.values('status').annotate(count=Count('id'))
            status_counts = {item['status']: item['count'] for item in status_data}
            
            # Aggregated data
            aggregated = queryset.aggregate(
                total_size=Sum('data_size_mb'),
                total_records=Sum('total_records')
            )
            
            return {
                'total_uploads': total_count,
                'status_breakdown': status_counts,
                'total_data_size_mb': round(float(aggregated['total_size'] or 0), 2),
                'total_records': int(aggregated['total_records'] or 0)
            }
            
        except Exception as e:
            logger.error(f"Error in get_statistics: {str(e)}")
            return {
                'total_uploads': 0,
                'status_breakdown': {},
                'total_data_size_mb': 0.0,
                'total_records': 0
            }
    
    def format_file_size(self, size_mb):
        """Format file size for display"""
        if not size_mb or size_mb < 1:
            return f"{(size_mb or 0) * 1024:.1f} KB"
        elif size_mb < 1024:
            return f"{size_mb:.1f} MB"
        else:
            return f"{size_mb / 1024:.1f} GB"
    
    def format_duration(self, seconds):
        """Format duration for display"""
        if not seconds:
            return None
        if seconds < 60:
            return f"{seconds:.0f}s"
        elif seconds < 3600:
            return f"{seconds / 60:.1f}m"
        else:
            return f"{seconds / 3600:.1f}h"

class InitializeWaterTrackingAPIView(APIView):
    """Initialize water supply tracking record for a specific month"""
    
    def post(self, request):
        try:
            month = request.data.get('month', timezone.now().strftime('%m%Y'))
            username = request.data.get('username', 'system')
            
            if not month:
                return Response(
                    {"error": "month is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            if not username:
                return Response(
                    {"error": "username is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validate month format (MMYYYY)
            try:
                datetime.strptime(month, '%m%Y')
            except ValueError:
                return Response(
                    {"error": "Invalid month format. Use MMYYYY (e.g., 122024)"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create tracking record for the month
            tracking, created = WaterUploadDataTracking.objects.get_or_create(
                upload_month=month,
                defaults={
                    'status': 'pending',
                    'user_upload': username,
                    'description': f'Water supply data upload for {month}'
                }
            )
            
            action = 'created' if created else 'already exists'
            
            return Response({
                'message': f'Water supply tracking for {month} {action}',
                'tracking_id': tracking.id,
                'created': created
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Water tracking initialization failed: {str(e)}")
            return Response({
                'error': f'Water tracking initialization failed: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WaterUploadDataAPIView(APIView):
    """Handle water supply data upload with background processing for large datasets"""
    
    def post(self, request):
        try:
            # Extract parameters
            month = request.data.get('month')
            username = request.data.get('username', 'system')
            api_token = request.data.get('api_token')  # Optional - we use fixed token

            # Fixed API token from supplier
            api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IlUyRnNkR1ZrWDErdE9ja29vVDV0NXdqWlBqTzhVc0V1ZnR2QytPUXp3Z2ljWkFPdkhNUkNqdzh0NUhOSENBRVZsVXVNWHBrc1RudUFxaUE3R0VtVExRSTZMaWNTVUlaN1BMb0xGOVczMWtjWnFoQmxFUThHVUFwSFpNS0NDVjN1RURhWDJSSjFwZDNqaFRGc2lmdUF3Zz09IiwiaWF0IjoxNzA5MDEwNjU0fQ.mhmfUuasPQnAtxTQmwIyofClMuOAKVKZloNskpG9fHo'
                        
            if not month:
                return Response({
                    'error': 'Missing required parameter: month'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Validate month format (MMYYYY)
            try:
                datetime.strptime(month, '%m%Y')
            except ValueError:
                return Response(
                    {"error": "Invalid month format. Use MMYYYY (e.g., 122024)"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Get tracking record
            try:
                tracking = WaterUploadDataTracking.objects.get(upload_month=month)
            except WaterUploadDataTracking.DoesNotExist:
                return Response({
                    'error': 'Tracking record not found. Please initialize tracking first.'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Check if already completed
            if tracking.status == 'completed':
                return Response({
                    'message': 'Water supply data already uploaded successfully',
                    'tracking_id': tracking.id,
                    'total_records': tracking.total_records,
                    'processed_records': tracking.processed_records
                }, status=status.HTTP_200_OK)
            
            # Check if already in progress
            if tracking.status == 'in_progress':
                return Response({
                    'message': 'Water supply data upload is already in progress',
                    'tracking_id': tracking.id,
                    'status': tracking.status
                }, status=status.HTTP_200_OK)
            
            # Update status to in_progress
            tracking.status = 'in_progress'
            tracking.upload_started = timezone.now()
            tracking.user_upload = username
            tracking.error_message = None  # Clear any previous errors
            tracking.save()
            
            # Log start
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Water supply upload started by {username} for month {month}'
            )
            
            # Start background processing for large datasets
            thread = threading.Thread(
                target=self.process_water_data_background,
                args=(tracking.id, api_token)
            )
            thread.daemon = True
            thread.start()
            
            return Response({
                'message': 'Water supply data upload started in background',
                'tracking_id': tracking.id,
                'status': 'in_progress',
                'note': 'Large dataset processing initiated. Check tracking status for updates.'
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Water upload failed: {str(e)}")
            return Response({
                'error': f'Water upload failed: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def process_water_data_background(self, tracking_id, api_token):
        """Background processing for large water supply datasets"""
        try:
            tracking = WaterUploadDataTracking.objects.get(id=tracking_id)
            
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message='Background processing started for water supply data'
            )
            
            # Fetch and process data with optimized handling
            result = self.fetch_and_process_water_data_optimized(tracking, api_token)
            
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Background processing completed: {result.get("message", "Unknown result")}'
            )
            
        except Exception as e:
            logger.error(f"Background water processing failed: {str(e)}")
            try:
                tracking = WaterUploadDataTracking.objects.get(id=tracking_id)
                tracking.status = 'failed'
                tracking.error_message = f'Background processing failed: {str(e)}'
                tracking.upload_completed = timezone.now()
                tracking.save()
                
                WaterUploadLog.objects.create(
                    tracking=tracking,
                    log_level='ERROR',
                    message=f'Background processing failed: {str(e)}'
                )
            except Exception as save_error:
                logger.error(f"Failed to save error state: {str(save_error)}")


# Updated fetch_and_process_water_data_optimized method
def fetch_and_process_water_data_optimized(self, tracking, api_token):
    """Optimized fetch for large water supply datasets with customer data"""
    try:
        water_api_base = getattr(settings, 'WATER_API_BASE_URL', 'http://202.137.141.244:3000')
        
        # Water Bill API endpoint
        bill_api_url = f"{water_api_base}/v3/api/loans/allbillmonth/{tracking.upload_month}"
        
        # Customer API endpoint
        customer_api_url = f"{water_api_base}/v3/api/loans/newconnection/{tracking.upload_month}"
        
        headers = {
            'Auth': api_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Connection': 'close'
        }
        
        # ========== Fetch Bill Data ==========
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='INFO',
            message=f'Fetching water bill data from: {bill_api_url}'
        )
        
        bill_response = requests.get(
            bill_api_url, 
            headers=headers, 
            timeout=600,
            stream=True
        )
        
        tracking.api_response_code = bill_response.status_code
        tracking.save()
        
        if bill_response.status_code != 200:
            error_msg = f'Water Bill API failed with status {bill_response.status_code}'
            try:
                error_content = bill_response.text[:1000]
                error_msg += f': {error_content}'
            except:
                pass
            raise Exception(error_msg)
        
        # Process bill response
        content = bill_response.content
        bill_response.close()
        
        content_size_mb = len(content) / (1024 * 1024)
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='INFO',
            message=f'Received {content_size_mb:.2f} MB of bill data'
        )
        
        try:
            bill_data = json.loads(content.decode('utf-8'))
        except json.JSONDecodeError as e:
            raise Exception(f'Invalid JSON response from Water Bill API: {str(e)}')
        
        # Extract bill records
        bill_records = self.extract_water_records(bill_data, tracking, 'bill')
        
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='INFO',
            message=f'Extracted {len(bill_records)} bill records'
        )
        
        # ========== Fetch Customer Data ==========
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='INFO',
            message=f'Fetching water customer data from: {customer_api_url}'
        )
        
        customer_records = []
        customer_error = None
        
        try:
            customer_response = requests.get(
                customer_api_url,
                headers=headers,
                timeout=600,
                stream=True
            )
            
            if customer_response.status_code != 200:
                customer_error = f'Customer API returned status {customer_response.status_code}'
                WaterUploadLog.objects.create(
                    tracking=tracking,
                    log_level='WARNING',
                    message=customer_error
                )
            else:
                customer_content = customer_response.content
                customer_response.close()
                
                customer_size_mb = len(customer_content) / (1024 * 1024)
                WaterUploadLog.objects.create(
                    tracking=tracking,
                    log_level='INFO',
                    message=f'Received {customer_size_mb:.2f} MB of customer data'
                )
                
                try:
                    customer_data = json.loads(customer_content.decode('utf-8'))
                    customer_records = self.extract_water_records(customer_data, tracking, 'customer')
                    
                    WaterUploadLog.objects.create(
                        tracking=tracking,
                        log_level='INFO',
                        message=f'Extracted {len(customer_records)} customer records'
                    )
                except json.JSONDecodeError as e:
                    customer_error = f'Invalid JSON from Customer API: {str(e)}'
                    WaterUploadLog.objects.create(
                        tracking=tracking,
                        log_level='ERROR',
                        message=customer_error
                    )
        
        except requests.exceptions.Timeout:
            customer_error = 'Customer API request timed out after 10 minutes'
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='ERROR',
                message=customer_error
            )
        
        except requests.exceptions.RequestException as e:
            customer_error = f'Customer API request failed: {str(e)}'
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='ERROR',
                message=customer_error
            )
        
        except Exception as e:
            customer_error = f'Unexpected error fetching customer data: {str(e)}'
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='ERROR',
                message=customer_error
            )
        
        # ========== Process Data ==========
        bill_processed = 0
        bill_failed = 0
        customer_processed = 0
        customer_failed = 0
        
        # Process bill records
        if bill_records:
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Processing {len(bill_records)} bill records'
            )
            bill_processed, bill_failed = self.insert_water_bill_data_optimized(
                bill_records, tracking
            )
        
        # Process customer records
        if customer_records:
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Processing {len(customer_records)} customer records'
            )
            customer_processed, customer_failed = self.insert_water_customer_info_data(
                customer_records, tracking
            )
        elif customer_error:
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='WARNING',
                message=f'Skipping customer data processing: {customer_error}'
            )
        
        # Calculate totals
        total_records = len(bill_records) + len(customer_records)
        total_processed = bill_processed + customer_processed
        total_failed = bill_failed + customer_failed
        
        # Determine status
        if total_failed == 0 and not customer_error:
            final_status = 'completed'
        elif bill_processed > 0 and customer_error:
            final_status = 'partial'
        elif total_failed > 0:
            final_status = 'partial'
        else:
            final_status = 'failed'
        
        # Update tracking
        tracking.status = final_status
        tracking.upload_completed = timezone.now()
        tracking.total_records = total_records
        tracking.processed_records = total_processed
        tracking.failed_records = total_failed
        tracking.data_size_mb = round(content_size_mb, 2)
        tracking.success_rates = (total_processed / total_records * 100) if total_records > 0 else 0
        tracking.save()
        
        # Calculate duration
        duration = None
        if tracking.upload_started and tracking.upload_completed:
            duration = (tracking.upload_completed - tracking.upload_started).total_seconds()
        
        message = f'Water upload completed - Bills: {bill_processed}/{len(bill_records)}, Customers: {customer_processed}/{len(customer_records)}'
        if customer_error:
            message += f' (Customer API Error: {customer_error})'
        
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='INFO' if final_status == 'completed' else 'WARNING',
            message=message
        )
        
        return {
            'message': 'Water supply data upload completed' + (' with warnings' if customer_error else ' successfully'),
            'tracking_id': tracking.id,
            'status': final_status,
            'bill_records': {
                'total': len(bill_records),
                'processed': bill_processed,
                'failed': bill_failed
            },
            'customer_records': {
                'total': len(customer_records),
                'processed': customer_processed,
                'failed': customer_failed,
                'error': customer_error
            },
            'data_size_mb': tracking.data_size_mb,
            'success_rate': tracking.success_rates,
            'upload_duration': duration
        }
        
    except Exception as e:
        tracking.status = 'failed'
        tracking.error_message = str(e)
        tracking.upload_completed = timezone.now()
        tracking.save()
        
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='ERROR',
            message=f'Water supply processing failed: {str(e)}'
        )
        
        return {
            'error': f'Failed to process water supply data: {str(e)}',
            'tracking_id': tracking.id,
            'status': 'failed'
        }


def extract_water_records(self, data, tracking, data_type):
    """Extract records from water supply API response"""
    records = []
    
    if isinstance(data, dict):
        # Log structure
        top_keys = list(data.keys())
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='INFO',
            message=f'{data_type.capitalize()} response keys: {top_keys}'
        )
        
        # Find data recursively
        def find_data_recursively(obj, path="root"):
            found_arrays = []
            if isinstance(obj, list):
                if len(obj) > 0:
                    found_arrays.append((path, len(obj), type(obj[0]).__name__))
            elif isinstance(obj, dict):
                for key, value in obj.items():
                    new_path = f"{path}.{key}"
                    if isinstance(value, list) and len(value) > 0:
                        found_arrays.append((new_path, len(value), type(value[0]).__name__))
                    elif isinstance(value, dict):
                        found_arrays.extend(find_data_recursively(value, new_path))
            return found_arrays
        
        found_arrays = find_data_recursively(data)
        
        if found_arrays:
            # Get largest array
            largest_array = max(found_arrays, key=lambda x: x[1])
            path, size, item_type = largest_array
            
            WaterUploadLog.objects.create(
                tracking=tracking,
                log_level='INFO',
                message=f'Using array at {path} with {size} items'
            )
            
            # Extract data
            try:
                current = data
                for part in path.split('.')[1:]:
                    current = current[part]
                if isinstance(current, list):
                    records = current
            except (KeyError, TypeError, IndexError) as e:
                WaterUploadLog.objects.create(
                    tracking=tracking,
                    log_level='ERROR',
                    message=f'Failed to extract from {path}: {str(e)}'
                )
        
        # Fallback to common keys
        if not records:
            common_keys = ['data', 'records', 'bills', 'items', 'results', 'customers', 'newconnection']
            for key in common_keys:
                if key in data and isinstance(data[key], list):
                    records = data[key]
                    WaterUploadLog.objects.create(
                        tracking=tracking,
                        log_level='INFO',
                        message=f'Found data using key: {key}'
                    )
                    break
    
    elif isinstance(data, list):
        records = data
    
    return records


def insert_water_customer_info_data(self, records, tracking):
    """Insert or update water customer records in w_customer_info table"""
    processed_count = 0
    failed_count = 0
    
    try:
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='INFO',
            message=f'Starting to process {len(records)} water customer records'
        )
        
        batch_size = 500
        for i in range(0, len(records), batch_size):
            batch = records[i:i + batch_size]
            
            for j, item in enumerate(batch):
                try:
                    if not isinstance(item, dict):
                        failed_count += 1
                        continue
                    
                    def safe_get(key, default=''):
                        value = item.get(key, default)
                        return value if value is not None else default
                    
                    customer_id = self.truncate(safe_get('CUSTOMER_ID', ''), 100)
                    
                    if not customer_id:
                        failed_count += 1
                        continue
                    
                    # Map API fields to model - adjust these based on actual API response
                    customer, created = w_customer_info.objects.update_or_create(
                        Customer_ID=customer_id,
                        defaults={
                            'No': self.truncate(safe_get('NO', safe_get('INDEX_NO', '')), 100),
                            'Company_name': self.truncate(safe_get('COMPANY_NAME', ''), 100),
                            'Name': self.truncate(safe_get('NAME', safe_get('GIVEN_NAME', '')), 100),
                            'Surname': self.truncate(safe_get('SURNAME', safe_get('FAMILY_NAME', '')), 100),
                            'National_ID': self.truncate(safe_get('NATIONAL_ID', safe_get('ID_NO', '')), 100),
                            'Passport': self.truncate(safe_get('PASSPORT', safe_get('PASSPORT_NO', '')), 100),
                            'Address': self.truncate(safe_get('ADDRESS', safe_get('FORW_ADDRESS', '')), 100),
                            'Dustrict_ID': self.truncate(safe_get('DISTRICT_ID', safe_get('DIS_ID', '')), 100),
                            'Province_ID': self.truncate(safe_get('PROVINCE_ID', safe_get('PRO_ID', '')), 100),
                            'Tel': self.truncate(safe_get('TEL', safe_get('TEL_NO', '')), 100),
                            'Email': self.truncate(safe_get('EMAIL', safe_get('EMAIL_NO', '')), 100),
                            'Cus_type': self.truncate(safe_get('CUSTOMER_TYPE', safe_get('SUPPLY_TYPE', '')), 100),
                            'Regis_date': self.truncate(safe_get('REGISTRATION_DATE', safe_get('REGIT_D', '')), 100)
                        }
                    )
                    
                    processed_count += 1
                
                except Exception as e:
                    failed_count += 1
                    if failed_count <= 10:
                        WaterUploadLog.objects.create(
                            tracking=tracking,
                            log_level='ERROR',
                            message=f'Failed to process customer record {i+j}: {str(e)}'
                        )
                    continue
            
            # Log progress
            if (i + batch_size) % 1000 == 0 or (i + batch_size) >= len(records):
                WaterUploadLog.objects.create(
                    tracking=tracking,
                    log_level='INFO',
                    message=f'Customer records progress: {min(i + batch_size, len(records))}/{len(records)}'
                )
        
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='INFO',
            message=f'Customer data processing completed. Processed: {processed_count}, Failed: {failed_count}'
        )
        
        return processed_count, failed_count
        
    except Exception as e:
        WaterUploadLog.objects.create(
            tracking=tracking,
            log_level='ERROR',
            message=f'Customer data insert failed: {str(e)}'
        )
        raise e


class WaterUploadTrackingDetailAPIView(APIView):
    """Get detailed water supply tracking information with logs"""
    
    def get(self, request, tracking_id):
        try:
            tracking = WaterUploadDataTracking.objects.get(id=tracking_id)
            serializer = WaterUploadTrackingDetailSerializer(tracking)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except WaterUploadDataTracking.DoesNotExist:
            return Response(
                {'error': 'Water supply tracking record not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

# Debug Views
class WaterDebugAPIView(APIView):
    """Debug view for water supply API testing"""
    
    def get(self, request):
        debug_info = {}
        
        try:
            # Test model counts
            tracking_count = WaterUploadDataTracking.objects.count()
            bill_count = Utility_Bill.objects.count()
            
            debug_info['water_tracking_count'] = tracking_count
            debug_info['total_utility_bills'] = bill_count
            
            # Recent tracking records
            recent_tracking = WaterUploadDataTracking.objects.all()[:3]
            debug_info['recent_tracking'] = [
                {
                    'id': record.id,
                    'upload_month': record.upload_month,
                    'status': record.status,
                    'total_records': record.total_records,
                    'processed_records': record.processed_records,
                    'data_size_mb': record.data_size_mb,
                    'user_upload': record.user_upload
                }
                for record in recent_tracking
            ]
            
        except Exception as e:
            debug_info['model_error'] = str(e)
        
        # Current month
        current_month = timezone.now().strftime('%m%Y')
        debug_info['current_month'] = current_month
        debug_info['api_base_url'] = getattr(settings, 'WATER_API_BASE_URL', 'http://202.137.141.244:3000')
        
        return Response({
            'debug_info': debug_info,
            'status': 'water_debug_complete'
        })

class WaterAPITestView(APIView):
    """Test water supply API connection and response"""
    
    def post(self, request):
        try:
            month = request.data.get('month', timezone.now().strftime('%m%Y'))
            
            # Fixed API token
            api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IlUyRnNkR1ZrWDErdE9ja29vVDV0NXdqWlBqTzhVc0V1ZnR2QytPUXp3Z2ljWkFPdkhNUkNqdzh0NUhOSENBRVZsVXVNWHBrc1RudUFxaUE3R0VtVExRSTZMaWNTVUlaN1BMb0xGOVczMWtjWnFoQmxFUThHVUFwSFpNS0NDVjN1RURhWDJSSjFwZDNqaFRGc2lmdUF3Zz09IiwiaWF0IjoxNzA5MDEwNjU0fQ.mhmfUuasPQnAtxTQmwIyofClMuOAKVKZloNskpG9fHo'
            
            # API endpoint
            water_api_base = getattr(settings, 'WATER_API_BASE_URL', 'http://202.137.141.244:3000')
            api_url = f"{water_api_base}/v3/api/loans/allbillmonth/{month}"
            
            headers = {
                'Auth': api_token,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            
            # Test with shorter timeout and head request first
            try:
                # First, try a HEAD request to check if endpoint exists
                head_response = requests.head(api_url, headers=headers, timeout=30)
                
                return JsonResponse({
                    'success': True,
                    'api_url': api_url,
                    'head_status_code': head_response.status_code,
                    'head_headers': dict(head_response.headers),
                    'message': f'API endpoint accessible. HEAD request returned {head_response.status_code}',
                    'note': 'GET request not attempted due to large response size. Use upload endpoint for full processing.'
                })
                
            except requests.exceptions.Timeout:
                return JsonResponse({
                    'success': False,
                    'error': 'API request timeout (30 seconds)',
                    'api_url': api_url,
                    'suggestion': 'API may have large response. Use background upload process.'
                })
            except requests.exceptions.ConnectionError:
                return JsonResponse({
                    'success': False,
                    'error': 'Cannot connect to water supply API',
                    'api_url': api_url
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'API test failed: {str(e)}'
            })
            
            
# Water Supply Summary API Views -------------------------------------


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, Count, Avg, Max, Min, Q
from datetime import datetime, timedelta
from django.utils import timezone
import calendar
from utility.models import WaterUploadDataTracking, WaterUploadLog
from utility.models import Utility_Bill
import logging

logger = logging.getLogger(__name__)

class WaterSummaryOverviewAPIView(APIView):
    """Get overall Water Supply summary statistics"""
    
    def get(self, request):
        try:
            # Get query parameters
            start_month = request.GET.get('start_month')  # MMYYYY format
            end_month = request.GET.get('end_month')      # MMYYYY format
            
            # Build base queryset
            queryset = WaterUploadDataTracking.objects.all()
            
            # Apply month filters
            if start_month and end_month:
                queryset = queryset.filter(upload_month__gte=start_month, upload_month__lte=end_month)
            elif start_month:
                queryset = queryset.filter(upload_month__gte=start_month)
            elif end_month:
                queryset = queryset.filter(upload_month__lte=end_month)
            
            # Overall statistics
            overall_stats = queryset.aggregate(
                total_uploads=Count('id'),
                total_records=Sum('total_records'),
                total_processed=Sum('processed_records'),
                total_failed=Sum('failed_records'),
                total_data_size=Sum('data_size_mb'),
                avg_success_rate=Avg('success_rates'),
                completed_uploads=Count('id', filter=Q(status='completed')),
                failed_uploads=Count('id', filter=Q(status='failed')),
                in_progress_uploads=Count('id', filter=Q(status='in_progress')),
                partial_uploads=Count('id', filter=Q(status='partial'))
            )
            
            # Calculate derived metrics
            success_rate = (overall_stats['total_processed'] / overall_stats['total_records'] * 100) if overall_stats['total_records'] else 0
            completion_rate = (overall_stats['completed_uploads'] / overall_stats['total_uploads'] * 100) if overall_stats['total_uploads'] else 0
            
            # Monthly trends (last 12 months)
            monthly_trends = self.get_monthly_trends(queryset)
            
            # Recent activity
            recent_activity = self.get_recent_activity()
            
            # Monthly breakdown
            monthly_breakdown = self.get_monthly_breakdown(queryset)
            
            return Response({
                'overview': {
                    'total_uploads': overall_stats['total_uploads'] or 0,
                    'total_records': overall_stats['total_records'] or 0,
                    'total_processed': overall_stats['total_processed'] or 0,
                    'total_failed': overall_stats['total_failed'] or 0,
                    'total_data_size_mb': round(overall_stats['total_data_size'] or 0, 2),
                    'overall_success_rate': round(success_rate, 2),
                    'completion_rate': round(completion_rate, 2),
                    'completed_uploads': overall_stats['completed_uploads'] or 0,
                    'failed_uploads': overall_stats['failed_uploads'] or 0,
                    'in_progress_uploads': overall_stats['in_progress_uploads'] or 0,
                    'partial_uploads': overall_stats['partial_uploads'] or 0,
                    'avg_success_rate': round(overall_stats['avg_success_rate'] or 0, 2)
                },
                'monthly_trends': monthly_trends,
                'recent_activity': recent_activity,
                'monthly_breakdown': monthly_breakdown
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in Water summary overview: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_monthly_trends(self, base_queryset):
        """Get monthly upload trends for the last 12 months"""
        try:
            # Get last 12 months in MMYYYY format
            monthly_data = []
            current_date = datetime.now()
            
            for i in range(12):
                # Calculate month and year for i months ago
                month_date = datetime(current_date.year, current_date.month, 1) - timedelta(days=30*i)
                month_str = f"{month_date.month:02d}{month_date.year}"
                
                month_stats = base_queryset.filter(upload_month=month_str).aggregate(
                    total_records=Sum('total_records'),
                    total_processed=Sum('processed_records'),
                    total_uploads=Count('id'),
                    total_data_size=Sum('data_size_mb'),
                    avg_success_rate=Avg('success_rates')
                )
                
                monthly_data.append({
                    'month': month_str,
                    'month_name': month_date.strftime('%b %Y'),
                    'total_records': month_stats['total_records'] or 0,
                    'total_processed': month_stats['total_processed'] or 0,
                    'total_uploads': month_stats['total_uploads'] or 0,
                    'total_data_size_mb': round(month_stats['total_data_size'] or 0, 2),
                    'avg_success_rate': round(month_stats['avg_success_rate'] or 0, 2)
                })
            
            return list(reversed(monthly_data))
        except Exception as e:
            logger.error(f"Error getting monthly trends: {str(e)}")
            return []
    
    def get_monthly_breakdown(self, base_queryset):
        """Get detailed breakdown by month"""
        try:
            monthly_stats = base_queryset.values('upload_month').annotate(
                total_records=Sum('total_records'),
                total_processed=Sum('processed_records'),
                total_uploads=Count('id'),
                total_data_size=Sum('data_size_mb'),
                avg_success_rate=Avg('success_rates'),
                completed_uploads=Count('id', filter=Q(status='completed')),
                failed_uploads=Count('id', filter=Q(status='failed')),
                latest_upload=Max('upload_completed')
            ).order_by('-upload_month')
            
            return [
                {
                    'upload_month': item['upload_month'],
                    'month_name': self.format_month_name(item['upload_month']),
                    'total_records': item['total_records'] or 0,
                    'total_processed': item['total_processed'] or 0,
                    'total_uploads': item['total_uploads'] or 0,
                    'total_data_size_mb': round(item['total_data_size'] or 0, 2),
                    'avg_success_rate': round(item['avg_success_rate'] or 0, 2),
                    'completed_uploads': item['completed_uploads'] or 0,
                    'failed_uploads': item['failed_uploads'] or 0,
                    'latest_upload': item['latest_upload'].isoformat() if item['latest_upload'] else None
                }
                for item in monthly_stats
            ]
        except Exception as e:
            logger.error(f"Error getting monthly breakdown: {str(e)}")
            return []
    
    def get_recent_activity(self):
        """Get recent upload activity"""
        try:
            recent_uploads = WaterUploadDataTracking.objects.filter(
                upload_completed__isnull=False
            ).order_by('-upload_completed')[:15]
            
            return [
                {
                    'id': upload.id,
                    'upload_month': upload.upload_month,
                    'month_name': self.format_month_name(upload.upload_month),
                    'total_records': upload.total_records,
                    'processed_records': upload.processed_records,
                    'status': upload.status,
                    'upload_started': upload.upload_started.isoformat() if upload.upload_started else None,
                    'upload_completed': upload.upload_completed.isoformat() if upload.upload_completed else None,
                    'data_size_mb': round(upload.data_size_mb, 2) if upload.data_size_mb else 0,
                    'success_rate': round(upload.success_rates, 2) if upload.success_rates else 0,
                    'user_upload': upload.user_upload,
                    'upload_duration': upload.upload_duration
                }
                for upload in recent_uploads
            ]
        except Exception as e:
            logger.error(f"Error getting recent activity: {str(e)}")
            return []
    
    def format_month_name(self, month_str):
        """Convert MMYYYY to readable format"""
        try:
            if len(month_str) == 6:
                month = int(month_str[:2])
                year = int(month_str[2:])
                return f"{calendar.month_abbr[month]} {year}"
        except:
            pass
        return month_str

class WaterSummaryByMonthAPIView(APIView):
    """Get detailed summary for a specific month"""
    
    def get(self, request):
        try:
            month = request.GET.get('month')
            
            if not month:
                return Response({'error': 'month parameter is required (MMYYYY format)'}, 
                              status=status.HTTP_400_BAD_REQUEST)
            
            # Validate month format
            try:
                datetime.strptime(month, '%m%Y')
            except ValueError:
                return Response({'error': 'Invalid month format. Use MMYYYY (e.g., 122024)'}, 
                              status=status.HTTP_400_BAD_REQUEST)
            
            # Get tracking record for this month
            try:
                tracking = WaterUploadDataTracking.objects.get(upload_month=month)
            except WaterUploadDataTracking.DoesNotExist:
                return Response({'error': f'No tracking record found for month {month}'}, 
                              status=status.HTTP_404_NOT_FOUND)
            
            # Get detailed logs for this month
            logs = WaterUploadLog.objects.filter(
                tracking=tracking
            ).order_by('-timestamp')[:50]
            
            # Get utility bill count for this month
            bill_count = Utility_Bill.objects.filter(
                InvoiceMonth=month
            ).count()
            
            # Calculate processing stats
            processing_stats = {
                'upload_duration_minutes': round(tracking.upload_duration / 60, 2) if tracking.upload_duration else 0,
                'records_per_second': round(tracking.processed_records / tracking.upload_duration, 2) if tracking.upload_duration else 0,
                'data_processing_rate_mb_per_min': round((tracking.data_size_mb * 60) / tracking.upload_duration, 2) if tracking.upload_duration else 0
            }
            
            
            return Response({
                'month_info': {
                    'upload_month': tracking.upload_month,
                    'month_name': WaterSummaryOverviewAPIView().format_month_name(tracking.upload_month),
                    'description': tracking.description
                },
                'summary': {
                    'total_records': tracking.total_records,
                    'processed_records': tracking.processed_records,
                    'failed_records': tracking.failed_records,
                    'success_rate': round(tracking.success_rates, 2),
                    'data_size_mb': round(tracking.data_size_mb, 2),
                    'status': tracking.status,
                    'user_upload': tracking.user_upload,
                    'upload_started': tracking.upload_started.isoformat() if tracking.upload_started else None,
                    'upload_completed': tracking.upload_completed.isoformat() if tracking.upload_completed else None,
                    'upload_duration': tracking.upload_duration,
                    'api_response_code': tracking.api_response_code,
                    'error_message': tracking.error_message
                },
                'processing_stats': processing_stats,
                'database_stats': {
                    'utility_bills_count': bill_count
                },
                'logs': [
                    {
                        'id': log.id,
                        'timestamp': log.timestamp.isoformat(),
                        'log_level': log.log_level,
                        'message': log.message,
                        'context_data': log.context_data
                    }
                    for log in logs
                ]
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in water summary by month: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WaterSummaryExportAPIView(APIView):
    """Export water supply summary data"""
    
    def post(self, request):
        try:
            export_type = request.data.get('export_type', 'overview')  # overview, month
            format_type = request.data.get('format', 'json')  # json, csv
            filters = request.data.get('filters', {})
            
            if export_type == 'overview':
                overview_view = WaterSummaryOverviewAPIView()
                mock_request = type('MockRequest', (), {'GET': filters})()
                response_data = overview_view.get(mock_request).data
            elif export_type == 'month':
                month_view = WaterSummaryByMonthAPIView()
                mock_request = type('MockRequest', (), {'GET': filters})()
                response_data = month_view.get(mock_request).data
            else:
                return Response({'error': 'Invalid export_type. Use: overview, month'}, 
                              status=status.HTTP_400_BAD_REQUEST)
            
            # Add export metadata
            export_data = {
                'export_info': {
                    'export_type': export_type,
                    'exported_at': timezone.now().isoformat(),
                    'filters_applied': filters,
                    'data_source': 'Water Supply Tracking System'
                },
                'data': response_data
            }
            
            return Response(export_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in water summary export: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WaterSummaryStatsAPIView(APIView):
    """Get quick stats for dashboard widgets"""
    
    def get(self, request):
        try:
            # Get current month stats
            current_month = timezone.now().strftime('%m%Y')
            
            # Overall counts
            total_months = WaterUploadDataTracking.objects.count()
            completed_months = WaterUploadDataTracking.objects.filter(status='completed').count()
            total_utility_bills = Utility_Bill.objects.count()
            
            # Current month status
            current_month_tracking = None
            try:
                current_month_tracking = WaterUploadDataTracking.objects.get(upload_month=current_month)
            except WaterUploadDataTracking.DoesNotExist:
                pass
            
            # Recent 30 days activity
            thirty_days_ago = timezone.now() - timedelta(days=30)
            recent_activity = WaterUploadDataTracking.objects.filter(
                created_at__gte=thirty_days_ago
            ).count()
            
            # Data size trends (last 6 months)
            data_size_trend = []
            for i in range(6):
                month_date = datetime.now() - timedelta(days=30*i)
                month_str = f"{month_date.month:02d}{month_date.year}"
                
                month_data = WaterUploadDataTracking.objects.filter(
                    upload_month=month_str
                ).aggregate(total_size=Sum('data_size_mb'))
                
                data_size_trend.append({
                    'month': month_str,
                    'month_name': month_date.strftime('%b %Y'),
                    'data_size_mb': round(month_data['total_size'] or 0, 2)
                })
            
            return Response({
                'quick_stats': {
                    'total_months_tracked': total_months,
                    'completed_months': completed_months,
                    'completion_percentage': round((completed_months / total_months * 100), 1) if total_months else 0,
                    'total_utility_bills': total_utility_bills,
                    'recent_activity_30_days': recent_activity
                },
                'current_month': {
                    'month': current_month,
                    'month_name': WaterSummaryOverviewAPIView().format_month_name(current_month),
                    'has_tracking': current_month_tracking is not None,
                    'status': current_month_tracking.status if current_month_tracking else None,
                    'total_records': current_month_tracking.total_records if current_month_tracking else 0,
                    'data_size_mb': round(current_month_tracking.data_size_mb, 2) if current_month_tracking and current_month_tracking.data_size_mb else 0
                },
                'data_size_trend': list(reversed(data_size_trend))
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in water summary stats: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
