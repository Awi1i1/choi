import random
print('trò chơi may mắn')

lev = input('chọn cấp độ - 1, 2, 3, 4, 5 ')

if lev == 1:
    cho = int(input('nhập số 1 - 3:\n'))
    mucTieu = random.randint(1,3)
    if cho == mucTieu:
        print('bạn thắng')
    else:
        print('bạn thua:')
elif lev == 2:
    cho = int(input('nhập số 1 - 5:\n'))
    mucTieu = random.randint(1,5)
    if cho == mucTieu:
        print('bạn thắng')
    else:
        print('bạn thua')
elif lev == 3:
    cho = int(input('nhập số 1 - 7:\n'))
    mucTieu = random.randint(1,7)
    if cho == mucTieu:
        print('bạn thắng')
    else:
        print('bạn thua')
elif lev == 4:
    cho = int(input('nhập số 1 - 10:\n'))
    mucTieu = random.randint(1,10)
    if cho == mucTieu:
        print('bạn thắng')
    else:
        print('bạn thua')
elif lev == 5:
    cho = int(input('nhập số 1 - 15:\n'))
    mucTieu = random.randint(1,15)
    if cho == mucTieu:
        print('bạn thắng')
    else:
        print('bạn thua')
else:
    print('gặp phải lỗi')
