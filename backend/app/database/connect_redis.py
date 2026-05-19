import redis

redis_client = None

def connect_redis():

    global redis_client

    try:
        redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
        redis_client.pint()

        print("Redis connected successfully")
        
    except Exception as e:
        print("Error in connecting to db and exception is: ", e)