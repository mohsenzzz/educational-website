from redis import Redis
client = Redis(host='192.168.56.16', port=6379)

def push_value(name, value):
    try:

        client.rpush(name, value)
        return True
    except:
        return f'{value} does not push to {name}'


def pop_value(name):
    try:
        code = client.blpop(name,timeout=30)
        return code
    except:
        return f'there is not code in {name}'