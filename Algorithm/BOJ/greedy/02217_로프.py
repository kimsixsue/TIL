N = int(input())  # len(rope)
endure = sorted([int(input()) for _ in range(N)], reverse=True)

w = endure[0]  # load * N
load = 0  # weight/N
for n in range(N):  # 임의로 몇 개의 로프를 골라서 사용
    load = endure[n] * (n + 1)
    if w < load:
        w = load  # 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량
print(w)
