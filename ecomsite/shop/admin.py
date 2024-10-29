from django.contrib import admin
from .models import Products, Order
# Register your models here.


admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shoping"
admin.site.index_title = "Manage ABC Shoping"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'dicsount_price', 'description', 'category')
    search_fields = ('title', 'category')
    list_editable = ('price', 'dicsount_price')

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)