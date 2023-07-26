# 최대 0.23ms
# 백준 1068과 유사

from collections import deque

def solution(n, wires):
    queue = deque()
    adj_list = [[] for _ in range(n+1)]
    parent = [0] * (n+1)
    remain_child = [0] * (n+1)  # 부모는 자식의 자손 노드를 전부 더하는데, 아직 더하지 않은 자식의 개수를 저장
    descendant_num = [1] * (n+1)  # 자신을 포함한 자손 노드 개수 저장(해당 노드를 루트노드로 하는 서브트리의 노드 개수와 같다.)
    visited = [False] * (n+1)  # bfs를 위한 방문 여부 check
    min_diff = n

    # 인접리스트 업데이트
    for i, j in wires:
        adj_list[i].append(j)
        adj_list[j].append(i)

    # 1번 노드를 루트로 삼는다.
    queue.append(1)
    visited[1] = True

    # bfs를 돌며 자식, 부모 정보를 업데이트 한다.
    while queue:
        node = queue.pop()

        for next in adj_list[node]:
            if not visited[next]:
                visited[next] = True
                remain_child[node] += 1
                parent[next] = node
                queue.append(next)

    # 리프노드를 먼저 remain에 넣어준다.
    for i in range(1, n+1):
        if remain_child[i] == 0:
            queue.append(i)

    # queue에는 자신을 포함한 자손 노드의 개수를 구한 노드만 넣는다.
    # queue에서 하나씩 빼서 해당 노드의 자손 노드 개수를 부모의 자손 노드 개수에  더한다.
    while queue:
        node = queue.popleft()
        # 부모의 자손 노드 개수 업데이트
        descendant_num[parent[node]] += descendant_num[node]
        remain_child[parent[node]] -= 1

        # node는 자손 노드의 개수를 다 구한 노드라면 정답을 구할 수 있다.
        # node와 부모 사이의 edge를 끊으면 node를 루트노드로 하는 서브트리의 노드 개수가 node의 자손 노드 개수와 같기 때문이다.
        min_diff = min(min_diff, abs(2 * descendant_num[node] - n))

        # 부모가 루트노드가 아니고, 부모의 자손 노드 개수가 업데이트가 완료된 경우에만 queue에 집어넣는다.
        if parent[node] != 1 and remain_child[parent[node]] == 0:
            queue.append(parent[node])

    return min_diff