TestCase = int(input())  # 테스트 케이스 개수
for T in range(1, TestCase + 1):
    str1 = input()       # 길이가  5 ≤ N ≤  100, N ≤ M
    str2 = input()       # 길이가 10 ≤ M ≤ 1000, N ≤ M
    print(f'#{T} {int(str1 in str2)}')  # 0 or 1
