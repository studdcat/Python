#You may use import as below.
#import math

def solution(pos):
    mx = [1, 2, 2, 1, -1, -2, -2, -1]
    my = [2, 1, -1, -2, -2, -1, 1, 2]
    dx = ord(pos[0]) - ord("A")
    dy = ord(pos[1]) - ord("1")
    count = 0

    for x in range(8):
        if 0 <= dx + mx[x] < 8 and 0 <= dy + my[x] < 8:
            count += 1
    answer = count
    return answer
    
#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")