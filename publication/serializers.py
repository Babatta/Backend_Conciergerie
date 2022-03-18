from rest_framework import serializers

from publication.models import Publication

class PulicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
