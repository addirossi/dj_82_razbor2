from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from main.filters import CarFilter
from main.models import Car, Sale
from main.serializers import CarSerializer, SaleSerializer


@api_view(['GET'])
def cars_list(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    data = serializer.data
    print(data)
    return Response(data)


class CreateCarView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarsListView(ListAPIView):
    queryset = Car.objects.prefetch_related('sales')
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    # filterset_fields = ['color']


from rest_framework.viewsets import ModelViewSet


class SaleDetails(RetrieveAPIView):
    queryset = Sale.objects.select_related('car')
    serializer_class = SaleSerializer
