from rest_framework import serializers

from service.models import Service

class Serviceserializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
