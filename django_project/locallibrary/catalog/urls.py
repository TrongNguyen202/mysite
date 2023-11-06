from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [path('', views.index, name='index'),]

urlpatterns+= [path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:id>', views.BookDetailView, name='book_detail')]

=======
urlpatterns = [path('', views.index, name='index'),]
>>>>>>> ec60141 (Add files via upload)
