from django.contrib import admin
from .models import userSignup,mynotes,adminRegister

# Register your models here.
class adminAdmin(admin.ModelAdmin):
    list_display=['username','password']

class signupAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','username','city','state','mobile']

class notesAdmin(admin.ModelAdmin):
    list_display=['title','cate','myfiles','comments']

admin.site.register(userSignup,signupAdmin)
admin.site.register(mynotes,notesAdmin)
admin.site.register(adminRegister,adminAdmin)