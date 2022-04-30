def solution(array, commands):
    answer = []
    for x in commands:
        a, b, c = x
        val = sorted(array[a - 1 : b])
        
        answer.append(val[c - 1])
    
    return answer

ret1 = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(ret1)