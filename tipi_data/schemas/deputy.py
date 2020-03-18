import marshmallow_mongoengine as ma

from tipi_data.models.deputy import Deputy


class DeputySchema(ma.ModelSchema):
    class Meta:
        model = Deputy
        model_skip_values = [None]
        model_fields_kwargs = {
                'email': {'load_only': True},
                'web': {'load_only': True},
                'twitter': {'load_only': True},
                'start_date': {'load_only': True},
                'end_date': {'load_only': True},
                'url': {'load_only': True},
                }


class DeputyExtendedSchema(ma.ModelSchema):
    class Meta:
        model = Deputy
        model_skip_values = [None]
        model_fields_kwargs = {
                'start_date': {'load_only': True},
                'end_date': {'load_only': True},
                }
