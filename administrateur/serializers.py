from rest_framework import serializers

from administrateur.models import Administrateur

class AdministrateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Administrateur
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
