import redis
import os


# Do something with .dbdata folder
REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')


r = redis.Redis(host=REDIS_HOST, port=6379, db=0)
stream_name = 'mystream'
while True:
    event = r.xread({stream_name: b"0-0"})
    print(event)


