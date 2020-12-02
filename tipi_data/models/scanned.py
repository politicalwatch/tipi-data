from tipi_data import db
from tipi_data.models.initiative import Tag


class ScannedResult(db.DynamicEmbeddedDocument):
    topics = db.ListField(db.StringField(), default=list)
    tags = db.EmbeddedDocumentListField(Tag, default=list)

class Scanned(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    title = db.StringField()
    excerpt = db.StringField()
    result = db.EmbeddedDocumentField(ScannedResult)
    created = db.DateTimeField()
    expiration = db.DateTimeField()
    verified = db.BooleanField()

    meta = {'collection': 'scanned'}
    # TODO Add indexes https://mongoengine-odm.readthedocs.io/guide/defining-documents.html#indexes
