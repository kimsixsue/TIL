import sys

sys.stdin = open('05201_컨테이너운반_sample_input.txt')

TC = int(input())  # 테스트케이스의 수
for T in range(1, TC + 1):

    N, M = map(int, input().split())  # len(w), len(t)
    w = sorted(list(map(int, input().split())), reverse=True)  # 컨테이너 화물 무게
    t = sorted(list(map(int, input().split())), reverse=True)  # 트럭 적재용량

    while w and t and w[0] > t[0]:  # 못 싣는 화물은 없앤다
        del w[0]
        N -= 1
    while w and t and w[-1] > t[-1]:  # 못 싣는 트럭은 없앤다
        del t[-1]
        M -= 1
    answer, w_index, t_index = 0, 0, 0
    while w and t:
        if w[w_index] <= t[t_index]:  # 트럭당 한 개의 컨테이너를 운반
            answer += w[w_index]  # 총 중량이 가장 클 때를 찾는다
            t_index += 1  # 다음 트럭
            if t_index >= M:
                break
        w_index += 1  # 다음 화물
        if w_index >= N:
            break
    print(f'#{T} {answer}')  # 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
