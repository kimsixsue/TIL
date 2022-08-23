T = int(input())  # 테스트 케이스의 수
for x in range(1, T + 1):
    N, Q = map(int, input().split())  # 1 ≤ N, Q ≤ 1000
    L, R = [0] * (Q + 1), [0] * (Q + 1)  # 1 ≤ Q ≤ 1000
    for i in range(1, Q + 1):  # 1 ≤ i ≤ Q
        L[i], R[i] = map(int, input().split())  # 1 ≤ L_i ≤ R_i ≤ N ≤ 1000
    box_number = [0] * (N + 1)
    for i in range(1, Q + 1):  # Q개의 작업을 수행한 다음, i 번째 작업에 대해
        box_number[L[i]: R[i] + 1] = [i] * (R[i] - L[i] + 1)  # L번 상자부터 R번 상자까지의 값을 i로 변경
    print(f'#{x}', *box_number[1:])  # 1번부터 N 번까지의 상자에 적혀있는 값들을 순서대로 출력
