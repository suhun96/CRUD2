import json

from django.http import JsonResponse
from django.views import View
from starring.models import Movie , Actor

class MovieView(View):
   def post(self,request):
       data = json.loads(request.body)
       Movie.objects.create(
        title        = data["title"],
        release_date =  data["release_date"],
        running_time =   data["running_time"]
        )
       return JsonResponse({"massage":"created"} , status=201 )
   
   def get(self,request):
        movies = Movie.objects.all()
        movie_list = []
        for movie in movies:
            films = movie.actor.all()
            film_list = []
            for film in films:
                film_list.append({
                    "actor"     : film.first_name + film.last_name
                })
            movie_list.append({
                "title"         : movie.title,
                "running_time"  : movie.running_time,
                "actor"         : film_list
            })
                
               
            
        return JsonResponse({"RESULT":movie_list}, status=200)
    

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        actor_list = []
        for actor in actors:
            movies = actor.movie.all()
            movie_list = []
            for movie in movies:
                movie_list.append({
                    "출연한 영화" : movie.title
                })
            
            actor_list.append({
                "성"    : actor.first_name,
                "이름"  : actor.last_name,
                "출연작": movie_list,
                
            })
        
        return JsonResponse({"결과" : actor_list})