from django.conf.urls.static import static

from django.urls import path

from brs import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),  # Search page URL
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('genre/fiction/', views.genre_fiction, name='genre_fiction'),
    path('genre/nonfiction/', views.genre_nonfiction, name='genre_nonfiction'),
    path('genre/sci-fi/', views.genre_sci_fi, name='genre_sci_fi'),
    path('SignIn/register/', views.register, name='register'),
    path('SignTn/login/', views.user_login, name='login'),
]
