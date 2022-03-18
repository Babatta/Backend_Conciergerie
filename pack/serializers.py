from rest_framework import serializers

from pack.models import Pack

class PackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pack
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
