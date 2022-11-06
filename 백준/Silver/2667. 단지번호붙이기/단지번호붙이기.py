import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # 정사각형 지도 크기

plan = [list(map(int, list(input()[:-1]))) for _ in range(N)]  # \n 제외
visited = [[False] * N for _ in range(N)]  # 1은 집이 있는 곳
delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
comp_num = list()  # 각 단지내 집 수
comp = -1
queue = deque()
while True:
    for row in range(N):
        for col in range(N):
            if plan[row][col] and not visited[row][col]:  # 1
                queue.append((row, col))
                visited[row][col] = True
                comp += 1  # 단지 번호
                comp_num.append(1)  # 새 단지의 첫 집
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in delta:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and plan[nr][nc] and not visited[nr][nc]:
                            queue.append((nr, nc))
                            visited[nr][nc] = True
                            comp_num[comp] += 1  # 새 단지내 집의 수 증가
    break  # 순회 완료
print(len(comp_num))  # 총 단지 수
comp_num.sort()  # 오름차순으로 정렬
for _ in comp_num:  # 각 단지내 집의 수
    print(_)
