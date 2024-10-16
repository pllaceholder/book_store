from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView

from book_shelf.models import Book


# class BooksListTemplateView(TemplateView):
#     template_name = 'book_shelf/books_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = Book.objects.all()
#         return context


class BooksList(ListView):
    template_name = 'book_shelf/books_list.html'
    model = Book
    context_object_name = 'books'


class BooksDetail(DetailView):
    template_name = 'book_shelf/book_detail.html'
    model = Book
    context_object_name = 'book'


class BooksUpdate(UpdateView):
    model = Book
    template_name = 'book_shelf/book_form.html'
    fields = ['title', 'author', 'description']

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.object.pk})


class BooksDelete(DeleteView):
    model = Book
    template_name = 'book_shelf/book_confirm_delete.html'
    success_url = reverse_lazy('books_list')
