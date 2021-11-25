# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(phrases, second):
    ret = ""
    lst = ["_" for x in range(len(phrases))]

    for z in phrases:
        lst.append(z)

    for y in range(second):
        lst = lst[1:] + lst[0]
    
    for a in range(14):
        ret = "".join(lst[a])
    answer = ret
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")