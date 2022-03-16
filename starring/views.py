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
        movie_list = [{
            "title"         : movie.title,
            "running_time"  : movie.running_time,
            "actor"         : 
                [actor.first_name + actor.last_name
             for actor in movie.actors_movie.all()]
            } for movie in Movie.objects.all()]
        return JsonResponse({"RESULT":movie_list}, status=200)
    

class ActorView(View):
    def get(self, request):
        
        # actors = Actor.objects.all()
        actor_list = [{
            '이름'      : actor.first_name + actor.last_name,
            '출연작'    : [movie.title for movie in actor.movies.all()]
            } for actor in Actor.objects.all()]
        
        # for actor in actors:
        #     movies = actor.movie.all()
        #     movie_list = []
        #     for movie in movies:
        #         movie_list.append({
        #             "출연한 영화" : movie.title
        #         })
            
        #     actor_list.append({
        #         "성"    : actor.first_name,
        #         "이름"  : actor.last_name,
        #         "출연작": movie_list,
                
        #     })
        
        return JsonResponse({"결과" : actor_list})