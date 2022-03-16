import json

from django.http import JsonResponse
from django.views import View
from book_author.models import *

class AuthorView(View):
    def get(self,request):
        authors = Author.objects.all()
        author_list = []
        for human in authors:
            authorsbooks = human.authorbook_set.all()
            book_list = []
            for book in authorsbooks:
                book_list.append({
                    "책이름" : book.books.title
                })
                     
            author_list.append({
                "저자" : human.name,
                "나이" : human.age,
                "책"   : book_list
            })
        return JsonResponse({"결과" : author_list } , status= 201)