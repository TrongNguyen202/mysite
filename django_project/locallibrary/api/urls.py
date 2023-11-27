from django.urls import path
from .views import BookList, BookDetail,AllBorrowed, RenewBook
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [  path('books/',BookList.as_view(),name = 'book_list'),
                 path('books/<int:pk>/',BookDetail.as_view()),
                 path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
                  path('allborrowed/', AllBorrowed.as_view(), name='allborrowed_list'),
                  path('books/<uuid:pk>/renew/', RenewBook.as_view(), name='book_renew'),
                  ]
