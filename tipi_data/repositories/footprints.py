from tipi_data.models.footprint import FootprintByTopic, \
        FootprintByDeputy, \
        FootprintByParliamentaryGroup


class Footprints():
    @staticmethod
    def get_all_topics():
        return FootprintByTopic.objects()

    @staticmethod
    def get_by_topic(topic):
        return FootprintByTopic.objects().get(name=topic)

    @staticmethod
    def get_max_by_all_topics():
         pipeline = [
                 {
                     "$project": {
                         "_id": 0,
                         "name": 1,
                         "deputy": {"$arrayElemAt": ["$deputies", 0]},
                         "parliamentarygroup": {"$arrayElemAt": ["$parliamentarygroups", 0]}
                         }
                     }
                 ]
         return FootprintByTopic.objects().aggregate(*pipeline)

    @staticmethod
    def get_all_deputies():
        return FootprintByDeputy.objects()

    @staticmethod
    def get_by_deputy(deputy):
        return FootprintByDeputy.objects().get(name=deputy)

    @staticmethod
    def get_all_parliamentarygroups():
        return FootprintByParliamentaryGroup.objects()

    @staticmethod
    def get_by_parliamentarygroup(parliamentarygroup):
        return FootprintByParliamentaryGroup.objects().get(name=parliamentarygroup)
