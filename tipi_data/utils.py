import hashlib
from slugify import slugify


def generate_id(*args):
    try:
        return hashlib.sha1(
                u''.join(args).encode('utf-8')
                ).hexdigest()
    except Exception:
        return 'ID_ERROR'

def generate_slug(*args):
    return slugify(u''.join(args).encode('utf-8'))
