import sys

sys.stdin = open('./05203_베이비진게임_sample_input.txt')

TC = int(input())  # 테스트케이스의 수
for T in range(1, TC + 1):

    card = list(map(int, input().split()))  # 12장
    player1 = [0 for _ in range(7)]
    player2 = [0 for _ in range(7)]
    turn, who = 0, 0

    while turn < 12:
        count = turn // 2 + 1

        if turn % 2:  # 홀수: 플레이어 2
            player2[count] = card[turn]  # draw
            player2.sort(reverse=True)
        else:  # 짝수: 플레이어 1
            player1[count] = card[turn]  # draw
            player1.sort(reverse=True)

        if count >= 3:  # 이때부터 승리 가능
            number = [0 for _ in range(10)]

            if turn % 2:  # 홀수: 플레이어 2
                for _ in range(count):
                    number[player2[_]] += 1
            else:  # 짝수: 플레이어 1
                for _ in range(count):
                    number[player1[_]] += 1

            for n in range(8):  # 런
                if number[n] and number[n + 1] and number[n + 2]:
                    who = 1 + turn % 2
                    break
            for n in number:  # triplet
                if n >= 3:
                    who = 1 + turn % 2
                    break

        if who:  # 승자 정해지면
            break

        turn += 1

    print(f'#{T} {who}')  # 12장 끝난 후 없으면 print 0
