from django.contrib import admin
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('job_title', 
                    'first_name', 
                    'last_name',
                    'alt_name', 
                    'birthday', 
                    'phone_number',
                    'group')

    # list_filter = ('job_title', 'manager', 'department')
    # prepopulated_fields = {"slug": ("job_title", "user")}

# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
