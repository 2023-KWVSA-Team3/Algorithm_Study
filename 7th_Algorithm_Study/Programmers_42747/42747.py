from itertools import takewhile

def solution(citations):
    citations.sort()
    n = len(citations)

    # 뒤에서부터 h번째 논문이 h번 이상 인용 되었다면 h번 이상 인용된 논문이 최소 h개 존재한다는 것이다.
    # 왜냐하면 citations는 정렬되어있기 때문에 뒤에서부터 h-1번째, h-2번째, ... 1번째 논문들도 h번 이상 인용된 것이기 떄문이다.
    answer = list(takewhile(lambda h: h <= citations[-h], range(1, n+1)))

    return len(answer)