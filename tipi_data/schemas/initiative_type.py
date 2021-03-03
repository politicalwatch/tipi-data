import marshmallow_mongoengine as ma

from tipi_data.models.initiative_type import InitiativeType


class InitiativeTypeSchema(ma.ModelSchema):
    class Meta:
        model = InitiativeType
        model_skip_values = [None]
        model_fields_kwargs = {
                'group': {'load_only': True}
            }
