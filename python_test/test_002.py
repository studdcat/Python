def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int("".join(numbers)))

ret =solution([3, 30, 34, 5, 9])
print(ret)

# [3, 30, 34, 5, 9]
# 333, 303030, 343434, 555, 999
# 33, 30, 34, 5, 9
# 9, 5, 34, 33, 30