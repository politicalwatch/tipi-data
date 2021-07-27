from tipi_data.models.initiative import Initiative


class Initiatives():
    @staticmethod
    def get_all():
        return Initiative.objects()

    @staticmethod
    def by_kb(kb):
        return Initiative.objects(
                tagged__match={
                    'knowledgebase': kb,
                    'topics': {'$size': {'$not': 0}}
                    }
                )

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
