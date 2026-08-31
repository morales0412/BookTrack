from django.shortcuts import render
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .forms import BookForm
# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "libros/listar_libros.html"
    form_class = BookForm

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        busqueda = self.request.GET.get("busqueda")
        status = self.request.GET.get("opcion_lectura")
        if busqueda:
            queryset = queryset.filter(title__icontains=busqueda)
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "libros/detalle_libro.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "libros/crear_libro.html"
    form_class = BookForm
    success_url = reverse_lazy("listar_libros")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
