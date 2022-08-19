count = int(input())
same = 0
for i in range(1, count+1):
    word = input()
    if word == word[::-1]:
        same = 1
    else:
        same = 0
    print(f'#{i} {same}')
