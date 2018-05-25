from rest_framework import serializers

from facts.models import Fact


class FactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fact
        fields = [
            'id',
            'fact',
            'timestamp',
        ]
        read_only = ['id']
