import marshmallow_mongoengine as ma

from tipi_data.models.initiative import Initiative


class ContentField(ma.fields.Field):
    def _serialize(self, value, attr, obj):
        return "\n".join(value)


class InitiativeSchema(ma.ModelSchema):
    class Meta:
        model = Initiative
        model_skip_values = [None]
        model_fields_kwargs = {
            "author_parliamentarygroups": {"load_only": True},
            "author_deputies": {"load_only": True},
            "author_others": {"load_only": True},
            "history": {"load_only": True},
            "extra": {"load_only": True},
            "content": {"load_only": True},
        }

    authors = ma.fields.Method("get_authors")
    deputies = ma.fields.Method("get_deputies")
    place = ma.fields.Method(serialize="_place_serializer")
    tagged = ma.fields.Method(serialize="_tagged_serializer")

    def get_authors(self, obj):
        return obj.author_others + obj.author_parliamentarygroups

    def get_deputies(self, obj):
        return obj.author_deputies

    def __init__(self, *args, **kwargs):
        if "kb" in kwargs:
            self.kb = kwargs["kb"]
            del kwargs["kb"]
        else:
            self.kb = False

        super().__init__(*args, **kwargs)

    def _place_serializer(self, obj):
        return obj.place if "place" in obj else ""

    def _tagged_serializer(self, obj):
        tagged = list(
            filter(lambda tagged: tagged.knowledgebase in self.kb, obj.tagged)
        )
        return list(map(lambda tag_set: tag_set.serialize(), tagged))


class InitiativeNoContentSchema(ma.ModelSchema):
    class Meta:
        model = Initiative
        model_skip_values = [None]
        model_fields_kwargs = {
            "author_parliamentarygroups": {"load_only": True},
            "author_deputies": {"load_only": True},
            "author_others": {"load_only": True},
            "content": {"load_only": True},
        }

    authors = ma.fields.Method("get_authors")
    deputies = ma.fields.Method("get_deputies")
    tagged = ma.fields.Method(serialize="_tagged_serializer")

    def get_authors(self, obj):
        return obj.author_others + obj.author_parliamentarygroups

    def get_deputies(self, obj):
        return obj.author_deputies

    def __init__(self, *args, **kwargs):
        if "kb" in kwargs:
            self.kb = kwargs["kb"]
            del kwargs["kb"]
        super().__init__(*args, **kwargs)

    def _tagged_serializer(self, obj):
        tagged = list(
            filter(lambda tagged: tagged.knowledgebase in self.kb, obj.tagged)
        )
        return list(map(lambda tag_set: tag_set.serialize(), tagged))


class InitiativeExtendedSchema(ma.ModelSchema):
    class Meta:
        model = Initiative
        model_skip_values = [None]
        model_fields_kwargs = {
            "author_parliamentarygroups": {"load_only": True},
            "author_deputies": {"load_only": True},
            "author_others": {"load_only": True},
        }

    authors = ma.fields.Method("get_authors")
    deputies = ma.fields.Method("get_deputies")
    content = ContentField(attribute="content")
    tagged = ma.fields.Method(serialize="_tagged_serializer")

    def get_authors(self, obj):
        return obj.author_others + obj.author_parliamentarygroups

    def get_deputies(self, obj):
        return obj.author_deputies

    def __init__(self, *args, **kwargs):
        if "kb" in kwargs:
            self.kb = kwargs["kb"]
            del kwargs["kb"]
        super().__init__(*args, **kwargs)

    def _tagged_serializer(self, obj):
        tagged = list(
            filter(lambda tagged: tagged.knowledgebase in self.kb, obj.tagged)
        )
        return list(map(lambda tag_set: tag_set.serialize(), tagged))
