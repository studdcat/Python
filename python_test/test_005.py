from tkinter import Y


def solution(numbers):
    answer = 0
    sum = 0

    for x in numbers:
        sum += x

    answer = 45 - sum
    return answer

ret = solution([5,8,4,0,6,7,9])
print(ret)