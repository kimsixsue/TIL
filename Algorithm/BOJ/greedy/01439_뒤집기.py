S = input()
length = len(S)  # 1~
chunk = 1  # 연속
for _ in range(length - 1):
    if S[_] != S[_ + 1]:  # 이웃이 다르면
        chunk += 1
print(chunk // 2)  # 행동의 최소 횟수
