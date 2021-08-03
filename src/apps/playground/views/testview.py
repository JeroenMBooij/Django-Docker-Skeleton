from django.shortcuts import render
from rest_framework.views import APIView

class TestView(APIView):

    def get(self, request):
        x = 1
        y = 2
        return render(request, 'test/hello.html', {"name": "Jeroen"})