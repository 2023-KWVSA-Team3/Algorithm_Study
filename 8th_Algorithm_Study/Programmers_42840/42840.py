def solution(answers):
    num = range(len(answers))

    a = len([i for i in num if answers[i] == i % 5 + 1])

    seq = [1, 3, 4, 5]
    b = len([i for i in num if (i%2 == 0 and answers[i] == 2) or (i%2 == 1 and answers[i] == seq[(i//2) % 4])])

    seq = [3, 1, 2, 4, 5]
    c = len([i for i in num if answers[i] == seq[(i//2) % 5]])

    correct = [a, b, c]
    return list(filter(lambda i: correct[i-1] == max(correct), range(1, 4)))