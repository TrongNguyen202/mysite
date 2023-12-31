from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance
# admin.site.register(Book)
# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['id', 'first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ['id', 'name']
# admin.site.register(BookInstance)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display =  ('status', 'due_back','id','book')
    fieldsets = (
        ('General', {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )
