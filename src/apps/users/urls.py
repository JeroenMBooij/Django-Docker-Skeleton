from django.urls import path
from .views import RegisterView
from .views import UserControllerView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('test/', UserControllerView.as_view())
]