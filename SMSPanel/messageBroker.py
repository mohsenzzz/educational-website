from redis import Redis



client= Redis('192.168.56.16','6379')
phone_numbers = list()

def push_value(queue, value):
    try:
        client.lpop(queue)
        client.rpush(queue, value)
        return True
    except:
        return f'{value} does not push to {queue}'


def pop_value(queue):
        phone_numbers =client.blpop(queue)
        return phone_numbers

