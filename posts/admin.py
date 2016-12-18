from django.contrib import admin

# Register your models here.
from .models import *
from .forms import admission_form






admin.site.register(admission)
admin.site.register(Tag)
admin.site.register(placement)
admin.site.register(placementhits)
admin.site.register(admissionhits)
admin.site.register(hostel)
admin.site.register(hostelhits)
admin.site.register(acad)
admin.site.register(acadhits)
admin.site.register(other)
admin.site.register(otherhits)
admin.site.register(soc)
admin.site.register(sochits)
# admin.site.register(admviews)
