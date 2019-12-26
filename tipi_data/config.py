MONGO_DB = 'tipidb'
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USER = ''
MONGO_PASSWORD = ''

try:
    from local_config import *
except:
    pass
