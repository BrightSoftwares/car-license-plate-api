from rest_framework import viewsets

from .models import Plate, Owner
from .serializers import PlateSerializer, OwnerSerializer


class OwnerView(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class PlateView(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
