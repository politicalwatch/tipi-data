from tipi_data.models.parliamentarygroup import Gender, \
        Ages, \
        ParliamentaryGroupComposition, \
        ParliamentaryGroup
from tipi_data.repositories.deputies import Deputies


class ParliamentaryGroups:
    @staticmethod
    def get_all():
        return ParliamentaryGroup.objects()

    @staticmethod
    def get_composition(short_group):
        return ParliamentaryGroupComposition(
                deputies=Deputies.get_total(short_group),
                gender=Gender(
                    female=Deputies.get_total_females(short_group),
                    male=Deputies.get_total_males(short_group)
                    ),
                ages=Ages(
                    under35=Deputies.get_total_under_35(short_group),
                    between35and49=Deputies.get_total_between_35_and_49(short_group),
                    between50and65=Deputies.get_total_between_50_and_65(short_group),
                    over65=Deputies.get_total_over_65(short_group)
                    )
                )
