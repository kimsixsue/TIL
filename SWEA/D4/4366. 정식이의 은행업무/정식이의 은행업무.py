TCN = int(input())  # 테스트케이스의 개수
for T in range(1, TCN + 1):

    bina_2 = input()
    tres_3 = input()
    # 각각의 수에서 단 한 자리만을 잘못 기억하고 있다

    # 이진수의 각 자리를 뒤집어준다.
    bina_candi = list()
    for two in range(len(bina_2)):
        bina_list = list(bina_2)
        if bina_list[two] == '0':  # 0이면 (+ 0으로 시작)
            bina_list[two] = '1'
        else:  # 1이면
            bina_list[two] = '0'
        bina_candi.append(int(''.join(bina_list), 2))

    # 삼진수 확인
    tres_candi = list()
    for tre in range(len(tres_3)):
        tres_list = list(tres_3)
        if tres_list[tre] == '0':  # 0이면 (+ 0으로 시작)
            tres_list[tre] = '1'
            tres_candi.append(int(''.join(tres_list), 3))
            tres_list[tre] = '2'
            tres_candi.append(int(''.join(tres_list), 3))
        if tres_list[tre] == '1':  # 1이면
            tres_list[tre] = '0'
            tres_candi.append(int(''.join(tres_list), 3))
            tres_list[tre] = '2'
            tres_candi.append(int(''.join(tres_list), 3))
        else:  # 2면
            tres_list[tre] = '1'
            tres_candi.append(int(''.join(tres_list), 3))
            tres_list[tre] = '0'
            tres_candi.append(int(''.join(tres_list), 3))

    answer = 0  # 원래 송금하기로 하였던 금액
    for n in bina_candi:
        if n in tres_candi:
            answer = n
            break
    print(f'#{T} {answer}')
