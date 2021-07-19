from tipi_data import db


class Tag(db.EmbeddedDocument):
    topic = db.StringField()
    subtopic = db.StringField()
    tag = db.StringField()
    times = db.IntField()

    def __str__(self):
        return self.tag


class Tagged(db.EmbeddedDocument):
    knowledgebase = db.StringField()
    topics = db.ListField(db.StringField(), default=list)
    tags = db.EmbeddedDocumentListField(Tag, default=list)


class Initiative(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    title = db.StringField()
    reference = db.StringField()
    initiative_type = db.StringField()
    initiative_type_alt = db.StringField()
    author_deputies = db.ListField(db.StringField(), default=list)
    author_parliamentarygroups = db.ListField(db.StringField(), default=list)
    author_others = db.ListField(db.StringField(), default=list)
    place = db.StringField()
    created = db.DateTimeField()
    updated = db.DateTimeField()
    history = db.ListField(db.StringField())
    status = db.StringField()
    tagged = db.EmbeddedDocumentListField(Tagged, default=list)
    url = db.URLField()
    content = db.ListField(db.StringField(), default=list)
    extra = db.DictField()

    meta = {
            'collection': 'initiatives',
            'ordering': ['-updated'],
            'indexes': [
                'reference',
                'updated',
                ]
            }
    # TODO Add indexes https://docs.mongoengine.org/guide/defining-documents.html#indexes

    def __str__(self):
        return "{} : {}".format(self.id, self.title)
