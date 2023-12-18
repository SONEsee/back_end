from os import truncate
from django.db import models
# from django.db.models.base import Model, ModelStateFieldsCacheDescriptor
from django.db.models.expressions import Value
from django.db.models.fields import NullBooleanField
from django.db.models.lookups import BuiltinLookup
from django.db.models.query_utils import select_related_descend
from django.utils.html import format_html
# from django.utils.html import TRAILING_PUNCTUATION_CHARS, format_html

class newsType(models.Model):
    nameL = models.CharField(max_length=100)
    nameE = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='newsType'
    def _str_(seft):
        return seft.nameL

class userInfo(models.Model):
    code = models.CharField(max_length=50)
    nameL = models.CharField(max_length=100)
    nameE = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='userInfo'
    def _str_(seft):
        return seft.nameL

class newsInfo(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nameE = models.CharField(max_length=100, null = True,blank=True)
    nameL = models.CharField(max_length=100, null= True, blank= True)
    descE  = models.TextField(null=True,blank=True)
    descL = models.TextField(null=True,blank =True )
    newsType = models.ForeignKey(newsType, null=True, blank=True ,on_delete=models.CASCADE)
    userInfo = models.ManyToManyField(userInfo,blank=True)
    nimage = models.FileField(upload_to='upload',null=True,blank=True)
    nFilesL = models.FileField(upload_to='uploadNewsFlils/uploadNewsFlilsL',null=True,blank=True)
    nFilesE = models.FileField(upload_to='uploadNewsFlils/uploadNewsFlilsE',null=True,blank=True)
    published = models.BooleanField(default=False)
    insertDate = models.DateTimeField(auto_now_add = True)
    updateDate = models.DateTimeField(auto_now = True)
    def _str_(self):
        return self.nameL
    def showImage(self):
        if self.nimage:
            return format_html('<img src="'+ self.nimage.url +'" height="40px" >')
        return ''
    showImage.allow_tags = True
    def showFiles(self):
        if self.nFiles:
            return format_html('<img src="'+ self.nFiles.url +'" height="40px" >')
        return ''
    showImage.allow_tags = True

class newsCommand(models.Model):
    code = models.ForeignKey(newsInfo,on_delete=models.CASCADE)
    commandL = models.CharField(max_length=50)
    commandE= models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    class Meta:
        ordering =['-id']
        verbose_name_plural='news'
    def _str_(self):
        return self.commandL

newsLevelChoice=(
    ('IND','Individual'),
    ('COM','Company'),
    ('UTI','Utility')
)

class proType(models.Model):
    nameL = models.CharField(max_length=100)
    nameE = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='proType'
    def _str_(seft):
        return seft.nameL

class productInfo(models.Model):
    code = models.CharField(max_length=10,unique=True)
    slug = models.SlugField(max_length=250,null=True,blank=True)
    nameL = models.CharField( max_length=250)
    nameE = models.CharField(max_length=250)
    descE = models.TextField(null=True,blank=True)
    descL = models.TextField(null=True,blank =True )
    price = models.IntegerField (default=0)
    proType = models.ForeignKey(proType, null=True,blank=True, on_delete=models.CASCADE)
    pimageL = models.FileField(upload_to='uploadProducts/uploadProductsL',null=True,blank=True)
    pimageE = models.FileField(upload_to='uploadProducts/uploadProductsE',null=True,blank=True)
    pFilesL = models.FileField(upload_to='uploadProducts/uploadProductsL',null=True,blank=True)
    pFilesE = models.FileField(upload_to='uploadProducts/uploadProductsE',null=True,blank=True)
    published = models.BooleanField(default=False)
    insertDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateDate = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        ordering=['id']
        verbose_name_plural='ProductInfo'
    def _str_(self):
        return self.nameL
    def pshowImage(self):
        if self.pimageL:
            return format_html('<img src="'+ self.pimageL.url +'" height="40px" >')
        return ''
    pshowImage.allow_tags =True
    def pshowFiles(self):
        if self.pFilesL:
            return format_html('<img src="'+ self.pFilesL.url +'" height="40px" >')
        return ''    
    pshowFiles.allow_tags =True
class customerInfo(models.Model):
    code = models.CharField(max_length=20,unique=True)
    nameL = models.CharField(max_length=2500)
    nameE = models.CharField(max_length=2500,null=True,blank=True)
    Address = models.TextField(null=True, blank=True)
    cusType = models.CharField(max_length=5,null=True,blank=True,choices=newsLevelChoice)
    enterpricecode = models.CharField(max_length=25,null=True,blank=True)
    companyNameL = models.CharField(max_length=550,null=True,blank=True)
    companyNameE = models.CharField(max_length=550,null=True,blank=True)
    nationalId = models.CharField(max_length=20)
    familyId = models.CharField(max_length=20)
    passportId = models.CharField(max_length=20)
    tel = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    productInfo = models.ForeignKey(productInfo, null=True,blank=True, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    class Meta:
        ordering =['-id']
        verbose_name_plural='CustomerInfo'
    def _str_(self):
        return self.nameL 
class memberType(models.Model):
    nameL = models.CharField(max_length=500)
    nameE = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural='memberType'
    def _str_(seft):
        return seft.nameL
class villageInfo(models.Model):
    nameL = models.CharField(max_length=500)
    nameE = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural='villageInfo'
    def _str_(self):
        return self.nameL
class districtInfo(models.Model):
    nameL = models.CharField(max_length=500)
    nameE = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural = 'districtInfo'
    def _str_(self):
        return self.nameL
class provInfo(models.Model):
    nameL = models.CharField(max_length=250)
    nameE = models.CharField(max_length=250)
    class meta:
        verbose_name_plural ='provInfo'
    def _str_(self):
        return self.nameL

class memberInfo(models.Model):
    code = models.CharField(max_length=20,unique=True)
    slug = models.SlugField(unique=True)
    nameL = models.CharField(max_length=2500,null=True, blank=True)
    nameE = models.CharField(max_length=2500,null=True,blank=True)
    descL = models.TextField(null=True,blank=True)
    descE = models .TextField(null=True, blank=True)
    streetInfoL = models.CharField(max_length=500,null=True, blank=True)
    streetInfoE = models.CharField(max_length=500,null=True, blank=True)
    villageInfo = models.ForeignKey(villageInfo, null=True,blank=True, on_delete=models.CASCADE)
    districtInfo = models.ForeignKey(districtInfo, null=True,blank=True,on_delete=models.CASCADE)
    provInfo = models.ForeignKey(provInfo, null=True,blank=True,on_delete=models.CASCADE)
    memberType = models.ForeignKey(memberType,null=True,blank=True, on_delete=models.CASCADE)
    mImage = models.FileField(upload_to='memberUpload',null=True,blank=True)
    published = models.BooleanField(default=True)
    dateRegis = models.DateField(null=True,blank=True)
    insertDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['code']
        verbose_name_plural='memberInfo'
    def _str_(self):
        return self.nameL
    def memShowImage(self):
        if self.mImage:
            return format_html('<img src="'+ self.mImage.url +'" height="40px" >')
        return ''
    memShowImage.allow_tags =True

class fdocType(models.Model):
    nameL = models.CharField(max_length=250)
    nameE = models.CharField(max_length=250)
    def _str_(self):
        return self.nameL

class fdocInfo(models.Model):
    code = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(unique=True)
    nameL = models.CharField(max_length=2500,null=True,blank=True)
    nameE = models.CharField(max_length=2500,null=True,blank=True)
    descL = models.TextField(null=True,blank=True)
    descE = models.TextField(null=True,blank=True)
    fdocType = models.ForeignKey(fdocType, null=True, blank=True, on_delete = models.CASCADE)
    dFilesL = models.FileField(upload_to='documentUpload/docL',null=True,blank=True)
    dFilesE = models.FileField(upload_to='documentUpload/docE',null=True,blank=True)
    published = models.BooleanField(default=True)
    insertDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now = True)
    class Meta:
        ordering =['-id']
        verbose_name_plural ='fdocInfo'
    def _str_(self):
        return self.nameL
    def docShowFiles(self):
        if self.dFiles:
            return format_html('<img src="' + self.dFiles.url + '" height="40px">')
        return ''
    docShowFiles.allow_tags = True

class jobInfo(models.Model):
    code = models.CharField(max_length=20,unique=True)
    slug = models.SlugField(unique=True)
    nameL = models.CharField(max_length=2500,null=True,blank=True)
    nameE = models.CharField(max_length=2500,null=True,blank=True)
    descL = models.TextField(null=True,blank=True)
    descE = models.TextField(null=True, blank=True)
    jimage = models.FileField(upload_to='jobUpload',null=True,blank=True)
    jfiles = models.FileField(upload_to='jobUpload',null=True,blank=True)
    published = models.BooleanField(default=True)
    insertDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'jobsInfo'
    def _str_(self):
        return self.nameL
    def jobShowImage(self):
        if self.jimage:
            return format_html('<img src="' + self.jimage.url + '" height="40px">')
        return ''
    jobShowImage.allow_tags = True
    def jobShowFile(self):
        if self.jfiles:
            return format_html('<img src="'+ self.jfiles.url +'" height="40px">')
        return ''
    jobShowFile.allow_tage = True

    
class H_Lang(models.Model):
    id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Trans_LA = models.TextField(null=True,blank=True)
    Trans_EN = models.TextField(null=True,blank=True)