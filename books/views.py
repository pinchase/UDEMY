from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse
def book_list(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the 'book_list.html' template with the list of books
    return render(request, 'book_list.html', {'books': books})

# def home(request):
#     return HttpResponse("Hello, world. You're at the Udemy Bookstore.")

def book_details(request, id):  # Accept 'id' as a parameter
    book = get_object_or_404(Book, pk=id)  # Fetch the book by primary key
    return render(request, 'book_details.html', {'book': book})