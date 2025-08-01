# cart/admin.py

from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    """Inline display for CartItems within the Cart admin."""
    model = CartItem
    extra = 1 # Number of empty forms to display

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at', 'total_price')
    inlines = [CartItemInline] # Show cart items directly in the cart admin page
    readonly_fields = ('created_at', 'updated_at', 'total_price') # These fields are auto-calculated
    search_fields = ('user__username',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'book', 'quantity', 'total_price')
    list_filter = ('cart__user',) # Filter by user associated with the cart
    search_fields = ('book__title', 'cart__user__username')
    readonly_fields = ('total_price',)