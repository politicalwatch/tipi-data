from tipi_data.models.topic import Topic

class KnowledgeBases():
    @staticmethod
    def get_all():
        kbs = []
        for topic in Topic.objects():
            kbs.append(topic.knowledgebase)
        return list(set(kbs))

    @staticmethod
    def get_public():
        kbs = []
        for topic in Topic.objects():
            if topic.public:
                kbs.append(topic.knowledgebase)
        return list(set(kbs))
