from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from sweets.models import SweetsData


class SweetsSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SweetsData
        fields = [
            'url',
            'name',
            'weight_grams',
            'kcal',
            'timestamp',
        ]
        read_only_fields = ['id', 'url']
        validators = [
            UniqueTogetherValidator(
                queryset=SweetsData.objects.all(),
                fields=('name', 'weight_grams')
            )
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)
