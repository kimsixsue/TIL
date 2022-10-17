import sys

input = sys.stdin.readline
N, M = map(int, input().split())  # 학생 N명, 키 비교 회수 M
edge = [list() for _ in range(N + 1)]  # 1번~N번
in_degree = [0 for _ in range(N + 1)]  # 1번~N번
for _ in range(M):  # 일부 학생들의 키만을 비교한 결과
    A, B = map(int, input().split())  # 두 학생의 번호 A, B
    edge[A].append(B)  # 학생 A가 학생 B의 앞에 서야 한다
    in_degree[B] += 1  # in-degree += 1
queue = [0] * N
front = rear = -1
for i in range(1, N + 1):  # 1번~N번
    if in_degree[i] == 0:  # in-degree == 0:
        front += 1
        queue[front] = i  # enqueue
topology = [0] * N
idx = 0
for i in range(1, N + 1):  # 1번~N번
    rear += 1
    student = queue[rear]  # dequeue
    topology[idx] = student  # Topology Sort
    idx += 1
    for B in edge[student]:  # adjacent[앞 학생]
        in_degree[B] -= 1  # in-degree[뒤 학생] -= 1
        if in_degree[B] == 0:  # in-degree[뒤 학생] == 0:
            front += 1
            queue[front] = B  # enqueue(뒤 학생]
print(*topology)  # 학생들을 키 순서대로 줄을 세운 결과를 출력
