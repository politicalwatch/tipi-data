from tipi_data.models.initiative import Initiative


class Initiatives():
    @staticmethod
    def get(id):
        return Initiative.objects().get(id=id)

    @staticmethod
    def get_all():
        return Initiative.objects()

    @staticmethod
    def by_kb(kb):
        query = {
            'tagged.knowledgebase': kb,
            'tagged.topics': {'$not': {'$size': 0}}
        }
        return Initiatives.by_query(query)

    @staticmethod
    def by_kb_untagged(kb):
        query = {
            'tagged.knowledgebase': { '$ne': kb},
        }
        return Initiatives.by_query(query)

    @staticmethod
    def by_tag(tag):
        return Initiative.objects(tagged__tags__tag=tag)

    @staticmethod
    def get_all_untagged():
        query = {
                '$or': [
                    {'tagged': []},
                    {'tagged': {'$exists': False}},
                    ]
                }
        return Initiatives.by_query(query)

    @staticmethod
    def by_query(query):
        return Initiative.objects(__raw__=query)

    @staticmethod
    def by_reference(reference):
        return Initiative.objects(reference=reference)
