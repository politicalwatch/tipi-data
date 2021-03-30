from tipi_data import db


class Voting(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    reference = db.StringField()
    title = db.StringField()

    total_yes = db.IntField()
    total_no = db.IntField()
    total_abstention = db.IntField()
    total_skip = db.IntField()
    total_present = db.IntField()

    by_party = db.DictField()
    by_deputy = db.DictField()

    meta = {'collection': 'votes'}
