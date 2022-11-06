import sys

input = sys.stdin.readline
N = int(input())  # 수의 개수(홀수)
count = [0 for _ in range(8001)]

# 1. 산술평균
total = 0
for i in range(N):
    n = int(input())
    count[n + 4000] += 1
    total += n
print(round(total / N))  # 소수점 이하 첫째 자리에서 반올림

# 2. 중앙값
cnt = 0
for _ in range(8001):
    if count[_] > 0:
        cnt += count[_]
        if cnt > N // 2:
            print(_ - 4000)
            break

# 3. 최빈값
f_index = 0
f_count = 0
s_index = list()
s_count = list()
for _ in range(8001):
    if count[_] > f_count:
        f_index = _
        f_count = count[_]
        s_index = list()
        s_count = list()
    if count[_] == f_count:
        s_index.append(_)
if len(s_index) <= 1:
    print(f_index - 4000)
else:  # # 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값
    print(s_index[1] - 4000)
# 4. 범위
big = small = 0
for _ in range(8001):
    if count[_] > 0:
        small = _
        break
for _ in range(8000, -1, -1):
    if count[_] > 0:
        big = _
        break
print(big - small)
