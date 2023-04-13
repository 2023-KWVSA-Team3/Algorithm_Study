def solution(nums):
    poncketmon = len(nums) // 2
    
    answer = list(set(nums))
    
    if len(answer) > poncketmon:
        return poncketmon
    else:
        return len(answer)