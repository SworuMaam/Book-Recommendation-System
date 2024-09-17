from django.shortcuts import render,redirect
from .models import Book
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def home(request):
    popular_books = Book.objects.all()  # or apply some filter to get popular books
    return render(request, 'book/home.html', {'popular_books': popular_books})

def about(request):
    return render(request,"book/about.html",{})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'book/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'book/login.html')
# def login(request):
#     return render(request, "book/login.html",{})

def search(request):
    query = request.GET.get('query', '')
    if query:
        # Search for books based on the query
        results = Book.objects.filter(title__icontains=query)  # Adjust as needed
    else:
        results = Book.objects.none()
    return render(request, 'book/search_results.html', {'results': results, 'query': query})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book/book_detail.html', {'book': book})

def genre_fiction(request):
    # Logic for fiction genre
    return render(request, 'book/genre_fiction.html')

def genre_nonfiction(request):
    # Logic for non-fiction genre
    return render(request, 'book/genre_nonfiction.html')

def genre_sci_fi(request):
    return render(request, 'book/genre_sci_fi.html')