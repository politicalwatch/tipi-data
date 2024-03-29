from tipi_data import db


class Gender(db.EmbeddedDocument):
    female = db.IntField()
    male = db.IntField()


class Ages(db.EmbeddedDocument):
    under35 = db.IntField()
    between35and49 = db.IntField()
    between50and65 = db.IntField()
    over65 = db.IntField()


class ParliamentaryGroupComposition(db.EmbeddedDocument):
    deputies = db.IntField()
    gender = db.EmbeddedDocumentField(Gender)
    ages = db.EmbeddedDocumentField(Ages)


class ParliamentaryGroup(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    shortname = db.StringField()
    composition = db.EmbeddedDocumentField(ParliamentaryGroupComposition)
    parties = db.ListField(db.StringField(), default=list)
    color = db.StringField()

    meta = {
            'collection': 'parliamentarygroups',
            'ordering': ['-composition__deputies'],
            'indexes': ['name']
            }

    def __str__(self):
        return self.name
