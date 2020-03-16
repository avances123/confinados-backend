from rest_framework_gis.serializers import GeoModelSerializer
from zonas.models import Zona


class ZonaSerializer(GeoModelSerializer):
    class Meta:
        model = Zona
        geo_field = "mpoly"
        fields = ['id', 'mpoly']
