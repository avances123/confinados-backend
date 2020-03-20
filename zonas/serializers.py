from rest_framework_gis.serializers import GeoModelSerializer, GeoFeatureModelSerializer
from zonas.models import Zona


#class ZonaSerializer(GeoFeatureModelSerializer): # para el geojson
class ZonaSerializer(GeoModelSerializer):
    class Meta:
        model = Zona
        geo_field = "mpoly"
        fields = ['id', 'mpoly']
