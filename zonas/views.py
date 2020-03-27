from rest_framework import viewsets, generics
from zonas.serializers import ZonaSerializer, MensajeSerializer
from zonas.models import Zona, Mensaje


class ZonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer


class MensajeViewSet(viewsets.ModelViewSet):
    serializer_class = MensajeSerializer

    def get_queryset(self):
        zona_id= self.request.query_params.get('zona', None)
        queryset = Mensaje.objects.all()
        if zona_id is not None:
            queryset = queryset.filter(zona=zona_id).order_by('-id')
        else:
            queryset = queryset.order_by('-id')[:10]

        return queryset


class MensajeCreateView(generics.CreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
