# 밀러 라빈 소수 판정법을 이용한 풀이
# 내장 함수 없이 직접 구현했지만, 내장 함수 사용시 약간 더 빠르게 동작한다.

# 순열을 중복없이 구한다.
# itertools 라이브러리를 사용해도 된다.
def permutations(arr, n):
    perm = []
    if n == 0:
        return perm

    arr_set = list(set(arr))
    for i in range(len(arr_set)):
        copy = arr[:]
        copy.remove(arr_set[i])

        postfixs = permutations(copy, n-1)
        if not postfixs:
            perm.append(arr_set[i])
        for postfix in postfixs:
            perm.append(arr_set[i] + postfix)

    return perm


# 분할과 정복을 이용해 a^n % p를 O(log n)에 구한다.
# 내장 함수 pow()를 사용해도 된다.
def get_pow(a, n, p):
    if n == 1:
        return a % p
    half_square = get_pow(a, n//2, p) ** 2 % p

    if n & 1 == 0:
        return half_square
    return half_square * a % p


# 밀러 라빈 소수 판별법으로 n이 소수인지 테스트한다.
# a^d % n == 1 -> n은 소수
# a^(d*2^r) % n == n-1 -> n은 소수
# 여기서 n-1 = d * 2^s 을 만족하는 홀수 d이다. 그리고 0 <= r < s 이다.
def miller_rabin(n, a):
    d = n-1
    s = 0

    # 먼저 d를 구한다.
    while d % 2 == 0:
        d >>= 1
        s += 1

    # temp = a^d % n = a^(d*2^0) % n
    temp = get_pow(a, d, n)
    if temp == 1 or temp == n-1:
        return True

    # r=0에 대해서 확인했으므로 1 <= r < s에 대해서 확인해본다.
    for _ in range(s-1):
        temp = get_pow(temp, 2, n)
        if temp == n-1:
            return True

    return False


def solution(numbers):
    count = 0
    num_set = set()
    # int 범위에서는 밑의 a들로만 테스트해도 소수라는 것을 확신할 수 있다.
    test_a = [2, 7, 61]

    # 밀러 라빈으로 소수인지 판단할때 짝수는 pass하기 때문에 만약 2가 존재한다면 count를 1 증가시켜준다.
    if '2' in list(numbers):
        count += 1

    # numbers로 만들 수 있는 순열을 모두 구한다.
    for n in range(1, len(numbers)+1):
        for num in permutations(list(numbers), n):
            num = int(''.join(num))

            # 짝수이거나 1이면 pass
            if num & 1 == 0 or num == 1:
                continue
            num_set.add(num)

    # 순열로 구한 수가 소수인지 확인해 본다.
    for num in num_set:
        is_prime = True

        for a in test_a:
            if not miller_rabin(num, a):
                is_prime = False
                break

        # num 자체가 test_a에 포함된 경우 밀러 라빈은 False를 반환한다.
        # 그런데 test_a는 소수이기 때문에 num이 test_a에 포함되는 경우 count를 1 증가시킨다.
        if is_prime or num in test_a:
            count += 1

    return count


'''
from itertools import permutations

# 루트 n까지만 확인한다.
def is_prime(n):
    sqrt = int(n ** 0.5) + 1
    for i in range(2, sqrt):
        if n % i == 0:
            return False

    return True
    
def solution(numbers):
    count = 0
    num_set = set()

    # 짝수는 pass하기 때문에 만약 2가 존재한다면 count를 1 증가시켜준다.
    if '2' in list(numbers):
        count += 1

    # numbers로 만들 수 있는 순열을 모두 구한다.
    for n in range(1, len(numbers)+1):
        for num in permutations(list(numbers), n):
            num = int(''.join(num))

            # 짝수이거나 1이면 pass
            if num & 1 == 0 or num == 1:
                continue
            num_set.add(num)

    # 순열로 구한 수가 소수인지 확인해 본다.
    for num in num_set:
        if is_prime(num):
            count += 1

    return count
'''