from django.contrib import admin

# Register your models here.
from .models import register, products, Cart


class registerAdmin(admin.ModelAdmin):
    list_display = ['username','email','password']

class productAdmin(admin.ModelAdmin):
    list_display = ['id','type','category','subcategory','name','brand','price','quantity','image']

class cartAdmin(admin.ModelAdmin):
    list_display = ['userid','product_id','quantity']
admin.site.register(register,registerAdmin)
admin.site.register(Cart,cartAdmin)
admin.site.register(products,productAdmin)

