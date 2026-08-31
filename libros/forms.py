from django.forms import ModelForm
from .models import Book
from django import forms


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "description",
            "genre",
            "author",
            "publisher",
            "publication_date",
            "pages",
            "status",
            "rating",
            "finished_date",
        ]
        widgets = {
            "title": forms.TextInput(placeholder="Titulo del libro"),
            "description": forms.Textarea(placeholder="Descripcion del libro"),
            "author": forms.TextInput(placeholder="Autor del libro"),
            "publisher": forms.TextInput(placeholder="Editorial del libro"),
            "pages": forms.NumberInput(placeholder="Numero de paginas"),
            "genre": forms.Select(placeholder="Genero del libro"),
            "status": forms.Select(placeholder="Estado del libro"),
            "publication_date": forms.DateInput(attr={"type": "date"}),
            "finished_date": forms.DateInput(attrs={"type": "date"}),
        }
