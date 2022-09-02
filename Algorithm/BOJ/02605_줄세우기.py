import sys

input = sys.stdin.readline
S = int(input())  # 학생 최대 100명
N = list(map(int, input().split()))  # 0 이상 index 이하, 번호
# 뽑은 번호만큼 앞자리로 가서 줄을 선다
line = list()  # 학생 번호
for n in range(S):
    length = len(line)
    # list index <- value insert
    line.insert(length - N[n], n + 1)
print(*line)
