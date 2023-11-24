from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializers
from catalog.models import Book
# Create your views here.

class BookList(APIView):
  permission_classes = (IsAuthenticated, )
  def get(self,request):
    book = Book.objects.all()
    data = BookSerializers(book, many=True).data
    return Response(data)  
