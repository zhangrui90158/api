import redis
from interface_framework.config.conf import redis_options

class MyRedis():
    def __init__(self):
        self.__redis = redis.StrictRedis(**redis_options)

    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        return

    def set(self,key,value):
        self.__redis.set(key,value)

if __name__ == '__main__':
    re = MyRedis()
    re.set("name","li")
    print(re.get("name"))