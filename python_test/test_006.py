def solution(a, b):
    answer = 0
    for x, y in zip(a, b):
        print(x, y)
        answer += x * y
    return answer

solution([1,2,3,4], [-3,-1,0,2])