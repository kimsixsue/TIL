import sys

input = sys.stdin.readline
# 인원, 방 최대 인원
N, K = map(int, input().split())
student = [[0, 0] for _ in range(6)]
room = 0
for _ in range(N):
    S, Y = map(int, input().split())
    # 학년, 성별
    student[Y - 1][S] += 1
for s in range(2):
    for g in range(6):
        if student[g][s]:
            if student[g][s] > K:  # 해당 경우 방 개수
                room += student[g][s] // K
                if student[g][s] % K:
                    room += 1
            elif student[g][s]:
                room += 1  # 해당 성별 학년 방 1개
print(room)
