from django.db import models
from django.utils import timezone


class Author (models.Model):
    name=models.CharField(max_length=30)
    birth_date=models.DateField()
    biography=models.TextField(max_length=5000)

    def __str__(self):
      return self.name


class Book (models.Model):
    title=models.CharField(max_length=30)
    publish_date=models.DateTimeField(default=timezone.now)
    price=models.IntegerField()
    author=models.ForeignKey('Author',on_delete=models.CASCADE,related_name='book_author')

    def __str__(self):
      return self.title


class Review (models.Model):
    book=models.ForeignKey('Book',on_delete=models.CASCADE,related_name='review_book')
    reviewer_name=models.CharField(max_length=30)
    content=models.TextField(max_length=50000)
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(1, 5)],default=1)

    

    def __str__(self):
      return self.book
