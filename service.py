from flask import Flask
from redis import Redis
import os
from producer import Producer
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
prod = Producer("mystream", host=REDIS_HOST, port=6379, db=0)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/test'
CORS(app)

db = SQLAlchemy(app)
r = Redis(host=REDIS_HOST, port=6379, db=0)


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(256))


@app.route('/test')
@prod.event('get', {'datetime': str(datetime.datetime.now())})
def main_route():
    return "Hello world"


@app.route('/info')
def get_database_info():
    db_info = Event.query.all()
    all_info = []
    for event in db_info:
        all_info.append(event.info)

    return str(all_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
