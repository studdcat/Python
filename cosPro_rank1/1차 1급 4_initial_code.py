#You may use import as below.
#import math

def solution(num):
    # Write code here.
    answer = 0
    answer = num + 1
    for x in range(answer):
        answer = str(answer).replace("0", "1")
    return int(answer)


#The following is code to output testcase.
num = 9949999
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".") # 9951111 