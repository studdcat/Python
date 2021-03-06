#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(commands):
    dict = {"L":-1, "R":1, "U":1, "D":-1}
    val = [0,0]
    for i in commands:
        if i == "L" or i == "R":
            val[0] += dict[i]
        elif i == "U" or i == "D":
            val[1] += dict[i]
    answer = val
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")