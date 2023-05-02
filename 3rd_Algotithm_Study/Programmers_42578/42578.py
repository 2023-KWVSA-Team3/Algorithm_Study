from collections import Counter
from functools import reduce


def solution(clothes):
    # 각 의상 종류당 옷의 수를 a, b, c, d라고 하면 전체 조합의 수는 (aC0 + aC1) * (bC0 + bC1) * (cC0 + cC1) * (dC0 + dC1) - 1 이다.
    # 각 의상 종류당 옷의 수는 Counter를 통해 구하고, 각 값을 reduce로 누적해서 곱하면 된다.
    return reduce(lambda x, y: x * y, [n+1 for n in Counter([row[1] for row in clothes]).values()]) - 1