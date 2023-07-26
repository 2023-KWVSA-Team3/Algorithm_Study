# 이분 탐색으로 푼 풀이(브루트 포스나 yellow의 약수를 찾는 것보다 효율적(O(log brown))

# x * y = brown + yellow
# x + y = (brown + 4)//2

# x + y 에서 x, y를 정한다. 이때 x와 y의 차가 작을 수록 그 곱은 더 커진다.
# 이를 이용해서 이분 탐색으로 그 차의 크기를 조절해서 답을 구한다.

# x < y 라고 하면, x는 1 ~ (x+y)//2 의 값을 가진다.
def solution(brown, yellow):
    m = brown + yellow
    s = (brown + 4) // 2

    # x가 가질 수 있는 최대값
    diff = (s // 2)

    # x가 가질 수 있는 최대값의 절반
    x = diff // 2
    y = s - x
    diff //= 2

    while x * y != m:
        if diff != 1:
            diff //= 2

        if x * y > m:
            x -= diff
            y += diff

        else:
            x += diff
            y -= diff

    return [y, x]


'''
# 근의 공식으로 푼 풀이(O(1))

# x * y = brown + yellow
# (x-2) * (y-2) = yellow
# x * y - brown = x * y - 2x - 2y + 4
# 2x + 2y = brown + 4

# x * y = brown + yellow
# x + y =  brown//2 + 2

# y = brown//2 + 2 - x
# x * (brown//2 + 2 - x) = brwon + yellow

# x^2 - (brown + 4)//2 * x + (brown + yellow)
# 위 방정식에서 얻은 두 근이 정답이다.
def solution(brown, yellow):
    b = (brown + 4) // 2
    c = brown + yellow

    answer = [(b + int((b ** 2 - 4 * c) ** 0.5)) // 2, (b - int((b ** 2 - 4 * c)) ** 0.5) // 2]

    return answer
'''