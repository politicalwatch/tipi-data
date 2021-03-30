import marshmallow_mongoengine as ma

from tipi_data.models.voting import Voting


class VotingSchema(ma.ModelSchema):
    class Meta:
        model = Voting
        model_skip_values = [None]
