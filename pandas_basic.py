# pandas_basic.py
import pandas as pd


def series_basic():
    s1 = pd.Series([2, 1, 4, 7])
    print(s1)
    print(type(s1))                                             # <class 'pandas.core.series.Series'>

    print(s1.index)                                             # RangeIndex(start=0, stop=4, step=1)
    print(list(s1.index))                                       # [0, 1, 2, 3]
    print(s1.values)                                            # [2 1 4 7]
    print(type(s1.values))                                      # <class 'numpy.ndarray'>

    s2 = pd.Series([2, 1, 4, 7], index=['a', 'b', 'c', 'd'])
    print(s2)
    print(s2.index)                                             # Index(['a', 'b', 'c', 'd'], dtype='object')
    print(list(s2.index))                                       # ['a', 'b', 'c', 'd']

    # 퀴즈
    # s2에서 3번째 위치한 값을 읽어오는 코드를 만드세요 (2가지)
    print(s2[2])
    print(s2['c'])
    print(s2.loc['c'])
    print(s2.iloc[2])
    print('-' * 30)

    # 퀴즈
    # s2에서 1, 4, 7의 3개를 한번에 읽어오는 코드를 만드세요 (2가지)
    print(s2[1:].values)

    print(s2['b':])
    print(type(s2['b':]))
    print(s2['b':].values)
    print(list(s2['b':]))

    print(s2.loc['b':])
    print(s2.iloc[1:])

    print(s2.loc[['b', 'c', 'd']])
    print(s2.iloc[[1, 2, 3]].values)
    print()

    print(s2.drop('a'))
    print(*s2.drop('a'))
    print(*s2.drop(['a']))
    print('-' * 30)


def dataframe_basic():
    df = pd.DataFrame({
        'year': [2018, 2019, 2020, 2018, 2019, 2020],
        'city': ['busan', 'busan', 'busan', 'suwon', 'suwon', 'suwon'],
        'rain': [200, 170, 195, 250, 220, 210],
    })
    print(df.info())
    print(df, end='\n\n')

    print(df.head(), end='\n\n')
    print(df.head(1), end='\n\n')
    print(df.tail(1), end='\n\n')
    print('-' * 30)

    # 퀴즈
    # rain 컬럼을 출력하세요 (2가지)
    print(df.rain, end='\n\n')
    print(df.loc[:, 'rain'])
    print(df.iloc[:, -1])

    df.index = list('abcdef')
    print(df.index)
    print(df)
    print('-' * 30)

    # 퀴즈
    # 'mokpo' 행만 출력하세요 (2가지)
    print(df.iloc[3:], end='\n\n')
    print(df.iloc[[3, 4, 5]])

    print(df.loc['d':])
    print(df.loc['d':'f'])
    print(df.loc[['d', 'e', 'f']])
    print()

    print((df.city == 'suwon').values)                          # [False False False  True  True  True]
    print(df.loc[df.city == 'suwon'])
    print(df[df.city == 'suwon'])


# series_basic()
dataframe_basic()
