import sys

sys.stdin = open('s_input.txt')


def is_monoton(num):  # 각 숫자의 자릿수가 단순하게 증가
    one = num % 10  # do-while
    while num:
        num //= 10
        if one < num % 10:
            return False
        one = num % 10
    return True  # num : 단조 증가하는 수


def find_max(num, n):
    big = 0
    for i in range(n):
        for j in range(i + 1, n):
            temp = num[i] * num[j]
            if is_monoton(temp):  # 단조 증가 수
                if big < temp:    # 최댓값 갱신
                    big = temp
    if not big:  # Ai x Aj 중에서 단조 증가하는 수가 없다면 -1을 출력
        return -1
    return big  # 1 ≤ i < j ≤ N, 단조 증가하는 수인 Ai x Aj 중에서 그 최댓값을 출력


T = int(input())  # 테스트 케이스의 수
for t in range(1, T + 1):
    N = int(input())  # 1 ≤ 자연수 N ≤ 1,000
    number = list(map(int, input().split()))  # 자연수 N개, A1, (1 ≤ Ai ≤ 30,000), AN
    print(f'#{t} {find_max(number, N)}')
