from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.contenttypes.models import ContentType

from django.core.urlresolvers import reverse
from answers.models import *
import datetime



from watson import search as watson


# Create your models here.

class Tag(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return str(self.slug)

    class Meta:
        ordering = ('slug',)

  
class admission(models.Model):
    

    adm_type=(
        ('UG','Under Graduate'),
        ('PG','Post Graduate'),
        ('LEET','UG Leet')
        

    )
    user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
    admission_Program= models.CharField(max_length=30,choices=adm_type)
    title = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    
    timestamp=models.DateTimeField()
    updated=models.DateTimeField()
    hits = models.IntegerField(default=0)
    

    

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.user)

    
     
           

    def get_absolute_url(self):
        return reverse("admquerydetail" , kwargs={"id":self.id})

    @property
    def answers(self):
        instance=self
        qs=admission_Answer.objects.filter_by_instance(instance)
        return qs 
    

    @property
    def get_content_type(self):
        instance=self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type
    

class admissionhits(models.Model):
    title = models.ForeignKey(admission)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40,null=True)
    created = models.DateTimeField()

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.ip)


   
    





class placement(models.Model):
    

    plc_type=(
        ('Internships','Internships'),
        ('Campus Placement','Campus Placement'),
        
        

    )
    user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
    Program = models.CharField(max_length=30,choices=plc_type)
    title = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    timestamp=models.DateTimeField()
    updated=models.DateTimeField()
    hits = models.IntegerField(default=0)





    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.user)

    
        
           

    def get_absolute_url(self):
        return reverse("plcmntquerydetail" , kwargs={"id":self.id})

    @property
    def answers(self):
        instance=self
        qs=placement_Answer.objects.filter_by_instance(instance)
        return qs 
    

    @property
    def get_content_type(self):
        instance=self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type

class placementhits(models.Model):
    title = models.ForeignKey(placement)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40,null=True)
    created = models.DateTimeField()

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.ip)
    



class hostel(models.Model):
    

    hostel_type=(
        ('Hostel C','Hostel C'),
        ('Hostel B','Hostel B'),
        ('Hostel A','Hostel A'),
        ('Hostel J','Hostel J'),
        ('Hostel H','Hostel H'),
        ('Hostel PG','Hostel PG'),
        ('Hostel I','Hostel I'),
        ('Hostel G','Hostel G'),
        ('Hostel E','Hostel E'),
        ('Other','Other')
        

    )
    user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
    hostel_choice= models.CharField(max_length=30,choices=hostel_type)
    title = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    
    timestamp=models.DateTimeField()
    updated=models.DateTimeField()
    hits = models.IntegerField(default=0)
    

    

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.user)

    
     
           

    def get_absolute_url(self):
        return reverse("hostelquerydetail" , kwargs={"id":self.id})

    @property
    def answers(self):
        instance=self
        qs=hostel_Answer.objects.filter_by_instance(instance)
        return qs 
    

    @property
    def get_content_type(self):
        instance=self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type
    

class hostelhits(models.Model):
    title = models.ForeignKey(hostel)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40,null=True)
    created = models.DateTimeField()

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.ip)






class acad(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
    title = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    
    timestamp=models.DateTimeField()
    updated=models.DateTimeField()
    hits = models.IntegerField(default=0)
    

    

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.user)

    
     
           

    def get_absolute_url(self):
        return reverse("acadquerydetail" , kwargs={"id":self.id})

    @property
    def answers(self):
        instance=self
        qs=acad_Answer.objects.filter_by_instance(instance)
        return qs 
    

    @property
    def get_content_type(self):
        instance=self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type
    

class acadhits(models.Model):
    title = models.ForeignKey(acad)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40,null=True)
    created = models.DateTimeField()

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.ip)




class other(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
    title = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    
    timestamp=models.DateTimeField()
    updated=models.DateTimeField()
    hits = models.IntegerField(default=0)
    

    

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.user)

    
     
           

    def get_absolute_url(self):
        return reverse("otherquerydetail" , kwargs={"id":self.id})

    @property
    def answers(self):
        instance=self
        qs=other_Answer.objects.filter_by_instance(instance)
        return qs 
    

    @property
    def get_content_type(self):
        instance=self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type
    

class otherhits(models.Model):
    title = models.ForeignKey(other)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40,null=True)
    created = models.DateTimeField()

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.ip)







class soc(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
    title = models.CharField(max_length=120)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    
    timestamp=models.DateTimeField()
    updated=models.DateTimeField()
    hits = models.IntegerField(default=0)
    

    

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.user)

    
     
           

    def get_absolute_url(self):
        return reverse("socquerydetail" , kwargs={"id":self.id})

    @property
    def answers(self):
        instance=self
        qs=soc_Answer.objects.filter_by_instance(instance)
        return qs 
    

    @property
    def get_content_type(self):
        instance=self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type
    

class sochits(models.Model):
    title = models.ForeignKey(soc)
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40,null=True)
    created = models.DateTimeField()

    def __unicode__(self):
        return '%s --------------------- %s' %(self.title,self.ip)


