def solution(absolutes, signs):
    answer = 0
    for abs, sig in zip(absolutes, signs):
        if sig:
            answer += abs
        else:
            answer -= abs
    return answer

ret = solution([4,7,12], ["true","false","true"])
print(ret)


