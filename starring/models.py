from django.db import models

class Actor(models.Model):
    first_name      = models.CharField(max_length=45)
    last_name       = models.CharField(max_length=45)
    date_of_birth   = models.DateField(auto_now=False,auto_now_add=False)
    movie           = models.ManyToManyField("Movie", through="MovieActor", related_name="actors_movie")
    class Meta:
        db_table = "actors"
        
class Movie(models.Model):
    title        = models.CharField(max_length=45)
    release_date = models.DateField(auto_now=False,auto_now_add=False)
    running_time = models.IntegerField()
    
    class Meta:
        db_table = "movies"

class MovieActor(models.Model):
    actor = models.ForeignKey("Actor", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "actors_movie"
    