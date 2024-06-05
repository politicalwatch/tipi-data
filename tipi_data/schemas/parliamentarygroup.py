import marshmallow_mongoengine as ma

from tipi_data.models.parliamentarygroup import ParliamentaryGroup
from tipi_data.models.footprint import FootprintByParliamentaryGroup
from tipi_data.schemas.footprint import FootprintByParliamentaryGroupSchema


class ParliamentaryGroupSchema(ma.ModelSchema):
    class Meta:
        model = ParliamentaryGroup

    footprint = ma.fields.Method("get_footprint")
    footprint_by_topics = ma.fields.Method("get_footprint_by_topics")

    def get_footprint(self, obj):
        try:
            fbd = FootprintByParliamentaryGroup.objects.get(id=obj.id)
            fbd_serialized = FootprintByParliamentaryGroupSchema().dump(fbd)
            return fbd_serialized["score"]
        except Exception:
            return 0.0

    def get_footprint_by_topics(self, obj):
        try:
            fbd = FootprintByParliamentaryGroup.objects.get(id=obj.id)
            fbd_serialized = FootprintByParliamentaryGroupSchema().dump(fbd)
            return fbd_serialized["topics"]
        except Exception:
            return list()


class ParliamentaryGroupCompactSchema(ma.ModelSchema):
    class Meta:
        model = ParliamentaryGroup
