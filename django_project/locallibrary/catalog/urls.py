from django.urls import path
from . import views
urlpatterns = [path('', views.index, name='index'),
path('books/', views.BookListView.as_view(), name='books'),
path('book/<int:id>', views.BookDetailView, name='book_detail'),
path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
# path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),


               ]
