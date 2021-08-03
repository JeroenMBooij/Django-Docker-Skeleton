from django.http.response import HttpResponse
from rest_framework.views import APIView
from django.http import HttpResponse

class RegisterView(APIView):

    def post(self, request):
        return HttpResponse("fuck off")