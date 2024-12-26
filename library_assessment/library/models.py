from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.CharField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    ratings_count = models.IntegerField(default=0)
    average_rating = models.IntegerField(default=0)
    text_reviews_count = models.IntegerField(default=0)
    works_count = models.IntegerField(default=0)
    fans_count = models.IntegerField(default=0)
    work_ids = models.ManyToManyField('Book', related_name='author_work_ids', blank=True)
    book_ids = models.ManyToManyField('Book', related_name='author_book_ids', blank=True)

    def __str__(self):
        return self.name
    
class Shelf(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.id

class Book(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')
    author_name = models.CharField(max_length=255)
    author_id = models.CharField(max_length=255)
    work_id = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)
    asin = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    average_rating = models.FloatField(default=0)
    rating_dist = models.TextField(blank=True, null=True)
    ratings_count = models.IntegerField(default=0)
    text_reviews_count = models.IntegerField(default=0)
    publication_date = models.CharField(max_length=50, blank=True, null=True)
    original_publication_date = models.CharField(max_length=50, blank=True, null=True)
    format = models.CharField(max_length=50, blank=True, null=True)
    edition_information = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    num_pages = models.IntegerField(default=0)
    series_id = models.CharField(max_length=255, blank=True, null=True)
    series_name = models.CharField(max_length=255, blank=True, null=True)
    series_position = models.CharField(max_length=50, blank=True, null=True)
    shelves = models.ManyToManyField(Shelf, related_name='books', blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


