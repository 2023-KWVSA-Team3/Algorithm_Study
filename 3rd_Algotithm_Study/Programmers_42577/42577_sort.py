def solution(phone_book):
    phone_book.sort()
    # 사전순으로 sort 후에 i번째 전화번호가 i+1번째 전화번호의 접두사라면, filter를 통해 i 값이 리스트에 저장된다.
    # 즉 아래 결과의 리스트가 비어있으면 어떤 번호가 다른 번호의 접두어가 아니라는 것을 의미한다. 따라서 리스트가 비어있는 경우에 True를 반환한다.
    return len(list(filter(lambda i: phone_book[i+1].startswith(phone_book[i]), range(len(phone_book)-1)))) == 0