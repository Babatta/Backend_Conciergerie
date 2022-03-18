from django.shortcuts import render
from django .http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from paiement.models import Paiement
from paiement.serializers import PaiementSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-credit',
}
    return Response(api_urls)

class PaiementViewSet(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer
def list_paiement(request):
    return HttpResponse('Bienvenue sur la liste des paiement')