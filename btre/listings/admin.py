from django.contrib import admin
from  .models import Listing

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ['id','title','state','city','price','bedrooms','bathrooms','is_published',]
    list_filter = ['state']
    list_display_links = ['id','title']
    list_editable =['price','is_published']
    search_fields = ['state','city',]
    actions = [ 'submit' ]
    lis_per_page = 2
    def submit():
        return

admin.site.register(Listing,ListingAdmin)
