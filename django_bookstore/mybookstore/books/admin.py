# books/admin.py

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'price_inr', 'published_year', 'is_trending')
    list_filter = ('is_trending', 'author', 'published_year')
    search_fields = ('title', 'author')
    # Make sure there is NO 'readonly_fields' line here at all, or it's commented out.
    # For example, this line should NOT exist:
    # readonly_fields = ('title', 'author', 'price', 'description', 'image_url', 'is_trending', 'published_year')