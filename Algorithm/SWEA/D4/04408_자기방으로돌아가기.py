T = int(input())
for t in range(1, T + 1):

    N = int(input())  # 돌아가야 할 학생들의 수
    now = [0] * N  # 각 학생의 현재 방 번호(≤400)
    back = [0] * N  # 돌아가야 할 방의 번호(≤400)
    student = [0] * N
    corridor = [0] * 200  # 학생들이 자기방으로 돌아가면서 지나는 복도의 구간이 겹치면, 학생들은 동시에 돌아갈 수 없다.
    time = 0  # 최단 단위 시간

    # student: 해당 student 가 지나는 복도의 구간
    for _ in range(N):
        now[_], back[_] = map(int, input().split())
        if now[_] > back[_]:  # 정렬
            now[_], back[_] = back[_], now[_]
        student[_] = (now[_] + 1) // 2 - 1, (back[_] + 1) // 2 - 1

    # time = max(corridor)
    for s in range(N):
        for move in range(student[s][0], student[s][1] + 1):
            corridor[move] += 1

    for _ in range(200):
        if time < corridor[_]:
            time = corridor[_]

    print(f'#{t} {time}')
