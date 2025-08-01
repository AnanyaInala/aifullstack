# orders/admin.py

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('book', 'quantity', 'price', 'total_price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_amount', 'payment_method', 'is_paid', 'delivery_status')
    list_filter = ('payment_method', 'is_paid', 'delivery_status', 'order_date')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]
    
    # 'user', 'order_date', 'total_amount' are read-only.
    # 'is_paid' and 'delivery_status' are editable.
    readonly_fields = ('user', 'order_date', 'total_amount')
    
    fieldsets = (
        (None, {
            'fields': ('user', 'order_date', 'total_amount', 'payment_method', 'is_paid')
        }),
        ('Delivery Information', {
            'fields': ('delivery_status',)
        }),
    )