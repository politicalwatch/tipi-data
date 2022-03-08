from datetime import datetime

from tipi_data import db


class FootprintElement(db.EmbeddedDocument):
    name = db.StringField()
    score = db.FloatField()

    def __str__(self):
        return f"{self.name}: {self.score}"


class FootprintByTopic(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    deputies = db.EmbeddedDocumentListField(FootprintElement)
    parliamentarygroups = db.EmbeddedDocumentListField(FootprintElement)
    computed_at = db.DateTimeField(default=datetime.now())
    meta = {
            'collection': 'footprint_by_topics',
            'indexes': ['name']
            }


class FootprintByDeputy(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    score = db.FloatField()
    topics = db.EmbeddedDocumentListField(FootprintElement)
    computed_at = db.DateTimeField(default=datetime.now())
    meta = {
            'collection': 'footprint_by_deputies',
            'indexes': ['name']
            }


class FootprintByParliamentaryGroup(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    score = db.FloatField()
    topics = db.EmbeddedDocumentListField(FootprintElement)
    computed_at = db.DateTimeField(default=datetime.now())
    meta = {
            'collection': 'footprint_by_parliamentarygroups',
            'indexes': ['name']
            }
