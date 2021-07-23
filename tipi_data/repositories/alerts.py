from tipi_data.models.alert import InitiativeAlert


class Alerts():
    @staticmethod
    def get_all():
        return InitiativeAlert.objects()
