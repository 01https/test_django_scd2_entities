from rest_framework import serializers
from entities.models import Entity, EntityDetail


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = "__all__"