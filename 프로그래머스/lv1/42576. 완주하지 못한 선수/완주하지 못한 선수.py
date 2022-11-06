def solution(participant, completion):
    names = dict()
    for p in participant:
        if names.get(p):
            names[p] += 1
        else:
            names[p] = 1
    for c in completion:
        if names.get(c):
            names[c] -= 1
    answer = ""
    for k, v in names.items():
        if v >= 1:
            answer = k
            break
    return answer
