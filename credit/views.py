from django.shortcuts import render
from django .http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from credit.models import Credit
from credit.serializers import CreditSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-credit',
}
    return Response(api_urls)

class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
def list_credit(request):
    return HttpResponse('Bienvenue sur la liste des credits')