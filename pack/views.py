from django.shortcuts import render
from django .http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from pack.models import Pack
from pack.serializers import PackSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-pack',
}
    return Response(api_urls)

class PackViewSet(viewsets.ModelViewSet):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer
def list_pack(request):
    return HttpResponse('Bienvenue sur la liste des packs')