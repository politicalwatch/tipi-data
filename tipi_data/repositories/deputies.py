from tipi_data.models.deputy import Deputy


class Deputies:
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
        return Deputy.actives(
                parliamentarygroup=group,
                age__gte=35,
                age__lte=49,
                ).count()

    @staticmethod
    def get_total_between_50_and_65(group):
        return Deputy.actives(
                parliamentarygroup=group,
                age__gte=50,
                age__lte=65,
                ).count()

    @staticmethod
    def get_total_over_65(group):
        return Deputy.actives(
                parliamentarygroup=group,
                age__gt=65
                ).count()
