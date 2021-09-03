from tipi_data.models.topic import Topic


class Topics():
    @staticmethod
    def get_all():
        return Topic.objects()

    @staticmethod
    def get_all_sorted():
        return Topics.get_all().natsorted()

    @staticmethod
    def get_public():
        return Topic.objects(public=True).natsorted()

    @staticmethod
    def get(id):
        return Topic.objects.get(id=id)

    @staticmethod
    def by_kb(kb):
        return Topic.objects(knowledgebase=kb)

    @staticmethod
    def by_kb_sorted(kb):
        Topics.by_kb(kb).natsorted()

    @staticmethod
    def get_subtopics():
        return Topic.objects().distinct('tags.subtopic')

    @staticmethod
    def get_subtopics_by_kb(kb):
        return Topics.by_kb(kb).distinct('tags.subtopic')

    @staticmethod
    def get_kbs():
        return Topic.objects().distinct('knowledgebase')
