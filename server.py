import psycopg2
import redis
import logging
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_session import Session
from api import routes

# Redis = redis.StrictRedis(host='localhost', port=6379, db=0)
app = Flask(__name__)
SECRET_KEY = b'\xadLh\x18F\x90\x08\xb2\xc1\xf4J\xd7\xa5\xb2\x9ch'
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

api = Api(app)
cors = CORS(app, supports_credentials=True)
logging.getLogger('flask_cors').level = logging.DEBUG
conn = psycopg2.connect(dbname='dogz', user='dogz', password='dogz', host='localhost', port='5432')

for route in routes.routes:
    api.add_resource(*route)

if __name__ == '__main__':
    api.run(debug=True)