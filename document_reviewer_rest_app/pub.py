import json
import redis
from django.conf import settings

redis_client = redis.StrictRedis(host=settings.REDIS_CONNECTION_PARAMS['host'], port=settings.REDIS_CONNECTION_PARAMS['port'], db=settings.REDIS_CONNECTION_PARAMS['db'],username=settings.REDIS_CONNECTION_PARAMS['username'],password=settings.REDIS_CONNECTION_PARAMS['password'])
def publish_data_on_redis(json_data, channel_name):
    redis_client.publish(channel_name, json.dumps(json_data))