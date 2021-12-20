# MoviesPandas_03.py
import pandas as pd
import numpy as np
import time
from tqdm import tqdm

movies = pd.read_csv('C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/ml-1m/movies.dat',
                     delimiter='::', engine='python', header=None,
                     names=['movie_id', 'title', 'genre'])
ratings = pd.read_csv('C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/ml-1m/ratings.dat',
                      delimiter='::', engine='python', header=None,
                      names=['user_id', 'movie_id', 'rating', 'timestamp'])
users = pd.read_csv('C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/ml-1m/users.dat',
                    delimiter='::', engine='python', header=None,
                    names=['user_id', 'gender', 'age', 'occupation', 'zip_code'])


df = pd.merge(pd.merge(users, ratings), movies)
print(df.info())

# 퀴즈
# 영화 데이터에 대해 영화에 대해 성별 평점을 구하세요.
p1 = df.pivot_table(values='rating', index='title', columns='gender')
print(p1)                                               # 3706, 2

# 퀴즈
# 평점 갯수가 500개 이상인 영화를 알려주세요.
p2 = df.pivot_table(values='rating', index='title', aggfunc='count')
print(p2[p2.values >= 500])
print(df.isna().sum())

counts = df.title.value_counts()
print(counts[counts >= 500])
# 이 방법은 자동으로 정렬까지 해주네

print(len(df.title.values))                 # 1000209
print(len(p1.index.values))                 # 3706

start = time.time()
# for title in tqdm(p1.index.values):
#     cnt = np.sum(df.title == title)
#     if cnt >= 500:
#         print(title, cnt)
# print(time.time()-start)                # 176.9962158203125
# 위의 방법은 연산량이 3706 * 1000209

# 이걸 획기적으로 줄일 수 있는 방법이 없을까
# 아래의 방법으로 하면 176.9962158203125 -> 0.45782947540283203 로 줄어든다
counts_500 = {}
for title in tqdm(df.title.values):
    if title not in counts_500:
        counts_500[title] = 1
    else:
        counts_500[title] += 1

counts_500_list = []
for k in tqdm(counts_500.items()):
    if k[-1] >= 500:
        counts_500_list.append(k)

print(time.time() - start)              # 0.45782947540283203
print(len(counts_500_list))             # 618

count = df.groupby('title').size()
over500 = count[count.values >= 500]
print(over500[over500 >= 500])


# 퀴즈
# 평점이 500개 이상인 영화들에 대한 평점을 알려주세요.
print(p1.loc[over500.index])
print(p1[p1.index.isin(over500.index)], end='\n\n')

# 퀴즈
# 평점 500개 이상의 영화에 대해 여성들이 가장 좋아하는 영화 top5 를 알려주세요.
rating_500 = p1.loc[over500.index]
print(rating_500.sort_values(by='F', ascending=False))
print(p1.loc[over500.index, 'F'].sort_values(ascending=False).head())
print(rating_500.nlargest(5, columns='F'))
print()

# numpy 로 푸는 방법
print(rating_500.iloc[np.argsort(rating_500.F.values)[-5:][::-1]])
print(np.argsort(rating_500.F.values)[-5:][::-1])
# 오 이렇게 하면 뒤집을 수 있구나
print(np.argsort(rating_500.F.values)[-5:])

# 퀴즈
# 평점 500개 이상의 영화에 대해 여성들이 남성들보다 좋아하는 영화를 알려주세요.
print(type(rating_500))
print(rating_500.loc[rating_500.F > rating_500.M])
rating_500['diff'] = rating_500.F > rating_500.M
print(rating_500[rating_500.F > rating_500.M].sort_values(by='diff', ascending=False))


