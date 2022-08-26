import sys

sys.stdin = open('./sample_input.txt')

TestCase = int(input())  # 테스트 케이스 개수
for T in range(1, TestCase + 1):

    str1 = input()  # 길이가  5 ≤ N ≤  100, N ≤ M
    str2 = input()  # 길이가 10 ≤ M ≤ 1000, N ≤ M

    chars_count = dict()
    for c in list(set(str1)):  # 문자열 str1에 포함된 글자들이
        chars_count[c] = 0

    for char in str2:  # str2에 몇 개씩 들어있는지 찾고
        if char in chars_count:
            chars_count[char] += 1

    count = 0  # 그중 가장 많은 글자의 개수를 출력
    for v in chars_count.values():
        if count < v:
            count = v
    print(f'#{T} {count}')  # 0 ~ 1000