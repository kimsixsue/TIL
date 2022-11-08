# https://docs.python.org/ko/3.9/library/bisect.html?highlight=bisect_left
from bisect import bisect_left
# https://docs.python.org/ko/3.9/library/collections.html#defaultdict-examples
from collections import defaultdict
# https://docs.python.org/ko/3.9/library/itertools.html?itertools.combinations#itertools.combinations
from itertools import combinations


# https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
def solution(info, query):  # 정답률 : 정확성 44.07%, 효율성 4.49%
    answer = list()
    # 누락된 값을 제공하기 위해 팩토리 함수를 호출하는 딕셔너리 서브 클래스
    # 첫 번째 인자는 default_factory 어트리뷰트의 초깃값을 제공합니다
    dictionary = defaultdict(list)
    # 지원자들을 그룹별로 적절하게 미리 분류
    for i in info:
        i = i.split()
        condition = i[:-1]
        score = int(i[-1])
        for _ in range(5):
            # 입력 iterable 에서 요소의 길이 r 서브 시퀀스들을 반환합니다.
            case = list(combinations([0, 1, 2, 3], _))
            for c in case:
                temp = condition.copy()
                for index in c:
                    temp[index] = "-"
                key = ''.join(temp)
                dictionary[key].append(score)
    # 같은 그룹의 지원자끼리 묶어두고, 해당 그룹에서 점수를 기준으로 오름차순 정렬
    for value in dictionary.values():
        value.sort()
    for qry in query:
        qry = qry.replace("and ", "")
        qry = qry.split()
        target_key = ''.join(qry[:-1])
        target_score = int(qry[-1])
        count = 0
        # 미리 분류해둔 그룹에서 X점 이상 맞은 지원자 수를 세주기
        # 배열에서 X 이상 숫자가 처음 나타나는 위치를 찾아야 하며, 이는 lower bound 를 이용
        if target_key in dictionary:
            target_list = dictionary[target_key]
            # 배열 이진 분할 알고리즘, 이미 정렬되었다고 가정
            index = bisect_left(target_list, target_score)
            count = len(target_list) - index
        answer.append(count)
    return answer


print(solution(  # result = [1, 1, 1, 1, 2, 4]
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
