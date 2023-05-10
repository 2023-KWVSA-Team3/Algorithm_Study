def solution(arr):
    # 첫번째 원소를 먼저 집어 넣는다.
    answer = [arr[0]]
    # i번째와 i-1번째 원소가 다르다면 두 원소는 연속되지 않은 것을 의미한다. 따라서 i번째 원소를 추가한다.
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer