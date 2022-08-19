T = int(input())  # 테스트 케이스의 수
for x in range(1, T + 1):
    A, B, C, number = [0] * 5001, [0] * 5001, [0] * 5001, [0] * 5001
    N = int(input())                                        # 1 ≤ 버스 노선 개수 N ≤  500
    for i in range(1, N + 1):                         # 1 ≤ A_i ≤ 버스 노선 번호 i ≤ B_i ≤ 5000
        A[i], B[i] = list(map(int, input().split()))  # 1 ≤ A_i ≤ 버스 정류장 번호 ≤ B_i ≤ 5000
    for bus in range(1, N + 1):
        for stop in range(A[bus], B[bus] + 1):
            number[stop] += 1        # number[j] = C[j]번 버스 정류장을 지나는 버스 노선의 개수
    answer = []
    P = int(input())                                        # 1 ≤ 버스 정류장 개수 P ≤ 500
    for j in range(1, P + 1):
        C[j] = int(input())                                 # 1 ≤ 버스 정류장 번호 ≤ 5000
        answer.append(number[C[j]])
    print(f'#{x}', *answer)
