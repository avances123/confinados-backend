from django.contrib.gis import admin
from zonas.models import Zona, Mensaje

#admin.site.register(Zona, admin.GeoModelAdmin)
admin.site.register(Zona, admin.OSMGeoAdmin)
