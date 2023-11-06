<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views.generic import ListView
from django.template.response import TemplateResponse


from django.views import generic
=======
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
>>>>>>> b2b31f4 (Creating ourhome page)
# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    context = {'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'num_authors': num_authors, }
    # Render the HTML template index.html with the data in the context variable
<<<<<<< HEAD
    return render(request, 'index.html', context=context)


class BookListView(ListView):
    model = Book
    context_object_name = 'my_book_list'
    queryset = Book.objects.all()
    template_name = 'book_list.html'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context



# def BookDetailView(request):
#     book = get_object_or_404(Book, pk=request.kwargs['pk'])
#
#     return render(request, 'book_detail.html', context={'book': book})


# class BookDetailView(generic.DetailView):
#     model = Book
#
#     def book_detail_view(request, primary_key):
#         book = get_object_or_404(Book, pk=primary_key)
#         template = loader.get_template('book_detail.html')
#         return render(request, template, context={'book': book})

# def BookDetailView(request,primary_key):
#     book = Book.objects.get(id=id)
#     context = {
#         'book':book
#     }
#
#     return render(request, 'book_detail.html', context=context)

def BookDetailView(request, id):
  book = Book.objects.get(id=id)
  template = loader.get_template('book_detail.html')
  context = {
    'book': book,
  }
  return HttpResponse(template.render(context, request))
=======
    return render(request, 'index.html', context=context)
>>>>>>> b2b31f4 (Creating ourhome page)
