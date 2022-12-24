from rest_framework import serializers
from .models import Item, Adicional

class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Item
        fields = '__all__'

class AdicionalSerializer(serializers.ModelSerializer):

    class Meta:

        model = Adicional
        fields = '__all__'