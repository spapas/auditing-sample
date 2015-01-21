from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, TemplateView

from auditable.views import AuditableMixin

from models import Book, SHBook, RBook
from forms import BookForm


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class BookCreateView(AuditableMixin, CreateView):
    model = Book
    form_class = BookForm


class SHBookCreateView(CreateView):
    model = SHBook


class RBookCreateView(CreateView):
    model = RBook


class BookUpdateView(AuditableMixin, UpdateView):
    model = Book
    form_class = BookForm


class SHBookUpdateView(UpdateView):
    model = SHBook


class RBookUpdateView(UpdateView):
    model = RBook


class BookListView(ListView):
    model = Book


class SHBookListView(ListView):
    model = SHBook


class RBookListView(ListView):
    model = RBook
