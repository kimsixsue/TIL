import sys

input = sys.stdin.readline
N = int(input())
number = sorted([int(input()) for _ in range(N)])
for _ in number:
    print(_)
