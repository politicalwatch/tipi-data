import marshmallow_mongoengine as ma

from tipi_data.models.parliamentarygroup import ParliamentaryGroup


class ParliamentaryGroupSchema(ma.ModelSchema):
    class Meta:
        model = ParliamentaryGroup
