from rest_framework import serializers

from boite.models import Boite

class BoiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boite
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
