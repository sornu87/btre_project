from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display =['id','name','phone','email','is_mvp']
    list_filter = ['name','is_mvp']
    list_display_links =['id','name']
    search_fields = ['id','name','phone','email','is_mvp']

admin.site.register(Realtor,RealtorAdmin)
