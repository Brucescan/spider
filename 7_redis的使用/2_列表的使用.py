import redis

r = redis.Redis(password='123456', decode_responses=True)

r.lpush('list', 1, 2, 3, 4)

print(r.lrange('list', 0, -1))

r.close()