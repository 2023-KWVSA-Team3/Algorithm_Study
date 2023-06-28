def solution(participant, completion):
    hash_table = {}

    # 참여자의 이름을 key 값으로 하고, 그에 대한 동명이인의 수를 value 값으로 삼는다.
    for part in participant:
        # 이름이 처음 나오면 0으로 초기화
        if part not in hash_table:
            hash_table[part] = 0
        hash_table[part] += 1

    # 완주자가 한명씩 나올때 마다 해당되는 key의 value 값을 1 감소시킨다.
    for comp in completion:
        hash_table[comp] -= 1
        # value 값이 0이면, 즉 해당 이름의 참여자가 모두 완주하면 hash table에서 삭제한다.
        if hash_table[comp] == 0:
            hash_table.pop(comp, None)

    # hash table에 남은 사람이 완주하지 못한 한명이므로 해당되는 key 값을 반환한다.
    return list(hash_table)[0]
