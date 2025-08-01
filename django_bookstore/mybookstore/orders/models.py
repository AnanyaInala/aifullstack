# orders/models.py

from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from decimal import Decimal

class Order(models.Model):
    """
    Represents a completed order made by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, default='Cash on Delivery')
    is_paid = models.BooleanField(default=False)
    delivery_status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Processing', 'Processing'),
            ('Shipped', 'Shipped'),
            ('Delivered', 'Delivered'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending'
    )

    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return f"Order {self.id} by {self.user.username} on {self.order_date.strftime('%Y-%m-%d %H:%M')}"

class OrderItem(models.Model):
    """
    Represents a single book item within a completed order.
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # The price field is now nullable to prevent this error
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.book.title} (Order {self.order.id})"

    @property
    def total_price(self):
        """
        Calculates the total price for this specific order item.
        Handles cases where price might be None.
        """
        if self.price is not None:
            return self.quantity * self.price
        return Decimal('0.00')