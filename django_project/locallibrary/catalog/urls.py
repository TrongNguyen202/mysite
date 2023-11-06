from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),]

urlpatterns+= [path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:id>', views.BookDetailView, name='book_detail')]

