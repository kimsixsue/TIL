tot = int(input())  # test case 개수
for i in range(1, tot + 1):  # 알파벳 숫자 쌍 개수
    cnt = int(input())
    zi = ''
    for j in range(cnt):
        abc, num = input().split()
        zi += abc * int(num)  # 압축해제된 전체 문자열
    line_count = ((len(zi) - 1) // 10) + 1  # 문자열을 나눌 줄 수
    print('#' + str(i))
    e = 0
    arr = []
    for e in range(0, len(zi), 10):
        para = zi[e: e + 10:]
        arr.append(para)
    for each in arr:
        print(each)
