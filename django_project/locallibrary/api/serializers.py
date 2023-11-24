
from rest_framework import serializers
from catalog.models import Book
class BookSerializers(serializers.ModelSerializer):

  class Meta:
        model = Book
        fields = ('title', 'author', 'summary','isbn','genre')
