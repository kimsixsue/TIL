from collections import deque

tcn = int(input())  # 테스트 케이스의 개수
for T in range(1, tcn + 1):
    N, M = map(int, input().split())
    # N != M, 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
    visited = [0] * 1000001
    oper = 999999
    q = deque()
    q.append(N)
    while q:
        t = q.popleft()
        if t == M:
            oper = visited[t]
            break
        if visited[t] > oper:
            break
        for i in [t + 1, t - 1, t * 2, t - 10]:
            if 1 <= i <= 1000000 and visited[i] == 0:
                visited[i] = visited[t] + 1
                q.append(i)
    print(f'#{T} {oper}')  # 최소 몇 번의 연산을 거쳐야 하는지
"""
3
2 7
3 15
36 1007

"""
