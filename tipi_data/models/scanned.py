from tipi_data import db
from tipi_data.models.initiative import Tagged


class Scanned(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    title = db.StringField()
    excerpt = db.StringField()
    result = db.EmbeddedDocumentListField(Tagged, default=list)
    created = db.DateTimeField()
    expiration = db.DateTimeField()
    verified = db.BooleanField()

    meta = {'collection': 'scanned'}
    # TODO Add indexes https://docs.mongoengine.org/guide/defining-documents.html#indexes

    def init_tagged_kb(self, kb):
        tagged = list(filter(lambda tagged: tagged.knowledgebase == kb, self.result))
        if len(tagged) > 0:
            return
        tagged = Tagged(knowledgebase=kb, topics=[], tags=[])
        self.result.append(tagged)

    def add_tag(self, kb, topic, subtopic, tag_name, times):
        tagged = list(filter(lambda tagged: tagged.knowledgebase == kb, self.result))

        if len(tagged) > 0:
            tagged = tagged[0]
        else:
            tagged = Tagged(knowledgebase=kb, topics=[], tags=[])
            self.result.append(tagged)

        tagged.add_tag(topic, subtopic, tag_name, times)
