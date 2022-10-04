import sys

input = sys.stdin.readline
N = int(input())
count = [0] * 10001
for _ in range(N):
    count[int(input())] += 1
for n in range(1, 10001):
    for _ in range(count[n]):
        print(str(n))
