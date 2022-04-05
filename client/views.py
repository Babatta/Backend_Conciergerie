from django.shortcuts import render
from rest_framework import viewsets
from client.models import Client
from client.serializers import ClientSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-client',
}
    return Response(api_urls)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

def list_client(request):
    return HttpResponse('Bienvenue sur la liste des clients')

@csrf_exempt
def clientApi(request,id=0):
    if request.method=='GET':
         clients = Client.objects.all().order_by()
         client_serializer = ClientSerializer(clients,many=True)
         return JsonResponse(client_serializer.data,safe=False)
    elif request.method=='POST':
        client_data=JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)
        if clientserializer.is_valid():
            client_serializer.save()
            return JsonResponse("Ajouter avec succé",safe=False)
        return JsonResponse("Erreur d'ajout ",safe=False)
    elif request.method== 'PUT':
        client_data = JSONParser().parse(request)
        client= Abonne.objects.get(ClientId=client_data['ClientId'])
        client_serializer = AbonneSerializer(client,data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Mise a jour avec succée",safe=False)
        return JsonResponse("Erreur de mise a jour ",safe=False)
    elif request.method== 'DELETE':
        client = Client.objects.get(client=id)
        client.delete()
        return JsonResponse("Supprimer avec succé",safe=False)