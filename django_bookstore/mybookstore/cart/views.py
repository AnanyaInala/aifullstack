# cart/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from books.models import Book # Import Book model
from orders.models import Order, OrderItem # <--- ADD THIS IMPORT
from decimal import Decimal # <--- ADD THIS IMPORT for precise calculations

@login_required
def cart_detail(request):
    """
    Displays the user's cart contents.
    """
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'cart': cart,
        'cart_items': cart.items.all(),
        'currency_symbol_usd': '$', # <--- ADD THIS
        'currency_symbol_inr': '₹', # <--- ADD THIS
    }
    return render(request, 'cart/cart_detail.html', context)

@login_required
def add_to_cart(request, book_id):
    """
    Adds a specified book to the user's cart.
    """
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    quantity = int(request.POST.get('quantity', 1))

    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        book=book,
        defaults={'quantity': quantity}
    )

    if not item_created:
        # If item already exists, update quantity
        cart_item.quantity += quantity
        cart_item.save()

    messages.success(request, f'"{book.title}" added to your cart!')
    return redirect('cart_detail') # Redirect to cart page after adding

@login_required
def update_cart_item(request, item_id):
    """
    Updates the quantity of a cart item or removes it.
    """
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    action = request.POST.get('action') # 'increase', 'decrease', 'remove'

    if action == 'increase':
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'Quantity of "{cart_item.book.title}" increased.')
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, f'Quantity of "{cart_item.book.title}" decreased.')
        else:
            # If quantity is 1 and decreased, remove the item
            cart_item.delete()
            messages.info(request, f'"{cart_item.book.title}" removed from cart.')
    elif action == 'remove':
        cart_item.delete()
        messages.info(request, f'"{cart_item.book.title}" removed from cart.')
    
    return redirect('cart_detail')

@login_required
def checkout(request):
    """
    Displays the checkout page with payment options.
    """
    cart, created = Cart.objects.get_or_create(user=request.user)
    if not cart.items.exists():
        messages.warning(request, "Your cart is empty. Please add items before checking out.")
        return redirect('cart_detail')

    context = {
        'cart': cart,
        'cart_items': cart.items.all(),
        'currency_symbol_usd': '$', # <--- ADD THIS
        'currency_symbol_inr': '₹', # <--- ADD THIS
    }
    return render(request, 'cart/checkout.html', context)

@login_required
def process_payment(request):
    """
    Handles the selected payment method.
    """
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        cart = get_object_or_404(Cart, user=request.user)

        if not cart.items.exists():
            messages.error(request, "Your cart is empty. Cannot process an empty order.")
            return redirect('cart_detail')

        if payment_method == 'upi' or payment_method == 'bank':
            messages.info(request, 'Payment option not available at the moment. Please try Cash on Delivery.')
            return redirect('checkout') # Stay on checkout page with message
        elif payment_method == 'cod':
            # --- Create the Order ---
            order = Order.objects.create(
                user=request.user,
                total_amount=cart.total_price, # Use the calculated total price from the cart
                payment_method='Cash on Delivery',
                is_paid=False, # COD is not paid upfront
                delivery_status='Pending'
            )

            # --- Move CartItems to OrderItems ---
            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    book=cart_item.book,
                    quantity=cart_item.quantity,
                    price=cart_item.book.price # Store the price at the time of order
                )
            
            # --- Clear the Cart ---
            cart.items.all().delete() # Delete all items from the cart

            messages.success(request, f'Order #{order.id} confirmed! You will receive your books in two days. Thank you for your purchase!')
            
            return redirect('order_history') # Redirect to order history to see the new order
        else:
            messages.error(request, 'Invalid payment method selected.')
            return redirect('checkout')
    return redirect('checkout') # Redirect if not a POST request
