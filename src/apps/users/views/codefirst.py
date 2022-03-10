from django.http.response import HttpResponse
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django.http import HttpResponse
from src.apps.users.models import User
from django.http import JsonResponse
import json
from src.apps.users.models.person import Person

from src.apps.users.serializers import UserSerializer

class UserControllerView(APIView):

    @extend_schema(
        # extra parameters added to the schema
        parameters=[
            OpenApiParameter(name='artist', description='Filter by artist', required=False, type=str),
            OpenApiParameter(
                name='release',
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description='Filter by release date',
                examples=[
                    OpenApiExample(
                        'Example 1',
                        summary='short optional summary',
                        description='longer description',
                        value='1993-08-23'
                    )
                ],
            ),
        ],
        # override default docstring extraction
        description='More descriptive text',
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                'Example 1',
                description='longer description',
                value="test"
            ),
        ],
    )
    def get(self, request):
        artist = request.query_params.get('artist')
        release = request.query_params.get('release')

        person = Person(artist)

        return JsonResponse(person.__dict__)

    @extend_schema(
        request=UserSerializer,
        responses={201: {}},
    )
    def post(self, request):
        user =  json.loads(request.body)
        username = user["name"]
        email = user["email"]
        return HttpResponse(status=201)