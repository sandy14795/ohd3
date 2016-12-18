from __future__ import unicode_literals
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from posts.models import *

# Create your models here.






class AnswerManager(models.Manager):
	#overriding all method to show parents only
	def all(self):
		qs = super(AnswerManager, self).filter(parent= None)
		return qs

	def filter_by_instance(self,instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id
		qs = super(AnswerManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent = None)
		return qs



class admission_Answer(models.Model):
    
    answer_text = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent=models.ForeignKey('self',null=True,blank=True)

    votes = models.IntegerField(default=0)

    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)

    objects = AnswerManager()

    class Meta:
    	ordering = ['-pub_date']

    def __unicode__(self):
        return ' %s ------ answered by  %s' %(self.answer_text,self.user)

    def children(self):  #replies
    	return admission_Answer.objects.filter(parent=self)

    @property
    def is_parent(self):
    	if self.parent is not None:

    	    return False

    	else:
    		return True    

class Voteradm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    answer = models.ForeignKey(admission_Answer)

    def __unicode__(self):
        return ' %s ------ voted by  %s' %(self.answer,self.user)


class placement_Answer(models.Model):
    
    answer_text = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent=models.ForeignKey('self',null=True,blank=True)
    votes = models.IntegerField(default=0)

    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)

    objects = AnswerManager()

    class Meta:
    	ordering = ['-pub_date']

    def __unicode__(self):
        return ' %s ------ answered by  %s' %(self.answer_text,self.user)

    def children(self):  #replies
    	return placement_Answer.objects.filter(parent=self)

    @property
    def is_parent(self):
    	if self.parent is not None:

    	    return False

    	else:
    		return True    

    	
class Voterplc(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    answer = models.ForeignKey(placement_Answer)

    def __unicode__(self):
        return ' %s ------ voted by  %s' %(self.answer,self.user)       






class hostel_Answer(models.Model):
    
    answer_text = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent=models.ForeignKey('self',null=True,blank=True)

    votes = models.IntegerField(default=0)

    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)

    objects = AnswerManager()

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return ' %s ------ answered by  %s' %(self.answer_text,self.user)

    def children(self):  #replies
        return hostel_Answer.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:

            return False

        else:
            return True    

class Voterhostel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    answer = models.ForeignKey(hostel_Answer)

    def __unicode__(self):
        return ' %s ------ voted by  %s' %(self.answer,self.user)







class acad_Answer(models.Model):
    
    answer_text = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent=models.ForeignKey('self',null=True,blank=True)

    votes = models.IntegerField(default=0)

    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)

    objects = AnswerManager()

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return ' %s ------ answered by  %s' %(self.answer_text,self.user)

    def children(self):  #replies
        return acad_Answer.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:

            return False

        else:
            return True    

class Voteracad(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    answer = models.ForeignKey(acad_Answer)

    def __unicode__(self):
        return ' %s ------ voted by  %s' %(self.answer,self.user)










class other_Answer(models.Model):
    
    answer_text = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent=models.ForeignKey('self',null=True,blank=True)

    votes = models.IntegerField(default=0)

    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)

    objects = AnswerManager()

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return ' %s ------ answered by  %s' %(self.answer_text,self.user)

    def children(self):  #replies
        return other_Answer.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:

            return False

        else:
            return True    

class Voterother(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    answer = models.ForeignKey(other_Answer)

    def __unicode__(self):
        return ' %s ------ voted by  %s' %(self.answer,self.user)       







class soc_Answer(models.Model):
    
    answer_text = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    parent=models.ForeignKey('self',null=True,blank=True)

    votes = models.IntegerField(default=0)

    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)

    objects = AnswerManager()

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return ' %s ------ answered by  %s' %(self.answer_text,self.user)

    def children(self):  #replies
        return soc_Answer.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:

            return False

        else:
            return True    

class Votersoc(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    answer = models.ForeignKey(soc_Answer)

    def __unicode__(self):
        return ' %s ------ voted by  %s' %(self.answer,self.user)