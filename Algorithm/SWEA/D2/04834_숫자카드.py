T = int(input())  # 1 ≤ 테스트 케이스 개수 ≤ 50
for i in range(1, T + 1):
    N = int(input())  # 5 ≤ 카드 장수 ≤ 100
    ai = input()  # 0 ≤ N개의 숫자 문자열 ai ≤ 9
    number = list(map(int, list(ai)))
    length = len(number)
    count = [0] * 10  # Sort
    m_number = m_count = 0
    for _ in range(length):
        count[number[_]] += 1
    for _ in range(10):
        if m_count <= count[_]:  # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽
            m_count = count[_]
            m_number = _
    print(f'#{i} {m_number} {m_count}')  # 가장 많은 카드의 숫자와 장 수
