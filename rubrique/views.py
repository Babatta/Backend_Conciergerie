from django.shortcuts import render
from django .http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rubrique.models import Rubrique
from rubrique.serializers import RubriqueSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-rubrique',
}
    return Response(api_urls)

class CreditViewSet(viewsets.ModelViewSet):
    queryset = Rubrique.objects.all()
    serializer_class = RubriqueSerializer

def list_rubrique(request):
    return HttpResponse('Bienvenue sur la liste des rubriques')