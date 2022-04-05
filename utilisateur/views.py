from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django .http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from utilisateur.models import Utilisateur
from utilisateur.serializers import UtilisateurSerializer
from rest_framework import viewsets
from rest_framework import permissions

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

@api_view(['GET', 'POST', 'DELETE','PUT'])
@csrf_exempt
def utilisateurApi(request,id=0):
    if request.method=='GET':
         utilisateurs = Utilisateur.objects.all().order_by()
         utilisateur_serializer = UtilisateurSerializer(utilisateurs,many=True)
         return JsonResponse(utilisateur_serializer.data,safe=False)
    elif request.method=='POST':
        utilisateur_data=JSONParser().parse(request)
        utilisateur_serializer = UtilisateurSerializer(data=utilisateur_data)
        if utilisateur_serializer.is_valid():
            utilisateur_serializer.save()
            return JsonResponse("Ajouter avec succé",safe=False)
        return JsonResponse("Erreur d'ajout ",safe=False)
    elif request.method== 'PUT':
        utilisateur_data = JSONParser().parse(request)
        utilisateur = Utilisateur.objects.get(UtilisateurId=utilisateur_data['UtilisateurId'])
        utilisateur_serializer = UtilisateurSerializer(utilisateur,data=utilisateur_data)
        if utilisateur_serializer.is_valid():
            utilisateur_serializer.save()
            return JsonResponse("Mise a jour avec succée",safe=False)
        return JsonResponse("Erreur de mise a jour ",safe=False)
    elif request.method== 'DELETE':
        utilisateur = Utilisateur.objects.get(UtilisateurId=id)
        utilisateur.delete()
        return JsonResponse("Supprimer avec succé",safe=False)


