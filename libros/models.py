from django.db import models
from accounts.models import User
# Create your models here.


class Book(models.Model):
    STATUS_CHOICES = [
        ("WANT_TO_READ", "Por leer"),
        ("READING", "Leyendo"),
        ("COMPLETED", "Completado"),
    ]
    GENRE_CHOICES = [
        ("FANTASY", "Fantasía"),
        ("SCI_FI", "Ciencia ficción"),
        ("MYSTERY", "Misterio"),
        ("HORROR", "Terror"),
        ("ROMANCE", "Romance"),
        ("HISTORY", "Historia"),
        ("BIOGRAPHY", "Biografía"),
        ("SELF_HELP", "Autoayuda"),
        ("TECHNOLOGY", "Tecnología"),
        ("OTHER", "Otro"),
    ]

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=100, null=False, blank=False)
    genre = models.CharField(
        max_length=20, choices=GENRE_CHOICES, null=False, blank=False
    )
    author = models.CharField(max_length=50, null=False, blank=False)
    publisher = models.CharField(max_length=50, null=False, blank=False)
    publication_date = models.DateField(null=False, blank=False)
    pages = models.PositiveIntegerField(null=False, blank=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        null=False,
        blank=False,
        default="WANT_TO_READ",
    )
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    finished_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author", "user"], name="unique_book_per_user"
            )
        ]
