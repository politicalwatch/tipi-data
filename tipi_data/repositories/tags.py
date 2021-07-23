from tipi_data.models.topic import Topic

import itertools
import pcre

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
                'compiletag': pcre.compile('(?i)' + delimiter.join(permutation))
            })
        return tags

    return [{
        'topic': topic['name'],
        'subtopic': tag['subtopic'],
        'tag': tag['tag'],
        'knowledgebase': topic['knowledgebase'],
        'compiletag': pcre.compile('(?i)' + tag['regex'])
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
    def by_name(name):
        tags = []
        for topic in Topic.objects():
            for tag in topic['tags']:
                if tag['tag'] != name:
                    continue

                tags = tags + compile_tag(topic, tag)
        return tags

    @staticmethod
    def by_topic(topic):
        tags = []
        for topic in Topic.objects():
            if topic['name'] != topic:
                continue

            for tag in topic['tags']:
                tags = tags + compile_tag(topic, tag)
        return tags

    @staticmethod
    def by_kb(kb):
        tags = []
        topics = Topic.objects(knowledgebase=kb)
        for topic in topics:
            for tag in topic['tags']:
                tags = tags + compile_tag(topic, tag)
        return tags

