from tipi_data.models.footprint import (
    FootprintByTopic,
    FootprintByDeputy,
    FootprintByParliamentaryGroup,
)


class Footprints:
    @staticmethod
    def get_all_topics():
        return FootprintByTopic.objects()

    @staticmethod
    def get_by_topic(topic):
        return FootprintByTopic.objects().get(name=topic)

    @staticmethod
    def get_range_by_all_topics():
        pipeline = [
            {
                "$project": {
                    "_id": 0,
                    "name": "$name",
                    "deputy": {
                        "max": {
                            "$first": {
                                "$filter": {
                                    "input": {
                                        "$sortArray": {
                                            "input": "$deputies",
                                            "sortBy": {"score": -1},
                                        }
                                    },
                                    "as": "deputy",
                                    "cond": {
                                        "$eq": [
                                            "$$deputy.score",
                                            {"$max": "$deputies.score"},
                                        ]
                                    },
                                }
                            }
                        },
                        "min": {
                            "$first": {
                                "$filter": {
                                    "input": {
                                        "$sortArray": {
                                            "input": "$deputies",
                                            "sortBy": {"score": 1},
                                        }
                                    },
                                    "as": "deputy",
                                    "cond": {"$gt": ["$$deputy.score", 0]},
                                }
                            }
                        },
                    },
                    "parliamentarygroup": {
                        "max": {
                            "$first": {
                                "$filter": {
                                    "input": {
                                        "$sortArray": {
                                            "input": "$parliamentarygroups",
                                            "sortBy": {"score": -1},
                                        }
                                    },
                                    "as": "pg",
                                    "cond": {
                                        "$eq": [
                                            "$$pg.score",
                                            {"$max": "$parliamentarygroups.score"},
                                        ]
                                    },
                                }
                            }
                        },
                        "min": {
                            "$first": {
                                "$filter": {
                                    "input": {
                                        "$sortArray": {
                                            "input": "$parliamentarygroups",
                                            "sortBy": {"score": 1},
                                        }
                                    },
                                    "as": "pg",
                                    "cond": {"$gt": ["$$pg.score", 0]},
                                }
                            }
                        },
                    },
                }
            },
            {"$sort": {"topic": 1}},
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
