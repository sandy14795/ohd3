"""ohd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns,include, url



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tags/(?P<tag>\w+)/$', 'posts.views.tag', name='tagt'),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^$', 'posts.views.home',name='home'),
    url(r'^about/', 'posts.views.about',name='about'),
    url(r'^contact/', 'posts.views.contact',name='contact'),

    url(r'^query/', 'posts.views.querytype',name='query'),
    url(r'^search/$', 'posts.views.search', name='search'),
    url(r'^latest/queries', 'posts.views.latestquerylist',name='latestquerylist'),
    url(r'^profile/(?P<id>\d+)/$', 'posts.views.profile',name='profile'),
    url(r'^myprofile', 'posts.views.ownprofile',name='ownprofile'),
    url(r'^myquestions', 'posts.views.myques',name='myques'),




    
    url(r'^ask_query/admissions/', 'posts.views.admquery',name='admqueryask'),
    url(r'^admissions/queries', 'posts.views.admquerylist',name='admquerylist'),
    url(r'^admissions/querydetail/(?P<id>\d+)/$', 'posts.views.admquerydetail',name='admquerydetail'),
    url(r'^admissions/querydetail/(?P<id>\d+)/edit/$', 'posts.views.admqueryupdate',name='admqueryedit'),
    url(r'^admissions/querydetail/(?P<id>\d+)/delete/$', 'posts.views.admquerydelete',name='admquerydel'),
    url(r'^voteadm/(?P<question_id>\d+)/(?P<answer_id>\d+)/(?P<op_code>\d+)/$', 'posts.views.voteadm', name='voteadm'),


    url(r'^ask_query/placements/', 'posts.views.plcmntquery',name='plcmntqueryask'),
    url(r'^placements/queries', 'posts.views.plcmntquerylist',name='plcmntquerylist'),
    url(r'^placements/querydetail/(?P<id>\d+)/$', 'posts.views.plcmntquerydetail',name='plcmntquerydetail'),
    url(r'^placements/querydetail/(?P<id>\d+)/edit/$', 'posts.views.plcmntqueryupdate',name='plcmntqueryedit'),
    url(r'^placements/querydetail/(?P<id>\d+)/delete/$', 'posts.views.plcmntquerydelete',name='plcmntquerydel'),
    url(r'^voteplc/(?P<question_id>\d+)/(?P<answer_id>\d+)/(?P<op_code>\d+)/$', 'posts.views.voteplc', name='voteplc'),


    url(r'^ask_query/hostel/', 'posts.views.hostelquery',name='hostelqueryask'),
    url(r'^hostel/queries', 'posts.views.hostelquerylist',name='hostelquerylist'),
    url(r'^hostel/querydetail/(?P<id>\d+)/$', 'posts.views.hostelquerydetail',name='hostelquerydetail'),
    url(r'^hostel/querydetail/(?P<id>\d+)/edit/$', 'posts.views.hostelqueryupdate',name='hostelqueryedit'),
    url(r'^hostel/querydetail/(?P<id>\d+)/delete/$', 'posts.views.hostelquerydelete',name='hostelquerydel'),
    url(r'^votehostel/(?P<question_id>\d+)/(?P<answer_id>\d+)/(?P<op_code>\d+)/$', 'posts.views.votehostel', name='votehostel'),


    url(r'^ask_query/academics/', 'posts.views.acadquery',name='acadqueryask'),
    url(r'^academics/queries', 'posts.views.acadquerylist',name='acadquerylist'),
    url(r'^academics/querydetail/(?P<id>\d+)/$', 'posts.views.acadquerydetail',name='acadquerydetail'),
    url(r'^academics/querydetail/(?P<id>\d+)/edit/$', 'posts.views.acadqueryupdate',name='acadqueryedit'),
    url(r'^academics/querydetail/(?P<id>\d+)/delete/$', 'posts.views.acadquerydelete',name='acadquerydel'),
    url(r'^voteacad/(?P<question_id>\d+)/(?P<answer_id>\d+)/(?P<op_code>\d+)/$', 'posts.views.voteacad', name='voteacad'),


    url(r'^ask_query/other/', 'posts.views.otherquery',name='otherqueryask'),
    url(r'^other/queries', 'posts.views.otherquerylist',name='otherquerylist'),
    url(r'^other/querydetail/(?P<id>\d+)/$', 'posts.views.otherquerydetail',name='otherquerydetail'),
    url(r'^other/querydetail/(?P<id>\d+)/edit/$', 'posts.views.otherqueryupdate',name='otherqueryedit'),
    url(r'^other/querydetail/(?P<id>\d+)/delete/$', 'posts.views.otherquerydelete',name='otherquerydel'),
    url(r'^voteother/(?P<question_id>\d+)/(?P<answer_id>\d+)/(?P<op_code>\d+)/$', 'posts.views.voteother', name='voteother'),


    url(r'^ask_query/soc/', 'posts.views.socquery',name='socqueryask'),
    url(r'^soc/queries', 'posts.views.socquerylist',name='socquerylist'),
    url(r'^soc/querydetail/(?P<id>\d+)/$', 'posts.views.socquerydetail',name='socquerydetail'),
    url(r'^soc/querydetail/(?P<id>\d+)/edit/$', 'posts.views.socqueryupdate',name='socqueryedit'),
    url(r'^soc/querydetail/(?P<id>\d+)/delete/$', 'posts.views.socquerydelete',name='socquerydel'),
    url(r'^votesoc/(?P<question_id>\d+)/(?P<answer_id>\d+)/(?P<op_code>\d+)/$', 'posts.views.votesoc', name='votesoc'),


    url(r'^accounts/',include('allauth.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
   


 


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

