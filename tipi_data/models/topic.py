from mongoengine.queryset import QuerySet
from natsort import natsorted, ns
import itertools
import pcre

from tipi_data import db



class TopicQuerySet(QuerySet):

    def natsorted(self):
        return natsorted(
                self,
                key=lambda x: x.name,
                alg=ns.IGNORECASE)



class Tag(db.EmbeddedDocument):
    tag = db.StringField()
    subtopic = db.StringField()
    regex = db.StringField()
    shuffle = db.BooleanField()

    def __str__(self):
        return tag


class Topic(db.Document):
    id = db.StringField(db_field='_id', primary_key=True)
    name = db.StringField()
    shortname = db.StringField()
    description = db.ListField(db.StringField())
    tags = db.EmbeddedDocumentListField(Tag)

    meta = {
            'collection': 'topics',
            'ordering': ['name'],
            'indexes': ['name'],
            'queryset_class': TopicQuerySet
            }
    # TODO Add indexes https://mongoengine-odm.readthedocs.io/guide/defining-documents.html#indexes

    def __str__(self):
        return self.name


    @staticmethod
    def get_tags():
        tags = []
        for topic in Topic.objects():
            for tag in topic['tags']:
                delimiter = '.*?' if '.*?' in tag['regex'] else '.*'
                if tag['shuffle']:
                    for permutation in itertools.permutations(tag['regex'].split(delimiter)):
                        tags.append({
                            'topic': topic['name'],
                            'subtopic': tag['subtopic'],
                            'tag': tag['tag'],
                            'compiletag': pcre.compile('(?i)' + delimiter.join(permutation))
                        })
                else:
                    tags.append({
                        'topic': topic['name'],
                        'subtopic': tag['subtopic'],
                        'tag': tag['tag'],
                        'compiletag': pcre.compile('(?i)' + tag['regex'])
                    })
        return tags
