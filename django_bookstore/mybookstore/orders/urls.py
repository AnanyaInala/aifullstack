# orders/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_history, name='order_history'), # Displays user's order history
]