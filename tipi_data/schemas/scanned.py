import marshmallow_mongoengine as ma
from tipi_data.models.scanned import Scanned


class ScannedSchema(ma.ModelSchema):
    class Meta:
        model = Scanned
        model_skip_values = [None]
