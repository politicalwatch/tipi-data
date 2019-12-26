from tipi_data import db


class Stats(db.DynamicDocument):
    meta = {'collection': 'statistics'}
