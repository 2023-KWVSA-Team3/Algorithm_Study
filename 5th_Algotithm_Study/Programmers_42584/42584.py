def solution(prices):
    prices_enum = [[i, p] for i, p in enumerate(prices)]
    stack = [prices_enum[0]]
    maintain = [0] * len(prices)

    for i in range(1, len(prices)):
        for j in range(len(stack)):
            maintain[stack[j][0]] += 1
        while len(stack) != 0 and prices[i] < stack[-1][1]:
            stack.pop()
        stack.append(prices_enum[i])

    return maintain
