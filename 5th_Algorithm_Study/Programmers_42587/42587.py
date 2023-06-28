from collections import deque

def solution(priorities, location):
    dq = deque([[l, p] for l, p in enumerate(priorities)])
    for count in range(1, len(priorities) + 1):
        index = dq.index(max(dq, key=lambda x: x[1]))
        dq.rotate(-index)
        if dq[0][0] == location:
            return count
        dq.popleft()