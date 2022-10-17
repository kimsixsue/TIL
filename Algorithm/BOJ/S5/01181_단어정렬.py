N = int(input())  # 1 <= N
dic = ['' for _ in range(N)]
for _ in range(N):
    word = input()
    length = len(word)  # <= 50
    dic[_] = length, word
dic.sort(key=lambda w: (w[0], w[1]))
temp = ''
for i in range(N):
    if dic[i][1] == temp:
        continue
    print(dic[i][1])
    temp = dic[i][1]
