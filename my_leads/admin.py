from django.contrib import admin
from .models import *
# Register your models here.


class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender','ip_address','address')
    list_per_page = 20

admin.site.register(Leads, LeadAdmin)
