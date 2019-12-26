import marshmallow_mongoengine as ma

from tipi_data.models.place import Place


class PlaceSchema(ma.ModelSchema):
    class Meta:
        model = Place
