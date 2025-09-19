from rest_framework import viewsets

from entities.models import Entity, EntityDetail
from entities.serializers import EntitySerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
