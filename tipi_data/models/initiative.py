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


class TopicAlignment(db.EmbeddedDocument):
    topic = db.StringField()
    percentage = db.FloatField()

    def __str__(self):
        return f"{self.topic}: {self.percentage}%"

    def serialize(self):
        return {
                'topic': self.topic,
                'percentage': self.percentage
                }


class Tagged(db.EmbeddedDocument):
    knowledgebase = db.StringField()
    topics = db.ListField(db.StringField(), default=list)
    topic_alignment = db.EmbeddedDocumentListField(TopicAlignment, default=list)
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
            'topic_alignment': list(map(lambda ta: ta.serialize(), self.topic_alignment)),
            'tags': list(map(lambda tag_set: tag_set.serialize(), self.tags))
        }


class Initiative(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    title = db.StringField()
    reference = db.StringField()
    initiative_type = db.StringField()
    initiative_type_alt = db.StringField()
    author_deputies = db.ListField(db.StringField(), default=list)
    author_parliamentarygroups = db.ListField(db.StringField(), default=list)
    author_others = db.ListField(db.StringField(), default=list)
    place = db.StringField()
    created = db.DateTimeField()
    updated = db.DateTimeField()
    history = db.ListField(db.StringField())
    status = db.StringField()
    tagged = db.EmbeddedDocumentListField(Tagged, default=list)
    url = db.URLField()
    content = db.ListField(db.StringField(), default=list)
    extra = db.DictField()

    meta = {
            'collection': 'initiatives',
            'ordering': ['-updated'],
            'indexes': [
                {
                    'fields': ['$title', '$content'],
                    'default_language': 'spanish'
                    },
                'reference',
                'updated',
                ]
            }

    def __str__(self):
        return "{} : {}".format(self.id, self.title)

    def untag(self):
        self.tagged = []

    def untag_kb(self, kb):
        tagged = list(filter(lambda tagged: tagged.knowledgebase != kb, self.tagged))
        self.tagged = tagged

    def init_tagged_kb(self, kb):
        tagged = list(filter(lambda tagged: tagged.knowledgebase == kb, self.tagged))
        if len(tagged) > 0:
            return
        tagged = Tagged(knowledgebase=kb, topics=[], tags=[])
        self.tagged.append(tagged)

    def add_tag(self, kb, topic, subtopic, tag_name, times):
        tagged = list(filter(lambda tagged: tagged.knowledgebase == kb, self.tagged))

        if len(tagged) > 0:
            tagged = tagged[0]
        else:
            tagged = Tagged(knowledgebase=kb, topics=[], tags=[])
            self.tagged.append(tagged)

        tagged.add_tag(topic, subtopic, tag_name, times)

    def remove_single_occurences(self):
        for tagged in self.tagged:
            tagged.remove_single_occurences()

    def has_tags(self):
        return any(tagged.has_topics for tagged in self.tagged)
