from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return (self.title + " by " + self.author)


#This is to deal with the new database
class PublicBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        app_label = 'public_library'