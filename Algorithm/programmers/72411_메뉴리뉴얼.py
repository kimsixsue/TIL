from itertools import combinations


def solution(orders, course):
    answer = list()
    course.sort(reverse=True)
    for cour in course:
        candidates = dict()
        for order in orders:
            order = sorted(order)
            for comb in combinations(order, cour):
                dish = ''.join(sorted(comb))
                if candidates.get(dish):
                    candidates[dish] += 1
                else:
                    candidates[dish] = 1
        if candidates:
            count = max(candidates.values())
            if 2 <= count:
                for k, v in candidates.items():
                    if v == count:
                        answer.append(k)
    answer.sort()
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
print(solution(orders, course))

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))
