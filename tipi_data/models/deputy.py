import datetime

from mongoengine.queryset import queryset_manager

from tipi_data import db


class Deputy(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    parliamentarygroup = db.StringField()
    image = db.StringField()
    email = db.EmailField()
    web = db.URLField()
    twitter = db.URLField()
    facebook = db.URLField()
    birthdate = db.DateTimeField()
    age = db.IntField()
    gender = db.StringField()
    constituency = db.StringField()
    public_position = db.ListField(db.StringField(), default=list)
    bio = db.ListField(db.StringField(), default=list)
    legislatures = db.ListField(db.StringField(), default=list)
    party_logo = db.StringField()
    party_name = db.StringField()
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

    def __str__(self):
        return self.name

    def calculate_age(self):
        if not self.birthdate:
            return
        today = datetime.datetime.today()
        years = today.year - self.birthdate.year
        if today.month < self.birthdate.month or \
                (today.month == self.birthdate.month and today.day < self.birthdate.day):
            years -= 1
        self.age = years

    def get_fullname(self):
        parts = self.name.split(',')
        name = parts[1] + ' ' + parts[0]
        return name.strip()

    @queryset_manager
    def actives(doc_cls, queryset):
        return queryset.filter(active=True)
