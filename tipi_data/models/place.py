from tipi_data import db


class Place(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()

    meta = {
            'collection': 'places',
            'ordering': ['name'],
            'indexes': ['name']
            }

    def __str__(self):
        return self.name
