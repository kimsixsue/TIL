T = int(input())  # 테스트 케이스의 개수
for t in range(1, T + 1):
    N = int(input())  # 5 <= N <= 50
    numbers = list(map(int, input().split()))  # N 개의 숫자
    for end in range(N - 1, 0, -1):
        for start in range(end):
            if numbers[start] > numbers[start + 1]:
                numbers[start], numbers[start + 1] = numbers[start + 1], numbers[start]
    print(f'#{t}', *numbers)  # N 길이의 숫자열을 오름차순으로 정렬하여 출력
