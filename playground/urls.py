from django.urls import path
from .views import TestView

urlpatterns = [
    path('hello/', TestView.as_view())
]
