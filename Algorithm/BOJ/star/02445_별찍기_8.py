# 빈칸이 짝수입니다. 가운데 줄이 0개이고, 한줄씩 멀어질 때마다 2씩 증가합니다.

N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
for _ in range(N - 1):  # 상단부
    print(('*' * (_ + 1)) + ' ' * (2 * (N - 1 - _)) + ('*' * (_ + 1)))
for _ in range(N):  # 하단부 (중간줄 포함)
    print(('*' * (N - _)) + ' ' * (2 * _) + ('*' * (N - _)))
