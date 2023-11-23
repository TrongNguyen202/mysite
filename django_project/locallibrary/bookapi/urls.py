from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [ path("books/", views.BookList.as_view(), name="books_list"),
                 path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), ]
