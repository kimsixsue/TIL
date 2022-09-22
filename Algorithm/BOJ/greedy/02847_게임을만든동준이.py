N = int(input())  # 레벨의 수
score = [int(input()) for _ in range(N)]  # 1~
down = 0  # 점수를 몇 번 감소
for n in range(N - 1, 0, -1):
    dif = score[n - 1] - score[n]
    if dif >= 0:
        down += dif + 1
        score[n - 1] -= dif + 1
print(down)
