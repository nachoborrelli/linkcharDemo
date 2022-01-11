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


class searchByAPIKeyword(APIView):
    def post(self, request):
        try:
            letter = request.data['keyword']
            entries = Entry.objects.filter(api__startswith=letter).values()
            return JsonResponse({"data": list(entries)})
        except:
           return JsonResponse({"error": "something went wrong"})

    def get(self, request):
        return HttpResponseNotFound("You must use POST in order to get the data")


class searchByCategory(APIView):
    def post(self, request):
        try:
            category = request.data['category']
            entries = Entry.objects.filter(category=category).values()
            return JsonResponse({"data": list(entries)})
        except:
           return JsonResponse({"error": "something went wrong"}) 

    def get(self, request):
        return HttpResponseNotFound("You must use POST in order to get the data")


class getOrderedEntries(APIView):
    def post(self, request):
        try:
            entries = Entry.objects.order_by('id').values()
            return JsonResponse({"data": list(entries)})
        except:
           return JsonResponse({"error": "something went wrong"}) 

    def get(self, request):
        return HttpResponseNotFound("You must use POST in order to get the data")


class getByID(APIView):
    def post(self, request):
        try:
            pk = request.data['pk']
            entry = Entry.objects.get(id=pk)
            jsonEntry = serializers.serialize('python', [ entry, ])
            return JsonResponse({"data": jsonEntry})
            
        except:
           return JsonResponse({"error": "something went wrong"}) 


    def get(self, request):
        return HttpResponseNotFound("You must use POST in order to get the data")
