from django.shortcuts import render
from django .http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utilisateur.models import Utilisateur
from utilisateur.serializers import UtilisateurSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-utilisateur',
}
    return Response(api_urls)

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all().order_by()
    serializer_class = UtilisateurSerializer

def home(request):
     return HttpResponse('Bienvenue sur la page d accueil')