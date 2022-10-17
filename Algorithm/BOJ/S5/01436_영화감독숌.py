# 종말의 숫자
# 666 이 들어가는 수
N = int(input())  # N번째 영화의 제목에 들어간 숫자
number = 666
for n in range(666, 6670000):
    if '666' in str(n):
        N -= 1
        if N == 0:
            print(n)
            break
