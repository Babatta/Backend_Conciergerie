from django.shortcuts import render
from abonne.models import Abonne
from abonne.serializers import AbonneSerializer
from django .http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

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

@api_view(['GET', 'POST', 'DELETE','PUT'])
@csrf_exempt
def abonneApi(request,id=0):
    if request.method=='GET':
         abonnes = Abonne.objects.all().order_by()
         abonne_serializer = AbonneSerializer(abonnes,many=True)
         return JsonResponse(abonne_serializer.data,safe=False)
    elif request.method=='POST':
        abonne_data=JSONParser().parse(request)
        abonne_serializer = AbonneSerializer(data=abonne_data)
        if abonne_serializer.is_valid():
            abonne_serializer.save()
            return JsonResponse("Ajouter avec succé",safe=False)
        return JsonResponse("Erreur d'ajout ",safe=False)
    elif request.method== 'PUT':
        abonne_data = JSONParser().parse(request)
        abonne = Abonne.objects.get(AbonneId=abonne_data['AbonneId'])
        abonne_serializer = AbonneSerializer(abonne,data=abonne_data)
        if abonne_serializer.is_valid():
            abonne_serializer.save()
            return JsonResponse("Mise a jour avec succée",safe=False)
        return JsonResponse("Erreur de mise a jour ",safe=False)
    elif request.method== 'DELETE':
        abonne = Abonne.objects.get(abonne=id)
        abonne.delete()
        return JsonResponse("Supprimer avec succé",safe=False)