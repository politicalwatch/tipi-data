import hashlib

from tipi_data import db

class Tag(db.EmbeddedDocument):
    topic = db.StringField()
    subtopic = db.StringField()
    tag = db.StringField()
    times = db.IntField()

    def __str__(self):
        return self.tag

    def serialize(self):
        return {
            'topic': self.topic,
            'subtopic': self.subtopic,
            'tag': self.tag,
            'times': self.times
        }

class Tagged(db.EmbeddedDocument):
    knowledgebase = db.StringField()
    topics = db.ListField(db.StringField(), default=list)
    tags = db.EmbeddedDocumentListField(Tag, default=list)

    def __str__(self):
        return self.knowledgebase

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_tag(self, topic, subtopic, tag_name, times):
        if list(filter(lambda tag: tag.tag == tag_name and tag.subtopic == subtopic, self.tags)) == []:
            tag = Tag(topic=topic, subtopic=subtopic, tag=tag_name, times=times)
            self.tags.append(tag)
            self.add_topic(topic)

    def remove_single_occurences(self):
        topics_counter = dict()
        for tag in self.tags:
            if tag['topic'] in topics_counter.keys():
                topics_counter[tag['topic']] += tag['times']
            else:
                topics_counter[tag['topic']] = tag['times']
        for key in topics_counter.keys():
            if topics_counter[key] == 1:
                self.tags = list(filter(lambda x: x['topic'] != key, self.tags))
        self.topics = sorted(list(set([tag['topic'] for tag in self.tags])))

    def has_topics(self):
        return len(self.topics) > 0

    def serialize(self):
        return {
            'knowledgebase': self.knowledgebase,
            'topics': self.topics,
            'tags': list(map(lambda tag_set: tag_set.serialize(), self.tags))
        }

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
    from_senate = db.BooleanField()
    justification_tagged = db.EmbeddedDocumentListField(Tagged, default=list)
    propossed_change_tagged = db.EmbeddedDocumentListField(Tagged, default=list)

    def set_id(self, id):
        self.id = self.reference + '/' + hashlib.md5(self.bulletin_name.encode()).hexdigest() + '/' + id.strip()

    def add_author(self, author):
        self.author_deputies.append(author)

    def add_type(self, type):
        self.type = type.capitalize()

    def add_applies_to(self, applies_to):
        self.applies_to = applies_to

    def add_group(self, group):
        self.author_parliamentarygroups.append(group)

    def set_justification(self, justification):
        self.justification = justification

    def set_propossed_change(self, propossed_change):
        self.propossed_change = propossed_change

    def mark_as_congress(self):
        self.from_senate = False

    def mark_as_senate(self):
        self.from_senate = True

    def add_justification_tag(self, kb, topic, subtopic, tag_name, times):
        tagged = list(filter(lambda tagged: tagged.knowledgebase == kb, self.justification_tagged))

        if len(tagged) > 0:
            tagged = tagged[0]
        else:
            tagged = Tagged(knowledgebase=kb, topics=[], tags=[])
            self.justification_tagged.append(tagged)

        tagged.add_tag(topic, subtopic, tag_name, times)

    def add_propossed_change_tag(self, kb, topic, subtopic, tag_name, times):
        tagged = list(filter(lambda tagged: tagged.knowledgebase == kb, self.propossed_change_tagged))

        if len(tagged) > 0:
            tagged = tagged[0]
        else:
            tagged = Tagged(knowledgebase=kb, topics=[], tags=[])
            self.propossed_change_tagged.append(tagged)

        tagged.add_tag(topic, subtopic, tag_name, times)
