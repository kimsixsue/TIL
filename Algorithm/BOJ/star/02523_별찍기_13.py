N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
for _ in range(N): # 가운데줄까지 출력
    print('*' * (_ + 1))
for _ in range(N - 1): # 가운데 후 줄부터 출력
    print('*' * (N - _ - 1))