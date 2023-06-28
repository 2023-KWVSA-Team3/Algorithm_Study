from heapq import heappop, heappush, heapify

# heap에서 최대값을 찾아 마지막 리프노드와 swap한다.
# 그 후 마지막 리프노드를 삭제한 뒤 heapify_up을 한다.
def heap_remove_max(heap):
    k = 0
    index = 0
    max_item = heap[0]
    max_index = 0

    # 효율성을 위해 리프노드에서만 최대값을 찾았다. 그냥 max()를 이용해도 된다.
    while True:
        if len(heap) <= 2**(k+1) - 1:
            index = 2 ** k - 1
            break
        k += 1

    for i in range(index, len(heap)):
        if max_item < heap[i]:
            max_item = heap[i]
            max_index = i

    # swap후 마지막 리프노드 제거
    heap[-1], heap[max_index] = heap[max_index], heap[-1]
    heap.pop()

    # heapify_up
    while max_index > 0 and max_index < len(heap):
        parent = (max_index - 1) // 2
        if heap[parent] > heap[max_index]:
            heap[parent], heap[max_index] = heap[max_index], heap[parent]
            max_index = parent
        else:
            break


def solution(operations):
    pq = []
    for op in operations:
        if op[0] == 'I':
            heappush(pq, int(op[2:]))
        elif not pq:
            continue
        elif op[2] == '1':
            heap_remove_max(pq)
        else:
            heappop(pq)

    min_item, max_item = 0, 0

    if pq:
        max_item = max(pq)
        min_item = pq[0]

    return [max_item, min_item]

''' 
# deque와 bisect 라이브러리를 이용한 풀이

from collections import deque
from bisect import insort
def solution(operations):
    dq = deque()

    for op in operations:
        if op[0] == 'I':
            insort(dq, int(op[2:]))
        elif not dq:
            continue
        elif op[2] == '1':
            dq.pop()
        else:
            dq.popleft()

    min_item, max_item = 0, 0

    if dq:
        max_item = dq[-1]
        min_item = dq[0]

    return [max_item, min_item]
'''
