from django.forms import model_to_dict
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response


class UserCreate(APIView):

    def post(self, request):
        data = request.data

        new_user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        return Response({'post': model_to_dict(new_user)})
