def solution(n):
    answer = ''
    count = 0
    lst = []

    lst[count] += 


    if n % 3 == 0:
        answer += str(4)
    elif n % 3 == 2:
        answer += str(2)
    elif n % 3 == 1:
        answer += str(1)

    while(n > 3):
        n -= 3
        count += 1

    if count % 3**count == 0:
        answer += str(4)
    elif count % 3**count == 2:
        answer += str(2)
    elif count % 3**count == 1:
        answer += str(1)

    return answer

print(solution(7))

20 / 3 = 6     13 / 3 = 4
6 / 3 = 2
18 / 3 0

     200    201  202
122  124    141  142