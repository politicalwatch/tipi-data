from tipi_data import db


class Search(db.DynamicEmbeddedDocument):
    hash = db.StringField()
    search = db.StringField()
    dbsearch = db.StringField()
    created = db.DateTimeField()
    validated = db.BooleanField(default=False)
    validation_email_sent = db.BooleanField()
    validation_email_sent_date = db.DateTimeField()

    def __str__(self):
        return self.hash


class Alert(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    email = db.EmailField()
    searches = db.EmbeddedDocumentListField(Search)

    meta = {'collection': 'alerts'}
    # TODO Add indexes https://mongoengine-odm.readthedocs.io/guide/defining-documents.html#indexes

    def __str__(self):
        return self.email


class InitiativeAlert(db.DynamicDocument):
    id = db.StringField(db_field='_id', primary_key=True)
    meta = {
        'collection': 'initiatives_alerts'
    }
