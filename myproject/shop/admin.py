from django.contrib import admin

# Register your models here.
from .models import register, products, Cart, Address, Order, OrderDetail, OrderStatus


class registerAdmin(admin.ModelAdmin):
    list_display = ['username','email','password']

class orderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_text']

class productAdmin(admin.ModelAdmin):
    list_display = ['id','type','category','subcategory','name','brand','price','quantity','image']

class cartAdmin(admin.ModelAdmin):
    list_display = ['userid','product_id','quantity']

class orderAdmin(admin.ModelAdmin):
    list_display = ['userid','address_id', 'status', 'status_text', 'amount', 'payment_method' ,'created', 'updated']

class orderDetailAdmin(admin.ModelAdmin):
	list_display=['order_id','product_id','quantity','price']

class cartAddress(admin.ModelAdmin):
	list_display=['userid','fname','lname','hm_name','address1','address2','pincode','mobile']

admin.site.register(register,registerAdmin)
admin.site.register(Cart,cartAdmin)
admin.site.register(products,productAdmin)
admin.site.register(Address,cartAddress)
admin.site.register(Order,orderAdmin)
admin.site.register(OrderStatus,orderStatusAdmin)
admin.site.register(OrderDetail,orderDetailAdmin)

