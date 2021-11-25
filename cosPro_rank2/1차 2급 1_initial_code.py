#You may use import as below.
#import math

def solution(shirt_size):
    
    lst = [0 for a in range(6)]
    
    for a in shirt_size:
        if a == "XS":
            lst[0] += 1
        elif a == "S":
            lst[1] += 1
        elif a == "M":
            lst[2] += 1
        elif a == "L":
            lst[3] += 1
        elif a == "XL":
            lst[4] += 1
        elif a == "XXL":
            lst[5] += 1
        
    answer = lst
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")