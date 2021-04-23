from tipi_data import db


class InitiativeType(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    group = db.StringField()
    meta = {
        'collection': 'initiative_types',
        'ordering': ['+name']
    }

    def __str__(self):
        return "{} : {}/{}".format(self.group, self.id, self.type)
