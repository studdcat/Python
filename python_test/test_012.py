from collections import deque
def solution(progresses, speeds):
    answer = [0 for x in range(len(progresses))]
    count = [0 for x in range(len(progresses))]

    for x in range(len(progresses)):
        while(progresses[x] < 100):
            progresses[x] = progresses[x] + speeds[x]
            count[x] += 1
            
    
    max = count[0]
    a = 0
    for x in range(len(count)):
        if max < count[x+1]:
            answer[x] += 1
            max = count[x+1]

        if max > count[x+1]:
            a += 1



    return answer

print(solution([93, 30, 55], [1, 30, 5]))

# [93, 30, 55]	[1, 30, 5]	[2, 1]
# 7 3 9
# 5 10 1 1 20 1