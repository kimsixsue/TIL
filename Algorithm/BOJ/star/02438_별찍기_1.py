N = int(input()) # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# i번째 줄에는 별 i개를 찍는 문제
for i in range(1, N+1): # 1 <= i <= N
    print("*" * i) # 문자열 곱하기 숫자는 해당 문자열을 해당 숫자만큼 반복합니다.

# import sys
# N = int(sys.stdin.readline())
# for i in range(N):
#     for j in range(0, i+1):
#         print('*', end='')
#     print()
