def solution(s):
    check = []
    for c in s:
        if not check and c == ')':
            return False
        elif c == '(':
            check.append('(')
        else:
            check.pop()

    return len(check) == 0