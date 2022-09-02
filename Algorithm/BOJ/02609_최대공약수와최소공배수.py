import sys

input = sys.stdin.readline
a, b = map(int, input().split())

# 최대 공약수
s = min(a, b)
for n in range(1, s + 1):
    if a % n or b % n:
        continue
    d = n
print(d)
# 최소공배수
print(a * b // d)
