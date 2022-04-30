def solution(nums):
    answer = 0
    return min( len(nums)/2, len(set(nums)) )

def solution(nums):
    kind = []
    answer = int(len(nums)/2) # 3
    for num in nums:
        if num not in kind:
            kind.append(num)
    result = len(kind) if answer > len(kind) else answer 
    return result
    
def solution(nums):
    answer = 0
    myList = set(nums)
    if len(nums)/2 > len(myList):
        answer = len(myList)
    else:
        answer = len(nums)/2
    return answer

print(solution([3,3,3,2,2,2]))