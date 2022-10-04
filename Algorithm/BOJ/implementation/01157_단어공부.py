s = sorted(list(input().upper()))
count = dict()
for _ in s:
    if _ not in count:
        count[_] = 1
    else:
        count[_] += 1
c = max(count.values())
flag = -1
for k in count:
    if count[k] == c:
        flag += 1
        alp = k
if flag:
    print('?')
else:
    print(alp)
