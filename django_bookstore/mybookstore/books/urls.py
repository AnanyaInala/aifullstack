# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Homepage (now only trending)
    path('all/', views.all_books, name='all_books'), # <--- New: All Books page
    path('<int:pk>/', views.book_detail, name='book_detail'),
]