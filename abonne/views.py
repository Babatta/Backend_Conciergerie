from django.shortcuts import render
from abonne.models import Abonne
from abonne.serializers import AbonneSerializer
from django .http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-abonne',
}
    return Response(api_urls)

class AbonneViewSet(viewsets.ModelViewSet):
    queryset = Abonne.objects.all()
    serializer_class = AbonneSerializer

def list_abonne(request):
    return HttpResponse('Bienvenue sur la liste des abonnes')