from django.db.models import Q
from rest_framework import generics, mixins

from sweets.models import SweetsData
from sweets.serializers import SweetsSerializer
from datetime import datetime


class SweetsDataAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'pk'
    serializer_class = SweetsSerializer

    def get_queryset(self):
        qs = SweetsData.objects.all()
        query_timestamp = self.request.GET.get('timestamp')
        if query_timestamp and query_timestamp.isdigit():
            timestamp = datetime.fromtimestamp(float(query_timestamp))
            qs = qs.filter(
                Q(timestamp__gte=timestamp)
            )
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class SweetsDataRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = SweetsSerializer

    def get_queryset(self):
        return SweetsData.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}
