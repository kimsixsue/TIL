def reverse(matrix):
    length = 1
    for line in range(100):
        for size in range(100, 1, -1):
            for start in range(0, 101 - size):
                for end in range(99, size - start - 2, -1):
                    if size == end - start + 1:
                        check = matrix[line][start: end + 1]
                        if (check == check[:: -1]) and (length < size):
                            length = size
    return length


for _ in range(10):              # 10개의 테스트케이스
    number = int(input())        # 테스트 케이스의 번호
    plane = [''] * 100           # 100x100 평면 글자판
    for row in range(100):       # 각 칸의 들어가는 글자는 'A', 'B', 'C' 중 하나
        plane[row] = input()     # 가로
    vertical_plane = [''] * 100  # 세로
    for row in range(100):
        for col in range(100):
            vertical_plane[row] += plane[col][row]
    long1 = reverse(plane)
    long2 = reverse(vertical_plane)
    if long1 >= long2:
        longest = long1
    else:
        longest = long2
    print(f'#{number} {longest}')  # 가장 긴 회문의 길이를 출력
