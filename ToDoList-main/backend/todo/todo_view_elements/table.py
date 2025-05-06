from django.forms import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Table, Group, Task
from ..responses import *


class TablesAPI(APIView):

    def get(self, request):
        if request.user.is_anonymous:
            return UNAUTHORIZED_401
        
        data = Table.objects.filter(user=request.user).values()
        return Response({'tables': list(data)}, 200)

    def post(self, request):
        if request.user.is_anonymous:
            return UNAUTHORIZED_401
        
        data = request.data
        Table.objects.create(
            name=data['name'],
            user=request.user
        )
        return Response(data, 200)

    def patch(self, request):
        if request.user.is_anonymous:
            return UNAUTHORIZED_401

        data = request.data
        Table.objects.filter(id=data['id']).update(name=data['name'])
        return Response(data, 200)

    def delete(self, request):
        if request.user.is_anonymous:
            return UNAUTHORIZED_401

        data = request.data
        Table.objects.filter(id=data['id']).delete()
        return Response(data, 200)


class TableAPI(APIView):

    def get(self, request, id):
        if request.user.is_anonymous:
            return UNAUTHORIZED_401
        
        table = Table.objects.get(user=request.user, id=id)
        groups = Group.objects.filter(table=table)
        tasks = Task.objects.filter(group__in=groups)

        response_data = {
            'table': model_to_dict(table),
            'groups': [model_to_dict(group) for group in groups],
            'tasks': [model_to_dict(task) for task in tasks]
        }

        return Response(response_data, 200)
