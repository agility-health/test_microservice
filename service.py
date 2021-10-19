from flask import Flask
from redis import Redis
import os
from sqlalchemy import create_engine


REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')


app = Flask(__name__)

r = Redis(host=REDIS_HOST, port=6379, db=0)


@app.route('/test')
def main_route():
    r.xadd('mystream', {'l': 1})
    return "Hello world"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
