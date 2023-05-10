def solution(s):
    # stack의 역할을 하는 리스트이다.
    check = []
    for c in s:
        if not check and c == ')':
            return False
        elif c == '(':
            check.append('(')
        else:
            check.pop()

    return len(check) == 0