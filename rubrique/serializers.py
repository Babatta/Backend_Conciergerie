from rest_framework import serializers

from rubrique.models import Rubrique

class RubriqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rubrique
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
