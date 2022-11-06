from collections import deque

for tcn in range(1, 11):
    data_length, start = map(int, input().split())
    data = list(map(int, input().split()))
    undirected = [list() for _ in range(101)]
    for i in range(data_length):
        if i % 2:
            so, ta = data[i - 1], data[i]
            undirected[so].append(ta)
    contact = [0 for _ in range(101)]
    queue = deque()
    queue.append(start)
    contact[start] = 1
    while queue:
        q = queue.popleft()
        if undirected[q]:
            for n in undirected[q]:
                if not contact[n]:
                    queue.append(n)
                    contact[n] = contact[q] + 1
    person, maximum = 0, 0
    for p in range(1, 101):
        if maximum <= contact[p]:
            maximum = contact[p]
            person = p
    # 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람
    print(f'#{tcn} {person}')
