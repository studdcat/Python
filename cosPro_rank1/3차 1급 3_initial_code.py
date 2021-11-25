#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(bishops):
    cnt = 0
    x = 0
    chess = [[0 for x in range(8)] for x in range(8)]

    for y in range(len(bishops)):
        dx = ord(bishops[y][0]) - ord("A")
        dy = ord(bishops[y][1]) - ord("1")

        chess[dx][dy] += 1

        for x in range(8):
            dx = dx + 1
            dy = dy + 1
            if dx >= 0 and dx < 8 and dy >=0 and dy < 8:
                chess[dx][dy] += 1

        dx = ord(bishops[y][0]) - ord("A")
        dy = ord(bishops[y][1]) - ord("1")

        for x in range(8):
            dx = dx + 1
            dy = dy - 1
            if dx >= 0 and dx < 8 and dy >=0 and dy < 8:
                chess[dx][dy] += 1

        dx = ord(bishops[y][0]) - ord("A")
        dy = ord(bishops[y][1]) - ord("1")

        for x in range(8):
            dx = dx - 1
            dy = dy - 1
            if dx >= 0 and dx < 8 and dy >=0 and dy < 8:
                chess[dx][dy] += 1

        dx = ord(bishops[y][0]) - ord("A")
        dy = ord(bishops[y][1]) - ord("1")

        for x in range(8):
            dx = dx - 1
            dy = dy + 1
            if dx >= 0 and dx < 8 and dy >=0 and dy < 8:
                chess[dx][dy] += 1
          
    for x in chess:
        for y in x:
            if y == 0:
                cnt += 1
    answer = cnt
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")