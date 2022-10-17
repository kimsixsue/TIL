from collections import deque

uno = deque(map(int, list(input())))
dos = deque(map(int, list(input())))
tre = deque(map(int, list(input())))
cua = deque(map(int, list(input())))  # 12시부터 시계방향, 0: N극, 1: S극
K = int(input())  # 1<= 회전횟수 <=100
for k in range(K):
    # 회전시킨 톱니바퀴의 번호(1, 2, 3, 4), 방향(1: 시계, -1: 반시계)
    number, direction = map(int, input().split())
    uno_right = uno[2]
    dos_right = dos[2]
    tre_right = tre[2]
    dos_left = dos[6]
    tre_left = tre[6]
    cua_left = cua[6]
    # uno[2]와 dos[6], dos[2]와 tre[6], tre[2]와 cua[6]은 맞닿음
    # 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전
    if number == 1:
        if uno_right != dos_left:
            if dos_right != tre_left:
                if tre_right != cua_left:
                    cua.rotate(-direction)
                tre.rotate(direction)
            dos.rotate(-direction)
        uno.rotate(direction)
    elif number == 2:
        if uno_right != dos_left:
            uno.rotate(-direction)
        if dos_right != tre_left:
            if tre_right != cua_left:
                cua.rotate(direction)
            tre.rotate(-direction)
        dos.rotate(direction)
    elif number == 3:
        if tre_right != cua_left:
            cua.rotate(-direction)
        if dos_right != tre_left:
            if uno_right != dos_left:
                uno.rotate(direction)
            dos.rotate(-direction)
        tre.rotate(direction)
    else:  # number == 4
        if tre_right != cua_left:
            if dos_right != tre_left:
                if uno_right != dos_left:
                    uno.rotate(-direction)
                dos.rotate(direction)
            tre.rotate(-direction)
        cua.rotate(direction)
print(uno[0] + dos[0] * 2 + tre[0] * 4 + cua[0] * 8)
# 네 톱니바퀴의 점수의 합
# 1번 톱니바퀴의 12시방향이 N 극이면 0점, S 극이면 1점
# 2번 톱니바퀴의 12시방향이 N 극이면 0점, S 극이면 2점
# 3번 톱니바퀴의 12시방향이 N 극이면 0점, S 극이면 4점
# 4번 톱니바퀴의 12시방향이 N 극이면 0점, S 극이면 8점
