from django.shortcuts import render
from django.http import HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import save_data

# Create your views here.
        
class createDatabase(APIView):

    def post(self, request):
        save_data()
        content = {'message': 'The database has been created'}
        return Response(content)

    def get(self, request):
        return HttpResponseNotFound("You must use POST in order to trigger this function")

class searchByKeyword(APIView):

    def get(self, request):
        return HttpResponseNotFound("You must use POST in order to get the data")