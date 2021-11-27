#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(N, M):
    ret = 0
    dis = M - N
    for a in range(N, N+dis+1):
        if a % 2 == 0:
            ret += a*a
    answer = ret
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
N = 4
M = 7
ret = solution(N, M)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")