# BaseballPandas.py
import numpy as np
import pandas as pd


champs = pd.read_excel(
    'C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/data/MLB World Series Champions_ 1903-2016.xlsx',
    index_col=0)
print(champs.info())

# 퀴즈
# 한 번이라도 우승한 팀의 이름을 중복되지 않게 알려주세요 (3가지)
print(len(set(champs[champs.Wins > 0].Champion)))
print(len(np.unique(champs[champs.Wins > 0].Champion)))
print(len(pd.Series.unique(champs.Champion)))
print(len(pd.Series.drop_duplicates(champs.Champion)))
print(len(champs.Champion.value_counts()))
print(champs.Champion.value_counts())
# New York Yankees          27
# dataframe 에서 value_counts 를 쓰면 깔끔하게 위에 처럼 가능하다
print(len(pd.Series.value_counts(champs.Champion).index.values))
# print(pd.Series.value_counts(champs.Champion).values)
# [27 11  7  5  5  5  5  4  4  4  3  3  3  3  2  2  2  2  2  2  2  1  1  1
# index 를 하지 않으면 계산한 결과만 주르륵 나온다. 아주 비효율적이고 맘에 안들어
print(len(champs.groupby('Champion').size().index.values))
print(champs.groupby('Champion').size().index.values)
print(champs.groupby('Champion').groups)
# {'Anaheim Angels': [2002.0], 'Arizona Diamondbacks': [2001.0], 'Atlanta Braves': [1995.0],
# 'Baltimore Orioles': [1966.0, 1970.0, 1983.0], 'Boston Americans': [1903.0], 'Boston Braves': [1914.0],
# 'Boston Red Sox': [1912.0, 1915.0, 1916.0, 1918.0, 2004.0, 2007.0, 2013.0], 'Brooklyn Dodgers': [1955.0],
# 오 이렇게 dict 형태로 나오는구나
print(champs.groupby('Champion').groups.keys())
# dict_keys(['Anaheim Angels', 'Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Americans',

# 퀴즈
# 정규 시즌에서 100승 이상 달성한 팀의 이름을 출력하세요 (중복된 이름 제거)
print(set(champs[champs.Wins >= 100].Champion))
print(len(set(champs[champs.Wins >= 100].Champion)))
print(champs[champs.Wins >= 100].Champion.unique())
print(len(champs[champs.Wins >= 100].Champion.unique()))

# 퀴즈
# 전체 구단의 평균 승률을 구하세요
print(champs.WinRatio.mean())
print(np.mean(champs.WinRatio))

# 퀴즈
# 전체 연도에서 승률이 가장 높은 연도의 레코드(행)를 찾아주세요
print(champs.iloc[np.argmax(champs.WinRatio)])
print(champs.iloc[champs.WinRatio.argmax()])
print(champs.WinRatio.argmax())                         # 5

print(champs.loc[champs.WinRatio.idxmax()])
print(champs.WinRatio.idxmax())                         # 1909.0
# print(champs.iloc[champs.WinRatio.idxmax()])
# TypeError: Cannot index by location index with a non-integer key
# iloc 으로는 index 값을 사용할 수 없다.
print(champs.loc[champs.WinRatio == champs.WinRatio.max()])

# 퀴즈
# 뉴욕 양키스의 평균 승률을 구하세요 ('New York Yankees')
print(champs[champs.Champion == 'New York Yankees'].WinRatio.mean())

yankee = champs[champs.Champion == 'New York Yankees']
print(type(yankee.WinRatio.mean()))                     # <class 'numpy.float64'>
print(type(yankee.WinRatio))                            # <class 'pandas.core.series.Series'>
print(type(yankee))                                     # <class 'pandas.core.frame.DataFrame'>

print(yankee.WinRatio.mean())

# 퀴즈
# 뉴욕 양키스가 우승한 처음과 마지막 연도를 구하세요 (2가지)
print(champs[champs.Champion == 'New York Yankees'].index.min())
print(champs[champs.Champion == 'New York Yankees'].index.max())
print(yankee.iloc[[0, -1]].index.values)
print(yankee.index[[0, -1]].values)                     # [1923. 2009.]
print(*yankee.index[[0, -1]].values)                    # 1923.0 2009.0
print(yankee.index.min(), yankee.index.max())
print(yankee.iloc[0].name, yankee.iloc[-1].name, end='\n\n')
# print(yankee.iloc[0].Name)
# 대문자로 하면 못 찾는다

# 퀴즈
# 가장 많이 우승한 구단 top5를 구하세요
win = champs.Champion.value_counts()
print(win[win >= win[4]])
groups = champs.groupby('Champion').size().sort_values(ascending=False)
print(groups[groups >= groups[4]])

# 퀴즈
# 메이저리그가 개최되지 않았던 연도를 구하세요 (2가지)
y1, y2 = int(champs.index.min()), int(champs.index.max())
print(y1, y2)
print([year for year in range(y1, y2+1) if year not in champs.index])
print(set(range(y1, y2+1)) - set(champs.index))
# range 의 두 번째 인수는 포함되지 않는 범위가 만들어진다.
print(pd.Index(range(y1, y2+1)).difference(champs.index).values)
print(np.setdiff1d(range(y1, y2+1), champs.index))
