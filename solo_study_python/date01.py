import datetime

now = datetime.datetime.now()

print("{0}년 {1}월 {2}일 {3}시 {4}분 {5}초".format(now.year, now.month, now.day,
                                             now.hour, now.minute, now.second))
