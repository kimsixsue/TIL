def binary_search(n, s, key):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if s[mid] == key:
            return 1
        elif key < s[mid]:
            high = mid - 1
        else:  # s[mid] < key
            low = mid + 1
    return 0


N = int(input())  # len(A)
A = list(map(int, input().split()))
A.sort()
M = int(input())  # len(B)
B = list(map(int, input().split()))
for _ in range(M):
    print(binary_search(N, A, B[_]))
