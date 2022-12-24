from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Item, Adicional
from .serializers import ItemSerializer, AdicionalSerializer

class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [SearchFilter]
    search_fields = ['titulo']

class AdicionalViewSet(viewsets.ModelViewSet):

    queryset = Adicional.objects.all()
    serializer_class = AdicionalSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']
