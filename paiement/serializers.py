from rest_framework import serializers

from paiement.models import Paiement

class PaiementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paiement
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
