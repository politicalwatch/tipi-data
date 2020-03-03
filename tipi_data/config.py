from os import environ as env


MONGO_HOST = env.get('MONGO_HOST', 'mongo')
MONGO_DB = env.get('MONGO_DB_NAME', 'tipidb')
MONGO_PORT = int(env.get('MONGO_PORT', '27017'))
MONGO_USER = env.get('MONGO_USER', 'tipi')
MONGO_PASSWORD = env.get('MONGO_PASSWORD', 'tipi')
