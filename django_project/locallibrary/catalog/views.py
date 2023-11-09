from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views.generic import ListView
from django.template.response import TemplateResponse
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import RenewBookForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    context_object_name = 'my_book_list'
    queryset = Book.objects.all()
    template_name = 'book_list.html'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context



def BookDetailView(request, id):
  book = Book.objects.get(id=id)
  template = loader.get_template('book_detail.html')
  context = {
    'book': book,
  }
  return HttpResponse(template.render(context, request))
# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = '/'


class LoanedBooksByUserListView(ListView):
    model = BookInstance
    context_object_name = 'bookinstance_list'
    queryset = BookInstance.objects.all()
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    def get_context_data(self, **kwargs):
        context = super(LoanedBooksByUserListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            return HttpResponseRedirect(reverse('my-borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {'form': form, 'book_instance': book_instance}
    return render(request, 'catalog/book_renew_librarian.html', context)

class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__' # Not recommended (potential security issue if more fields added)
class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
