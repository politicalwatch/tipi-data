import marshmallow_mongoengine as ma

from tipi_data.models.initiative import Initiative


class AuthorsField(ma.fields.Field):
    def _serialize(self, value, attr, obj):
        return obj.author_others + obj.author_parliamentarygroups


class DeputiesField(ma.fields.Field):
    def _serialize(self, value, attr, obj):
        return value

class ContentField(ma.fields.Field):
    def _serialize(self, value, attr, ob):
        return '\n'.join(value)


class InitiativeSchema(ma.ModelSchema):
    class Meta:
        model = Initiative
        model_skip_values = [None]
        model_fields_kwargs = {
                'author_deputies': {'load_only': True},
                'author_parliamentarygroups': {'load_only': True},
                'author_others': {'load_only': True},
                'history': {'load_only': True},
                'extra': {'load_only': True},
                'content': {'load_only': True},
                }

    authors = AuthorsField(attribute='author_parliamentarygroups')
    deputies = DeputiesField(attribute='author_deputies')
    place = ma.fields.Method(serialize="_place_serializer")
    tagged = ma.fields.Method(serialize="_tagged_serializer")

    def __init__(self, *args, **kwargs):
        if 'kb' in kwargs:
            self.kb = kwargs['kb']
            del kwargs['kb']
        else:
            self.kb = False

        super().__init__(*args, **kwargs)

    def _place_serializer(self, obj):
        return obj.place if 'place' in obj else ''

    def _tagged_serializer(self, obj):
        if self.kb:
            tagged = list(filter(lambda tagged: tagged.knowledgebase in self.kb, obj.tagged))
        else:
            tagged = list(filter(lambda tagged: tagged.public, obj.tagged))
        return list(map(lambda tag_set: tag_set.serialize(), tagged))


class InitiativeNoContentSchema(ma.ModelSchema):
    class Meta:
        model = Initiative
        model_skip_values = [None]
        model_fields_kwargs = {
                'author_deputies': {'load_only': True},
                'author_parliamentarygroups': {'load_only': True},
                'author_others': {'load_only': True},
                'content': {'load_only': True},
                }

    authors = AuthorsField(attribute='author_parliamentarygroups')
    deputies = DeputiesField(attribute='author_deputies')
    related = ma.fields.Method(serialize="_related_serializer")
    tagged = ma.fields.Method(serialize="_tagged_serializer")

    def __init__(self, *args, **kwargs):
        if 'kb' in kwargs:
            self.kb = kwargs['kb']
            del kwargs['kb']
        super().__init__(*args, **kwargs)

    def _related_serializer(self, obj):
        related = InitiativeSchema(many=True).dump(Initiative.all(reference=obj['reference']))
        if related.errors:
            return []
        related = [r for r in related.data if r['id'] != obj['id']]
        self._process_soft_related(related)
        return related

    # Soft related means that it is related but does not have any topics
    def _process_soft_related(self, related):
        for r in related:
            if len(r['topics']) == 0:
                del r['id']

    def _tagged_serializer(self, obj):
        if self.kb:
            tagged = list(filter(lambda tagged: tagged.knowledgebase in self.kb, obj.tagged))
        else:
            tagged = list(filter(lambda tagged: tagged.public, obj.tagged))
        return list(map(lambda tag_set: tag_set.serialize(), tagged))

class InitiativeExtendedSchema(ma.ModelSchema):
    class Meta:
        model = Initiative
        model_skip_values = [None]
        model_fields_kwargs = {
                'author_deputies': {'load_only': True},
                'author_parliamentarygroups': {'load_only': True},
                'author_others': {'load_only': True},
                }

    authors = AuthorsField(attribute='author_parliamentarygroups')
    deputies = DeputiesField(attribute='author_deputies')
    related = ma.fields.Method(serialize="_related_serializer")
    content = ContentField(attribute='content')
    tagged = ma.fields.Method(serialize="_tagged_serializer")

    def __init__(self, *args, **kwargs):
        if 'kb' in kwargs:
            self.kb = kwargs['kb']
            del kwargs['kb']
        super().__init__(*args, **kwargs)

    def _related_serializer(self, obj):
        related = InitiativeSchema(many=True).dump(Initiative.all(reference=obj['reference']))
        if related.errors:
            return []
        related = [r for r in related.data if r['id'] != obj['id']]
        self._process_soft_related(related)
        return related

    # Soft related means that it is related but does not have any topics
    def _process_soft_related(self, related):
        for r in related:
            if len(r['topics']) == 0:
                del r['id']

    def _tagged_serializer(self, obj):
        if self.kb:
            tagged = list(filter(lambda tagged: tagged.knowledgebase in self.kb, obj.tagged))
        else:
            tagged = list(filter(lambda tagged: tagged.public, obj.tagged))
        return list(map(lambda tag_set: tag_set.serialize(), tagged))
