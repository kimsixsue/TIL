# len(number), Sum
N, S = map(int, input().split())
number = list(map(int, input().split()))
end = 0
concat = 0
length = 0
short = [N+1]
for start in range(N):
    while concat < S and end < N:
        concat += number[end]
        length += 1
        end += 1
    if S <= concat and length < short[-1]:
        short.append(length)
    concat -= number[start]
    length -= 1
if short[-1] == N+1:
    print(0)
else:
    print(short[-1])
