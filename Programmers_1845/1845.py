def solution(nums):
	# N/2와 포켓몬 종류의 수 중 작은 값 반환
	# dict 대신 set이나 Counter 사용 가능
	return min(len(nums) // 2, len(dict.fromkeys(nums, 0)))
