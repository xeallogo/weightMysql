from rest_framework import serializers 
from weights.models import Weight
 

 # In the inner class Meta, we declare 2 attributes: model: the model for Serializer and fields: a tuple of field names to be included in the serialization
 
class WeightSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Weight
        fields = ('id',
                  'date',
                  'weight')