def solution(phone_book):
    phone_hash = {}
    n = 1
    # 전화번호 최대길이 저장
    max_len = len(max(phone_book, key=len))

    while n < max_len:
        # 매 루프마다 길이가 n인 전화번호를 hash table에 넣는다.
        for phone_num in phone_book:
            if len(phone_num) == n:
                phone_hash[phone_num] = 1

        # 길이가 n인 전화번호를 모두 넣었으면, 해당 전화번호가 접두사인 번호가 있는지 찾는다. 만약 있으면 False를 반환한다.
        for phone_num in phone_book:
            if len(phone_num) > n and phone_num[0:n] in phone_hash:
                return False

        n += 1

    # 모든 전화번호를 hash table에 넣었음에도 접두사인 번호가 없다면 True를 반환한다.
    return True
