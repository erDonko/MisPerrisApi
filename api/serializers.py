from rest_framework import serializers
from App import models

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'desc',
        )
        model = models.Est