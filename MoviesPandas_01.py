# MoviesPandas_01.py
import operator
import pandas as pd
import collections


pd.set_option('max_columns', 1000)
pd.set_option('display.width', 1000)


def get_ratings():
    # 퀴즈
    # 영화 데이터 파일 3개를 읽어오세요 (경고가 있으면 안됩니다)
    movies = pd.read_csv('C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/ml-1m/movies.dat',
                         delimiter='::', engine='python', header=None,
                         names=['movie_id', 'title', 'genre'])
    ratings = pd.read_csv('C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/ml-1m/ratings.dat',
                          delimiter='::', engine='python', header=None,
                          names=['user_id', 'movie_id', 'rating', 'timestamp'])
    users = pd.read_csv('C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/ml-1m/users.dat',
                        delimiter='::', engine='python', header=None,
                        names=['user_id', 'gender', 'age', 'occupation', 'zip_code'])

    # 퀴즈
    # movies 데이터프레임을 아래 코드에 연동하세요
    df = pd.merge(pd.merge(users, ratings), movies)
    print(df.info())

    return df


if __name__ == '__main__':
    df = get_ratings()

    # 퀴즈
    # 가장 많이 본 영화 제목을 알려주세요
    # 1번
    freq = collections.Counter(df.title)
    # print(freq)                         # 자동으로 제일 많은 것부터 정렬해서 출력함
    print(freq.most_common(1))              # [('American Beauty (1999)', 3428)]

    # 2번
    uniques = {}
    for t in df.title:
        if t not in uniques:
            uniques[t] = 1
        else:
            uniques[t] += 1
    # print(uniques)
    # print(uniques.keys())                   # title 만 출력
    # print(uniques.items())                  # ("One Flew Over the Cuckoo's Nest (1975)", 1725)
    # print(type(list(uniques.items())[0]))   # <class 'tuple'>
    # tuple 형태로 되어 있네

    top1, title = 0, ''
    for k in uniques:
        if top1 < uniques[k]:
            top1 = uniques[k]
            title = k

    print(title, top1)                  # American Beauty (1999) 3428

    # 3번
    # print(df.title.value_counts)

    counts = pd.Series.value_counts(df.title)
    print(counts)
    # American Beauty (1999)                                   3428
    # Star Wars: Episode IV - A New Hope (1977)                2991
    print(type(counts))                     # <class 'pandas.core.series.Series'>
    # print(counts.index)
    print(counts[0])                        # 3428
    # index 가 각각의 title 로 되어있다보니 value 값만 나와서 이름은 안나오고 숫자만 나오는 구나
    print(counts[:1])                       # American Beauty (1999)    3428

    # 퀴즈
    # 2번에서 만들었던 딕셔너리(uniques)를 빈도순으로 정렬하세요
    print(sorted(uniques, reverse=True)[:2])
    print(sorted(uniques)[-2:])
    print()
    # 이건 뭘 기준으로 정렬한거지 대체...?
    # title 기준으로 정렬되는 구나
    # x = {'a': 5, 'b': 3, 'c': 1}
    # print(sorted(x, reverse=True))
    # dict 형태일 때는 key 값을 기준으로 정렬해주는 구나

    # lambda
    print(sorted(uniques, key=lambda k: uniques[k], reverse=True)[:2])
    print(sorted(uniques.items(), key=lambda item: item[0], reverse=True)[:2])  # wrong
    # tuple 형태로 되어 있기 때문에 값을 title 그대로 주는 것과 동일하다.
    # [('eXistenZ (1999)', 410), ('Zeus and Roxanne (1997)', 23)]
    print(sorted(uniques.items(), key=lambda item: item[1], reverse=True)[:2])
    # [('American Beauty (1999)', 3428), ('Star Wars: Episode IV - A New Hope (1977)', 2991)]
    # print(sorted(uniques.items(), key=lambda item: item[2], reverse=True)[:2])
    # IndexError: tuple index out of range
    # 역시 위에 내가 해석한대로 이런 에러 메세지가 나면서 멈추네
    print(sorted(uniques.items(), key=lambda item: item[-1], reverse=True)[:2])
    print(sorted(uniques.items(), key=lambda item: -item[1])[:2])
    print()

    print(sorted([(uniques[k], k) for k in uniques], reverse=True)[:2])
    print(sorted([(k, uniques[k]) for k in uniques], reverse=True, key=lambda t: t[1])[:2])
    print()

    print(sorted(uniques.items(), key=operator.itemgetter(1), reverse=True)[:2])
    print(sorted(uniques.items(), key=operator.itemgetter(0), reverse=True)[:2])
    # 이건 title 기준으로 정렬되네
    print(sorted(uniques.items(), key=operator.itemgetter(1, 0), reverse=True)[:2])
    # 먼저 values 크기로 정렬하고 title 기준으로 정렬하는 것 -> itemgetter 다중조건

