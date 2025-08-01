# orders/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_history(request):
    """
    Displays the current user's order history.
    """
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    
    context = {
        'orders': orders,
        'currency_symbol_usd': '$',
        'currency_symbol_inr': '₹',
    }
    return render(request, 'orders/order_history.html', context)