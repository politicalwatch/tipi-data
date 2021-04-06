import marshmallow_mongoengine as ma

from tipi_data.models.video import Video


class VideoSchema(ma.ModelSchema):
    class Meta:
        model = Video
        model_skip_values = [None]
