N = int(input())  # 전체 사람의 수
p = [list(map(int, input().split())) for _ in range(N)]
rank = [1 for _ in range(N)]
for r in range(N):
    for i in range(N):
        if p[r][0] < p[i][0] and p[r][1] < p[i][1]:
            rank[r] += 1
print(*rank)
