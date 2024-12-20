import re

import marshmallow_mongoengine as ma

from tipi_data.models.deputy import Deputy
from tipi_data.models.footprint import FootprintByDeputy
from tipi_data.schemas.footprint import FootprintByDeputySchema


class DeputySchema(ma.ModelSchema):
    class Meta:
        model = Deputy
        model_skip_values = [None]
        model_fields_kwargs = {
            "email": {"load_only": True},
            "web": {"load_only": True},
            "twitter": {"load_only": True},
            "facebook": {"load_only": True},
            "public_position": {"load_only": True},
            "legislatures": {"load_only": True},
            "party_logo": {"load_only": True},
            "bio": {"load_only": True},
            "start_date": {"load_only": True},
            "end_date": {"load_only": True},
            "url": {"load_only": True},
            "extra": {"load_only": True},
        }

    footprint = ma.fields.Method("get_footprint")
    footprint_by_topics = ma.fields.Method("get_footprint_by_topics")

    def get_footprint(self, obj):
        try:
            fbd = FootprintByDeputy.objects.get(id=obj.id)
            fbd_serialized = FootprintByDeputySchema().dump(fbd)
            return fbd_serialized["score"]
        except Exception:
            return 0.0

    def get_footprint_by_topics(self, obj):
        try:
            fbd = FootprintByDeputy.objects.get(id=obj.id)
            fbd_serialized = FootprintByDeputySchema().dump(fbd)
            return fbd_serialized["topics"]
        except Exception:
            return list()


def transform_dates(text):
    REGEX = re.compile(
        "[A-Z][a-z]{1,2}\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dev)\s(\d{2})\s00:00:00\sCES?T\s(\d{4})"
    )
    MONTHS = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    results = REGEX.finditer(text)
    for result in results:
        full_date = result.group(0)
        month = result.group(1)
        day = result.group(2)
        year = result.group(3)
        new_date = day + "/" + MONTHS[month] + "/" + year
        text = text.replace(full_date, new_date)
    return text


class PublicPositionsField(ma.fields.Field):
    def _serialize(self, positions, attr, obj):
        clean_positions = []
        for position in positions:
            clean_positions.append(transform_dates(position))
        return clean_positions


class ExtraField(ma.fields.Field):
    def _serialize(self, extra, attr, obj):
        if not extra:
            return extra
        new_declarations = {}
        for declaration, link in extra["declarations"].items():
            new_declaration = transform_dates(declaration)
            new_declarations[new_declaration] = link

        extra["declarations"] = new_declarations
        return extra


class DeputyExtendedSchema(ma.ModelSchema):
    class Meta:
        model = Deputy
        model_skip_values = [None]
        model_fields_kwargs = {
            "start_date": {"load_only": True},
            "end_date": {"load_only": True},
        }

    footprint = ma.fields.Method("get_footprint")
    footprint_by_topics = ma.fields.Method("get_footprint_by_topics")
    public_position = PublicPositionsField(attribute="public_position")
    extra = ExtraField(attribute="extra")

    def get_footprint(self, obj):
        try:
            fbd = FootprintByDeputy.objects.get(id=obj.id)
            fbd_serialized = FootprintByDeputySchema().dump(fbd)
            return fbd_serialized["score"]
        except Exception:
            return 0.0

    def get_footprint_by_topics(self, obj):
        try:
            fbd = FootprintByDeputy.objects.get(id=obj.id)
            fbd_serialized = FootprintByDeputySchema().dump(fbd)
            return fbd_serialized["topics"]
        except Exception:
            return list()


class DeputyCompactSchema(ma.ModelSchema):
    class Meta:
        model = Deputy
        model_skip_values = [None]
        model_fields_kwargs = {
            "email": {"load_only": True},
            "web": {"load_only": True},
            "twitter": {"load_only": True},
            "facebook": {"load_only": True},
            "public_position": {"load_only": True},
            "legislatures": {"load_only": True},
            "party_logo": {"load_only": True},
            "bio": {"load_only": True},
            "start_date": {"load_only": True},
            "end_date": {"load_only": True},
            "url": {"load_only": True},
            "extra": {"load_only": True},
        }
