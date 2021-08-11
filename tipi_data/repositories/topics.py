from tipi_data.models.topic import Topic


class Topics():
    @staticmethod
    def get_all():
        return Topic.objects()

    @staticmethod
    def get_public():
        return Topic.objects(public=True)

    @staticmethod
    def get(id):
        return Topic.objects.get(id=id)

    @staticmethod
    def by_kb(kb):
        query = {
            'knowledgebase': {
                '$in': kb
            }
        }
        return Topic.objects(__raw__=query)

    @staticmethod
    def get_kbs():
        return Topic.objects().distinct('knowledgebase')
