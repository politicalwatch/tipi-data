from tipi_data import db


class Deputy(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    parliamentarygroup = db.StringField()
    image = db.URLField()
    email = db.EmailField()
    web = db.URLField()
    twitter = db.URLField()
    facebook = db.URLField()
    constituency = db.StringField()
    public_charges = db.ListField(db.StringField(), default=list)
    birthday = db.StringField()
    bio = db.ListField(db.StringField(), default=list)
    start_date = db.DateTimeField()
    end_date = db.DateTimeField()
    url = db.URLField()
    active = db.BooleanField()
    extra = db.DictField()

    meta = {
            'collection': 'deputies',
            'ordering': ['name'],
            'indexes': ['name']
            }
    # TODO Add indexes https://mongoengine-odm.readthedocs.io/guide/defining-documents.html#indexes

    def __str__(self):
        return self.name
