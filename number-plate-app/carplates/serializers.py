import string
from rest_framework import serializers
from carplates.models import CarPlate


class CarPlateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:carplates-detail')

    class Meta:
        model = CarPlate
        fields = '__all__'

    def validate_plate_number(self, data):
        # generate LT letters
        uppercases = string.ascii_uppercase
        for r_letter in 'QWX':
            uppercases_lt = uppercases.replace(r_letter, '')
            uppercases = uppercases_lt

        # validate plate number length
        if len(data) != 6:
            raise serializers.ValidationError('Not enough/too much characters')
        else:
            # validate LT letters
            for letter in data[:3].upper():
                if letter not in uppercases_lt:
                    raise serializers.ValidationError('Foreign letter')
            # validate numbers
            if not data[3:].isdigit():
                raise serializers.ValidationError('Invalid number')
        return data.upper()
