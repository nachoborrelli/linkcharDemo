from django.shortcuts import render
from django.http import HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse

from .tasks import save_data
import json
from .models import Entry

# Create your views here.
        
class createDatabase(APIView):

    def post(self, request):
        message = save_data()
        content = {'message': message}
        return Response(content)

    def get(self, request):
        return HttpResponseNotFound("You must use POST in order to trigger this function")

class searchByKeyword(APIView):
    def post(self, request):
        letter = request.data['keyword']
        entries = Entry.objects.filter(api__startswith=letter).values()
        return JsonResponse({"data": list(entries)})

    def get(self, request):
        return HttpResponseNotFound("You must use POST in order to get the data")