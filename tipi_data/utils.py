import hashlib


def generate_id(*args):
    try:
        return hashlib.sha1(
                u''.join(args).encode('utf-8')
                ).hexdigest()
    except Exception:
        return 'ID_ERROR'
