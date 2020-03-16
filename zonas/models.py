from django.contrib.gis.db import models
import uuid

class Zona(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()
