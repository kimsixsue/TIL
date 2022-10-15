N = int(input())  # 1 <= 시험장의 개수
A = list(map(int, input().split()))  # 1 <= 각 시험장에 있는 응시자의 수
# 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명
# 부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명
B, C = map(int, input().split())
# 각각의 시험장에 총감독관은 오직 1명
# 각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수를 출력
total = N
for i in range(N):
    r = A[i] - B
    if r > 0:
        total += (r // C) + bool(r % C)
print(total)
