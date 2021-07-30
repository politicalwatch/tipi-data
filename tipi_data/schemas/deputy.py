import marshmallow_mongoengine as ma
import re

from tipi_data.models.deputy import Deputy


class DeputySchema(ma.ModelSchema):
    class Meta:
        model = Deputy
        model_skip_values = [None]
        model_fields_kwargs = {
                'email': {'load_only': True},
                'web': {'load_only': True},
                'twitter': {'load_only': True},
                'facebook': {'load_only': True},
                'constituency': {'load_only': True},
                'public_position': {'load_only': True},
                'birthdate': {'load_only': True},
                'gender': {'load_only': True},
                'legislatures': {'load_only': True},
                'party_logo': {'load_only': True},
                'party_name': {'load_only': True},
                'bio': {'load_only': True},
                'start_date': {'load_only': True},
                'end_date': {'load_only': True},
                'url': {'load_only': True},
                'extra': {'load_only': True},
                }


class DeputyExtendedSchema(ma.ModelSchema):
    class Meta:
        model = Deputy
        model_skip_values = [None]
        model_fields_kwargs = {
                'start_date': {'load_only': True},
                'end_date': {'load_only': True},
                }
