from django.contrib import admin
from .models import Brand, Product,Customer, Order, OrderItem,ShippingAddress
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display=['name', 'slug']
    prepopulated_fields ={'slug':('name',)}

admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'brand', 'price', 'slug']
    prepopulated_fields ={'slug':('name',)}

admin.site.register(Product,ProductAdmin)

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)