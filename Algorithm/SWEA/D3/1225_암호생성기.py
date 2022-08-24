number = [1, 2, 3, 4, 5]  # 감소 한 사이클

for _ in range(10):

    tcn = int(input())  # 테스트 케이스의 번호
    queue = list(map(int, input().split()))  # 8개의 숫자 데이터

    idx = 0

    while queue[-1] > 0:  # 숫자가 0 이하가 되면 종료
        queue[0] -= number[idx]
        idx = (idx + 1) % 5  # idx 0 ~ 4 == number 1 ~ 5
        queue.append(queue.pop(0))

    queue[-1] = 0

    print(f'#{tcn}', *queue)  # 8자리의 암호
