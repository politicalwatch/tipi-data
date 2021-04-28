from mongoengine.queryset import queryset_manager

from tipi_data import db


class Tag(db.EmbeddedDocument):
    topic = db.StringField()
    subtopic = db.StringField()
    tag = db.StringField()
    times = db.IntField()

    def __str__(self):
        return self.tag


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
    topics = db.ListField(db.StringField(), default=list)
    tags = db.EmbeddedDocumentListField(Tag, default=list)
    tagged = db.BooleanField()
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
    # TODO Add indexes https://mongoengine-odm.readthedocs.io/guide/defining-documents.html#indexes

    def __str__(self):
        return "{} : {}".format(self.id, self.title)

    @queryset_manager
    def objects(doc_cls, queryset):
        return queryset.filter(topics__exists=True, topics__not__size=0)

    @queryset_manager
    def all(doc_cls, queryset):
        return queryset
