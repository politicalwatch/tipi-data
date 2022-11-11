from tipi_data.models.voting import Voting
from tipi_data.models.voting import Voting, TotalsVotes, ByDeputy, GroupVote, ByGroup
from tipi_data.repositories.parliamentarygroups import ParliamentaryGroups
from tipi_data.utils import generate_id


class Votings():
    @staticmethod
    def get_by(reference):
        return Voting.objects(reference=reference)

    @staticmethod
    def get_totals_votes(data):
        totals = data.get('totales')
        return TotalsVotes(
            present=totals.get('presentes'),
            skip=totals.get('noVotan'),
            yes=totals.get('afavor'),
            no=totals.get('enContra'),
            abstention=totals.get('abstenciones')
            )

    @staticmethod
    def get_votes_by_deputies(data):
        votes = data.get('votaciones')
        deputies_votes = list()
        for vote in votes:
            deputy_vote = ByDeputy(
                    name=vote.get('diputado'),
                    seat=vote.get('asiento'),
                    group=vote.get('grupo'),
                    vote=vote.get('voto')
                    )
            deputies_votes.append(deputy_vote)
        return deputies_votes

    @staticmethod
    def get_votes_by_group(data):

        VOTE_MAP = {
                'Sí': 'yes',
                'No': 'no',
                'Abstención': 'abstention',
                'No vota': 'skip'
                }

        def get_group_index(lst, val):
            for i, d in enumerate(lst):
                if d['name'] == val:
                    return i
            return -1

        group_votes = [
                ByGroup(
                    name=group['shortname'],
                    votes=GroupVote(
                        yes=0,
                        no=0,
                        abstention=0,
                        skip=0
                        )
                    )
                for group in ParliamentaryGroups.get_all()
                ]

        votes = data.get('votaciones')
        for vote in votes:
            group = vote.get('grupo')
            group_index = get_group_index(group_votes, group)
            if group_index == -1:
                continue
            group_votes[group_index]['votes'][VOTE_MAP[vote['voto']]] += 1

        return group_votes

    @staticmethod
    def save(reference, data):
        votes = Voting()
        information = data.get('informacion')
        votes['id'] = generate_id(
                reference,
                information.get('textoExpediente') + '\n' + information.get('tituloSubGrupo'))
        votes['reference'] = reference
        votes['title'] = information.get('textoExpediente')
        votes['subgroup_text'] = information.get('textoSubGrupo')
        votes['subgroup_title'] = information.get('tituloSubGrupo')

        votes['totals'] = Votings.get_totals_votes(data)
        votes['by_deputies'] = Votings.get_votes_by_deputies(data)
        votes['by_groups'] = Votings.get_votes_by_group(data)

        votes.save()
