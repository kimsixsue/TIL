N = int(input())  # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
for i in range(0, N+1):
    print("*" * (N-i))
# 첫 줄은 N 개만큼 *이 나와야하므로 N-i 개만큼 출력한다.
