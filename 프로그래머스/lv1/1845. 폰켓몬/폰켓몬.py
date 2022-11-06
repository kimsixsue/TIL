def solution(nums):
    N = len(nums)
    pkm = dict()
    for n in nums:
        if pkm.get(n):
            pkm[n] += 1
        else:
            pkm[n] = 1
    count = 0
    for k in pkm.keys():
        count += 1
    answer = min(count, N // 2)
    return answer
