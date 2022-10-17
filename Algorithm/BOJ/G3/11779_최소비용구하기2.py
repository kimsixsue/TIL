from heapq import heappush, heappop

n = int(input())  # 도시 1~  1000
m = int(input())  # 버스 1~100000
adj_list = [list() for _ in range(n + 1)]
for _ in range(m):  # 버스 비용 0~99999
    s, t, c = map(int, input().split())
    adj_list[s].append((t, c))  # undirected
start, goal = map(int, input().split())  # 출발, 도착
total = [100000001] * (n + 1)  # 최소비용
hq = list()
total[0], total[start] = 0, 0
heappush(hq, (0, start))
ancestor = [_ for _ in range(n + 1)]  # 조상(부모,대표) 갱신
while hq:
    cost_s, source = heappop(hq)
    if total[source] < cost_s:
        continue
    for target, cost in adj_list[source]:
        cost_t = cost_s + cost
        if cost_t < total[target]:
            total[target] = cost_t
            heappush(hq, (cost_t, target))
            ancestor[target] = source
print(total[goal])  # 출발 도시에서 도착 도시까지 가는데 드는 최소 비용
path = list()
while True:
    path.append(goal)
    goal = ancestor[goal]
    if goal == start:
        break
path = path[::-1]
print(len(path) + 1)
print(f'{start}', *path)
