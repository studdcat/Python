import datetime

now = datetime.datetime.now()

month = now.month

if 3 <= month <= 5:
    print("이번 달은 {0}월로 봄입니다!".format(now.month))

elif 6 <= month <= 8:
    print("이번 달은 {0}월로 여름입니다!".format(now.month))


elif 9 <= month <= 11:
    print("이번 달은 {0}월로 가을입니다!".format(now.month))

    
else: 
    print("이번 달은 {0}월로 겨울입니다!".format(now.month))
