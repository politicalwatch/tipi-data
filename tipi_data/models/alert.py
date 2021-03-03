from tipi_data import db
from tipi_data.models.initiative import Initiative


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


def create_alert(initiative: Initiative):
    initiative_alert = InitiativeAlert(
            id=initiative['id'],
            title=initiative['title'],
            reference=initiative['reference'],
            initiative_type=initiative['initiative_type'],
            initiative_type_alt=initiative['initiative_type_alt'],
            author_deputies=initiative['author_deputies'],
            author_parliamentarygroups=initiative['author_parliamentarygroups'],
            author_others=initiative['author_others'],
            place=initiative['place'],
            created=initiative['created'],
            updated=initiative['updated'],
            history=initiative['history'],
            status=initiative['status'],
            topics=initiative['topics'],
            tags=initiative['tags'],
            tagged=initiative['tagged'],
            url=initiative['url'],
            extra=initiative['extra'],
            )
    initiative_alert.save()
