from tipi_data.models.topic import Topic


class Topics():
    @staticmethod
    def get_all():
        return Topic.objects()

    @staticmethod
    def get_kbs():
        return Topic.objects().distinct('knowledgebase')
