import redis

r = redis.StrictRedis(host="127.0.0.1", port=6379, db=0, decode_responses=True, password='123456')

# 最后一项为自动解码
r.set('name', 'liu')

print(r.get('name'))
# 关闭链接

r.close()
