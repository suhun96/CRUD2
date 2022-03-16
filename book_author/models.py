from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=45)
    age  = models.IntegerField()
    
    class Meta:
        db_table = "authors"
        
class Book(models.Model):
    title            = models.CharField(max_length=45)
    publication_date = models.DateField(auto_now=False,auto_now_add=False)
    
    class Meta:
        db_table = "books"
    
class AuthorBook(models.Model):
    authors = models.ForeignKey("Author", on_delete=models.CASCADE)
    books   = models.ForeignKey("Book", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "authorsbooks"