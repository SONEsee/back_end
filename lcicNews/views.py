from django.shortcuts import render, get_object_or_404
from .models import newsType,newsInfo,memberType,memberInfo,proType,productInfo,fdocType,fdocInfo,jobInfo,H_Lang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    newsType_v =newsType.objects.all()
    newsInfo_v =newsInfo.objects.filter(published=True)
    # Change_Lang= request.GET.get('Lang')
    # Lang='la'
    # if Change_Lang == "en" and Lang == "en":
    #     Lang ='en'
    # elif Change_Lang == "en" or Lang == "la":
    #     Lang = 'en'
    # elif Change_Lang == "" and Lang == "la":
    #     Lang = 'la'
    Lang= request.GET.get('Lang')
    if Lang == 'en':
        Lang='en'
    elif Lang == 'la':
        Lang='la'
    else:
        Lang='la'
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
    H_nl = H_Lang.objects.filter(id=29)
    H_n = H_Lang.objects.filter(id=30)
    H_l = H_Lang.objects.filter(id=31)
    H_login = H_Lang.objects.filter(id=46)
    Type_V = request.GET.get('newsTypeid')
    if Type_V:
        newsInfo_v = newsInfo_v.filter(newsType=Type_V)
    
    paginator = Paginator(newsInfo_v, 10)
    page = request.GET.get('page')
    try:
        newsInfo_v = paginator.page(page)
    except PageNotAnInteger:
        newsInfo_v = paginator.page(1)
    except EmptyPage:
        newsInfo_v = paginator.page(paginator.num_page)

    return render(request,'News/index.html',{'newsType_v':newsType_v,'newsInfo_v':newsInfo_v,'Type_V':Type_V,'Lang':Lang, 'H_Lang_v':H_Lang_v, 'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_nl':H_nl, 'H_n':H_n, 'H_l':H_l,'H_login':H_login })

def NewDetail(request):
    slugID = request.GET.get('slug')
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Lang is "":
        Lang='la'
    if Change_Lang:
        Lang= Change_Lang= request.GET.get('Lang')
    if Lang is "la":
        Lang='la'
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
    H_nl = H_Lang.objects.filter(id=29)
    H_n = H_Lang.objects.filter(id=30)
    H_l = H_Lang.objects.filter(id=31)
    H_login = H_Lang.objects.filter(id=46)
    if slugID:
        newsInfo_v = newsInfo.objects.filter(published=True)
        newsInfo_v = newsInfo_v.filter(id=slugID)        
    return render(request,'News/newsDetail.html',{'newsInfo_v':newsInfo_v,'slugID':slugID,'Lang':Lang, 'H_Lang_v':H_Lang_v,'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_nl':H_nl, 'H_n':H_n, 'H_l':H_l, 'H_login':H_login  })

def jobs(request):
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Lang is "":
        Lang='la'
    if Change_Lang:
        Lang= Change_Lang= request.GET.get('Lang')
    if Lang is "la":
        Lang='la'
    jobsInfo_v = jobInfo.objects.all()
    jobsInfo_v = jobInfo.objects.filter(published=True)
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
    H_nl = H_Lang.objects.filter(id=29)
    H_n = H_Lang.objects.filter(id=30)
    H_l = H_Lang.objects.filter(id=31)
    H_join = H_Lang.objects.filter(id=32)
    H_login = H_Lang.objects.filter(id=46)

    return render(request,'News/jobs.html',{'jobsInfo_v':jobsInfo_v,'Lang':Lang, 'H_Lang_v':H_Lang_v,'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_nl':H_nl, 'H_n':H_n, 'H_l':H_l, 'H_join':H_join, 'H_login':H_login  })

def members(request):
    memberType_v =memberType.objects.all()
    memberInfo_v =memberInfo.objects.filter(published=True)
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Lang is "":
        Lang='la'
    if Change_Lang:
        Lang= Change_Lang= request.GET.get('Lang')
    if Lang is "la":
        Lang='la'
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
    H_nl = H_Lang.objects.filter(id=29)
    H_n = H_Lang.objects.filter(id=30)
    H_l = H_Lang.objects.filter(id=31)
    H_login = H_Lang.objects.filter(id=46)

    mType_v = request.GET.get('memberTypeid')
    if mType_v:
        memberInfo_v = memberInfo_v.filter(memberType=mType_v)
    
    paginator = Paginator(memberInfo_v, 20)
    page = request.GET.get('page')
    try:
        memberInfo_v = paginator.page(page)
    except PageNotAnInteger:
        memberInfo_v = paginator.page(1)
    except EmptyPage:
        memberInfo_v = paginator.page(paginator.num_pages)
    
    return render(request,'News/members.html',{'memberType_v':memberType_v,'memberInfo_v':memberInfo_v,'mType_v':mType_v,'Lang':Lang, 'H_Lang_v':H_Lang_v,'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_nl':H_nl, 'H_n':H_n, 'H_l':H_l, 'H_login': H_login    })

def documentInfo(request):
    documType_v = fdocType.objects.all()
    documentInfo_v = fdocInfo.objects.filter(published=True)
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Lang is "":
        Lang='la'
    if Change_Lang:
        Lang= Change_Lang= request.GET.get('Lang')
    if Lang is "la":
        Lang='la'
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
    H_nl = H_Lang.objects.filter(id=29)
    H_n = H_Lang.objects.filter(id=30)
    H_l = H_Lang.objects.filter(id=31)
    H_login = H_Lang.objects.filter(id=46)
    return render(request,'News/docinfo.html',{'docmType_v': documType_v,'documentInfo_v':documentInfo_v,'Lang':Lang, 'H_Lang_v':H_Lang_v,'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_nl':H_nl, 'H_n':H_n, 'H_l':H_l, 'H_login': H_login  })

def products(request):
    proType_v =proType.objects.all()
    productInfo_v =productInfo.objects.filter(published=True)
    pType_v = request.GET.get('proTypeid')
    if pType_v:
        productInfo_v = productInfo.objects.filter(proType=pType_v)
    Change_Lang= request.GET.get('Lang')
    Lang='la'
    if Lang is "":
        Lang='la'
    if Change_Lang:
        Lang= Change_Lang= request.GET.get('Lang')
    if Lang is "la":
        Lang='la'
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
    H_nl = H_Lang.objects.filter(id=29)
    H_n = H_Lang.objects.filter(id=30)
    H_l = H_Lang.objects.filter(id=31)
    H_login = H_Lang.objects.filter(id=46)
    return render(request,'News/products.html',{'proType_v':proType_v,'productInfo_v':productInfo_v,'pType_v':pType_v,'Lang':Lang, 'H_Lang_v':H_Lang_v,'H_com':H_com, 'H_notice':H_notice, 'H_pro':H_pro, 'H_mem':H_mem, 'H_form':H_form,'H_about':H_about, 'H_job':H_job, 'H_contact':H_contact,'H_la':H_la, 'H_en':H_en, 'H_history':H_history, 'H_organize':H_organize, 'H_bod':H_bod, 'H_md':H_md, 'H_memlcic':H_memlcic, 'H_allmem':H_allmem, 'H_mi':H_mi, 'H_pros':H_pros, 'H_allpro':H_allpro, 'H_news':H_news, 'H_new':H_new, 'H_more':H_more,'H_rmore':H_rmore, 'H_ofl':H_ofl, 'H_loca':H_loca, 'H_cap':H_cap, 'H_nl':H_nl, 'H_n':H_n, 'H_l':H_l, 'H_login':H_login })




        