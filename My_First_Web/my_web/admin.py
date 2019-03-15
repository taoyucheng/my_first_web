from django.contrib import admin
from my_web import models
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','phone','sex','create_time',)
    list_editable = ('sex',)

class Cloud_DiskAdmin(admin.ModelAdmin):
    list_display = ("customer","file_name","create_time")

class LogAdmin(admin.ModelAdmin):
    list_display = ("customer","log_head","create_time")

admin.site.register(models.Customer,CustomerAdmin)
admin.site.register(models.Cloud_Disk,Cloud_DiskAdmin)
admin.site.register(models.Log,LogAdmin)
