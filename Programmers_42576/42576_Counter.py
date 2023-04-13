from collections import Counter

def solution(participant, completion):
    # Counter 함수를 이용해서 key는 이름, value는 동명이인의 수로 삼는다.
    # 그후 참여자 Counter에서 완주자 Counter를 빼면 완주하지 못한 사람 1명만 남게된다.
    return list((Counter(participant) - Counter(completion)))[0]

