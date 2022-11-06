def solution(clothes):
    com = dict()
    for n,k in clothes:
        if com.get(k):
            com[k].add(n)
        else:
            com[k]={n}
    answer = 1
    for c,i in com.items():
        answer *= len(i)+1
    answer -= 1
    return answer