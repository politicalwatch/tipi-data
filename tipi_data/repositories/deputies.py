from datetime import datetime

from tipi_data.models.deputy import Deputy


class Deputies:
    @staticmethod
    def get_all():
        return Deputy.objects()

    @staticmethod
    def get_total(group):
        return Deputy.actives(
                parliamentarygroup=group
                ).count()

    @staticmethod
    def get_total_females(group):
        return Deputy.actives(
                parliamentarygroup=group,
                gender='Mujer'
                ).count()

    @staticmethod
    def get_total_males(group):
        return Deputy.actives(
                parliamentarygroup=group,
                gender='Hombre'
                ).count()

    @staticmethod
    def get_total_under_35(group):
        return Deputy.actives(
                parliamentarygroup=group,
                age__lt=35
                ).count()

    @staticmethod
    def get_total_between_35_and_49(group):
        return Deputies.get_total_between_ages(group, 35, 49)

    @staticmethod
    def get_total_between_50_and_65(group):
        return Deputies.get_total_between_ages(group, 50, 65)

    @staticmethod
    def get_total_between_ages(group, gt, lt):
        return Deputy.actives(
                parliamentarygroup=group,
                age__gte=gt,
                age__lte=lt,
                ).count()

    @staticmethod
    def get_total_over_65(group):
        return Deputy.actives(
                parliamentarygroup=group,
                age__gt=65
                ).count()

    @staticmethod
    def get_birthdays():
        pipeline = [
                { '$addFields': {
                    'birthDay': { '$dayOfMonth': '$birthdate' },
                    'birthMonth': { '$month': '$birthdate' },
                    'todayDay': { '$dayOfMonth': datetime.today() },
                    'todayMonth': { '$month': datetime.today() }
                    }
                 },
                { '$match': {
                    '$expr': {
                        '$and': [
                            { '$eq': ['$birthDay', '$todayDay'] },
                            { '$eq': ['$birthMonth', '$todayMonth'] }
                            ]
                        }
                    }
                 }
                ]
        return Deputy.actives().aggregate(*pipeline)
