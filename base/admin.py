from django.contrib import admin

# Register your models here.

from .models import Mentor, Company, Specializations


admin.site.register(Mentor)
admin.site.register(Company)
admin.site.register(Specializations)