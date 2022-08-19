def brute_force():
    pattern = input()   # 찾을 문자열
    text = input()      # 검색할 문장
    m = len(pattern)    # 찾을 문자열
    n = len(text)       # 검색할 문장
    number = 0
    for idx in range(n - m + 1):  # 검색할 문장
        for jdx in range(m):      # 찾을 문자열
            if pattern[jdx: jdx + m] == text[idx: idx + m]:
                number += 1  # 문자열이 해당 위치에 있으면
            break  # 다음 인덱스부터 문자열 탐색하기
    return number  # 개수를 반환


for _ in range(10):
    testcase = input()  # 테스트 케이스의 번호
    answer = brute_force()
    print(f'#{testcase} {answer}')
