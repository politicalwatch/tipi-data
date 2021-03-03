from tipi_data import db


class InitiativeType(db.Document):
    code = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    group = db.StringField()
    meta = {
        'collection': 'initiative_types'
    }

    def __str__(self):
        return "{} : {}/{}".format(self.group, self.code, self.type)
