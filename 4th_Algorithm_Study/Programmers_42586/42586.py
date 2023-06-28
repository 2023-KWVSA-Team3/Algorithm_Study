from math import ceil
def solution(progresses, speeds):
    # 각 작업의 배포까지 남은 일자를 계산해서 리스트로 저장한다.
    days = [ceil((100 - p)/s) for p, s in zip(progresses, speeds)]

    # days의 원소를 순회하며 가장 긴 배포일자를 계속해서 업데이트 한다.
    max_day = days[0]
    # 긱 배포마다 몇개의 기능이 배포 되는지를 저장한다. 따라서 처음 배포에 0개의 기능을 배포하는 것으로 초기화 한다.
    answer = [0]

    for day in days:
        # day가 max_day보다 크면 해당 기능은 새로 배포해야 한다.
        # 따라서 max_day를 새로 업데이트 하고, 새로운 배포에 해당 기능을 배포하므로 answer에 1을 추가한다.
        if day > max_day:
            max_day = day
            answer.append(1)
        # day가 max_day보다 작거나 같으면, 앞에서 max_day를 업데이트 시킨 기능과 함께 배포된다. 따라서 answer의 마지막 원소를 1 증가시킨다.
        else:
            answer[-1] += 1

    return answer