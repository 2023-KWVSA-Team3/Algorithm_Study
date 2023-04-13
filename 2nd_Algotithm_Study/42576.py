def solution(participant, completion):
    participant.sort()
    completion.sort()

    # 완주하지 못한 선수가 중간에 있을 경우
    for p, c in zip(participant, completion):
        if p != c:
            return p
    # 완주하지 못한 선수가 맨 마지막에 있을 경우
    return participant[-1]