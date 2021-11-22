def solution(arr, K):
    n = len(arr)
    count = 0
    for p in range(0, n):
        for q in range(p + 1, n):
            for r in range(q + 1, n):
                print(r)
                if (arr[p] + arr[q] + arr[r]) % K == 0:
                    count += 1
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")