from tipi_data.models.footprint import FootprintByTopic, FootprintByDeputy


class Footprints():
    @staticmethod
    def get_all_topics():
        return FootprintByTopic.objects()

    @staticmethod
    def get_by_topic(topic):
        return FootprintByTopic.objects().get(name=topic)

    @staticmethod
    def get_all_deputies():
        return FootprintByDeputy.objects()

    @staticmethod
    def get_by_deputy(deputy):
        return FootprintByDeputy.objects().get(name=deputy)
