from django.shortcuts import render
from django .http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from service.models import Service
from service.serializers import Serviceserializer
from rest_framework.generics import ListAPIView
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-service',
}
    return Response(api_urls)

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = Serviceserializer
def list_service(request):
    return HttpResponse('Bienvenue sur la liste des services')