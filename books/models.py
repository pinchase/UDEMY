from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date=models.DateField()
    isbn = models.CharField(max_length=12)
    pages=models.IntegerField()
    def __str__(self):
        return self.title


