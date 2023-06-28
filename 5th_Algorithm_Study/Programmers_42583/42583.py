from collections import deque

def solution(bridge_length, weight, truck_weights):
    wait = deque([i, w] for i, w in enumerate(truck_weights))
    on_bridge = deque()
    remain_length = [bridge_length + 1] * len(truck_weights)
    answer = 0

    while wait:
        seconds = 1
        if weight - wait[0][1] < 0 or len(on_bridge) >= bridge_length:
            seconds = remain_length[on_bridge[0]]
            weight += truck_weights[on_bridge.popleft()]
        for i in on_bridge:
            remain_length[i] -= seconds
        if weight - wait[0][1] >= 0:
            on_bridge.append(wait[0][0])
            weight -= wait[0][1]
            wait.popleft()
            remain_length[on_bridge[-1]] -= 1
        if remain_length[on_bridge[0]] == 0:
            weight += truck_weights[on_bridge.popleft()]
        answer += seconds

    return answer + remain_length[-1]
