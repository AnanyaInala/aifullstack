# books/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q # Import Q object for complex queries
from .models import Book

@login_required
def home(request):
    """
    Displays the bookstore homepage with ONLY trending books.
    """
    bookstore_name = "My Awesome Bookstore" # You can change this name!
    trending_books = Book.objects.filter(is_trending=True).order_by('title')

    context = {
        'bookstore_name': bookstore_name,
        'trending_books': trending_books,
        'currency_symbol_usd': '$', # For display
        'currency_symbol_inr': '₹', # For display
    }
    return render(request, 'home.html', context)

@login_required
def all_books(request):
    """
    Displays all books with search and filter/sort options.
    """
    bookstore_name = "My Awesome Bookstore" # Can reuse or define differently
    books = Book.objects.all()

    # --- Search Logic ---
    query = request.GET.get('q')
    if query:
        books = books.filter(
            Q(title__icontains=query) | # Case-insensitive search in title
            Q(author__icontains=query) # Case-insensitive search in author
        )

    # --- Filter/Sort Logic ---
    sort_by = request.GET.get('sort_by', 'title') # Default sort by title
    order = request.GET.get('order', 'asc') # Default order ascending

    if sort_by == 'price':
        if order == 'desc':
            books = books.order_by('-price')
        else:
            books = books.order_by('price')
    elif sort_by == 'published_year':
        if order == 'desc':
            books = books.order_by('-published_year')
        else:
            books = books.order_by('published_year')
    else: # Default or invalid sort_by, sort by title
        if order == 'desc':
            books = books.order_by('-title')
        else:
            books = books.order_by('title')

    context = {
        'bookstore_name': bookstore_name,
        'books': books, # Renamed from trending_books to just books
        'query': query, # Pass back the query for the search bar
        'sort_by': sort_by, # Pass back the sort_by for dropdown selection
        'order': order, # Pass back the order for dropdown selection
        'currency_symbol_usd': '$', # For display
        'currency_symbol_inr': '₹', # For display
    }
    return render(request, 'books/all_books.html', context) # Render new template

@login_required
def book_detail(request, pk): # <--- CORRECTED FUNCTION
    """
    Displays the details of a single book.
    """
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book,
        'currency_symbol_usd': '$', # Pass currency symbols
        'currency_symbol_inr': '₹', # Pass currency symbols
    }
    return render(request, 'books/book_detail.html', context) # <--- THIS IS THE MISSING RETURN