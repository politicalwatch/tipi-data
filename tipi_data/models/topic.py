from mongoengine.queryset import QuerySet
from natsort import natsorted, ns

from tipi_data import db


class TopicQuerySet(QuerySet):

    def natsorted(self):
        return natsorted(
                self,
                key=lambda x: x.name,
                alg=ns.IGNORECASE)


class Tag(db.EmbeddedDocument):
    tag = db.StringField()
    subtopic = db.StringField()
    regex = db.StringField()
    shuffle = db.BooleanField()

    def __str__(self):
        return self.tag


class Topic(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    shortname = db.StringField()
    description = db.ListField(db.StringField())
    tags = db.EmbeddedDocumentListField(Tag)
    knowledgebase = db.StringField()
    public = db.BooleanField()

    meta = {
            'collection': 'topics',
            'ordering': ['name'],
            'indexes': ['name'],
            'queryset_class': TopicQuerySet
            }
    # TODO Add indexes https://docs.mongoengine.org/guide/defining-documents.html#indexes

    def __str__(self):
        return self.name
