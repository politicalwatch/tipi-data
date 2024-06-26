from mongoengine import NotUniqueError
from mongoengine.queryset import DoesNotExist

from tipi_data.models.initiative import Initiative
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

    @staticmethod
    def create_alert(initiative: Initiative, reason: str = ''):
        try:
            prev = InitiativeAlert.objects().get(id=initiative['id'])
            reason = prev['reason']
        except DoesNotExist:
            pass

        initiative_alert = InitiativeAlert(
                id=initiative['id'],
                title=initiative['title'],
                reference=initiative['reference'],
                initiative_type=initiative['initiative_type'],
                initiative_type_alt=initiative['initiative_type_alt'],
                author_deputies=initiative['author_deputies'],
                author_parliamentarygroups=initiative['author_parliamentarygroups'],
                author_others=initiative['author_others'],
                place=initiative['place'],
                created=initiative['created'],
                updated=initiative['updated'],
                history=initiative['history'],
                status=initiative['status'],
                tagged=initiative['tagged'],
                url=initiative['url'],
                extra=initiative['extra'],
                reason=reason
                )
        try:
            initiative_alert.save()
        except Exception:
            pass
