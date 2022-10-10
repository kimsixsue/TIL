T = int(input())  # 총 테스트 케이스의 개수
for x in range(1, T + 1):
    # 도시의 크기(5~20), 하나의 집이 지불할 수 있는 비용(1~10)
    N, M = map(int, input().split())
    city = [input().split() for _ in range(N)]
    where = list()
    for row in range(N):
        for col in range(N):
            if city[row][col] == '1':  # '1': 집(반드시 존재함), '0': 나머지
                where.append((row, col))
    answer = 0
    for row in range(N):
        for col in range(N):
            domain = list()
            for r, c in where:
                dom = abs(row - r) + abs(col - c) + 1
                domain.append(dom)
            domain.sort()  # 서비스(운영) 영역의 크기
            for count in range(len(domain), 0, -1):  # 1 <= count
                K = domain[count - 1]  # 서비스(운영) 영역의 크기
                operation = K * K + (K - 1) * (K - 1)  # 운영 비용
                # 보안회사의 이익 = 서비스 제공받는 집들을 통해 얻는 수익 - 운영 비용
                if count * M >= operation:  # 손해를 보지 않으면서 (0 이상)
                    if answer < count:  # 서비스를 가장 많은 집들에 제공할 때,
                        answer = count  # 서비스를 제공 받는 집들의 수
    print(f"#{x} {answer}")
