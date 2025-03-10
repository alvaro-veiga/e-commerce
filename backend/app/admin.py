from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user", "totalPrice", "createdAt"
    ]