from rest_framework import serializers

from credit.models import Credit

class CreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credit
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
