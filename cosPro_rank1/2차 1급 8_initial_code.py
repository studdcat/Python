def solution(arr):
    left, right = 0, len(arr) - 1
    idx = 0
    answer = [0 for _ in range(len(arr))]
    while left <= right:
        if idx % 2 == 0:
            answer[idx] = arr[left] # answer[1, 6, ] 
            left += 1               # left = 0, 1  right = 5, 4
        else:                       # idx = 0, 1, 2
            answer[idx] = arr[right]
            right -= 1
        idx += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
arr = [1, 2, 3, 4, 5, 6]
ret = solution(arr) # [1, 6, 2, 5, 3, 4]

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")