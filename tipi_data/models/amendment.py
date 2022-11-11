from tipi_data import db

class Amendment(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    bulletin_name = db.StringField()
    type = db.StringField()
    applies_to = db.StringField()
    reference = db.StringField()
    author_deputies = db.ListField(db.StringField(), default=list)
    author_parliamentarygroups = db.ListField(db.StringField(), default=list)
    justification = db.ListField(db.StringField(), default=list)
    propossed_change = db.ListField(db.StringField(), default=list)

    def set_id(self, id):
        self.id = self.reference + '/' + id

    def add_author(self, author):
        self.author_deputies.append(author)

    def add_type(self, type):
        self.type = type

    def add_applies_to(self, applies_to):
        self.applies_to = applies_to

    def add_group(self, group):
        self.author_parliamentarygroups.append(group)

    def set_justification(self, justification):
        self.justification = justification

    def set_propossed_change(self, propossed_change):
        self.propossed_change = propossed_change
