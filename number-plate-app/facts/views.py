from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status
from facts.models import Fact
from facts.serializers import FactsSerializer


class CreateModelMixinMany(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            many=isinstance(request.data, list)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class FactsAPIView(CreateModelMixinMany, generics.ListAPIView):

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
