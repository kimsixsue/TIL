from heapq import heappush, heappop

N, E = map(int, input().split())
adj_list = [list() for _ in range(N + 1)]
for _ in range(E):
    source, target, weight = map(int, input().split())
    adj_list[source].append((target, weight))  # 인접 리스트
INF = 1e9
total = [INF] * (N + 1)  # 최대값으로 초기화
start = 0
hq = list()  # 최소힙
total[start] = 0
heappush(hq, (0, start))  # 시작점 추가
while hq:
    cost_s, source = heappop(hq)  # 최소 비용 간선 선택
    if total[source] < cost_s:  # 테이블에 저장된 최소값 보다 크면 continue
        continue
    for target, weight in adj_list[source]:  # 다음 노드로 가는 비용 계산해서
        cost_t = cost_s + weight
        if cost_t < total[target]:
            total[target] = cost_t  # 최소값 테이블에 업데이트 후
            heappush(hq, (cost_t, target))  # 힙에 추가
print(total)
