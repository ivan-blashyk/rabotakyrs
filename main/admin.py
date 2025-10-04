from django.contrib import admin
from .models import category,Product

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','available','created','updated']
    list_filter = ['available','created','updated','category']
    list_editable = ['price','available']
    prepopulated_fields =  {'slug': ('name',)}
    