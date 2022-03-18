from rest_framework import serializers

from abonne.models import Abonne

class AbonneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abonne
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
