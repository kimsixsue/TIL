import sys

sys.stdin = open('./01486_장훈이의높은선반_input.txt')


def safe_tower(n, b):  # 경우의수는 2**n 가지
    safe_c = list()

    for c in range(1, 2 ** n):
        temp_num = 0
        temp_index = 0

        while c >= 2:
            binary = c % 2
            temp_num += binary * H[temp_index]
            temp_index += 1
            c //= 2
        temp_num += c % 2 * H[temp_index]
        if temp_num >= b:
            safe_c.append(temp_num)

    safe = min(safe_c) - b
    return safe  # 안전한 조합


T = int(input())  # 테스트 케이스의 수
for t in range(1, T + 1):
    N, B = map(int, input().split())
    # 점원 1~20명 /// 선반 높이 <= sum(H)
    H = list(map(int, input().split()))
    # 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것
    print(f'#{t} {safe_tower(N, B)}')
