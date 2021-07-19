from tipi_data.models.initiative import Initiative


def get_initiatives(kb=None, query=None, limit=0, skip=0):
    if not kb:
        return Initiative.objects(__raw__=query).limt(limit).skip(skip)
    return Initiative.objects(
            tagged__match={
                'knowledgebase': kb,
                'topics': {'$not': {'$size': 0}}
                }
            ).filter(__raw__=query).limit(limit).skip(skip)
