from django .http import HttpResponse
from rest_framework.response import Response
from localisation.models import Localisation
from localisation.serializers import LocalisationSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import viewsets


@api_view(['GET'])
def apiOverview(request):
        api_urls = {
            'List': 'list-localisation',
        }
        return Response(api_urls)

class LocalisationViewSet(viewsets.ModelViewSet):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer


def localisation(request):
    return HttpResponse('Bienvenue sur la page des localisations')