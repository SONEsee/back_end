from django.contrib import admin
from .models import H_Lang, fdocInfo, fdocType, jobInfo, villageInfo,districtInfo,provInfo, memberType, memberInfo, proType,productInfo, userInfo, newsType, newsInfo, newsCommand, customerInfo 

class newsCommandAdminStackedInline(admin.StackedInline):
    model = newsCommand

class newCommandAdminTabularInline(admin.TabularInline):
    model = newsCommand
    extra = 1

class newsAdmin(admin.ModelAdmin):
    list_display=['code','nameL','showImage','published']
    list_filter=['newsType']
    search_fields=['nameL','userInfo']
    fieldsets=(
        (None , { 'fields':['code','nimage','published']} ),
        ('Lao' , {'fields':['nameL','descL','nFilesL']}),
        ('English' , {'fields':['nameE','descE','nFilesE']}),
        ('Category', {'fields':['newsType','userInfo'],'classes':['collapse']})
    )
    inlines = [newCommandAdminTabularInline]

class productInforAdmin(admin.ModelAdmin):
    list_display=['code','nameL','pshowImage','pshowFiles']
    list_filter=['proType']
    prepopulated_fields = {'slug':['nameE']}
    fieldsets=(
            (None,{'fields':['code','nameL','nameE','slug','descL','descE','price']}),
            ('Type',{'fields':['proType']}),
            ('Lao',{'fields':['pimageL','pFilesL']}),
            ('English',{'fields':['pimageE','pFilesE']}),
            (None,{'fields':['published']})
    )

class customerInforAdmin(admin.ModelAdmin):
    list_display=['code','nameL','Address']
    list_filter = ['productInfo']
    search_fields=['cusType','nameL']
    fieldsets=(
        (None,{'fields':['code','cusType','productInfo','price','tel','email']}),
        ('IND',{'fields':['nameL','nameE','Address','nationalId','familyId','passportId']}),
        ('COM',{'fields':['enterpricecode','companyNameL','companyNameE']})
    )

class memberInforAdmin(admin.ModelAdmin):
    list_display=['code','nameL','memShowImage','mImage','published']
    search_fields=['nameL','nameE']
    prepopulated_fields = {'slug':['nameE']}

class documentInfoAdmin(admin.ModelAdmin):
    list_display=['code','nameL','dFilesE','published']
    search_fields=['nameL','nameE']
    prepopulated_fields ={'slug':['nameE']}
    fieldsets=(
        (None,{'fields':['code','nameL','nameE','slug','descL','descE','fdocType']}),
        ('Lao',{'fields':['dFilesL']}),
        ('English',{'fields':['dFilesE']}),
        (None,{'fields':['published']})
    )

class jobsInfoAdmin(admin.ModelAdmin):
    list_display=['code','nameL','nameE','jobShowImage','published']
    search_fields = ['nameL','nameE']
    prepopulated_fields = {'slug':['nameE']}
    fieldsets=(
        (None, {'fields':['code','nameE','nameL','slug','jimage','jfiles']}),
        ('Type:',{'fields':['descL','descE','published']})
    )
class H_LangAdmin(admin.ModelAdmin):
    list_display=['id','Trans_LA','Trans_EN']
    search_fields=['id','Trans_LA','Trans_EN']
    fieldsets = (
        (None,{'fields':['id','Trans_LA','Trans_EN']}),
    )
admin.site.register(userInfo)
admin.site.register(newsType)
admin.site.register(newsInfo,newsAdmin)
admin.site.register(proType)
admin.site.register(productInfo,productInforAdmin)
admin.site.register(customerInfo,customerInforAdmin)
admin.site.register(memberType)
admin.site.register(villageInfo)
admin.site.register(districtInfo)
admin.site.register(provInfo)
admin.site.register(memberInfo,memberInforAdmin)
admin.site.register(fdocType)
admin.site.register(fdocInfo,documentInfoAdmin)
admin.site.register(jobInfo,jobsInfoAdmin)
admin.site.register(H_Lang,H_LangAdmin)