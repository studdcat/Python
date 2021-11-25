# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(s1, s2):
    s1_val = []
    s2_val = []
    length_a = len(s1) + len(s2)
    length_b = len(s2) + len(s1)

    for x in range(len(s1)):
        s1_val.insert(0, s1[-x -1])
        s2_val.append(s2[x])
        if s1_val == s2_val:
            length_a -= len(s1_val)

    s1_val = []
    s2_val = []

    for y in range(len(s1)):
        s2_val.insert(0, s2[-y -1])
        s1_val.append(s1[y])
        print(s2_val, s1_val)
        if s2_val == s1_val:
            length_b -= len(s2_val)

    if length_a >= length_b:
        length = length_b
    else:
        length = length_a

    answer = length
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")