N = int(input())  # 사람의 수
P = list(map(int, input().split()))  # 각 사람이 돈을 인출하는데 걸리는 시간
# i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분
P.sort()  # 정렬
total = 0
for n in range(N):  # 누적 합
    total += P[n] * (N - n)
print(total)  # 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
