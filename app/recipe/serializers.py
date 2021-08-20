# from django.db import models
# from django.db.models import fields
from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializers for Tag objects"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only = ('id',)
