from django.shortcuts import render, get_object_or_404 , redirect
from .models import *
from answers.models import *
from answers.forms import *
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse,Http404,HttpResponseForbidden
from django.contrib.contenttypes.models import ContentType
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from operator import attrgetter
from itertools import chain
from django.db.models import Q
import datetime
from django.contrib.auth.models import User
from django.conf import settings
import re
from watson import search as watson
# Create your views here.

def profile(request,id = None):
	instance=get_object_or_404( User,id=id)
	

	context = {
	"prof":instance,
	}
	return render(request,"profile.html",context)	

def ownprofile(request):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	

	context = {	}
	return render(request,"ownprofile.html",context)		

def search(request):

	search_results = watson.filter(admission,request.POST['word'])
	search_results2 = watson.filter(placement,request.POST['word'])
	search_results3 = watson.filter(hostel,request.POST['word'])
	search_results4 = watson.filter(acad,request.POST['word'])
	search_results5 = watson.filter(other,request.POST['word'])
	search_results6 = watson.filter(soc,request.POST['word'])


	all1 = list(sorted(chain(search_results,search_results2,search_results3,search_results4,search_results5,search_results6),key=attrgetter("timestamp"),reverse = True))



	paginator = Paginator(all1, 10)
	page = request.GET.get('page')
	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		questions = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		questions = paginator.page(paginator.num_pages)


	count = len(all1)
	

		
	context = {
			'all' : questions,
			'count' : count,

		}
	return render(request,"search.html",context)

def myques(request):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	i = get_object_or_404( User,username = request.user.username)	
	query_list = admission.objects.filter(user = i).order_by("-timestamp")
	query_list2 = placement.objects.filter(user = i).order_by("-timestamp")
	query_list3 = hostel.objects.filter(user = i).order_by("-timestamp")
	query_list4 = acad.objects.filter(user = i).order_by("-timestamp")
	query_list5 = other.objects.filter(user = i).order_by("-timestamp")
	query_list6 = soc.objects.filter(user = i).order_by("-timestamp")


	latest = list(sorted(chain(query_list,query_list2,query_list3,query_list4,query_list5,query_list6),key=attrgetter("timestamp"),reverse = True))
	count = len(latest)
	context = {
			'all' : latest,
			'count' : count,

		}
	return render(request,"myquestions.html",context)


def home(request):
	query_list = admission.objects.all().order_by("-timestamp")
	query_list2 = placement.objects.all().order_by("-timestamp")
	query_list3 = hostel.objects.all().order_by("-timestamp")
	query_list4 = acad.objects.all().order_by("-timestamp")
	query_list5 = other.objects.all().order_by("-timestamp")
	query_list6 = soc.objects.all().order_by("-timestamp")



	latest = list(sorted(chain(query_list,query_list2,query_list3,query_list4,query_list5,query_list6),key=attrgetter("timestamp"),reverse = True))
	all1 = list(sorted(chain(query_list,query_list2,query_list3,query_list4,query_list5,query_list6),key=attrgetter("timestamp"),reverse = True))


	c = len(latest)

	# count = admission_Answer.objects.count
	paginator = Paginator(query_list, 10 )
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)



	paginator = Paginator(query_list2, 10 )
	page = request.GET.get('page')
	try:
		queryset2 = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset2 = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset2 = paginator.page(paginator.num_pages)

	paginator = Paginator(query_list3, 10 )
	page = request.GET.get('page')
	try:
		queryset3 = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset3 = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset3 = paginator.page(paginator.num_pages)

	paginator = Paginator(query_list4, 10 )
	page = request.GET.get('page')
	try:
		queryset4 = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset4 = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset4 = paginator.page(paginator.num_pages)

	paginator = Paginator(query_list5, 10 )
	page = request.GET.get('page')
	try:
		queryset5 = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset5 = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset5 = paginator.page(paginator.num_pages)

	paginator = Paginator(query_list6, 10 )
	page = request.GET.get('page')
	try:
		queryset6 = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset6 = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset6 = paginator.page(paginator.num_pages)            

	
	paginator = Paginator(latest, 15 )
	page = request.GET.get('page')
	try:
		latest1 = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    latest1 = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    latest1 = paginator.page(paginator.num_pages)

	        

	context = RequestContext(request, {
		'query':queryset,
		
		'queryplc' :queryset2 ,
		'queryhostel' :queryset3 ,
		'queryacad' :queryset4 ,
		'queryother' :queryset5 ,
		'querysoc' :queryset6 ,
		'latest': latest1,
		'all' : all1,
		'count':c,
		})
	return render(request,"home.html",context)

def tag(request,tag = None):
	word = tag
	query_list = admission.objects.filter(tags__slug__contains=word).order_by("-timestamp")
	query_listplc = placement.objects.filter(tags__slug__contains=word).order_by("-timestamp")
	query_listhostel = hostel.objects.filter(tags__slug__contains=word).order_by("-timestamp")
	query_listacad = acad.objects.filter(tags__slug__contains=word).order_by("-timestamp")
	query_listother = other.objects.filter(tags__slug__contains=word).order_by("-timestamp")
	query_listsoc = soc.objects.filter(tags__slug__contains=word).order_by("-timestamp")

	latest = list(sorted(chain(query_list,query_listplc,query_listhostel,query_listacad,query_listother,query_listsoc),key=attrgetter("timestamp"),reverse = True))



	query_adm = admission.objects.all().order_by("-timestamp")
	query_plc = placement.objects.all().order_by("-timestamp")
	query_hostel = hostel.objects.all().order_by("-timestamp")
	query_acad = acad.objects.all().order_by("-timestamp")
	query_other = other.objects.all().order_by("-timestamp")
	query_soc = soc.objects.all().order_by("-timestamp")

	all1 = list(sorted(chain(query_adm,query_plc,query_hostel,query_acad,query_other,query_soc),key=attrgetter("timestamp"),reverse = True))

	paginator = Paginator(query_list, 10 )
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	paginator = Paginator(query_listplc, 10 )
	page = request.GET.get('page')
	try:
		queryset2 = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset2 = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		queryset2 = paginator.page(paginator.num_pages)    

	paginator = Paginator(query_listhostel, 10 )
	page = request.GET.get('page')
	try:
		queryset3 = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset3 = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		queryset3 = paginator.page(paginator.num_pages) 

	
	paginator = Paginator(query_listacad, 10 )
	page = request.GET.get('page')
	try:
		queryset4 = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset4 = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		queryset4 = paginator.page(paginator.num_pages) 	

	paginator = Paginator(query_listother, 10 )
	page = request.GET.get('page')
	try:
		queryset5 = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset5 = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		queryset5 = paginator.page(paginator.num_pages)

	paginator = Paginator(query_listsoc, 10 )
	page = request.GET.get('page')
	try:
		queryset6 = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset6 = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		queryset6 = paginator.page(paginator.num_pages) 	 
##########33 latest tags
	
	paginator = Paginator(latest, 15 )
	page = request.GET.get('page')
	try:
		latest1 = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    latest1 = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    latest1 = paginator.page(paginator.num_pages)

	template = loader.get_template('home.html')
	context = RequestContext(request, {


		'query':queryset,
		
		'queryplc': queryset2,
		'queryhostel': queryset3,
		'queryacad': queryset4,
		'queryother': queryset5,
		'querysoc': queryset6,
		'latest' : latest1,
		'all' : all1,
		
		})
	return HttpResponse(template.render(context))





def latestquerylist(request):
	query_adm = admission.objects.all().order_by("-timestamp")
	query_plc = placement.objects.all().order_by("-timestamp")
	query_hostel = hostel.objects.all().order_by("-timestamp")
	query_acad = acad.objects.all().order_by("-timestamp")
	query_other = other.objects.all().order_by("-timestamp")
	query_soc = soc.objects.all().order_by("-timestamp")

	all1 = list(sorted(chain(query_plc,query_adm,query_hostel,query_acad,query_other,query_soc),key=attrgetter("timestamp"),reverse = True))	

	paginator = Paginator(all1, 30 )
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
	
	"query":queryset,
	}
 	return render(request,"latestlist.html",context)

		

def about(request):
	return render(request,"aboutus.html",{})

def contact(request):
	return render(request,"contact.html",{})


def querytype(request):
	return render(request,"querytype.html",{})


def admquery(request):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	form = admission_form(request.POST or None)
	

	if form.is_valid():


		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		regex = r"([$&+:;=?@#|'<>.^*()%!-])"
		if re.search(regex, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid using speacial characters in tags"})

		reg = r"([ \t\n\r\f\v])"
		if re.search(reg, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid spaces in tags"})
		instance.user=request.user
		instance.save()
		
			





		tagt = tags_text.split(',')
		print tagt
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form":form,
	
	}
	return render(request,"adm_query.html",context)

def admquerylist(request):
	query_list = admission.objects.all().order_by("-timestamp")
	paginator = Paginator(query_list, 30 )
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
	
	"query":queryset,
	}
 	return render(request,"admquerylist.html",context)

def admquerydetail(request,id=None):
	instance=get_object_or_404( admission,id=id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id

	


				
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)
	if not admissionhits.objects.filter(
					title=instance,
					session=request.session.session_key,ip=request.META['REMOTE_ADDR']):
		view = admissionhits(title=instance,
							ip=request.META['REMOTE_ADDR'],
							created=datetime.datetime.now(),
							session=request.session.session_key)
		view.save()
		instance.hits = instance.hits + 1
		instance.save()
	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = admission_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = admission_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = admission_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = admission_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	
		
	answers = admission_Answer.objects.filter_by_instance(instance).order_by("-votes")	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	
	
	}
 	return render(request,"admquerydetail.html",context)

def admqueryupdate(request,id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	
	instance=get_object_or_404( admission,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post')
    
	c=len(instance.tags.all())
	t= instance.tags.all()
	d=''
	for x in range(0,c-1) :
		d=d+str(t[x])+','

	d=d+str(t[c-1])
	tt=d
	form = admission_form(request.POST or None ,instance= instance, initial = {'tags': tt })
	


	if form.is_valid():
		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		instance.save()
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"instance":instance,
	"form":form,
	
	}
	return render(request,"adm_query.html",context)
		

def admquerydelete(request, id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')

	instance=get_object_or_404( admission,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post') 
	instance.delete()
	return redirect('admquerylist')

def voteadm(request, question_id, answer_id,op_code):
	instance=get_object_or_404( admission,id= question_id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	user_ob = request.user
	answer = admission_Answer.objects.get(pk=answer_id)
	answers = admission_Answer.objects.filter_by_instance(instance).order_by("-votes")
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)
	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = admission_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = admission_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = admission_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = admission_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	

	if admission_Answer.objects.filter(id=answer_id, user=user_ob).exists():
		return render(request, 'admquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You cannot vote on your answer!"})

	if Voteradm.objects.filter(answer = answer_id, user = user_ob).exists():
		return render(request, 'admquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You've already cast vote on this answer!"})

	if op_code == '0':
		answer.votes += 1

	if op_code == '1':
		answer.votes -= 1
	answer.save()
	v = Voteradm()
	v.user = request.user
	v.answer = answer
	v.save()	
	answers = admission_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	
	}
 	return render(request,"admquerydetail.html",context)












	##########################################3





def plcmntquery(request):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	form = placement_form(request.POST or None)
	

	if form.is_valid():


		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		regex = r"([$&+:;=?@#|'<>.^*()%!-])"
		if re.search(regex, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid using speacial characters in tags"})

		reg = r"([ \t\n\r\f\v])"
		if re.search(reg, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid spaces in tags"})
		instance.user=request.user
		instance.save()
		
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form":form,
	
	}
	return render(request,"plcmnt_query.html",context)

def plcmntquerylist(request):
	query_list = placement.objects.all().order_by("-timestamp")
	paginator = Paginator(query_list, 30 )
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
	
	"query":queryset,
	}
 	return render(request,"plcmntquerylist.html",context)

def plcmntquerydetail(request,id=None):
	instance=get_object_or_404( placement,id=id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)

	if not placementhits.objects.filter(
					title=instance,
					session=request.session.session_key,ip=request.META['REMOTE_ADDR']):
		view = placementhits(title=instance,
							ip=request.META['REMOTE_ADDR'],
							created=datetime.datetime.now(),
							session=request.session.session_key)
		view.save()
		instance.hits = instance.hits + 1
		instance.save()



	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = placement_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = placement_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = placement_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = placement_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	
		
	answers = placement_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	}
 	return render(request,"plcmntquerydetail.html",context)

def plcmntqueryupdate(request,id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	
	instance=get_object_or_404( placement,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post')
    
	c=len(instance.tags.all())
	t= instance.tags.all()
	d=''
	for x in range(0,c-1) :
		d=d+str(t[x])+','

	d=d+str(t[c-1])
	tt=d
	form = placement_form(request.POST or None ,instance= instance, initial = {'tags': tt })
	


	if form.is_valid():
		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		instance.save()
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"instance":instance,
	"form":form,
	
	}
	return render(request,"plcmnt_query.html",context)
		

def plcmntquerydelete(request, id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')

	instance=get_object_or_404( placement,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post') 
	instance.delete()
	return redirect('plcmntquerylist')	



def voteplc(request, question_id, answer_id,op_code):
	instance=get_object_or_404( placement,id= question_id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	user_ob = request.user
	answer = placement_Answer.objects.get(pk=answer_id)
	answers = placement_Answer.objects.filter_by_instance(instance).order_by("-votes")
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)
	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = placement_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = placement_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = placement_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = placement_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	

	if placement_Answer.objects.filter(id=answer_id, user=user_ob).exists():
		return render(request, 'plcmntquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You cannot vote on your answer!"})

	if Voterplc.objects.filter(answer = answer_id, user = user_ob).exists():
		return render(request, 'plcmntquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You've already cast vote on this answer!"})

	if op_code == '0':
		answer.votes += 1

	if op_code == '1':
		answer.votes -= 1
	answer.save()
	v = Voterplc()
	v.user = request.user
	v.answer = answer
	v.save()	
	answers = placement_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	
	
	}
 	return render(request,"plcmntquerydetail.html",context)


# =======================================================================================================



def hostelquery(request):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	form = hostel_form(request.POST or None)
	

	if form.is_valid():


		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		regex = r"([$&+:;=?@#|'<>.^*()%!-])"
		if re.search(regex, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid using speacial characters in tags"})

		reg = r"([ \t\n\r\f\v])"
		if re.search(reg, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid spaces in tags"})
		instance.user=request.user
		instance.save()
		
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form":form,
	
	}
	return render(request,"hostel_query.html",context)

def hostelquerylist(request):
	query_list = hostel.objects.all().order_by("-timestamp")
	paginator = Paginator(query_list, 30 )
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
	
	"query":queryset,
	}
 	return render(request,"hostelquerylist.html",context)

def hostelquerydetail(request,id=None):
	instance=get_object_or_404( hostel,id=id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)

	if not hostelhits.objects.filter(
					title=instance,
					session=request.session.session_key,ip=request.META['REMOTE_ADDR']):
		view = hostelhits(title=instance,
							ip=request.META['REMOTE_ADDR'],
							created=datetime.datetime.now(),
							session=request.session.session_key)
		view.save()
		instance.hits = instance.hits + 1
		instance.save()



	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = hostel_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = hostel_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = hostel_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = hostel_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	
		
	answers = hostel_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	}
 	return render(request,"hostelquerydetail.html",context)

def hostelqueryupdate(request,id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	
	instance=get_object_or_404( hostel,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post')
    
	c=len(instance.tags.all())
	t= instance.tags.all()
	d=''
	for x in range(0,c-1) :
		d=d+str(t[x])+','

	d=d+str(t[c-1])
	tt=d
	form = hostel_form(request.POST or None ,instance= instance, initial = {'tags': tt })
	


	if form.is_valid():
		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		instance.save()
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"instance":instance,
	"form":form,
	
	}
	return render(request,"hostel_query.html",context)
		

def hostelquerydelete(request, id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')

	instance=get_object_or_404( hostel,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post') 
	instance.delete()
	return redirect('hostelquerylist')	



def votehostel(request, question_id, answer_id,op_code):
	instance=get_object_or_404( hostel,id= question_id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	user_ob = request.user
	answer = hostel_Answer.objects.get(pk=answer_id)
	answers = hostel_Answer.objects.filter_by_instance(instance).order_by("-votes")
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)
	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = hostel_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = hostel_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = hostel_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = hostel_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	

	if hostel_Answer.objects.filter(id=answer_id, user=user_ob).exists():
		return render(request, 'hostelquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You cannot vote on your answer!"})

	if Voterhostel.objects.filter(answer = answer_id, user = user_ob).exists():
		return render(request, 'hostelquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You've already cast vote on this answer!"})

	if op_code == '0':
		answer.votes += 1

	if op_code == '1':
		answer.votes -= 1
	answer.save()
	v = Voterhostel()
	v.user = request.user
	v.answer = answer
	v.save()	
	answers = hostel_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	
	
	}
 	return render(request,"hostelquerydetail.html",context)




# =============================================================================




def acadquery(request):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	form = acad_form(request.POST or None)
	

	if form.is_valid():


		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		regex = r"([$&+:;=?@#|'<>.^*()%!-])"
		if re.search(regex, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid using speacial characters in tags"})

		reg = r"([ \t\n\r\f\v])"
		if re.search(reg, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid spaces in tags"})
		instance.user=request.user
		instance.save()
		
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form":form,
	
	}
	return render(request,"acad_query.html",context)

def acadquerylist(request):
	query_list = acad.objects.all().order_by("-timestamp")
	paginator = Paginator(query_list, 30 )
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
	
	"query":queryset,
	}
 	return render(request,"acadquerylist.html",context)

def acadquerydetail(request,id=None):
	instance=get_object_or_404( acad,id=id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)

	if not acadhits.objects.filter(
					title=instance,
					session=request.session.session_key,ip=request.META['REMOTE_ADDR']):
		view = acadhits(title=instance,
							ip=request.META['REMOTE_ADDR'],
							created=datetime.datetime.now(),
							session=request.session.session_key)
		view.save()
		instance.hits = instance.hits + 1
		instance.save()



	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = acad_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = acad_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = acad_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = acad_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	
		
	answers = acad_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	}
 	return render(request,"acadquerydetail.html",context)

def acadqueryupdate(request,id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	
	instance=get_object_or_404( acad,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post')
    
	c=len(instance.tags.all())
	t= instance.tags.all()
	d=''
	for x in range(0,c-1) :
		d=d+str(t[x])+','

	d=d+str(t[c-1])
	tt=d
	form = acad_form(request.POST or None ,instance= instance, initial = {'tags': tt })
	


	if form.is_valid():
		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		instance.save()
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"instance":instance,
	"form":form,
	
	}
	return render(request,"acad_query.html",context)
		

def acadquerydelete(request, id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')

	instance=get_object_or_404( acad,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post') 
	instance.delete()
	return redirect('acadquerylist')	



def voteacad(request, question_id, answer_id,op_code):
	instance=get_object_or_404( acad,id= question_id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	user_ob = request.user
	answer = acad_Answer.objects.get(pk=answer_id)
	answers = acad_Answer.objects.filter_by_instance(instance).order_by("-votes")
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)
	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = acad_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = acad_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = acad_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = acad_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	

	if acad_Answer.objects.filter(id=answer_id, user=user_ob).exists():
		return render(request, 'acadquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You cannot vote on your answer!"})

	if Voteracad.objects.filter(answer = answer_id, user = user_ob).exists():
		return render(request, 'acadquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You've already cast vote on this answer!"})

	if op_code == '0':
		answer.votes += 1

	if op_code == '1':
		answer.votes -= 1
	answer.save()
	v = Voteracad()
	v.user = request.user
	v.answer = answer
	v.save()	
	answers = acad_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	
	
	}
 	return render(request,"acadquerydetail.html",context)


# ==========================================================================================



def otherquery(request):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	form = other_form(request.POST or None)
	

	if form.is_valid():


		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		regex = r"([$&+:;=?@#|'<>.^*()%!-])"
		if re.search(regex, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid using speacial characters in tags"})

		reg = r"([ \t\n\r\f\v])"
		if re.search(reg, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid spaces in tags"})
		instance.user=request.user
		instance.save()
		
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form":form,
	
	}
	return render(request,"other_query.html",context)

def otherquerylist(request):
	query_list = other.objects.all().order_by("-timestamp")
	paginator = Paginator(query_list, 30 )
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
	
	"query":queryset,
	}
 	return render(request,"otherquerylist.html",context)

def otherquerydetail(request,id=None):
	instance=get_object_or_404( other,id=id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)

	if not otherhits.objects.filter(
					title=instance,
					session=request.session.session_key,ip=request.META['REMOTE_ADDR']):
		view = otherhits(title=instance,
							ip=request.META['REMOTE_ADDR'],
							created=datetime.datetime.now(),
							session=request.session.session_key)
		view.save()
		instance.hits = instance.hits + 1
		instance.save()



	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = other_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = other_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = other_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = other_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	
		
	answers = other_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	}
 	return render(request,"otherquerydetail.html",context)

def otherqueryupdate(request,id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	
	instance=get_object_or_404( other,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post')
    
	c=len(instance.tags.all())
	t= instance.tags.all()
	d=''
	for x in range(0,c-1) :
		d=d+str(t[x])+','

	d=d+str(t[c-1])
	tt=d
	form = other_form(request.POST or None ,instance= instance, initial = {'tags': tt })
	


	if form.is_valid():
		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		instance.save()
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"instance":instance,
	"form":form,
	
	}
	return render(request,"other_query.html",context)
		

def otherquerydelete(request, id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')

	instance=get_object_or_404( other,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post') 
	instance.delete()
	return redirect('otherquerylist')	



def voteother(request, question_id, answer_id,op_code):
	instance=get_object_or_404( other,id= question_id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	user_ob = request.user
	answer = other_Answer.objects.get(pk=answer_id)
	answers = other_Answer.objects.filter_by_instance(instance).order_by("-votes")
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)
	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = other_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = other_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = other_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = other_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	

	if other_Answer.objects.filter(id=answer_id, user=user_ob).exists():
		return render(request, 'otherquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You cannot vote on your answer!"})

	if Voterother.objects.filter(answer = answer_id, user = user_ob).exists():
		return render(request, 'otherquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You've already cast vote on this answer!"})

	if op_code == '0':
		answer.votes += 1

	if op_code == '1':
		answer.votes -= 1
	answer.save()
	v = Voterother()
	v.user = request.user
	v.answer = answer
	v.save()	
	answers = other_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	
	
	}
 	return render(request,"otherquerydetail.html",context)



# = ==================================================================================================



def socquery(request):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	form = soc_form(request.POST or None)
	

	if form.is_valid():


		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		regex = r"([$&+:;=?@#|'<>.^*()%!-])"
		if re.search(regex, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid using speacial characters in tags"})

		reg = r"([ \t\n\r\f\v])"
		if re.search(reg, tags_text):
			return render(request,"adm_query.html",{"form":form,"message":"Avoid spaces in tags"})
		instance.user=request.user
		instance.save()
		
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form":form,
	
	}
	return render(request,"soc_query.html",context)

def socquerylist(request):
	query_list = soc.objects.all().order_by("-timestamp")
	paginator = Paginator(query_list, 30 )
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    #If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {
	
	"query":queryset,
	}
 	return render(request,"socquerylist.html",context)

def socquerydetail(request,id=None):
	instance=get_object_or_404( soc,id=id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)

	if not sochits.objects.filter(
					title=instance,
					session=request.session.session_key,ip=request.META['REMOTE_ADDR']):
		view = sochits(title=instance,
							ip=request.META['REMOTE_ADDR'],
							created=datetime.datetime.now(),
							session=request.session.session_key)
		view.save()
		instance.hits = instance.hits + 1
		instance.save()



	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = soc_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = soc_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = soc_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = soc_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	
		
	answers = soc_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	}
 	return render(request,"socquerydetail.html",context)

def socqueryupdate(request,id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')
	
	instance=get_object_or_404( soc,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post')
    
	c=len(instance.tags.all())
	t= instance.tags.all()
	d=''
	for x in range(0,c-1) :
		d=d+str(t[x])+','

	d=d+str(t[c-1])
	tt=d
	form = soc_form(request.POST or None ,instance= instance, initial = {'tags': tt })
	


	if form.is_valid():
		instance=form.save(commit=False)
		tags_text = form.cleaned_data.get('tags')
		instance.save()
		tagt = tags_text.split(',')
		for tag in tagt:
			if tag != '':
				tag=tag.rstrip()
				tag=tag.lstrip()
				try:
					t = Tag.objects.get(slug=tag)
					instance.tags.add(t)
				except Tag.DoesNotExist:
					t=Tag()
					t.slug = tag
					t.save()
					instance.tags.add(t)
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"instance":instance,
	"form":form,
	
	}
	return render(request,"soc_query.html",context)
		

def socquerydelete(request, id=None):
	if not request.user.is_authenticated():
		raise Http404('You have to login')

	instance=get_object_or_404( soc,id=id)
	if instance.user != request.user :
		raise Http404('You are not the author of this post') 
	instance.delete()
	return redirect('socquerylist')	



def votesoc(request, question_id, answer_id,op_code):
	instance=get_object_or_404( soc,id= question_id)
	i = get_object_or_404( User,username = instance.user)
	p = i.id
	user_ob = request.user
	answer = soc_Answer.objects.get(pk=answer_id)
	answers = soc_Answer.objects.filter_by_instance(instance).order_by("-votes")
	initial_data = {
			"content_type" : instance.get_content_type,
			"object_id" : instance.id,
			}
	answer_form = AnswerForm(request.POST or None , initial = initial_data )
	reply_form = ReplyForm(request.POST or None , initial = initial_data)
	if(request.user.is_authenticated):
	    # if (request.user != instance.user):
			

			if answer_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = soc_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = soc_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())


			
			if reply_form.is_valid():
				c_type = answer_form.cleaned_data.get('content_type')
				content_type = ContentType.objects.get(model=c_type)
				obj_id = answer_form.cleaned_data.get('object_id')
				content_data = answer_form.cleaned_data.get('answer_text')
				parent_obj = None
				try:
					parent_id = int(request.POST.get("parent_id"))
				except:
					parent_id = None

				if parent_id:
					parent_qs = soc_Answer.objects.filter(id= parent_id)
					if parent_qs.exists() and parent_qs.count() == 1:
						parent_obj = parent_qs.first()


				new_answer, created = soc_Answer.objects.get_or_create(

					user=request.user,
					content_type=content_type,
					object_id=obj_id,
					answer_text=content_data,
					pub_date = datetime.datetime.now(),
					parent = parent_obj



					)
				return HttpResponseRedirect(new_answer.content_object.get_absolute_url())	

	if soc_Answer.objects.filter(id=answer_id, user=user_ob).exists():
		return render(request, 'socquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You cannot vote on your answer!"})

	if Votersoc.objects.filter(answer = answer_id, user = user_ob).exists():
		return render(request, 'socquerydetail.html', {'instance': instance, 'answers': answers, 	"answer_form":answer_form,
	"reply_form":reply_form,"p":p,
	 'message':"You've already cast vote on this answer!"})

	if op_code == '0':
		answer.votes += 1

	if op_code == '1':
		answer.votes -= 1
	answer.save()
	v = Votersoc()
	v.user = request.user
	v.answer = answer
	v.save()	
	answers = soc_Answer.objects.filter_by_instance(instance)	
	context = {
	"instance":instance,
	"answers":answers,
	"answer_form":answer_form,
	"reply_form":reply_form,
	"p":p,
	
	
	}
 	return render(request,"socquerydetail.html",context)
