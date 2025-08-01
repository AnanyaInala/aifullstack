# cart/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'), # Displays the cart contents
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'), # Adds a book to the cart
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'), # Updates quantity or removes item
    path('checkout/', views.checkout, name='checkout'), # Displays payment options
    path('process_payment/', views.process_payment, name='process_payment'), # Handles payment selection
]