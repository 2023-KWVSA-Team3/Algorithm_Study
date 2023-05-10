from math import ceil
def solution(progresses, speeds):
    days = [ceil((100 - p)/s) for p, s in zip(progresses, speeds)]

    max_day = days[0]
    answer = [0]

    for day in days:
        if day > max_day:
            max_day = day
            answer.append(1)
        else:
            answer[-1] += 1

    return answer