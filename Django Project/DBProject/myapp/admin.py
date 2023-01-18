from django.contrib import admin
from .models import userInfo

# Register your models here.

class userinfoAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','dob','mobile','address']

admin.site.register(userInfo,userinfoAdmin)