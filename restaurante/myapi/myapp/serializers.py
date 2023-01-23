from rest_framework import serializers
from .models import Item, Adicional, Mesa

class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Item
        fields = '__all__'

class AdicionalSerializer(serializers.ModelSerializer):

    class Meta:

        model = Adicional
        fields = '__all__'

class MesaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Mesa
        fields = '__all__'