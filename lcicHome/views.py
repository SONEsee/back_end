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
from .models import EnterpriseInfo
from .serializers import EnterpriseInfoSerializer

class EnterpriseInfoSearch(APIView):
    def post(self, request):
        LCICID = request.data.get('LCICID')
        EnterpriseID = request.data.get('EnterpriseID')
        
        print("LCIC: ",LCICID)
        print("Enterpriseid: ",EnterpriseID)
        
        if LCICID is not None and EnterpriseID is not None:
            try:
                enterprise_info = EnterpriseInfo.objects.filter(LCICID=LCICID, EnterpriseID=EnterpriseID)
                investor_info = InvestorInfo.objects.filter(EnterpriseID=EnterpriseID)
                for i in investor_info:
                    invesinfo = i.investorName
                    # print(invesinfo)
                serializer = EnterpriseInfoSerializer(enterprise_info, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except EnterpriseInfo.DoesNotExist:
                return Response({'error': 'EnterpriseInfo not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'LCICID and EnterpriseID are required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
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



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import B1, B1_Monthly
# from datetime import datetime
# from django.utils import timezone

# @csrf_exempt
# def upload_files(request):
#     if request.method == 'POST':
#         try:
#             files = request.FILES.getlist('files')
#             for file in files:
#                 if file.name.endswith('.json'):
#                     data = json.load(file)
#                     for item in data:
#                         lon_open_date = timezone.make_aware(datetime.strptime(item.get('lon_open_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_open_date') else None
#                         lon_exp_date = timezone.make_aware(datetime.strptime(item.get('lon_exp_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_exp_date') else None
#                         lon_ext_date = timezone.make_aware(datetime.strptime(item.get('lon_ext_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_ext_date') else None
#                         lon_insert_date = timezone.make_aware(datetime.strptime(item.get('lon_insert_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_insert_date') else None
#                         lon_update_date = timezone.make_aware(datetime.strptime(item.get('lon_update_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_update_date') else None
#                         lon_applied_date = timezone.make_aware(datetime.strptime(item.get('lon_applied_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_applied_date') else None

#                         is_disputed = 1 if item.get('is_disputed', 0) else 0

#                         # Remove id if present
#                         if 'id' in item:
#                             del item['id']

#                         # print("ການສ້າງ B1_Monthly ໃໝ່:", item)

#                         B1_Monthly.objects.create(
#                             lcicID=item.get('lcicID', ),
#                             com_enterprise_code=item.get('com_enterprise_code'),
#                             segmentType=item.get('segmentType'),
#                             bnk_code=item.get('bnk_code'),
#                             customer_id=item.get('customer_id'),
#                             branch_id=item.get('branch_id'),
#                             lon_sys_id=item.get('lon_sys_id'),
#                             loan_id=item.get('loan_id'),
#                             lon_open_date=lon_open_date,
#                             lon_exp_date=lon_exp_date,
#                             lon_ext_date=lon_ext_date,
#                             lon_int_rate=item.get('lon_int_rate', 0),
#                             lon_purpose_code=item.get('lon_purpose_code'),
#                             lon_credit_line=item.get('lon_credit_line', 0),
#                             lon_currency_code=item.get('lon_currency_code'),
#                             lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                             lon_account_no=item.get('lon_account_no'),
#                             lon_no_days_slow=item.get('lon_no_days_slow'),
#                             lon_class=item.get('lon_class'),
#                             lon_type=item.get('lon_type'),
#                             lon_term=item.get('lon_term'),
#                             lon_status=item.get('lon_status'),
#                             lon_insert_date=lon_insert_date,
#                             lon_update_date=lon_update_date,
#                             lon_applied_date=lon_applied_date,
#                             is_disputed=is_disputed,
#                         )

#                         existing_record = B1.objects.filter(
#                             bnk_code=item.get('bnk_code'),
#                             branch_id=item.get('branch_id'),
#                             customer_id=item.get('customer_id'),
#                             loan_id=item.get('loan_id')
#                         ).first()

#                         if existing_record:
#                             existing_record.lcicID = item.get('lcicID', existing_record.lcicID)
#                             existing_record.com_enterprise_code = item.get('com_enterprise_code', existing_record.com_enterprise_code)
#                             existing_record.segmentType = item.get('segmentType', existing_record.segmentType)
#                             existing_record.lon_sys_id = item.get('lon_sys_id', existing_record.lon_sys_id)
#                             existing_record.lon_open_date = lon_open_date or existing_record.lon_open_date
#                             existing_record.lon_exp_date = lon_exp_date or existing_record.lon_exp_date
#                             existing_record.lon_ext_date = lon_ext_date or existing_record.lon_ext_date
#                             existing_record.lon_int_rate = item.get('lon_int_rate', existing_record.lon_int_rate)
#                             existing_record.lon_purpose_code = item.get('lon_purpose_code', existing_record.lon_purpose_code)
#                             existing_record.lon_credit_line = item.get('lon_credit_line', existing_record.lon_credit_line)
#                             existing_record.lon_currency_code = item.get('lon_currency_code', existing_record.lon_currency_code)
#                             existing_record.lon_outstanding_balance = item.get('lon_outstanding_balance', existing_record.lon_outstanding_balance)
#                             existing_record.lon_account_no = item.get('lon_account_no', existing_record.lon_account_no)
#                             existing_record.lon_no_days_slow = item.get('lon_no_days_slow', existing_record.lon_no_days_slow)
#                             existing_record.lon_class = item.get('lon_class', existing_record.lon_class)
#                             existing_record.lon_type = item.get('lon_type', existing_record.lon_type)
#                             existing_record.lon_term = item.get('lon_term', existing_record.lon_term)
#                             existing_record.lon_status = item.get('lon_status', existing_record.lon_status)
#                             existing_record.lon_insert_date = lon_insert_date or existing_record.lon_insert_date
#                             existing_record.lon_update_date = lon_update_date or existing_record.lon_update_date
#                             existing_record.lon_applied_date = lon_applied_date or existing_record.lon_applied_date
#                             existing_record.is_disputed = is_disputed
#                             existing_record.save()
#                         else:
#                             # print("ການສ້າງ B1 ໃໝ່:", item)
#                             B1.objects.create(
#                                 lcicID=item.get('lcicID', ''),
#                                 com_enterprise_code=item.get('com_enterprise_code'),
#                                 segmentType=item.get('segmentType'),
#                                 bnk_code=item.get('bnk_code'),
#                                 customer_id=item.get('customer_id'),
#                                 branch_id=item.get('branch_id'),
#                                 lon_sys_id=item.get('lon_sys_id'),
#                                 loan_id=item.get('loan_id'),
#                                 lon_open_date=lon_open_date,
#                                 lon_exp_date=lon_exp_date,
#                                 lon_ext_date=lon_ext_date,
#                                 lon_int_rate=item.get('lon_int_rate', 0),
#                                 lon_purpose_code=item.get('lon_purpose_code'),
#                                 lon_credit_line=item.get('lon_credit_line', 0),
#                                 lon_currency_code=item.get('lon_currency_code'),
#                                 lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                 lon_account_no=item.get('lon_account_no'),
#                                 lon_no_days_slow=item.get('lon_no_days_slow'),
#                                 lon_class=item.get('lon_class'),
#                                 lon_type=item.get('lon_type'),
#                                 lon_term=item.get('lon_term'),
#                                 lon_status=item.get('lon_status'),
#                                 lon_insert_date=lon_insert_date,
#                                 lon_update_date=lon_update_date,
#                                 lon_applied_date=lon_applied_date,
#                                 is_disputed=is_disputed,
#                             )

#             return JsonResponse({'message': 'Upload successful'}, status=200)

#         except Exception as e:
#             # print("Errorບອນໃດຫະ:", e)
#             return JsonResponse({'error': str(e)}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=400)


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# import math
# from .models import B1, B1_Monthly, Upload_File, memberInfo, User_Group, SType, Upload_Type
# from datetime import datetime
# from django.utils import timezone

# def human_readable_size(size_bytes): #/ຟັງຊັ້ນນີ້ກວດສອບວ່າຄ່າຂອງ Size_bytes ເທົ່າກັບສູນຫຼືບໍ່ຖ້າເທົ່າຈະຄືນຄ່າເປັນສູນ
#     if size_bytes == 0:
#         return "0B"
#     size_name = ("B", "KB", "MB", "GB", "TB") #size_name ຖືກສ້າງຂື້ນເພື່ອເກັບຮັກສາການວັດແທກຂະຫນາດໄຟລ໌ຕ່າງໆ, ຈາກ bytes (B) ເຖິງ terabytes (TB).
#     i = int(math.floor(math.log(size_bytes, 1024))) # ພື້ນຖານ 1024 logarithm ຂອງ size_bytes ຖືກຄິດໄລ່ໂດຍໃຊ້ math.log(size_bytes, 1024)math.floor ແມ່ນໃຊ້ເພື່ອປັດລົງໄປຫາຈຳນວນທີ່ໃກ້ທີ່ສຸດ. ນີ້ກໍານົດດັດຊະນີ i ສໍາລັບຫນ່ວຍງານນີ້ຊ່ວຍຄິດໄລ່ວ່າຫນ່ວຍໃດຂະຫນາດໄຟລ໌ຄວນຈະຢູ່ໃນ (bytes, kilobytes, megabytes, ແລະອື່ນໆ).
#     p = math.pow(1024, i) #ຖືກຄິດໄລ່ເປັນ 1024 ຍົກໃຫ້ກໍາລັງຂອງ i, ເຊິ່ງໃຫ້ຈໍານວນ bytes ໃນຫນ່ວຍງານທີ່ເຫມາະສົມ (ຕົວຢ່າງ, ຖ້າ i ເທົ່າກັບ 1, p ແມ່ນ 1024, ເຊິ່ງເປັນຈໍານວນ bytes ໃນກິໂລໄບ).
#     s = round(size_bytes / p, 2)   #size_bytes ຖືກແບ່ງໂດຍ p ເພື່ອປ່ຽນຂະຫນາດໄຟລ໌ເປັນຫນ່ວຍທີ່ເຫມາະສົມ. ຜົນໄດ້ຮັບຈະຖືກປັດເປັນສອງຕໍາແໜ່ງທົດສະນິຍົມໂດຍໃຊ້ຮອບ
#     return f"{s} {size_name[i]}"

# @csrf_exempt
# def upload_files(request):
#     if request.method == 'POST':
#         try:
#             user = request.user
#             files = request.FILES.getlist('files')
#             for file in files:
#                 if file.name.endswith('.json'):
#                     data = json.load(file)
#                     file_size = file.size
#                     file_size_hr = human_readable_size(file.size)  # Convert to human-readable size

#                     # ບັນທຶກຂໍ້ມູນການອັບໂຫລດໄຟລ໌
#                     upload_file = Upload_File.objects.create(
#                         fileName=file.name,
#                         fileSize=file_size_hr,  # Save the human-readable size
#                         path="uploadFiles/" + file.name,
#                         insertDate=timezone.now(),
#                         updateDate=timezone.now(),
#                         period="period_value",  # ປັບຕາມຄ່າທີ່ຕ້ອງການ
#                         status="status_value",  # ປັບຕາມຄ່າທີ່ຕ້ອງການ
#                         status_upload="status_upload_value",  # ປັບຕາມຄ່າທີ່ຕ້ອງການ
#                         FileType="json",  # ປັບຕາມຄ່າທີ່ຕ້ອງການ
#                         MID=user.memberinfo if hasattr(user, 'memberinfo') else None,
#                         GID=user.user_group if hasattr(user, 'user_group') else None,
#                         SType=user.stype if hasattr(user, 'stype') else None,
#                         UType=user.upload_type if hasattr(user, 'upload_type') else None,
#                     )

#                     for item in data:
#                         lon_open_date = timezone.make_aware(datetime.strptime(item.get('lon_open_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_open_date') else None
#                         lon_exp_date = timezone.make_aware(datetime.strptime(item.get('lon_exp_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_exp_date') else None
#                         lon_ext_date = timezone.make_aware(datetime.strptime(item.get('lon_ext_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_ext_date') else None
#                         lon_insert_date = timezone.make_aware(datetime.strptime(item.get('lon_insert_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_insert_date') else None
#                         lon_update_date = timezone.make_aware(datetime.strptime(item.get('lon_update_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_update_date') else None
#                         lon_applied_date = timezone.make_aware(datetime.strptime(item.get('lon_applied_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_applied_date') else None

#                         # ປ່ຽນຄ່າ is_disputed ເປັນຈໍານວນເຕັມ (0 ສໍາລັບ False, 1 ສໍາລັບ True)
#                         is_disputed = 1 if item.get('is_disputed', 0) else 0

#                         # ສ້າງບັນທຶກໃນ B1_Monthly
#                         B1_Monthly.objects.create(
#                             lcicID=item.get('lcicID', ''),
#                             # period=item.get('period', ''),
#                             com_enterprise_code=item.get('com_enterprise_code'),
#                             segmentType=item.get('segmentType'),
#                             bnk_code=item.get('bnk_code'),
#                             customer_id=item.get('customer_id'),
#                             branch_id=item.get('branch_id'),
#                             lon_sys_id=item.get('lon_sys_id'),
#                             loan_id=item.get('loan_id'),
#                             lon_open_date=lon_open_date,
#                             lon_exp_date=lon_exp_date,
#                             lon_ext_date=lon_ext_date,
#                             lon_int_rate=item.get('lon_int_rate', 0),
#                             lon_purpose_code=item.get('lon_purpose_code'),
#                             lon_credit_line=item.get('lon_credit_line', 0),
#                             lon_currency_code=item.get('lon_currency_code'),
#                             lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                             lon_account_no=item.get('lon_account_no'),
#                             lon_no_days_slow=item.get('lon_no_days_slow'),
#                             lon_class=item.get('lon_class'),
#                             lon_type=item.get('lon_type'),
#                             lon_term=item.get('lon_term'),
#                             lon_status=item.get('lon_status'),
#                             lon_insert_date=lon_insert_date,
#                             lon_update_date=lon_update_date,
#                             lon_applied_date=lon_applied_date,
#                             is_disputed=is_disputed,
#                         )

#                         # ກວດເບິ່ງແລະປັບປຸງຫຼືສ້າງບັນທຶກໃນ B1
#                         existing_record = B1.objects.filter(
#                             bnk_code=item.get('bnk_code'),
#                             branch_id=item.get('branch_id'),
#                             customer_id=item.get('customer_id'),
#                             loan_id=item.get('loan_id')
#                         ).first()

#                         if existing_record:
#                             existing_record.lcicID = item.get('lcicID', existing_record.lcicID)
#                             # existing_record.period = item.get('period', existing_record.period)
#                             existing_record.com_enterprise_code = item.get('com_enterprise_code', existing_record.com_enterprise_code)
#                             existing_record.segmentType = item.get('segmentType', existing_record.segmentType)
#                             existing_record.lon_sys_id = item.get('lon_sys_id', existing_record.lon_sys_id)
#                             existing_record.lon_open_date = lon_open_date or existing_record.lon_open_date
#                             existing_record.lon_exp_date = lon_exp_date or existing_record.lon_exp_date
#                             existing_record.lon_ext_date = lon_ext_date or existing_record.lon_ext_date
#                             existing_record.lon_int_rate = item.get('lon_int_rate', existing_record.lon_int_rate)
#                             existing_record.lon_purpose_code = item.get('lon_purpose_code', existing_record.lon_purpose_code)
#                             existing_record.lon_credit_line = item.get('lon_credit_line', existing_record.lon_credit_line)
#                             existing_record.lon_currency_code = item.get('lon_currency_code', existing_record.lon_currency_code)
#                             existing_record.lon_outstanding_balance = item.get('lon_outstanding_balance', existing_record.lon_outstanding_balance)
#                             existing_record.lon_account_no = item.get('lon_account_no', existing_record.lon_account_no)
#                             existing_record.lon_no_days_slow = item.get('lon_no_days_slow', existing_record.lon_no_days_slow)
#                             existing_record.lon_class = item.get('lon_class', existing_record.lon_class)
#                             existing_record.lon_type = item.get('lon_type', existing_record.lon_type)
#                             existing_record.lon_term = item.get('lon_term', existing_record.lon_term)
#                             existing_record.lon_status = item.get('lon_status', existing_record.lon_status)
#                             existing_record.lon_insert_date = lon_insert_date or existing_record.lon_insert_date
#                             existing_record.lon_update_date = lon_update_date or existing_record.lon_update_date
#                             existing_record.lon_applied_date = lon_applied_date or existing_record.lon_applied_date
#                             existing_record.is_disputed = is_disputed
#                             existing_record.save()
#                         else:
#                             B1.objects.create(
#                                 lcicID=item.get('lcicID', ''),
#                                 # period=item.get('period', ''),
#                                 com_enterprise_code=item.get('com_enterprise_code'),
#                                 segmentType=item.get('segmentType'),
#                                 bnk_code=item.get('bnk_code'),
#                                 customer_id=item.get('customer_id'),
#                                 branch_id=item.get('branch_id'),
#                                 lon_sys_id=item.get('lon_sys_id'),
#                                 loan_id=item.get('loan_id'),
#                                 lon_open_date=lon_open_date,
#                                 lon_exp_date=lon_exp_date,
#                                 lon_ext_date=lon_ext_date,
#                                 lon_int_rate=item.get('lon_int_rate', 0),
#                                 lon_purpose_code=item.get('lon_purpose_code'),
#                                 lon_credit_line=item.get('lon_credit_line', 0),
#                                 lon_currency_code=item.get('lon_currency_code'),
#                                 lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                 lon_account_no=item.get('lon_account_no'),
#                                 lon_no_days_slow=item.get('lon_no_days_slow'),
#                                 lon_class=item.get('lon_class'),
#                                 lon_type=item.get('lon_type'),
#                                 lon_term=item.get('lon_term'),
#                                 lon_status=item.get('lon_status'),
#                                 lon_insert_date=lon_insert_date,
#                                 lon_update_date=lon_update_date,
#                                 lon_applied_date=lon_applied_date,
#                                 is_disputed=is_disputed,
#                             )

#             return JsonResponse({'message': 'Upload successful'}, status=200)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=400)


# views.py
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




# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# import math
# from .models import B1, B1_Monthly, Upload_File, memberInfo, User_Group, SType, Upload_Type, EnterpriseInfo, B_Data_is_damaged, data_edit
# from datetime import datetime
# from django.utils import timezone
# import logging

# def human_readable_size(size_bytes):
#     if size_bytes == 0:
#         return "0B"
#     size_name = ("B", "KB", "MB", "GB", "TB")
#     i = int(math.floor(math.log(size_bytes, 1024)))
#     p = math.pow(1024, i)
#     s = round(size_bytes / p, 2)
#     return f"{s} {size_name[i]}"

# logger = logging.getLogger(__name__)

# @csrf_exempt
# def upload_files(request):
#     if request.method == 'POST':
#         try:
#             user = request.user
#             files = request.FILES.getlist('files')
#             warnings = []

#             for file in files:
#                 if file.name.endswith('.json'):
#                     data = json.load(file)
#                     file_size = file.size
#                     file_size_hr = human_readable_size(file.size)

#                     upload_file = Upload_File.objects.create(
#                         fileName=file.name,
#                         fileSize=file_size_hr,
#                         path="uploadFiles/" + file.name,
#                         insertDate=timezone.now(),
#                         updateDate=timezone.now(),
#                         period="period_value",
#                         status="status_value",
#                         status_upload="status_upload_value",
#                         FileType="json",
#                         MID=user.memberinfo if hasattr(user, 'memberinfo') else None,
#                         GID=user.user_group if hasattr(user, 'user_group') else None,
#                         SType=user.stype if hasattr(user, 'stype') else None,
#                         UType=user.upload_type if hasattr(user, 'upload_type') else None,
#                     )

#                     for item in data:
#                         com_enterprise_code = item.get('com_enterprise_code', '')
#                         lcicID = item.get('lcicID', '')

#                         # Check EnterpriseInfo
#                         enterprise_info = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first()
#                         if not enterprise_info:
#                             warnings.append(f'EnterpriseInfo with EnterpriseID {com_enterprise_code} not found')
#                             lcicID_error_status = 1 if lcicID != '' else 10
#                             com_enterprise_code_error_status = 20 if com_enterprise_code != '' else '02'

#                             B_Data_is_damaged.objects.create(
#                                 lcicID=lcicID,
#                                 period=item.get('period', ''),
#                                 com_enterprise_code=com_enterprise_code,
#                                 segmentType=item.get('segmentType', ''),
#                                 bnk_code=item.get('bnk_code', ''),
#                                 customer_id=item.get('customer_id', ''),
#                                 branch_id=item.get('branch_id', ''),
#                                 lon_sys_id=item.get('lon_sys_id', ''),
#                                 loan_id=item.get('loan_id', ''),
#                                 lon_open_date=item.get('lon_open_date', None),
#                                 lon_exp_date=item.get('lon_exp_date', None),
#                                 lon_ext_date=item.get('lon_ext_date', None),
#                                 lon_int_rate=item.get('lon_int_rate', 0),
#                                 lon_purpose_code=item.get('lon_purpose_code', ''),
#                                 lon_credit_line=item.get('lon_credit_line', 0),
#                                 lon_currency_code=item.get('lon_currency_code', ''),
#                                 lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                 lon_account_no=item.get('lon_account_no', ''),
#                                 lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                                 lon_class=item.get('lon_class', ''),
#                                 lon_type=item.get('lon_type', ''),
#                                 lon_term=item.get('lon_term', ''),
#                                 lon_status=item.get('lon_status', ''),
#                                 lon_insert_date=item.get('lon_insert_date', None),
#                                 lon_update_date=item.get('lon_update_date', None),
#                                 lon_applied_date=item.get('lon_applied_date', None),
#                                 is_disputed=item.get('is_disputed', 0),
#                                 lcicID_error=lcicID_error_status,
#                                 com_enterprise_code_error=com_enterprise_code_error_status,
#                             )
#                             continue

#                         if lcicID != enterprise_info.LCICID:
#                             lcicID = enterprise_info.LCICID

#                         data_edit.objects.create(
#                             lcicID=lcicID,
#                             period=item.get('period', ''),
#                             com_enterprise_code=com_enterprise_code,
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
#                         )

#                         lon_open_date = timezone.make_aware(datetime.strptime(item.get('lon_open_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_open_date') else None
#                         lon_exp_date = timezone.make_aware(datetime.strptime(item.get('lon_exp_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_exp_date') else None
#                         lon_ext_date = timezone.make_aware(datetime.strptime(item.get('lon_ext_date'), '%Y-%m-%d'), timezone.get_current_timezone()) if item.get('lon_ext_date') else None
#                         lon_insert_date = timezone.make_aware(datetime.strptime(item.get('lon_insert_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_insert_date') else None
#                         lon_update_date = timezone.make_aware(datetime.strptime(item.get('lon_update_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_update_date') else None
#                         lon_applied_date = timezone.make_aware(datetime.strptime(item.get('lon_applied_date'), '%Y-%m-%d %H:%M:%S'), timezone.get_current_timezone()) if item.get('lon_applied_date') else None

#                         is_disputed = 1 if item.get('is_disputed', 0) else 0

#                         B1_Monthly.objects.create(
#                             lcicID=lcicID,
#                             com_enterprise_code=item.get('com_enterprise_code'),
#                             segmentType=item.get('segmentType'),
#                             bnk_code=item.get('bnk_code'),
#                             customer_id=item.get('customer_id'),
#                             branch_id=item.get('branch_id'),
#                             lon_sys_id=item.get('lon_sys_id'),
#                             loan_id=item.get('loan_id'),
#                             lon_open_date=lon_open_date,
#                             lon_exp_date=lon_exp_date,
#                             lon_ext_date=lon_ext_date,
#                             lon_int_rate=item.get('lon_int_rate', 0),
#                             lon_purpose_code=item.get('lon_purpose_code'),
#                             lon_credit_line=item.get('lon_credit_line', 0),
#                             lon_currency_code=item.get('lon_currency_code'),
#                             lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                             lon_account_no=item.get('lon_account_no'),
#                             lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                             lon_class=item.get('lon_class'),
#                             lon_type=item.get('lon_type'),
#                             lon_term=item.get('lon_term'),
#                             lon_status=item.get('lon_status'),
#                             lon_insert_date=lon_insert_date,
#                             lon_update_date=lon_update_date,
#                             lon_applied_date=lon_applied_date,
#                             is_disputed=is_disputed,
#                         )

#                         existing_b1 = B1.objects.filter(
#                             bnk_code=item.get('bnk_code'),
#                             branch_id=item.get('branch_id'),
#                             customer_id=item.get('customer_id'),
#                             loan_id=item.get('loan_id')
#                         ).first()

#                         if existing_b1:
#                             existing_b1.lcicID = lcicID
#                             existing_b1.com_enterprise_code = item.get('com_enterprise_code')
#                             existing_b1.segmentType = item.get('segmentType')
#                             existing_b1.bnk_code = item.get('bnk_code')
#                             existing_b1.customer_id = item.get('customer_id')
#                             existing_b1.branch_id = item.get('branch_id')
#                             existing_b1.lon_sys_id = item.get('lon_sys_id')
#                             existing_b1.loan_id = item.get('loan_id')
#                             existing_b1.lon_open_date = lon_open_date
#                             existing_b1.lon_exp_date = lon_exp_date
#                             existing_b1.lon_ext_date = lon_ext_date
#                             existing_b1.lon_int_rate = item.get('lon_int_rate', 0)
#                             existing_b1.lon_purpose_code = item.get('lon_purpose_code')
#                             existing_b1.lon_credit_line = item.get('lon_credit_line', 0)
#                             existing_b1.lon_currency_code = item.get('lon_currency_code')
#                             existing_b1.lon_outstanding_balance = item.get('lon_outstanding_balance', 0)
#                             existing_b1.lon_account_no = item.get('lon_account_no')
#                             existing_b1.lon_no_days_slow = item.get('lon_no_days_slow', 0)
#                             existing_b1.lon_class = item.get('lon_class')
#                             existing_b1.lon_type = item.get('lon_type')
#                             existing_b1.lon_term = item.get('lon_term')
#                             existing_b1.lon_status = item.get('lon_status')
#                             existing_b1.lon_insert_date = lon_insert_date
#                             existing_b1.lon_update_date = lon_update_date
#                             existing_b1.lon_applied_date = lon_applied_date
#                             existing_b1.is_disputed = is_disputed
#                             existing_b1.save()
#                         else:
#                             B1.objects.create(
#                                 lcicID=lcicID,
#                                 com_enterprise_code=item.get('com_enterprise_code'),
#                                 segmentType=item.get('segmentType'),
#                                 bnk_code=item.get('bnk_code'),
#                                 customer_id=item.get('customer_id'),
#                                 branch_id=item.get('branch_id'),
#                                 lon_sys_id=item.get('lon_sys_id'),
#                                 loan_id=item.get('loan_id'),
#                                 lon_open_date=lon_open_date,
#                                 lon_exp_date=lon_exp_date,
#                                 lon_ext_date=lon_ext_date,
#                                 lon_int_rate=item.get('lon_int_rate', 0),
#                                 lon_purpose_code=item.get('lon_purpose_code'),
#                                 lon_credit_line=item.get('lon_credit_line', 0),
#                                 lon_currency_code=item.get('lon_currency_code'),
#                                 lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                 lon_account_no=item.get('lon_account_no'),
#                                 lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                                 lon_class=item.get('lon_class'),
#                                 lon_type=item.get('lon_type'),
#                                 lon_term=item.get('lon_term'),
#                                 lon_status=item.get('lon_status'),
#                                 lon_insert_date=lon_insert_date,
#                                 lon_update_date=lon_update_date,
#                                 lon_applied_date=lon_applied_date,
#                                 is_disputed=is_disputed,
#                             )
#             return JsonResponse({'status': 'success', 'warnings': warnings})
#         except Exception as e:
#             logger.exception("Failed to upload files")
#             return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)




# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser
# from django.urls import reverse
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
# from django.utils.decorators import method_decorator
# import requests

# from .models import File
# from .serializers import FileSerializer

# class FileUploadView3(generics.CreateAPIView):
#     queryset = File.objects.all()
#     serializer_class = FileSerializer
#     parser_classes = (MultiPartParser, FormParser)

#     @method_decorator(ensure_csrf_cookie)
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         files = request.FILES.getlist('file')
#         csrf_token = request.META.get('CSRF_COOKIE', '')

#         for file in files:
#             if file.name.endswith('.json'):
#                 upload_url = request.build_absolute_uri(reverse('upload_files'))
#                 with file.open('rb') as f:
#                     files_data = {'file': f}
#                     headers = {'X-CSRFToken': csrf_token}
#                     response = requests.post(upload_url, files=files_data, headers=headers)
#                     if response.status_code != 200:
#                         return JsonResponse({'status': 'error', 'message': 'Failed to process file'}, status=500)
#         return response
# views.py


# from rest_framework import generics
# from rest_framework.parsers import MultiPartParser, FormParser
# from django.urls import reverse
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.utils.decorators import method_decorator
# import requests

# from .models import Upload_File
# from .serializers import FileSerializer

# class FileUploadView3(generics.CreateAPIView):
#     queryset = Upload_File.objects.all()
#     serializer_class = FileSerializer
#     parser_classes = (MultiPartParser, FormParser)

#     @method_decorator(ensure_csrf_cookie)
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         files = request.FILES.getlist('file')
#         csrf_token = request.META.get('CSRF_COOKIE', '')

#         for file in files:
#             if file.name.endswith('.json'):
#                 try:
#                     period_parts = file.name.split('_,.json')[0].split('_')
#                     if len(period_parts) >= 4:
#                         period = period_parts[2] + "_" + period_parts[3]
#                     else:
#                         return JsonResponse({'status': 'error', 'message': 'ຮູບແບບຟາຍບໍ່ຖຶກຕອ້ງ'}, status=400)

#                     upload_file_instance = Upload_File.objects.create(
#                         fileName=file.name,
#                         fileSize=human_readable_size(file.size),
#                         path="uploadFiles/" + file.name,
#                         period=period,
#                         status="ກຳລັງອັບໂຫລດ",
#                         status_upload="ກຳລັງອັບໂຫລດ",
#                         FileType="json",
#                         MID=request.user.memberinfo if hasattr(request.user, 'memberinfo') else None,
#                         GID=request.user.user_group if hasattr(request.user, 'user_group') else None,
#                         SType=request.user.stype if hasattr(request.user, 'stype') else None,
#                         UType=request.user.upload_type if hasattr(request.user, 'upload_type') else None,
#                     )
#                     FID = upload_file_instance.FID

#                     upload_url = request.build_absolute_uri(reverse('upload_files'))
#                     with file.open('rb') as f:
#                         files_data = {'file': f}
#                         headers = {'X-CSRFToken': csrf_token}
#                         response = requests.post(upload_url, files=files_data, headers=headers, data={'period': period, 'FID': FID})
#                         if response.status_code != 200:
#                             upload_file_instance.status = "ອັບໂຫລດບໍ່ສຳເລັດ."
#                             upload_file_instance.status_upload = "ອັບໂຫລດບໍ່ສຳເລັດ."
#                             upload_file_instance.save()
#                             return JsonResponse({'status': 'error', 'message': 'ປະມວນຜົນໄຟລ໌ບໍ່ສຳເລັດ'}, status=500)

#                         upload_file_instance.status = "ອັບໂຫລດສຳເລັດແລ້ວ"
#                         upload_file_instance.status_upload = "ອັບໂຫລດສຳເລັດແລ້ວ"
#                         upload_file_instance.save()

#                 except IndexError:
#                     return JsonResponse({'status': 'error', 'message': 'ຮູບແບບຊື່ໄຟລ໌ບໍ່ຖືກຕ້ອງ.'}, status=400)

#         http_response = HttpResponse(response.content, status=response.status_code)
#         http_response.set_cookie('csrftoken', csrf_token)
#         return http_response
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# import math
# from .models import Upload_File, memberInfo, User_Group, SType, Upload_Type, EnterpriseInfo, B_Data_is_damaged, data_edit
# from datetime import datetime
# from django.utils import timezone
# import logging

# logger = logging.getLogger(__name__)

# def human_readable_size(size_bytes):
#     if size_bytes == 0:
#         return "0B"
#     size_name = ("B", "KB", "MB", "GB", "TB")
#     i = int(math.floor(math.log(size_bytes, 1024)))
#     p = math.pow(1024, i)
#     s = round(size_bytes / p, 2)
#     return f"{s} {size_name[i]}"

# @csrf_exempt
# def upload_files(request):
#     if request.method == 'POST':
#         try:
#             user = request.user
#             file = request.FILES.get('file')
#             warnings = []
#             period = request.POST.get('period')
#             FID = request.POST.get('FID')

#             if file and file.name.endswith('.json'):
#                 data = json.load(file)
#                 file_size = file.size
#                 file_size_hr = human_readable_size(file.size)

#                 upload_file = Upload_File.objects.get(FID=FID)
#                 upload_file.fileName = file.name
#                 upload_file.fileSize = file_size_hr
#                 upload_file.path = "uploadFiles/" + file.name
#                 upload_file.insertDate = timezone.now()
#                 upload_file.updateDate = timezone.now()
#                 upload_file.period = period
#                 upload_file.status = "ອັບໂຫຼດສຳເລັດແລ້ວ"
#                 upload_file.status_upload = "ອັບໂຫຼດສຳເລັດແລ້ວ"
#                 upload_file.FileType = "json"
#                 upload_file.MID = user.memberinfo if hasattr(user, 'memberinfo') else None
#                 upload_file.GID = user.user_group if hasattr(user, 'user_group') else None
#                 upload_file.SType = user.stype if hasattr(user, 'stype') else None
#                 upload_file.UType = user.upload_type if hasattr(user, 'upload_type') else None
#                 upload_file.save()

#                 total_count = len(data)
#                 error_count = 0

#                 for item in data:
#                     try:
#                         com_enterprise_code = item.get('com_enterprise_code', '')
#                         lcicID = item.get('lcicID', '')

#                         enterprise_info = EnterpriseInfo.objects.filter(
#                             EnterpriseID=com_enterprise_code
#                         ).first()

#                         def parse_and_make_aware(date_str):
#                             if date_str:
#                                 try:
#                                     dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
#                                     return timezone.make_aware(dt)
#                                 except ValueError:
#                                     return None
#                             return None

#                         lon_insert_date = parse_and_make_aware(item.get('lon_insert_date', None))
#                         lon_update_date = parse_and_make_aware(item.get('lon_update_date', None))
#                         lon_applied_date = parse_and_make_aware(item.get('lon_applied_date', None))

#                         if enterprise_info and (lcicID == enterprise_info.LCICID or com_enterprise_code == enterprise_info.EnterpriseID):
#                             # Update com_enterprise_code to be correct if it matches in EnterpriseInfo
#                             correct_com_enterprise_code = enterprise_info.EnterpriseID
#                             data_edit.objects.create(
#                                 lcicID=lcicID,
#                                 period=period,
#                                 com_enterprise_code=correct_com_enterprise_code,
#                                 segmentType=item.get('segmentType', ''),
#                                 bnk_code=item.get('bnk_code', ''),
#                                 customer_id=item.get('customer_id', ''),
#                                 branch_id=item.get('branch_id', ''),
#                                 lon_sys_id=item.get('lon_sys_id', ''),
#                                 loan_id=item.get('loan_id', ''),
#                                 lon_open_date=item.get('lon_open_date', None),
#                                 lon_exp_date=item.get('lon_exp_date', None),
#                                 lon_ext_date=item.get('lon_ext_date', None),
#                                 lon_int_rate=item.get('lon_int_rate', 0),
#                                 lon_purpose_code=item.get('lon_purpose_code', ''),
#                                 lon_credit_line=item.get('lon_credit_line', 0),
#                                 lon_currency_code=item.get('lon_currency_code', ''),
#                                 lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                 lon_account_no=item.get('lon_account_no', ''),
#                                 lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                                 lon_class=item.get('lon_class', ''),
#                                 lon_type=item.get('lon_type', ''),
#                                 lon_term=item.get('lon_term', ''),
#                                 lon_status=item.get('lon_status', ''),
#                                 lon_insert_date=lon_insert_date,
#                                 lon_update_date=lon_update_date,
#                                 lon_applied_date=lon_applied_date,
#                                 is_disputed=item.get('is_disputed', 0),
#                                 id_file=FID
#                             )
#                         else:
#                             error_count += 1
#                             B_Data_is_damaged.objects.create(
#                                 lcicID=lcicID,
#                                 period=period,
#                                 com_enterprise_code=com_enterprise_code,
#                                 segmentType=item.get('segmentType', ''),
#                                 bnk_code=item.get('bnk_code', ''),
#                                 customer_id=item.get('customer_id', ''),
#                                 branch_id=item.get('branch_id', ''),
#                                 lon_sys_id=item.get('lon_sys_id', ''),
#                                 loan_id=item.get('loan_id', ''),
#                                 lon_open_date=item.get('lon_open_date', None),
#                                 lon_exp_date=item.get('lon_exp_date', None),
#                                 lon_ext_date=item.get('lon_ext_date', None),
#                                 lon_int_rate=item.get('lon_int_rate', 0),
#                                 lon_purpose_code=item.get('lon_purpose_code', ''),
#                                 lon_credit_line=item.get('lon_credit_line', 0),
#                                 lon_currency_code=item.get('lon_currency_code', ''),
#                                 lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                 lon_account_no=item.get('lon_account_no', ''),
#                                 lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                                 lon_class=item.get('lon_class', ''),
#                                 lon_type=item.get('lon_type', ''),
#                                 lon_term=item.get('lon_term', ''),
#                                 lon_status=item.get('lon_status', ''),
#                                 lon_insert_date=lon_insert_date,
#                                 lon_update_date=lon_update_date,
#                                 lon_applied_date=lon_applied_date,
#                                 is_disputed=item.get('is_disputed', 0),
#                                 lcicID_error=1,
#                                 com_enterprise_code_error=None,    
#                                 id_file=FID
#                             )

#                     except Exception as e:
#                         logger.error(f"Error processing item: {e}")

#                 error_percentage = (error_count / total_count) * 100
#                 upload_file.percentage = error_percentage
#                 upload_file.save()

#                 return JsonResponse({'status': 'success', 'warnings': warnings})

#             return JsonResponse({'status': 'error', 'message': 'ໄຟລ໌ບໍ່ຖືກຕ້ອງ'}, status=400)

#         except Exception as e:
#             logger.error(f"Error uploading file: {e}")
#             return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# import math
# from .models import Upload_File, memberInfo, User_Group, SType, Upload_Type, EnterpriseInfo, B_Data_is_damaged, data_edit
# from datetime import datetime
# from django.utils import timezone
# import logging

# logger = logging.getLogger(__name__)

# def human_readable_size(size_bytes):
#     if size_bytes == 0:
#         return "0B"
#     size_name = ("B", "KB", "MB", "GB", "TB")
#     i = int(math.floor(math.log(size_bytes, 1024)))
#     p = math.pow(1024, i)
#     s = round(size_bytes / p, 2)
#     return f"{s} {size_name[i]}"

# @csrf_exempt
# def upload_files(request):
#     if request.method == 'POST':
#         try:
#             user = request.user
#             file = request.FILES.get('file')
#             warnings = []
#             period = request.POST.get('period')
#             FID = request.POST.get('FID')

#             if file and file.name.endswith('.json'):
#                 data = json.load(file)
#                 file_size = file.size
#                 file_size_hr = human_readable_size(file.size)

#                 upload_file = Upload_File.objects.get(FID=FID)
#                 upload_file.fileName = file.name
#                 upload_file.fileSize = file_size_hr
#                 upload_file.path = "uploadFiles/" + file.name
#                 upload_file.insertDate = timezone.now()
#                 upload_file.updateDate = timezone.now()
#                 upload_file.period = period
#                 upload_file.status = "ອັບໂຫຼດສຳເລັດແລ້ວ"
#                 upload_file.status_upload = "ອັບໂຫຼດສຳເລັດແລ້ວ"
#                 upload_file.FileType = "json"
#                 upload_file.MID = user.memberinfo if hasattr(user, 'memberinfo') else None
#                 upload_file.GID = user.user_group if hasattr(user, 'user_group') else None
#                 upload_file.SType = user.stype if hasattr(user, 'stype') else None
#                 upload_file.UType = user.upload_type if hasattr(user, 'upload_type') else None
#                 upload_file.save()

#                 total_count = len(data)
#                 error_count = 0

#                 for item in data:
#                     try:
#                         com_enterprise_code = item.get('com_enterprise_code', '')
#                         lcicID = item.get('lcicID', '')
#                         lcicID_info = EnterpriseInfo.objects.filter(
#                             LCICID=lcicID
#                         ).first()

#                         enterprise_info = EnterpriseInfo.objects.filter(
#                             EnterpriseID=com_enterprise_code
#                         ).first()
                        
                        

#                         def parse_and_make_aware(date_str):
#                             if date_str:
#                                 try:
#                                     dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
#                                     return timezone.make_aware(dt)
#                                 except ValueError:
#                                     return None
#                             return None

#                         lon_insert_date = parse_and_make_aware(item.get('lon_insert_date', None))
#                         lon_update_date = parse_and_make_aware(item.get('lon_update_date', None))
#                         lon_applied_date = parse_and_make_aware(item.get('lon_applied_date', None))

#                         if enterprise_info and (lcicID == enterprise_info.LCICID or com_enterprise_code == enterprise_info.EnterpriseID):
                           
#                             correct_com_enterprise_code = enterprise_info.EnterpriseID
#                             correct_lcicID = enterprise_info.LCICID
#                             data_edit.objects.create(
#                                 lcicID=correct_lcicID,
#                                 period=period,
#                                 com_enterprise_code=correct_com_enterprise_code,
#                                 segmentType=item.get('segmentType', ''),
#                                 bnk_code=item.get('bnk_code', ''),
#                                 customer_id=item.get('customer_id', ''),
#                                 branch_id=item.get('branch_id', ''),
#                                 lon_sys_id=item.get('lon_sys_id', ''),
#                                 loan_id=item.get('loan_id', ''),
#                                 lon_open_date=item.get('lon_open_date', None),
#                                 lon_exp_date=item.get('lon_exp_date', None),
#                                 lon_ext_date=item.get('lon_ext_date', None),
#                                 lon_int_rate=item.get('lon_int_rate', 0),
#                                 lon_purpose_code=item.get('lon_purpose_code', ''),
#                                 lon_credit_line=item.get('lon_credit_line', 0),
#                                 lon_currency_code=item.get('lon_currency_code', ''),
#                                 lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                 lon_account_no=item.get('lon_account_no', ''),
#                                 lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                                 lon_class=item.get('lon_class', ''),
#                                 lon_type=item.get('lon_type', ''),
#                                 lon_term=item.get('lon_term', ''),
#                                 lon_status=item.get('lon_status', ''),
#                                 lon_insert_date=lon_insert_date,
#                                 lon_update_date=lon_update_date,
#                                 lon_applied_date=lon_applied_date,
#                                 is_disputed=item.get('is_disputed', 0),
#                                 id_file=FID
#                             )
#                         elif enterprise_info and (com_enterprise_code  == enterprise_info.EnterpriseID or lcicID == enterprise_info.LCICID):

#                             correct_lcicID = lcicID_info.LCICID
#                             correct_com_enterprise_code = lcicID_info.EnterpriseID
                            
#                             data_edit.objects.create(
#                                 lcicID=correct_lcicID,
#                                 period=period,
#                                 com_enterprise_code=correct_com_enterprise_code,
#                                 segmentType=item.get('segmentType', ''),
#                                 bnk_code=item.get('bnk_code', ''),
#                                 customer_id=item.get('customer_id', ''),
#                                 branch_id=item.get('branch_id', ''),
#                                 lon_sys_id=item.get('lon_sys_id', ''),
#                                 loan_id=item.get('loan_id', ''),
#                                 lon_open_date=item.get('lon_open_date', None),
#                                 lon_exp_date=item.get('lon_exp_date', None),
#                                 lon_ext_date=item.get('lon_ext_date', None),
#                                 lon_int_rate=item.get('lon_int_rate', 0),
#                                 lon_purpose_code=item.get('lon_purpose_code', ''),
#                                 lon_credit_line=item.get('lon_credit_line', 0),
#                                 lon_currency_code=item.get('lon_currency_code', ''),
#                                 lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                 lon_account_no=item.get('lon_account_no', ''),
#                                 lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                                 lon_class=item.get('lon_class', ''),
#                                 lon_type=item.get('lon_type', ''),
#                                 lon_term=item.get('lon_term', ''),
#                                 lon_status=item.get('lon_status', ''),
#                                 lon_insert_date=lon_insert_date,
#                                 lon_update_date=lon_update_date,
#                                 lon_applied_date=lon_applied_date,
#                                 is_disputed=item.get('is_disputed', 0),
#                                 id_file=FID
#                             )
#                         else:
#                             error_count += 1
#                             B_Data_is_damaged.objects.create(
#                                 lcicID=lcicID,
#                                 period=period,
#                                 com_enterprise_code=com_enterprise_code,
#                                 segmentType=item.get('segmentType', ''),
#                                 bnk_code=item.get('bnk_code', ''),
#                                 customer_id=item.get('customer_id', ''),
#                                 branch_id=item.get('branch_id', ''),
#                                 lon_sys_id=item.get('lon_sys_id', ''),
#                                 loan_id=item.get('loan_id', ''),
#                                 lon_open_date=item.get('lon_open_date', None),
#                                 lon_exp_date=item.get('lon_exp_date', None),
#                                 lon_ext_date=item.get('lon_ext_date', None),
#                                 lon_int_rate=item.get('lon_int_rate', 0),
#                                 lon_purpose_code=item.get('lon_purpose_code', ''),
#                                 lon_credit_line=item.get('lon_credit_line', 0),
#                                 lon_currency_code=item.get('lon_currency_code', ''),
#                                 lon_outstanding_balance=item.get('lon_outstanding_balance', 0),
#                                 lon_account_no=item.get('lon_account_no', ''),
#                                 lon_no_days_slow=item.get('lon_no_days_slow', 0),
#                                 lon_class=item.get('lon_class', ''),
#                                 lon_type=item.get('lon_type', ''),
#                                 lon_term=item.get('lon_term', ''),
#                                 lon_status=item.get('lon_status', ''),
#                                 lon_insert_date=lon_insert_date,
#                                 lon_update_date=lon_update_date,
#                                 lon_applied_date=lon_applied_date,
#                                 is_disputed=item.get('is_disputed', 0),
#                                 lcicID_error=1,
#                                 com_enterprise_code_error=None,    
#                                 id_file=FID
#                             )

#                     except Exception as e:
#                         logger.error(f"Error processing item: {e}")

#                 error_percentage = (error_count / total_count) * 100
#                 upload_file.percentage = error_percentage
#                 upload_file.save()
#                 print("Error percentage: ", error_percentage)
#                 print("Error count: ", error_count)
#                 print("Total count: ", total_count)

#                 return JsonResponse({'status': 'success', 'warnings': warnings})

#             return JsonResponse({'status': 'error', 'message': 'ໄຟລ໌ບໍ່ຖືກຕ້ອງ'}, status=400)

#         except Exception as e:
#             logger.error(f"Error uploading file: {e}")
#             return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)



     

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

# class FileUploadViewC(generics.CreateAPIView):
#     queryset = Upload_File_C.objects.all()
#     serializer_class = FileSerializer
#     parser_classes = (MultiPartParser, FormParser)

#     @method_decorator(ensure_csrf_cookie)
#     def post(self, request, *args, **kwargs):
#         files = request.FILES.getlist('file')
#         csrf_token = request.META.get('CSRF_COOKIE', '')

#         for file in files:
#             if file.name.endswith('.json'):
#                 try:
#                     period_parts = file.name.split('_,.json')[0].split('_')
#                     if len(period_parts) >= 4:
#                         period = period_parts[2] + "_" + period_parts[3]
#                     else:
#                         return JsonResponse({'status': 'error', 'message': 'Invalid file name format'}, status=400)

#                     file_instance = Upload_File_C.objects.create(
#                         fileUpload=file,
#                         fileName=file.name,
#                         fileSize=str(file.size),
#                         path="uploadFilesC/" + file.name,
#                         period=period,
#                         status='new',
#                         statussubmit='pending',
#                         status_upload='in_progress',
#                         FileType='json',
#                         percentage=0.0
#                     )

#                     result = process_uploaded_file(file_instance)

#                     if result['status'] == 'error':
#                         return JsonResponse(result, status=400)

#                 except IndexError:
#                     return JsonResponse({'status': 'error', 'message': 'Invalid file name format'}, status=400)

#         response = JsonResponse({'status': 'success', 'message': 'All files processed successfully'})
#         response.set_cookie('csrftoken', csrf_token)
#         return response

class FileUploadViewC(generics.CreateAPIView):
    queryset = Upload_File_C.objects.all()
    
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    @method_decorator(ensure_csrf_cookie)
    
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        print("user_id:", user_id)
        if not user_id:
            return JsonResponse({'status': 'error', 'message': 'User ID is required'}, status=400)
        files = request.FILES.getlist('file')
        print("files:", files)
        csrf_token = request.META.get('CSRF_COOKIE', '')

        for file in files:
            if file.name.endswith('.json'):
                try:
                # ອ່ານໄຟລ໌ JSON
                    file_content = file.read().decode('utf-8')
                    file_data = json.loads(file_content)
                    print("data:", file_data)

                # ເຊັກວ່າ file_data ແມ່ນ list ຫຼື dictionary
                    if isinstance(file_data, list):
                    # ຖ້າຫາກແມ່ນ list, ດຶງຂໍ້ມູນອັນທີ່ຕ້ອງການຈາກອອບເຈັກອັນໃນ
                        file_data = file_data[0]  # ດຶງອັນທຳອິດຈາກ list ແຕ່ຖ້າມີຫຼາຍອັນເຈົ້າອາດຕ້ອງແກ້ໄຂໃຫ້ເໝາະສົມ
                    elif not isinstance(file_data, dict):
                        return JsonResponse({'status': 'error', 'message': 'Invalid JSON structure'}, status=400)

                    file_name_parts = file.name.split('_')
                    if len(file_name_parts) >= 4:
                        period = file_name_parts[3][1:]
                        print("period:", period)
                    else:
                        return JsonResponse({'status': 'error', 'message': 'Invalid file name format'}, status=400)
                
                    bnk_code = file_data.get('bnk_code')
                    print("bnk_code:", bnk_code)
                    if bnk_code is None:
                        return JsonResponse({'status': 'error', 'message': 'bnk_code is required'}, status=400)
                    if str(bnk_code) != user_id != str(bnk_code):
                        return JsonResponse({'status': 'error', 'message': 'User ID does not match bnk_code'}, status=405)
                    if Upload_File_C.objects.filter(fileName=file.name, user_id=user_id).exists():
                        return JsonResponse({'status': 'error', 'message': 'File already exists'}, status=404)
                    
                    file_name_parts = file.name.split('_')
                    if len(file_name_parts) >= 4:
                        period_str = file_name_parts[3]
                        period_month = int(period_str[1:3])
                        # print("period_month:", period_month)
                        period_year = int(period_str[3:])
                        
                        file_period = int(f"{period_year:04d}{period_month:02d}")
                        print("file_period:", file_period)

                    file_instance = Upload_File_C.objects.create(
                        fileUpload=file,
                        user_id=user_id,
                        fileName=file.name,
                        fileSize=str(file.size),
                        path="uploadFilesC/" + file.name,
                        period=period,
                        status='new',
                        statussubmit='pending',
                        status_upload='in_progress',
                        FileType='json',
                        percentage=0.0
                    )

                    result = process_uploaded_file(file_instance)

                    status_value = result.get('status', None)

                    if status_value == '400':
                        file_instance.status_upload = 'failed'
                        file_instance.save()
                        return JsonResponse(result, status=400)
                    else:
                        file_instance.status_upload = 'completed'
                    file_instance.save()

                except IndexError:
                    return JsonResponse({'status': 'error', 'message': 'Invalid file name format'}, status=400)

        response = JsonResponse({'status': 'success', 'message': 'All files processed successfully'})
        response.set_cookie('csrftoken', csrf_token)
        return response

# class FileUploadViewC(generics.CreateAPIView):
#     queryset = Upload_File_C.objects.all()
#     serializer_class = FileSerializer
#     parser_classes = (MultiPartParser, FormParser)

#     @method_decorator(ensure_csrf_cookie)
#     def post(self, request, *args, **kwargs):
#         user_id = request.data.get('user_id')
#         if not user_id:
#             return JsonResponse({'status': 'error', 'message': 'User ID is required'}, status=400)

#         files = request.FILES.getlist('file')
#         if not files:
#             return JsonResponse({'status': 'error', 'message': 'No files uploaded'}, status=401)

#         csrf_token = request.META.get('CSRF_COOKIE', '')
#         for file in files:
#             if file.name.endswith('.json'):
#                 try:
#                     file_content = file.read().decode('utf-8')
#                     file_data = json.loads(file_content)
#                     if isinstance(file_data, list):
#                         file_data = file_data[0]

#                     bnk_code = file_data.get('bnk_code')
#                     if bnk_code is None:
#                         return JsonResponse({'status': 'error', 'message': 'bnk_code is required'}, status=400)
#                     if str(user_id)  != str(bnk_code):
#                         return JsonResponse({'status': 'error', 'message': 'User ID does not match bnk_code'}, status=405)
                    
#                     file_name_parts = file.name.split('_')
#                     if len(file_name_parts) >= 4:
#                         period = file_name_parts[3][1:]
#                     else:
#                         return JsonResponse({'status': 'error', 'message': 'Invalid file name format'}, status=400)
                    
#                     if Upload_File_C.objects.filter(fileName=file.name, user_id=user_id).exists():
#                         return JsonResponse({'status': 'error', 'message': 'File already exists'}, status=404)
#                     file_name_parts = file.name.split('_')
#                     if len(file_name_parts) >= 4:
#                         period_str = file_name_parts[3]
#                         period_month = int(period_str[1:3])
                        
#                         period_year = int(period_str[3:])
                        
                        
#                         file_period = int(f"{period_year:04d}{period_month:02d}")
                        

#                         c1_entries = C1.objects.filter(bnk_code=bnk_code)
                        
#                         if c1_entries.exists():
#                             latest_c1 = c1_entries.order_by('-period').first()
                            
#                             c1_period_str = str(latest_c1.period)
                            
                            
#                             if len(c1_period_str) == 6:
#                                 c1_period_month = c1_period_str[:2]
                                
#                                 c1_period_year = c1_period_str[2:]
                                
#                                 c1_period = int(f"{c1_period_year}{c1_period_month}")
                                
#                             else:
#                                 return JsonResponse({'status': 'error', 'message': 'Invalid C1 period format'}, status=406)
                            
#                             if file_period < c1_period:
#                                 return JsonResponse({'status': 'error', 'message': 'File period is greater than C1 period'}, status=407)
#                             else:
#                                 pass
#                         else:
#                             return JsonResponse({'status': 'error', 'message': 'C1 data not found'}, status=408)
                    
                            
#                     file_instance = Upload_File_C.objects.create(
#                         fileUpload=file,
#                         user_id=user_id,
#                         fileName=file.name,
#                         fileSize=str(file.size),
#                         path="uploadFilesC/" + file.name,
#                         period=period,
#                         status='new',
#                         statussubmit='pending',
#                         status_upload='in_progress',
#                         FileType='json',
#                         percentage=0.0
#                     )

                    
#                     result = process_uploaded_file(file_instance, user_id, period)

#                     status_value = result.get('status', None)
#                     if status_value == '400':
#                         file_instance.status_upload = 'failed'
#                     else:
#                         file_instance.status_upload = 'completed'

#                     file_instance.save()

#                 except Exception as e:
                   
#                     return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
                

#         response = JsonResponse({'status': 'success', 'message': 'All files processed successfully'})
#         response.set_cookie('csrftoken', csrf_token)
#         return response





import json
from django.utils.encoding import smart_str
from django.utils import timezone
from .models import EnterpriseInfo, C_error,C1_disptes,CDL

# def process_uploaded_file(uploaded_data):
    
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
#                     collateral_insert_date=timezone.now(),
#                     collateral_update_date=timezone.now()
#                 )
#                 error_records += 1
                
#                 continue
#             bank_customer_ID = item.get('bank_customer_ID', '')
#             c1_record = C1.objects.filter(lcicID=lcicID, com_enterprise_code=com_enterprise_code).first()
#             if c1_record and c1_record.bank_customer_ID != bank_customer_ID:
#                 C1_disptes.objects.create(
#                     lcicID=lcicID,
#                     id_file=cid,
#                     com_enterprise_code=com_enterprise_code,
#                     bank_customer_ID=bank_customer_ID,
#                     bnk_code=item.get('bnk_code', ''),
#                     branch_id_code=item.get('branch_id_code', ''),
#                     loan_id=item.get('loan_id', ''),
#                     col_id=item.get('col_id', ''),
#                     col_type=item.get('col_type', ''),
                   
#                     insert_date=timezone.now(),
#                     update_date=timezone.now()
#                     )
#                 continue

           
#             col_type = item.get('col_type', '').lower()
#             if col_type == "C2.2":
#                 CDL.objects.create(
#                     id_file=cid,
#                     c1=lcicID,
#                     c2=com_enterprise_code,
#                     c3=item.get('bnk_code', ''),
#                     c4=item.get('col_type', ''),
#                     c5=item.get('bank_customer_ID', ''),
#                     c6=item.get('branch_id_code', ''),
#                     c7=item.get('loan_id', ''),
#                     c8=item.get('col_id', ''),
#                     c9=item.get('account_no', ''),
#                     c10=item.get('account_type', ''),
#                     c11=item.get('value', ''),
#                     c12=item.get('value_unit', ''),
#                     c13=item.get('mia_status', ''),
#                     c14=item.get('mia_insert_date', ''),
#                     c15=item.get('owner_name', ''),
#                     c16=item.get('owner_surname', ''),
#                     c17=item.get('owner_gender', ''),
#                     c18=item.get('owner_lao_name', ''),
#                     c19=item.get('owner_lao_surname', ''),
#                     c39=timezone.now().date(),
#                     c40=timezone.now().date()
#                 )

            
#             # elif col_type == "C2.1" or col_type == "c2.1":
#             #      col_real_estates.objects.create(
#             #         lcicID=item.get('lcicID', ''),
#             #         bnk_code=item.get('bnk_code', ''),
#             #         col_type=col_type,
#             #         col_value=item.get('col_value', ''), #ໃໝ່
#             #         com_enterprise_code=item.get('com_enterprise_code', ''),
#             #         bank_customer_ID=item.get('bank_customer_ID', ''),
#             #         branch_id_code=item.get('branch_id_code', ''),
#             #         loan_id=item.get('loan_id', ''),
#             #         plot_vilid=item.get('plot_vilid', ''),
#             #         plot_unit=item.get('plot_unit', ''),
#             #         land_no=item.get('land_no', ''),
#             #         land_out_time=item.get('land_out_time', ''),
#             #         land_type=item.get('land_type', ''),
#             #         col_area=item.get('col_area', ''),
#             #         land_registry_book_no=item.get('land_registry_book_no', ''),
#             #         land_document_no=item.get('land_document_no', ''),   
#             #         place_regist_land=item.get('place_regist_land', ''),
#             #         land_map_no=item.get('land_map_no', ''),
#             #         land_plot_no=item.get('land_plot_no', ''),
#             #         land_regis_date=item.get('land_regis_date', ''),
#             #         land_area=item.get('land_area', ''),
#             #         land_unit=item.get('land_unit', ''),
#             #         owner_name=item.get('owner_name', ''),
#             #         owner_birth_date=item.get('owner_birth_date', ''),
#             #         owner_nationality=item.get('owner_nationality', ''),
#             #         owner_occupation=item.get('owner_occupation', ''),
#             #         current_unit=item.get('current_unit', ''),

#             #         current_vilid=item.get('current_vilid', ''),

#             #         spouse_name=item.get('spouse_name', ''),
#             #         spouse_birth_date=item.get('spouse_birth_date', None),
#             #         spouse_nationality=item.get('spouse_nationality', ''),
#             #         spouse_occupation=item.get('spouse_occupation', ''),
#             #         land_acquisition=item.get('land_acquisition', ''),
#             #         ownership_status=item.get('ownership_status', ''),
#             #         id_file=cid,
#             #         insert_date=timezone.now().date(),
#             #         update_date=timezone.now().date()
                    
#             #     )
#             # elif col_type == "eqi":
#             #      col_equipment_eqi.objects.create(
#             #         bank_customer_ID=item.get('bank_customer_ID', ''),
#             #         lcicID=item.get('lcicID', ''),
#             #         bnk_code=item.get('bnk_code', ''),
#             #         com_enterprise_code=item.get('com_enterprise_code', ''),
#             #         col_type=col_type,
#             #         branch_id_code=item.get('branch_id_code', ''),
#             #         loan_id=item.get('loan_id', ''),
#             #         col_id=item.get('col_id', ''),
#             #         machine_type=item.get('machine_type', ''),
#             #         machine_no=item.get('machine_no', ''),
#             #         value=item.get('value', ''),
#             #         id_file=cid,
#             #         insert_date=timezone.now().date(),
#             #         update_date=timezone.now().date()
#             #     )
#             # elif col_type == "prj":
#             #      col_project_prj.objects.create(
#             #         bank_customer_ID=item.get('bank_customer_ID', ''),
#             #         lcicID=item.get('lcicID', ''),
#             #         bnk_code=item.get('bnk_code', ''),
#             #         com_enterprise_code=item.get('com_enterprise_code', ''),
#             #         col_type=col_type,
#             #         branch_id_code=item.get('branch_id_code', ''),
#             #         loan_id=item.get('loan_id', ''),
#             #         project_type=item.get('project_type', ''),
#             #         col_id=item.get('col_id', ''),
#             #         project_name_en=item.get('project_name_en', ''),
#             #         ministry=item.get('ministry', ''),
#             #         project_namber=item.get('project_namber', ''),
#             #         project_name_la=item.get('project_name_la', ''),
#             #         value=item.get('value', ''),
#             #         id_file=cid,
#             #         insert_date=timezone.now().date(),
#             #         update_date=timezone.now().date()
#             #     )
#             # elif col_type == "veh":
#             #      col_vechicle_veh.objects.create(
#             #         lcicID=item.get('lcicID', ''),
#             #         com_enterprise_code=item.get('com_enterprise_code', ''),
#             #         col_type=col_type,
#             #         bnk_code=item.get('bnk_code', ''),
#             #         bank_customer_ID = item.get('bank_customer_ID', ''),
#             #         branch_id_code=item.get('branch_id_code', ''),
#             #         loan_id=item.get('loan_id', ''),
#             #         col_id=item.get('col_id', ''),
#             #         name_owner = item.get('name_owner', ''),
#             #         plate_number = item.get('plate_number', ''),
#             #         engine_number = item.get('engine_number', ''),
#             #         body_numbe = item.get('body_numbe', ''),
#             #         model = item.get('model', ''),
#             #         value = item.get('value', ''),
#             #         id_file=cid,
#             #         insert_date=timezone.now().date(),
#             #         update_date=timezone.now().date()
#             #     )
#             # elif col_type == "gua":
#             #      col_guarantor_gua.objects.create(
#             #         lcicID=item.get('lcicID', ''),
#             #         com_enterprise_code=item.get('com_enterprise_code', ''),
#             #         col_type=col_type,
#             #         bnk_code=item.get('bnk_code', ''),
#             #         bank_customer_ID = item.get('bank_customer_ID', ''),
#             #         branch_id_code=item.get('branch_id_code', ''),
#             #         loan_id=item.get('loan_id', ''),
#             #         col_id=item.get('col_id', ''),
#             #         guarantor_nationality = item.get('guarantor_nationality', ''),
#             #         national_id = item.get('national_id', ''),
#             #         national_expiry_date = item.get('national_expiry_date', ''),
#             #         passport = item.get('passport', ''),
#             #         passport_expiry_date = item.get('passport_expiry_date', ''),
#             #         familybook = item.get('familybook', ''),
#             #         familybook_province_code_of_issue = item.get('familybook_province_code_of_issue', ''),
#             #         familybook_issue_date = item.get('familybook_issue_date', ''),
#             #         birthdate = item.get('birthdate', ''),
#             #         gender = item.get('gender', ''),
#             #         ist_name_english = item.get('ist_name_english', ''),
#             #         ist_name_lao = item.get('ist_name_lao', ''),
#             #         nickname_english = item.get('nickname_english', ''),
#             #         nickname_lao = item.get('nickname_lao', ''),
#             #         surname_english = item.get('surname_english', ''),
#             #         surname_lao = item.get('surname_lao', ''),
#             #         address_number_street_english = item.get('address_number_street_english', ''),
#             #         address_number_street_lao = item.get('address_number_street_lao', ''),
#             #         address_village_english = item.get('address_village_english', ''),
#             #         address_village_lao = item.get('address_village_lao', ''),
#             #         address_sub_district_english = item.get('address_sub_district_english', ''),
#             #         address_sub_district_lao = item.get('address_sub_district_lao', ''),
#             #         address_district_english = item.get('address_district_english', ''),
#             #         address_district_lao = item.get('address_district_lao', ''),
#             #         address_province_code = item.get('address_province_code', ''),
#             #         enterprise_code = item.get('enterprise_code', ''),
#             #         registration_date_of_issue = item.get('registration_date_of_issue', ''),
#             #         registration_place_issue = item.get('registration_place_issue', ''),
#             #         company_name_english = item.get('company_name_english', ''),
#             #         company_name_lao = item.get('company_name_lao', ''),
#             #         category = item.get('category', ''),
#             #         insert_date=timezone.now().date(),
#             #         id_file=cid,
#             #         update_date=timezone.now().date()
#             #     )
#             # elif col_type == "gold":
#             #      col_goldsilver_gold.objects.create(
#             #         lcicID=item.get('lcicID', ''),
#             #         com_enterprise_code=item.get('com_enterprise_code', ''),
#             #         col_type=col_type,
#             #         bnk_code=item.get('bnk_code', ''),
#             #         bank_customer_ID = item.get('bank_customer_ID', ''),
#             #         branch_id_code=item.get('branch_id_code', ''),
#             #         loan_id=item.get('loan_id', ''),
#             #         col_id=item.get('col_id', ''),
#             #         weight = item.get('weight', ''),
#             #         unit = item.get('unit', ''),
#             #         value=item.get('value', ''),
#             #         id_file=cid,
#             #         insert_date=timezone.now().date(),
#             #         update_date=timezone.now().date()
#             #     )
#             C1.objects.create(
#                 lcicID=lcicID,
#                 com_enterprise_code=com_enterprise_code,
#                 bnk_code=item.get('bnk_code', ''),
#                 bank_customer_ID=item.get('bank_customer_ID', ''),
#                 branch_id_code=item.get('branch_id_code', ''),
#                 # loan_id=item.get('loan_id', ''),
#                 col_id=item.get('col_id', ''),
#                 loan_id=item.get('loan_id', ''),
#                 col_type=col_type,
#                 id_file=cid,
                
#                 insert_date=timezone.now().date(),
#                 update_date=timezone.now().date()
#             )
#         if total_records > 0:
#              percentage = (100 * (total_records - error_records)) / total_records
#              print("percentage",percentage)
#              print("tota",total_records)
#         else:
#             percentage = 0
#         uploaded_data.percentage = percentage
#         uploaded_data.save()
#         return result

#     except Exception as e:
        
#         print(f"An error occurred: {e}")
#         return {'status': 'error', 'message': str(e)}
    
from datetime import datetime

def process_uploaded_file(uploaded_data):
    try:
        total_records = 0
        error_records = 0
        
        with uploaded_data.fileUpload.open('rb') as file:
            file_content = file.read()
            json_content = json.loads(smart_str(file_content))

        result = {'status': 'success'}

        for item in json_content:
            lcicID = item.get('lcicID', None)
            if lcicID == '':
                lcicID = None

            com_enterprise_code = item.get('com_enterprise_code', '')
            cid = uploaded_data.CID

            lcic_exists = EnterpriseInfo.objects.filter(LCICID=lcicID).exists()
            enterprise_code_exists = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).exists()

         
            if not lcicID and not com_enterprise_code:
                collateral_status = '33'
                datamatch = ''
            elif not lcicID:
                if enterprise_code_exists:
                    collateral_status = '01'
                    datamatch = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first().LCICID
                else:
                    collateral_status = '03'
                    datamatch = ''
            elif not com_enterprise_code:
                if lcic_exists:
                    collateral_status = '10'
                    datamatch = EnterpriseInfo.objects.filter(LCICID=lcicID).first().EnterpriseID
                else:
                    collateral_status = '30'
                    datamatch = ''
            else:
                matching_record = EnterpriseInfo.objects.filter(LCICID=lcicID, EnterpriseID=com_enterprise_code).exists()
                if not matching_record:
                    collateral_status = '44'
                else:
                    collateral_status = '00'

           
            if collateral_status != '00':
                C_error.objects.create(
                    id_file=cid,
                    lcicID=lcicID,
                    com_enterprise_code=com_enterprise_code,
                    bnk_code=item.get('bnk_code', ''),
                    branch_id_code=item.get('branch_id_code', ''),
                    bank_customer_ID=item.get('bank_customer_ID', ''),
                    loan_id=item.get('loan_id', ''),
                    col_id=item.get('col_id', ''),
                    col_type=item.get('col_type', ''),
                    collateral_status=collateral_status,
                    datamatch=datamatch,
                    collateral_insert_date=timezone.now(),
                    collateral_update_date=timezone.now()
                )
                error_records += 1
                continue

        
            try:
                mia_insert_date = datetime.strptime(item.get('mia_insert_date', ''), '%Y-%m-%d')
            except ValueError:
                mia_insert_date = None

           
            if item.get('col_type', '').lower() == "c2.2":
                CDL.objects.create(
                    id_file=cid,
                    c1=lcicID,
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
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.1":
                CDL.objects.create(
                    id_file=cid,
                    c1=lcicID,
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
                    c18=item.get('land_regist_date', ''),
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
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.3":
                CDL.objects.create(
                    id_file=cid,
                    c1=lcicID,
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
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.4":
                CDL.objects.create(
                    id_file=cid,
                    c1=lcicID,
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
                    c11=item.get('project_nuber', ''),
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
                    c40=timezone.now().date(),
                    c41=timezone.now().date()

                )
            elif item.get('col_type', '').lower() == "c2.5":
                CDL.objects.create(
                    id_file=cid,
                    c1=lcicID,
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
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.6":
                CDL.objects.create(
                    id_file=cid,
                    c1=lcicID,
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
                    c40=timezone.now().date(),
                    c41=timezone.now().date()
                )
            elif item.get('col_type', '').lower() == "c2.7":
                CDL.objects.create(
                    id_file=cid,
                    c1=lcicID,
                    col_type=item.get('col_type', ''),
                    c2=com_enterprise_code,
                    c3=item.get('bnk_code', ''),
                    c4=item.get('bank_customer_ID', ''),
                    c5=item.get('branch_id_code', ''),

                )

           
            C1.objects.create(
                lcicID=lcicID,
                com_enterprise_code=com_enterprise_code,
                bnk_code=item.get('bnk_code', ''),
                bank_customer_ID=item.get('bank_customer_ID', ''),
                branch_id_code=item.get('branch_id_code', ''),
                col_id=item.get('col_id', ''),
                loan_id=item.get('loan_id', ''),
                col_type=item.get('col_type', '').lower(),
                id_file=cid,
                insert_date=timezone.now().date(),
                update_date=timezone.now().date()
            )

        return result
    
    

    except Exception as e:
        print(f"An error occurred: {e}")
        return {'status': 'error', 'message': str(e)}


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

                        
                        b1_entries = B1.objects.filter(bnk_code=bnk_code)
                        if b1_entries.exists():
                            latest_b1_entry = b1_entries.order_by('-period').first()
                            b1_period_str = str(latest_b1_entry.period)
                            if len(b1_period_str) == 6:
                                b1_period_month = b1_period_str[:2]
                                b1_period_year = b1_period_str[2:]
                                b1_period = int(f"{b1_period_year}{b1_period_month}")
                                print("B1 Period (Converted to YYYYMM):", b1_period)
                            else:
                                return JsonResponse({'status': 'error', 'message': 'Invalid B1 period format'}, status=404)

                            
                            if file_period < b1_period:
                                return JsonResponse({'status': 'error', 'message': 'Cannot upload data for a previous period'}, status=405)
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
                        response = requests.post(upload_url, files=files_data, headers=headers, data={'period': period_str, 'file_id': file_id, 'user_id': user_id})
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
            print("user_id",user_id)
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
                        lcicID = item.get('lcicID', '')
                        lcicID_get = None
                        lcicID_error_status = '33'

                        if com_enterprise_code and lcicID:
                            enterprise_info_by_code = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first()
                            enterprise_info_by_id = EnterpriseInfo.objects.filter(LCICID=lcicID).first()
                            
                            if enterprise_info_by_code and enterprise_info_by_id:
                                lcicID_error_status = '0'
                               
                                data_edit.objects.create(
                                    lcicID=lcicID,
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
                                    # user_id=item.get('user_id', ''),
                                    lon_status=item.get('lon_status', ''),
                                    lon_insert_date=item.get('lon_insert_date', None),
                                    lon_update_date=item.get('lon_update_date', None),
                                    lon_applied_date=item.get('lon_applied_date', None),
                                    is_disputed=item.get('is_disputed', 0),
                                    id_file=FID
                                )
                                continue
                            else:
                                if enterprise_info_by_code:   #ມີ enterprise code ແຕ່ບໍ່ມີ lcicID 
                                    lcicID_get = enterprise_info_by_code.LCICID
                                    lcicID_error_status = '01'
                                elif enterprise_info_by_id:  #ມີ lcicID ແຕ່ບໍ່ມີ enterprise code
                                    lcicID_get = enterprise_info_by_id.EnterpriseID
                                    lcicID_error_status = '10'
                        elif com_enterprise_code:
                            enterprise_info_by_code = EnterpriseInfo.objects.filter(EnterpriseID=com_enterprise_code).first() #ມີ enterprise code ແຕ່ lcicID ຜິດ
                            if enterprise_info_by_code:
                                lcicID_get = enterprise_info_by_code.LCICID
                                lcicID_error_status = '31'
                            else:
                                lcicID_error_status = '31'
                        elif lcicID:
                            enterprise_info_by_id = EnterpriseInfo.objects.filter(LCICID=lcicID).first() #ມີ lcicID ແຕ່ enterprise code ຜິດ
                            if enterprise_info_by_id:
                                lcicID_get = enterprise_info_by_id.EnterpriseID
                                lcicID_error_status = '13'
                            else:
                                lcicID_error_status = '13'
                       
                        # else:
                        #     lcicID_error_status = '13'

                        B_Data_is_damaged.objects.create(
                            lcicID=lcicID,
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
                            lcicID_error=lcicID_error_status,
                            lcicID_get=lcicID_get,
                            id_file=FID
                        )

                        if lcicID_error_status != '0':
                            erroneous_items += 1

                    except Exception as e:
                        B_Data_is_damaged.objects.create(
                            lcicID=item.get('lcicID', ''),
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








from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def update_statussubmit(request):
    try:
        FID = request.POST.get('FID')
        file = Upload_File.objects.get(FID=FID)
        file.statussubmit = "0"  
        file.save()
        return JsonResponse({'status': 'success', 'message': 'statussubmit updated successfully'})
    except Upload_File.DoesNotExist:
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



from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Upload_File, data_edit, B1, B1_Monthly, disputes

@csrf_exempt
@require_POST
def confirm_upload(request):
    try:
        FID = request.POST.get('FID')
        if not FID:
            return JsonResponse({'status': 'error', 'message': 'File ID is required'}, status=400)

        data_edits = data_edit.objects.filter(id_file=FID)
        if not data_edits.exists():
            return JsonResponse({'status': 'error', 'message': 'No data found for the given File ID'}, status=404)

        for item in data_edits:
            try:
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
                    b1_monthly_mismatch = B1_Monthly.objects.filter(
                        bnk_code=item.bnk_code,
                        branch_id=item.branch_id,
                        customer_id=item.customer_id,
                        loan_id=item.loan_id,
                        period=item.period
                    ).exclude(
                        com_enterprise_code=item.com_enterprise_code,
                        lcicID=item.lcicID
                    ).exists()

                    b1_mismatch = B1.objects.filter(
                        bnk_code=item.bnk_code,
                        branch_id=item.branch_id,
                        customer_id=item.customer_id,
                        loan_id=item.loan_id,
                        period=item.period
                    ).exclude(
                        com_enterprise_code=item.com_enterprise_code,
                        lcicID=item.lcicID
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
                            is_disputed=item.is_disputed
                        )
                        continue  
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
                    }
                )
                
                b1, created = B1.objects.update_or_create(
                    bnk_code=item.bnk_code,
                    branch_id=item.branch_id,
                    customer_id=item.customer_id,
                    loan_id=item.loan_id,
                    defaults={
                        'lcicID': item.lcicID,
                        'com_enterprise_code': item.com_enterprise_code,
                        'segmentType': item.segmentType,
                        'bnk_code': item.bnk_code,
                        'user_id': item.user_id,
                        'customer_id': item.customer_id,
                        'branch_id': item.branch_id,
                        'lon_sys_id': item.lon_sys_id,
                        'loan_id': item.loan_id,
                        'period': item.period,
                        'product_type': item.product_type,    
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
                        'status_customer': '1' if created else '0'
                    }
                )
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f'Error while processing item with id {item.id}: {str(e)}'}, status=500)

        return JsonResponse({'status': 'success', 'message': 'Data successfully confirmed and updated'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'Error in confirm_upload: {str(e)}'}, status=500)


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
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import UploadedFile
from .serializers import UploadedFileSerializer

class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UploadedFileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import UploadedFile
from .serializers import UploadedFileSerializer

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('files')
        uploaded_files = []

        for file in files:
            uploaded_file = UploadedFile(
                name=file.name,
                file=file,
                size=file.size,
                uploaded_by=request.user
            )
            uploaded_file.save()
            uploaded_files.append(uploaded_file)

        serializer = UploadedFileSerializer(uploaded_files, many=True)
        return Response({
            'message': 'Files successfully uploaded!',
            'uploadedFiles': serializer.data
        }, status=status.HTTP_201_CREATED)






# views.py
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

from rest_framework import generics
from .models import Upload_File
from .serializers import UploadFileSerializer

class UploadFileList(generics.ListAPIView):
    serializer_class = UploadFileSerializer
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Upload_File.objects.filter(user_id=user_id)
        return Upload_File.objects.all()


from rest_framework import generics
from .models import Upload_File_C
from .serializers import UploadFilecSerializer

class UploadFilecList(generics.ListAPIView):
    queryset = Upload_File_C.objects.all()
    serializer_class = UploadFilecSerializer


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


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Collateral

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'status': 'error', 'message': 'No file provided'}, status=400)

        file = request.FILES['image']

        try:
            
            file_path = default_storage.save(f'collaterals/{file.name}', ContentFile(file.read()))

           
            collateral = Collateral(filename=file.name, pathfile=file_path, status=1)
            collateral.save()
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error saving file: {str(e)}'}, status=500)

        return JsonResponse({'status': 'success', 'message': 'File uploaded successfully', 'filename': file.name})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)



from django.http import JsonResponse
from .models import Collateral

def get_collaterals(request):
    collaterals = Collateral.objects.filter(status=1).values('id', 'filename', 'image', 'pathfile', 'status')
    return JsonResponse(list(collaterals), safe=False)

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

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logging.info(f"Request Headers: {request.headers}")
        logging.info(f"User: {request.user}")
        user = request.user
        serializer = LoginSerializer(user)
        return Response(serializer.data)



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

@api_view(['POST'])
def create_enterprise_info(request):
    if request.method == 'POST':
        serializer = EnterpriseInfoSerializer(data=request.data)
        if serializer.is_valid():
            
            max_lcicid = EnterpriseInfo.objects.aggregate(max_lcicid=Max('LCICID'))['max_lcicid']
            
            if max_lcicid is not None:
                new_lcicid = max_lcicid + 1
            else:
                new_lcicid = 1  

            serializer.validated_data['LCICID'] = new_lcicid
            serializer.save()

            
            # Collateral.objects.filter(status='1').update(status='0')

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EnterpriseInfo

@api_view(['GET'])
def get_last_lcicid(request):
    last_lcicid = EnterpriseInfo.objects.latest('LCICID').LCICID
    return Response({'last_lcicid': last_lcicid})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Collateral

@csrf_exempt
def confirm_image(request, id):
    if request.method == 'POST':
        try:
            collateral = Collateral.objects.get(id=id)
            collateral.status = 0
            collateral.save()
            return JsonResponse({'status': 'success', 'message': 'Image confirmed successfully'})
        except Collateral.DoesNotExist:
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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Login, User_Group, memberInfo
from .serializers import LoginSerializer
from django.contrib.auth.hashers import make_password
import logging
logger = logging.getLogger(__name__)

#br dai sai to ni
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
                return Response({"detail": "No bank information found."}, status=status.HTTP_404_NOT_FOUND)
            
            logger.info(f"Retrieved {all_user.count()} bank records.")
            serializer = LoginSerializer(all_user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            return Response({"detail": "An error occurred while retrieving bank information."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EnterpriseInfo, B1_Yearly, InvestorInfo, B1_Monthly
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
            loan_info = B1.objects.filter(com_enterprise_code=enterprise_id)
            inves_info = InvestorInfo.objects.filter(EnterpriseID=enterprise_id)

            print("Enterprise_info", ent_info)
            print("Loan_Info", loan_info)
            print("Investor_Info", inves_info)
            
            if not ent_info.exists():
                return Response({"detail": "Enterprise information not found."}, status=status.HTTP_404_NOT_FOUND)
            

            
            loan_info_list_inactive = []
            for loan in loan_info:
                if loan.lon_status == status_inactive:
                    lon_class_history = B1.objects.filter(
                        bnk_code=loan.bnk_code, 
                        com_enterprise_code=enterprise_id, 
                        loan_id=loan.loan_id
                    ).order_by('-id')[:12]
                    lon_class_history_list = list(lon_class_history.values())
                    loan_data_inactive = {
                        "id": loan.lon_sys_id,
                        "bank": loan.bnk_code,
                        "lon_open_date": loan.lon_open_date,
                        "lon_end_date":loan.lon_exp_date,
                        "lon_ext_date":loan.lon_ext_date,
                        "lon_interest":loan.lon_int_rate,
                        "lon_purpose":loan.lon_purpose_code,
                        "lon_credit_line": loan.lon_credit_line,
                        "lon_outstanding_balance": loan.lon_outstanding_balance,
                        "lon_currency_code": loan.lon_currency_code,
                        "lon_no_days_slow": loan.lon_no_days_slow,
                        "lon_class": loan.lon_class,
                        "lon_type":loan.lon_type,
                        "lon_term":loan.lon_term,
                        "lon_status":loan.lon_status
                    }
                    loan_info_list_inactive.append(loan_data_inactive)
                    print("Loan Data for InActive:", loan_data_inactive)
                    
                else:
                    print("Non InActive List")
                    

            # Serialize the retrieved objects
            ent_info_serializer = EnterpriseInfoSerializer(ent_info, many=True)
            loan_info_serializer = B1Serializer(loan_info, many=True)
            inves_info_serializer = InvestorInfoSerializer(inves_info, many=True)
            
            response_data = {
                'enterprise_info': ent_info_serializer.data,
                'loan_info': loan_info_serializer.data,
                'inves_info': inves_info_serializer.data,
                # 'active_loans': loan_info_list_active,
                'inactive_loans': loan_info_list_inactive
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
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
            print("user_data: ", user_data)
            
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
        sidebar_items = SidebarItem.objects.all()
        serializer = SidebarItemSerializer(sidebar_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SidebarSubItemListView(APIView):
    def get(self, request):
        sidebar_sub_items = SidebarSubItem.objects.all()
        serializer = SidebarSubItemSerializer(sidebar_sub_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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