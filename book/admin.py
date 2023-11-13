from django.contrib import admin
from .models import Author, Book, Review


#class BookAdmin(admin.ModelAdmin):
    #list_display=['title','author','publish_date']
    #search_fields=('title','author')
    #list_filter=('price')

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)