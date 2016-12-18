from django import forms
from .models import *
from pagedown.widgets import PagedownWidget



class admission_form(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget())
	tags = forms.CharField(label='Enter comma separated tags')
	class Meta:
		model=admission
		fields=['admission_Program','title','content','tags']


class placement_form(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget())
	tags = forms.CharField(label='Enter comma separated tags')
	class Meta:
		model=placement
		fields=['Program','title','content','tags']

class hostel_form(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget())
	tags = forms.CharField(label='Enter comma separated tags')
	class Meta:
		model=hostel
		fields=['hostel_choice','title','content','tags']


class acad_form(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget())
	tags = forms.CharField(label='Enter comma separated tags')
	class Meta:
		model=acad
		fields=['title','content','tags']


class other_form(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget())
	tags = forms.CharField(label='Enter comma separated tags')
	class Meta:
		model=other
		fields=['title','content','tags']

class soc_form(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget())
	tags = forms.CharField(label='Enter comma separated tags')
	class Meta:
		model=soc
		fields=['title','content','tags']