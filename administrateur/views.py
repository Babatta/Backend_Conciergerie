from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
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

@csrf_exempt
def administrateurApi(request,id=0):
    if request.method=='GET':
         administrateurs = Administrateur.objects.all().order_by()
         administrateur_serializer = AdministrateurSerializer(administrateurs,many=True)
         return JsonResponse(administrateur_serializer.data,safe=False)
    elif request.method=='POST':
        administrateur_data=JSONParser().parse(request)
        administrateur_serializer = AdministrateurSerializer(data=administrateur_data)
        if  administrateur_serializer.is_valid():
            administrateur_serializer.save()
            return JsonResponse("Ajouter avec succé",safe=False)
        return JsonResponse("Erreur d'ajout ",safe=False)
    elif request.method== 'PUT':
        administrateur_data = JSONParser().parse(request)
        administrateur = Administrateur.objects.get(AdministrateurId=administrateur_data['AdministrateurId'])
        administrateur_serializer = AdministrateurSerializer(administrateur,data=administrateur_data)
        if administrateur_serializer.is_valid():
            administrateur_serializer.save()
            return JsonResponse("Mise a jour avec succée",safe=False)
        return JsonResponse("Erreur de mise a jour ",safe=False)
    elif request.method== 'DELETE':
        administrateur = Administrateur.objects.get(abonne=id)
        administrateur.delete()
        return JsonResponse("Supprimer avec succé",safe=False)