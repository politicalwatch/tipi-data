import marshmallow_mongoengine as ma

from tipi_data.models.footprint import FootprintByTopic, \
        FootprintByDeputy, \
        FootprintByParliamentaryGroup


class FootprintByTopicSchema(ma.ModelSchema):
    class Meta:
        model = FootprintByTopic


class FootprintByDeputySchema(ma.ModelSchema):
    class Meta:
        model = FootprintByDeputy


class FootprintByParliamentaryGroupSchema(ma.ModelSchema):
    class Meta:
        model = FootprintByParliamentaryGroup
