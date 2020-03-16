from rest_framework import viewsets
from zonas.serializers import ZonaSerializer
from zonas.models import Zona


class ZonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer

