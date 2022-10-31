big_gap, best = 0, list()


def solution(n, info):  # 화살 n발, pc info_i = count(10-i)점, length = 11
    def back(mark_0, i, pc, bsk, bolt):
        if n < bolt:  # 화살 n발
            return
        if i == 11:  # len(best) == 11
            global big_gap, best
            gap = bsk - pc  # 점수 차이
            if big_gap < gap:  # 가장 낮은 점수를 더 많이 맞힌 경우
                big_gap = gap  # 갱신
                mark_0[10] = n - bolt  # sum(best) == n, 꼭 n발을 다 쏴야 합니다
                best = mark_0  # 가장 큰 점수 차이로 우승할 수 있는 방법
            return
        k = 10 - i  # 과녁 점수   
        if bolt < n:  # 둘다 과녁의 n 점까지 맞힐 수 있음
            mark_2 = mark_0[:]  # deepcopy
            mark_2[k] = info[k] + 1  # 과녁 점수
            back(mark_2, i + 1, pc, bsk + i, bolt + info[k] + 1)  # 김범수
        mark_1 = mark_0[:]  # deepcopy
        if 1 <= info[k]:  # 과녁 점수
            back(mark_1, i + 1, pc + i, bsk, bolt)  # 어피치
        else:
            back(mark_1, i + 1, pc, bsk, bolt)  # 안 쏨

    back([0] * 11, 0, 0, 0, 0)  # mark_0, i, pc, bsk, bolt
    global best
    if best:  # 김범수가 우승할 방법이 있는 경우
        return best
    else:  # 김범수가 우승할 수 없는 경우
        return [-1]
