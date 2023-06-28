import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville) # min heap으로 만든다.

    while len(scoville) > 1 and scoville[0] < K:
        lowest = heapq.heappop(scoville)
        lowest_2nd = heapq.heappop(scoville)
        heapq.heappush(scoville, lowest + lowest_2nd * 2)

        count += 1

    # scoville에 음식이 하나만 남았는데 K보다 작은 경우 더이상 음식을 섞을 수 없다.
    if scoville[0] < K:
        return -1

    return count
