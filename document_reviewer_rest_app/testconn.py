"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-13251.crce182.ap-south-1-1.ec2.redns.redis-cloud.com',
    port=13251,
    decode_responses=True,
    username="default",
    password="Pr790xdcjtj1HWdIvygcnDvZGtBwWzxd",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

