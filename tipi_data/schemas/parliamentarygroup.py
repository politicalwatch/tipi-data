import marshmallow_mongoengine as ma

from tipi_data.models.parliamentarygroup import ParliamentaryGroup
from tipi_data.models.footprint import FootprintByParliamentaryGroup
from tipi_data.schemas.footprint import FootprintByParliamentaryGroupSchema


class FootprintField(ma.fields.Field):
    def _serialize(self, id, attr, obj):
        try:
            fbpg_serialized = FootprintByParliamentaryGroupSchema().dump(
                    FootprintByParliamentaryGroup.objects.get(id=id)
                    )
            return fbpg_serialized.data['score']
        except Exception:
            return 0.0


class FootprintTopicsField(ma.fields.Field):
    def _serialize(self, id, attr, obj):
        try:
            fbd_serialized = FootprintByParliamentaryGroupSchema().dump(
                    FootprintByParliamentaryGroup.objects.get(id=id)
                    )
            return fbd_serialized.data['topics']
        except Exception:
            return list()


class ParliamentaryGroupSchema(ma.ModelSchema):
    class Meta:
        model = ParliamentaryGroup

    footprint = FootprintField(attribute='id')
    footprint_by_topics = FootprintTopicsField(attribute='id')
