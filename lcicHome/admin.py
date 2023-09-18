from django.contrib import admin
from django.contrib.admin.helpers import AdminField
from .models import H_Lang, H_imageBar, H_newsCommand,H_newsCommand, H_newsType, H_newsInfo,  H_proType, H_productInfo, H_userInfo, User_Login, User_Group, Menu, SubMenu, GroupSubMenu, Login

class newsCommandAdminStackedInline(admin.StackedInline):
    model = H_newsCommand

class newCommandAdminTabularInline(admin.TabularInline):
    model = H_newsCommand
    extra = 1
class H_newsAdmin(admin.ModelAdmin):
    list_display=['code','nameL','showImage','nFiles','published']
    list_filter=['newsType']
    search_fields=['nameL','userInfo']
    fieldsets=(
        (None , { 'fields':['code','nameL','descL','nimage','nFiles','published']} ),
        ('English' , {'fields':['nameE','descE']}),
        ('Category', {'fields':['newsType','userInfo'],'classes':['collapse']})
    )
    inlines = [newCommandAdminTabularInline]

class H_imageBarAdmin(admin.ModelAdmin):
    list_display=['code','nameL','ImageB','imageSlidMain','published']
    list_filter = ['published']
    search_fields=['nameL']
    fieldsets=(
        (None,{'fields':['code','nameL','detailL','imageBar','imageS','published']}),
        ('English',{'fields':['nameE','detailE']})
    )
class H_productInforAdmin(admin.ModelAdmin):
    list_display=['code','nameL','pshowImage','pFiles']
    list_filter=['proType']
    prepopulated_fields = {'slug':['nameE']}
    fieldsets=(
            (None,{'fields':['code','nameL','nameE','slug','descL','descE','price']}),
            ('Type',{'fields':['proType','pimage','pFiles','published']}),
    )

class User_GroupAdmin(admin.ModelAdmin):
    list_display=['nameL','nameE']
    search_fields=('GID','nameL')
    fieldsets=(
              (None,{'fields':['nameL','nameE']}),
              
    )

class GroupSubMenuInline(admin.TabularInline):
    model= GroupSubMenu
    extra= 5

class SubmenuInline(admin.TabularInline):
    model= SubMenu
    extra= 3
    
class SubMenuAdmin(admin.ModelAdmin):
    list_display=['MID','nameL','nameE']
    search_fields=('SMID','nameL')
    fieldsets=(
              (None,{'fields':['nameL','nameE'],'classes':['collapse']}),
    )
    inlines = [GroupSubMenuInline]
    
class MenuAdmin(admin.ModelAdmin):
    list_display=['nameL','nameE']
    search_fields=('MID','nameL')
    fieldsets=(
              (None,{'fields':['nameL','nameE'],'classes':['collapse']}),
              
    )
    inlines = [SubmenuInline]

class GroupSubMenuAdmin(admin.ModelAdmin):
    list_display=['GID','SMID','insertDate','updateDate']
    search_fields=('GID','insertDate','updateDate')
    fieldsets = (
        ('GroupSubMenu',{'fields':['SMID','insertDate','updateDate']}),
    )
    
class LoginAdmin(admin.ModelAdmin):
    list_display=['nameL','surnameL','nameE','surnameE','username','password','insertDate','updateDate','is_active']
    list_filter=['is_active']
    search_fields=['UID','nameL','surnameL','nameE','surnameE','username','insertDate','updateDate']
    fieldsets = (
        (None,{'fields':['nameL','surnameL','nameE','surnameE']}),
        ('UserName & Password',{'fields':['username','password',]}),
        ('Date',{'fields':['insertDate','updateDate',]}),
        ('Active',{'fields':['is_active',]}),
    )
    
admin.site.register(H_imageBar,H_imageBarAdmin)
admin.site.register(H_proType)
admin.site.register(H_productInfo,H_productInforAdmin)
admin.site.register(H_newsType)
admin.site.register(H_userInfo)
admin.site.register(H_newsInfo,H_newsAdmin)
admin.site.register(H_Lang)
admin.site.register(User_Login)
admin.site.register(User_Group,User_GroupAdmin)
admin.site.register(Menu,MenuAdmin)
admin.site.register(SubMenu,SubMenuAdmin)
admin.site.register(GroupSubMenu,GroupSubMenuAdmin)
admin.site.register(Login,LoginAdmin)
