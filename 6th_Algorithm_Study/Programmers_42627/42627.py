from heapq import heappop, heappush, heapify

def solution(jobs):
    # jobs를 PQ로 만든다.
    # 이때 우선순위는 요청 시점이 빠를수록 높다. 만약 요청 시점이 같다면 우선순위는 소요 시간이 짧을 수록 높다.
    heapify(jobs)

    # workable은 현재 바로 작업을 수행할 수 있는 jobs들을 모아놓는다.
    # 이 때 workable은 소요 시간을 기준으로 한 min heap이다.
    workable = []

    cur_time = 0 # 현재 시간을 저장한다.
    elapsed = [] # 각 작업의 요청부터 종료까지 걸린 시간을 저장한다.

    # workable에서 소요시간이 가장 짧은 작업을 꺼내서 해당 작업을 수행한다.
    # 작업을 하나 수행할 때마다 cur_time이 업데이트 되고, 이로인해 수행이 가능해진 jobs의 작업들을 빼서 workable에 집어 넣는다.
    while jobs:
        # 현재 수행 가능한 작업이 workable 뿐만 아니라 jobs에도 없는 경우 cur_time을 다음 작업 요청 시점으로 업데이트 한다.
        if not workable and cur_time < jobs[0][0]:
            cur_time = jobs[0][0]

        while jobs and cur_time >= jobs[0][0]:
            # workable에는 수행 시간 기준으로 min heap을 만들기 위해 reversed()를 취한다.
            # 즉 요청 시점과 수행 시간의 순서를 바꾼다.
            heappush(workable, list(reversed(heappop(jobs))))

        job_to_do = heappop(workable)
        cur_time += job_to_do[0]
        elapsed.append(cur_time - job_to_do[1])

    # jobs가 비면 이제 모든 작업이 수행 가능하므로 workable에 있는 모든 작업을 수행한다.
    for _ in range(len(workable)):
        job_to_do = heappop(workable)
        cur_time += job_to_do[0]
        elapsed.append(cur_time - job_to_do[1])

    return sum(elapsed) // len(elapsed)