import json


def max_popularity(movies):
    """
        가장 인기 있는 영화 상세 정보 출력
    """
    want = ['id', 'title']
    new_list = []
    for movie in movies:
        new_dict = {}
        for w in want:
            new_dict[w] = movie.get(w)
        new_list.append(new_dict)

    for i in range(len(new_list)):
        id_1 = new_list[i].get('id')
        json_file = open(f'data/movies/{id_1}.json', encoding='utf-8')
        json_detail = json.load(json_file)
        new_list[i]['popularity'] = json_detail.get('popularity')

    popularity = 0
    id_2 = ''
    for m in new_list:
        if m['popularity'] > popularity:
            popularity = m['popularity']    # 129.919
            id_2 = m['id']    # 496243
    json_file = open(f'data/movies/{id_2}.json', encoding='utf-8')
    parasite = json.load(json_file)
    pop_want = ['title', 'tagline', 'genres', 'runtime', 'release_date', 'homepage', 'overview']
    
    p_d = {}
    for pw in pop_want:
        p_d[pw] = parasite[pw]
    genres = []
    for g in p_d['genres']:
        genres.append(g['name'])

    ti = f"    제목: {p_d['title']}\n"
    ta = f"    표어: {p_d['tagline']}\n"
    ge = f"    장르: {genres}\n"
    ru = f"  런타임: {p_d['runtime']}분\n"
    re = f"  개봉일: {p_d['release_date']}\n"
    ho = f"홈페이지: {p_d['homepage']}\n"
    ov = f"  오버뷰: {p_d['overview']}\n"

    popular = ti + ta + ge + ru + re + ho + ov
    return popular


movies_json = open('./data/movies.json', encoding='UTF8')
movies_list = json.load(movies_json)

print(max_popularity(movies_list))
