# books/models.py

from django.db import models
from decimal import Decimal # Import for a default value

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_inr = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        default=Decimal('0.00'),
        help_text="Price in Indian Rupees (INR)"
    )
    description = models.TextField()
    image_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="URL for the book cover image"
    )
    is_trending = models.BooleanField(default=False)
    published_year = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Year the book was published"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('book_detail', args=[str(self.id)])