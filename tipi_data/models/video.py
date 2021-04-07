from tipi_data import db


class Video(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    reference = db.StringField()
    link = db.StringField()
    session_name = db.StringField()
    speaker = db.StringField()
    type = db.StringField()
    date = db.IntField()

    meta = {'collection': 'videos'}
