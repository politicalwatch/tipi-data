from tipi_data import db


class TotalsVotes(db.EmbeddedDocument):
    present = db.IntField()
    skip = db.IntField()
    yes = db.IntField()
    no = db.IntField()
    abstention = db.IntField()


class ByDeputy(db.EmbeddedDocument):
    name = db.StringField()
    seat = db.StringField()
    group = db.StringField()
    vote = db.StringField()


class GroupVote(db.EmbeddedDocument):
    yes = db.IntField(default=0)
    no = db.IntField(default=0)
    abstention = db.IntField(default=0)
    skip = db.IntField(default=0)


class ByGroup(db.EmbeddedDocument):
    name = db.StringField()
    votes = db.EmbeddedDocumentField(GroupVote)


class Voting(db.DynamicDocument):
    id = db.StringField(db_field='_id', primary_key=True)
    reference = db.StringField()
    title = db.StringField()
    subgroup_text = db.StringField()
    subgroup_title = db.StringField()

    totals = db.EmbeddedDocumentField(TotalsVotes)

    by_deputies = db.EmbeddedDocumentListField(ByDeputy, default=[])
    by_groups = db.EmbeddedDocumentListField(ByGroup, default=[])

    meta = {'collection': 'votes'}
