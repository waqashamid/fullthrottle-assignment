from rest_framework import serializers
from . import models

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'body', 'created', 'modified', 'frequency', )
        model = models.Word