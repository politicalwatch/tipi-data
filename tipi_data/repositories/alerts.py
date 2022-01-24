from tipi_data.models.alert import Alert, InitiativeAlert


class Alerts():
    @staticmethod
    def get_all():
        return Alert.objects()

    @staticmethod
    def get_validated():
        return Alert.objects.filter(searches__validated=True)

class InitiativeAlerts():
    @staticmethod
    def get_all():
        return InitiativeAlert.objects()

    @staticmethod
    def clear():
        InitiativeAlert.drop_collection()

    @staticmethod
    def by_search(search, kb):
        query = search
        query['tagged.knowledgebase'] = kb
        return InitiativeAlert.objects(
            __raw__=query
        )

