from time import localtime

tm = localtime()
start_day = "%d-01-01"%tm.tm_year
elapsed_day = tm.tm_yday
print("오늘은 [{}]이후 [{}]일째 되는 날입니다.".format(start_day, elapsed_day))