N = int(input())  # 회의의 수 1~
I = [list(map(int, input().split())) for _ in range(N)]
I.sort()  # 회의
I.sort(key=lambda I: I[1])  # 0~
number = 1  # 최대 사용할 수 있는 회의의 최대 개수
time = I[0][1]  # 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다
for n in range(1, N):
    if I[n][0] >= time:
        number += 1
        time = I[n][1]
print(number)
