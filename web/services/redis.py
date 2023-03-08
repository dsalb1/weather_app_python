import time
import json
import redis

r = redis.Redis(host='redis', port=6379)


class Redis:
    def __init__(self):
        self.redis = r

    def get_dict(self, k):
        retries = 5
        while True:
            try:
                val = self.redis.get(k)
                if val:
                    val = json.loads(val)
                return val
            except redis.exceptions.ConnectionError as err:
                if retries == 0:
                    raise err
                retries -= 1
                time.sleep(0.5)

    def set_dict(self, k, v):
        self.redis.set(k, json.dumps(v), 30)
