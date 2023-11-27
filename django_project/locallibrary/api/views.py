from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import BookSerializers, BookInsSerializers,RenewBookSerializer
from catalog.models import Book,BookInstance
# Create your views here.

class BookList(APIView):
  permission_classes = (IsAuthenticated, )
  pagination_class = PageNumberPagination
  def get(self,request):
    book = Book.objects.all()
    paginator = self.pagination_class()
    result_page = paginator.paginate_queryset(book, request)
    data = BookSerializers(result_page, many=True).data
    return paginator.get_paginated_response(data)  
  def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#option
class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except RestrictedError as e:
            return Response({"error": str({e})}, status=status.HTTP_400_BAD_REQUEST)

class Book_Detail(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, id):
        book = self.get_object(id)
        data = BookSerializers(book).data
        return Response(data)

    def put(self, request, id):
        book = self.get_object(id)
        serializer = BookSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        try:
            book = self.get_object(id)
            bookins = BookInstance.objects.filter(book=book)
            if bookins:
                return Response({"err": "Book có ràng buộc không thể xóa"}, status=status.HTTP_400_BAD_REQUEST)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RestrictedError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AllBorrowed(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        bookins = BookInstance.objects.all()
        data = BookInsSerializers(bookins, many=True).data
        return Response(data)


class RenewBook(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return BookInstance.objects.get(pk=pk)
        except BookInstance.DoesNotExist:
            raise Http404
    def has_permission(self, request, book_instance):
        
        return request.user.has_perm('catalog.can_mark_returned')
    def post(self, request, pk):
        book_instance = self.get_object(pk)

        
        if not self.has_permission(request, book_instance):
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        serializer = RenewBookSerializer(book_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
