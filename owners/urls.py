from django.urls import path
from .views import OwnersView
from .views import DogsView
urlpatterns = [
    path('owner',OwnersView.as_view()),
    path('dog',DogsView.as_view())
]