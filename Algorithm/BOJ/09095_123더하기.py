import sys
input = sys.stdin.readline

way = [0] * 11
way[1:4] = 1, 2, 4
for w in range(4, 11):
    way[w] = w

for _ in range(int(input())):  # 테스트 케이스의 개수
    print(way[int(input())])  # n을 1, 2, 3의 합으로 나타내는 방법의 수
