def solution(n, number):
    candi = [{n}]  # n 만 사용
    for answer in range(1, 9):  # 1~8  # n 은 1 이상 9 이하
        can = {int(str(n) * answer)}  # n ~ nnnnnnnn
        for a in range(1, answer // 2 + 1):  # 1~4
            for x in candi[a]:
                for y in candi[answer - a]:
                    can.add(x * y)
                    can.add(x + y)
                    can.add(x - y)  # for 문 절반만
                    can.add(y - x)
                    if x != 0:  # 나누기 연산에서 나머지는 무시
                        can.add(y // x)
                    if y != 0:
                        can.add(x // y)
        if number in can:  # N 사용횟수의 최솟값
            return answer  # answer <= 8
        candi.append(can)
    else:  # if 9 <= answer:
        answer = -1
        return answer


print(solution(5, 12))  # 4
print(solution(2, 11))  # 3
