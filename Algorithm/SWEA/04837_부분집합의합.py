A = list(range(1, 13))  # 1부터 12까지의 숫자를 원소로 가진 집합
for testcase in range(1, int(input()) + 1):  # 1 ≤ 테스트 케이스 개수 ≤ 50
    N, K = map(int, input().split())  # 1 ≤ 부분집합 원소의 수 N ≤ 12, 1 ≤ 부분 집합의 합 K ≤ 100
    count = 0  # 해당하는 부분집합이 없는 경우 0을 출력
    for outer in range(1 << 12):
        case = []
        total = 0
        for inner in range(12):
            if outer & (1 << inner):
                case.append(A[inner])
        if len(case) == N:
            for _ in case:
                total += _
            if total == K:  # 모든 부분 집합을 만들어 답을 찾아도 된다.
                count += 1
    print(f'#{testcase} {count}')  # 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수
