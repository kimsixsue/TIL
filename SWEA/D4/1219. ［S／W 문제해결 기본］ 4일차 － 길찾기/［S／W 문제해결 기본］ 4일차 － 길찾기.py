A, B = 0, 99
for _ in range(10):
    testcase, total = map(int, input().split())  # 길의 총 개수
    origin = list(map(int, input().split()))  # 순서쌍
    direct1, direct2, stack = [-1] * 100, [-1] * 100, [-1] * 100
    for way in range(0, total * 2, 2):
        if direct1[origin[way]] > -1:
            direct2[origin[way]] = origin[way + 1]
        else:  # direct1 우선 채움
            direct1[origin[way]] = origin[way + 1]
    top = -1
    depart = A
    while 1:
        if direct1[depart] == 99 or direct2[depart] == 99:
            answer = 1
            break  # A 도시에서 B 도시로 가는 길이 존재하는지
        elif direct1[A] == -1 and direct2[A] == -1:
            answer = 0
            break
        elif direct1[depart] != -1:
            top += 1
            stack[top] = depart
            depart = direct1[depart]
            direction = 1
        elif direct2[depart] != -1:
            top += 1
            stack[top] = depart
            depart = direct2[depart]
            direction = 2
        else:
            if direction == 1:
                direct1[stack[top]] = -1
            elif direction == 2:
                direct2[stack[top]] = -1
            depart = stack[top]
            top -= 1

    print(f'#{testcase} {answer}')
