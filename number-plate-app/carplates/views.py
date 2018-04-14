from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from carplates.models import CarPlate
from carplates.serializers import CarPlateSerializer


class CarPlatesViewSet(viewsets.ViewSet):

    def list(self, request):
        """
        Get all existing car plates
        """
        queryset = CarPlate.objects.all()
        serializer = CarPlateSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)

    def retrieve(self, request, pk=None):
        """
        Get single car plate data by id
        """
        obj = get_object_or_404(CarPlate, pk=pk)
        serializer = CarPlateSerializer(obj)
        return Response(serializer.data)

    def create(self, request):
        serializer = CarPlateSerializer(data=request.data)
        if serializer.is_valid():
            queryset = CarPlate.objects.create(**serializer.validated_data)
            data = CarPlateSerializer(queryset).data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {'errors': serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Update car plate data. Plate_number is non updatable.
        """
        non_update = ['plate_number']
        update_field = ['first_name', 'last_name']

        obj = get_object_or_404(CarPlate, pk=pk)
        for key in request.data:
            if key in non_update:
                data = {'error': 'Trying update non updatable'}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        for key in update_field:
            data = request.data.get(key)
            setattr(obj, key, data)
            obj.save()
            data = CarPlateSerializer(obj).data
        return Response(data)

    def destroy(self, request, pk=None):
        """
        Delete car plate data
        """
        obj = get_object_or_404(CarPlate, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
