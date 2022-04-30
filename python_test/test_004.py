from tkinter import X


def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]

    for idx, ans in enumerate(answers):

        if ans == p1[idx % len(p1)]:
            scores[0] += 1

        if ans == p2[idx % len(p2)]:
            scores[1] += 1

        if ans == p3[idx % len(p3)]:
            scores[2] += 1

    for idx, x in enumerate(scores):

        if x == max(scores):
            answer.append(idx + 1)

    return answer

ret = solution([1,3,2,4,2])
print(ret)