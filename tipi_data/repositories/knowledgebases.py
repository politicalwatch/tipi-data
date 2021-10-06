from tipi_data.models.topic import Topic

class KnowledgeBases():
    @staticmethod
    def get_all():
        return Topic.objects().distinct('knowledgebase')

    @staticmethod
    def get_public():
        return Topic.objects(public=True).distinct('knowledgebase')
