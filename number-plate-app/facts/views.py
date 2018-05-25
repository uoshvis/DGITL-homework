from django.db.models import Q
from rest_framework import generics, mixins

from facts.models import Fact
from facts.serializers import FactsSerializer


class FactsAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'pk'
    serializer_class = FactsSerializer

    def get_queryset(self):
        qs = Fact.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
            ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FactsRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = FactsSerializer

    def get_queryset(self):
        return Fact.objects.all()
