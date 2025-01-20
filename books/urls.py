from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
      path('book_details/<int:id>/', views.book_details, name='book_details'), # URL to display the book list
     # path('', views.home, name='home'), # URL to display the book list
]
