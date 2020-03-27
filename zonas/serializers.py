from rest_framework_gis.serializers import GeoModelSerializer, GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer
from zonas.models import Zona, Mensaje


class MensajeSerializer(ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['zona', 'texto', 'updated' , 'autor', 'titulo']

class ZonaSerializer(GeoModelSerializer):

    class Meta:
        model = Zona
        geo_field = "mpoly"
        fields = ['id', 'mpoly']
