import hashlib
from slugify import slugify
from uuid import uuid4


def generate_id(*args):
    try:
        return hashlib.sha1(
                u''.join(args).encode('utf-8')
                ).hexdigest()
    except Exception:
        return 'ID_ERROR'

def generate_slug(*args):
    return "{}-{}".format(
            slugify( u''.join(args).encode('utf-8')),
            str(uuid4()).split('-')[0])
