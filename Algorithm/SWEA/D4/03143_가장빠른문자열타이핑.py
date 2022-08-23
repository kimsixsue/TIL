T = int(input())  # 테스트 케이스의 수 T
for testcase in range(1, T + 1):
    A, B = input().split()  # 두 문자열 A, B
    len_a = len(A)  # A의 길이 1이상 10000이하
    len_b = len(B)  # B의 길이 1이상   100이하
    i = count = 0
    while i < len_a:
        if A[i: i + len_b] == B:
            i += len_b
        else:
            i += 1
        count += 1
    print(f'#{testcase} {count}')  # A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값
