from django.contrib import admin
from .models import Product,Orderssssss
# Register your models here.
@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):
    pass 
@admin.register(Orderssssss) 
class OrderssssssAdmin(admin.ModelAdmin):
    pass 