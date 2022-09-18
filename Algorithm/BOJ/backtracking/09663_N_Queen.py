# https://velog.io/@hope1213/백준-9663-N-Queen-파이썬
# PyPy3
def n_queen(depth):
    global count
    if depth == N:
        count += 1
        return

    for n in range(N):
        if not checked[n]:
            col[depth] = n
            flag = True
            for d in range(depth):
                if abs(col[depth] - col[d]) == abs(depth - d):
                    flag = False
                    break
            if flag:
                checked[n] = 1
                n_queen(depth + 1)
                checked[n] = 0


N = int(input())
count = 0
col = [0] * N
checked = [0] * N
n_queen(0)
print(count)
