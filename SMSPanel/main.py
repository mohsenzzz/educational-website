from random import randint


from messageBroker import pop_value, push_value, phone_numbers, client

if __name__ == '__main__':
    print('start redis')

    while True:
        phone = pop_value('phone')
        code = randint(12345,98765)
        print(code)
        phone = phone[1].decode('utf-8')
        push_value(phone,code)
      # value = pop_value('phone')
      # print(value)