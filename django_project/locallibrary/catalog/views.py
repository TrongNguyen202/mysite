from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book, Author, BookInstance, Genre
# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    context = {'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'num_authors': num_authors,
               'num_visits':num_visits,
               }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
class BookListView(ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'my_book_list'
    queryset = Book.objects.all()
    template_name = 'book_list.html'

   
def book_detail(request, id):
  book = get_object_or_404(Book, id=id)
  template = loader.get_template('book_detail.html')
  context = {
    'book': book,
  }
  return HttpResponse(template.render(context, request))


class LoanedBooksByUserListView(ListView):
    model = BookInstance
    context_object_name = 'bookinstance_list'
    queryset = BookInstance.objects.all()
    template_name = 'bookinstance_list_borrowed_user.html'
