import sys

sys.stdin = open('./01244_최대상금_input.txt')


def big(number, depth, count):
    global answer
    temp = int(''.join(number))  # 숫자 합치기
    if temp in answer[depth]:  # 중복 없이 숫자 추가
        return
    else:
        answer[depth].append(temp)

    if depth == count:  # depth == 교환 횟수
        return

    for left in range(length):  # Sorting
        for right in range(left + 1, length):  # Sorting
            number[left], number[right] = number[right], number[left]
            big(number, depth + 1, count)
            number[left], number[right] = number[right], number[left]


T = int(input())  # 전체 테스트 케이스의 수
for C in range(1, T + 1):
    money, cnt = input().split()
    length = len(money)  # 자릿수
    cnt = int(cnt)  # 교환 횟수
    money = list(money)  # char 분할
    answer = [list() for _ in range(cnt + 1)]

    big(money, 0, cnt)
    print(f'#{C} {max(answer[-1])}')
