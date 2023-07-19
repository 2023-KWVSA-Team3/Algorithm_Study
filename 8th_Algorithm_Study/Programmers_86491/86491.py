# 먼저 가로는 모든 카드를 포함해야 하므로 모든 길이중 가장 긴 길이로 삼는다.
# 그러고나서 지갑의 크기를 줄이기 위해 자신의 길이중 짧은 길이를 세로로 삼아야 한다.(자신의 길이 중 긴 길이는 가로보다 짧거나 같기 때문에 들어갈 수 있다.)
# 따라서 각 명함의 짧은 길이들 중에서 가장 긴 길이를 세로로 삼는다.
def solution(sizes):
    sizes = [sorted(size) for size in sizes]
    max_w = max(sizes, key=lambda x: x[1])[1]
    max_h = max(sizes, key=lambda x: x[0])[0]

    return max_w * max_h