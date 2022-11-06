def solution(genres, plays):
    length = len(plays)
    gen, p = dict(), dict()
    for i in range(length):
        if gen.get(genres[i]):
            gen[genres[i]].append((i, plays[i]))
            p[genres[i]] += plays[i]
        else:
            gen[genres[i]] = [(i, plays[i])]
            p[genres[i]] = plays[i]
    order = sorted(p.items(), key=lambda _: _[1], reverse=True)
    for k, v in gen.items():
        gen[k].sort(key=lambda v: v[1], reverse=True)
    mix = dict()
    for k, v in order:
        mix[k] = gen[k]
    answer = list()
    for g in mix.values():
        answer.append(g[0][0])
        if len(g) >= 2:
            answer.append(g[1][0])
    return answer
