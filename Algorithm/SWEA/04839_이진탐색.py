def binary_search(pages, target):
    count = 0
    left = 1
    right = pages
    while 1:
        count += 1
        center = (left + right) // 2
        if center == target:
            return count
        elif center < target:
            left = center
        elif center > target:
            right = center


for testcase in range(1, int(input()) + 1):  # 1 <= 테스트 케이스 개수 <= 50
    P, Pa, Pb = list(map(int, input().split()))  # 1<= 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb <=1000
    AB0 = binary_search(P, Pa) - binary_search(P, Pb)
    result = ''  # 지정된 페이지를 먼저 펼치는 사람이 누구인지 알아내 출력하시오.
    if AB0 < 0:
        result = 'A'
    elif AB0 > 0:
        result = 'B'
    elif AB0 == 0:  # 비긴 경우는 0을 출력한다.
        result = '0'
    print(f'#{testcase} {result}')
