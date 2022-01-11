from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import save_data

# Create your views here.
        
class createDatabase(APIView):

    def get(self, request):
        save_data()
        content = {'message': 'The database has been created'}
        return Response(content)

class searchByKeyword(APIView):

    def get(self, request):
        content = {'message': 'The database has been created'}
        return Response(content)