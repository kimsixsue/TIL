import sys

input = sys.stdin.readline
N = int(input())  # 사람
S, T = map(int, input().split())  # Source Target
M = int(input())  # 관계
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)
# BFS
distance = [-1] * (N + 1)  # 관계가 없을 때로 초기화
queue = [S]  # 시작
distance[S] += 1  # 거리 0부터 시작
while queue:
    s = queue.pop()
    for n in edge[s]:
        if distance[n] == -1:  # 첫 확인 시
            queue.append(n)
            distance[n] = distance[s] + 1  # 촌수
print(distance[T])
