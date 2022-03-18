from django.shortcuts import render
from django .http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from administrateur.models import Administrateur
from administrateur.serializers import AdministrateurSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-utilisateur',
}
    return Response(api_urls)

class AdministrateurViewSet(viewsets.ModelViewSet):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer

def list_administrateur(request):
    return HttpResponse('Bienvenue sur la liste des administrateurs')