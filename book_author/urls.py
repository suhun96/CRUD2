from django.urls import path
# from .views import 
from .views import AuthorView
urlpatterns = [
    path('author',AuthorView.as_view())
]