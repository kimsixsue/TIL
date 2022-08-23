def max_index():
    index = 0
    for _ in range(100):
        if heights[index] < heights[_]:
            index = _
    return index


def min_index():
    index = 0
    for _ in range(100):
        if heights[index] > heights[_]:
            index = _
    return index


result = ''
for t in range(1, 11):
    dump_count = int(input())
    heights = list(map(int, input().split()))
    for _ in range(dump_count):
        heights[max_index()] -= 1
        heights[min_index()] += 1
    result += f'#{t} {heights[max_index()] - heights[min_index()]}\n'
print(result.rstrip('\n'))
