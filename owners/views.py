import json
from unittest import result

from django.http import JsonResponse
from django.views import View
from owners.models import Owner, Dog


class OwnersView(View):
    def post(self, request):
        data=   json.loads(request.body)
        Owner.objects.create(            
                name = data['name'], 
                email = data['email'],
                age =   data['age']
        )
        return JsonResponse({'massasge' : 'created'}, status=201)  
    
    def get(self, request):
        result = [{
            'name'     : owner.name,
            'age'      : owner.age,
            'email'    : owner.email,
            # 'pet_list' : [{
            #     'name' : dog.name,
            #     'age' : dog.age
            #     } for dog in owner.dog_set.all()]
        } for owner in Owner.objects.all()]
             
        return JsonResponse({'result':result}, status=200) 
    

class DogsView(View):
    def post(self, request):
        data=  json.loads(request.body)
        owners= Owner.objects.get(name=data['owner'])
        Dog.objects.create(
            name=   data['name'],
            age=    data['age'],
            owner_id= owners.id
        )
        return JsonResponse({'massage':'created'}, status=201)
    
    def get(self, request):
        dogs = Dog.objects.all()
        result = []
        for dog in dogs:
            result.append(
            {
                "owner": dog.owner.name, 
                "name": dog.name,
                "age": dog.age,
            })
        
        return JsonResponse({'massage': result }, status=201)
    
    
    