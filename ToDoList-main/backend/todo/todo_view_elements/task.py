from ..models import Task
from ..responses import *

from rest_framework.views import APIView
from rest_framework.response import Response


class TaskAPI(APIView):

    def post(self, request):
        if request.user.is_anonymous:
            return UNAUTHORIZED_401

        data = request.data
        Task.objects.create(
            name=data['name'],
            group_id=data['group_id'],
            description=data['description'],
            color=data['color']
        )
        return Response(data)

    def patch(self, request):
        if request.user.is_anonymous:
            return UNAUTHORIZED_401

        data = request.data
        Task.objects.filter(id=data['id']).update(
            name=data['name'],
            color=data['color'],
            description=data['description'],
            group=data['group']
        )
        return Response(data)

    def delete(self, request):
        if request.user.is_anonymous:
            return UNAUTHORIZED_401
        
        data = request.data
        Task.objects.delete(id=data['id'])
        return Response(data)
