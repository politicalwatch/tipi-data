from tipi_data.models.topic import Topic

import itertools
import regex

def compile_tag(topic, tag):
    delimiter = '.*?' if '.*?' in tag['regex'] else '.*'
    if tag['shuffle']:
        tags = []
        for permutation in itertools.permutations(tag['regex'].split(delimiter)):
            tags.append({
                'topic': topic['name'],
                'subtopic': tag['subtopic'],
                'tag': tag['tag'],
                'knowledgebase': topic['knowledgebase'],
                'public': topic['public'],
                'compiletag': regex.compile('(?i)' + delimiter.join(permutation))
            })
        return tags

    return [{
        'topic': topic['name'],
        'subtopic': tag['subtopic'],
        'tag': tag['tag'],
        'knowledgebase': topic['knowledgebase'],
        'public': topic['public'],
        'compiletag': regex.compile('(?i)' + tag['regex'])
    }]

class Tags():
    @staticmethod
    def get_all():
        tags = []
        for topic in Topic.objects():
            for tag in topic['tags']:
                tags = tags + compile_tag(topic, tag)
        return tags

    @staticmethod
    def by_name(topic, tag):
        try:
            topic = Topic.objects.get(name=topic)
            return compile_tag(
                    topic,
                    list(filter(
                        lambda x: x['tag'] == tag,
                        topic['tags']
                        ))[0]
                    )
        except KeyError:
            return None
        except IndexError:
            return None

    @staticmethod
    def by_topic(topic):
        tags = []
        try:
            topic = Topic.objects.get(name=topic)
            for tag in topic['tags']:
                tags = tags + compile_tag(topic, tag)
            return tags
        except KeyError:
            return []
        except IndexError:
            return []

    @staticmethod
    def by_kb(kb):
        tags = []
        topics = Topic.objects(knowledgebase=kb)
        for topic in topics:
            for tag in topic['tags']:
                tags = tags + compile_tag(topic, tag)
        return tags

