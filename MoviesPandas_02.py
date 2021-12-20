# MoviesPandas_02.py
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt


def get_ratings():
    start = time.time()

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
    middle = time.time()

    # 퀴즈
    # movies 데이터프레임을 아래 코드에 연동하세요
    df = pd.merge(pd.merge(users, ratings), movies)
    print(df.info())

    print('middle :', middle - start)           # middle : 3.842663049697876
    print(' merge :', time.time() - middle)     # merge : 0.46511101722717285

    return df


if __name__ == '__main__':
    df = get_ratings()

    p1 = pd.DataFrame.pivot_table(df, values='rating', columns='gender')
    print(p1, end='\n\n')
    print(type(p1))                         # <class 'pandas.core.frame.DataFrame'>
    print(p1.values)                        # [[3.62036601 3.56887853]]
    print(p1.columns)                       # Index(['F', 'M'], dtype='object', name='gender')
    print(p1.index)                         # Index(['rating'], dtype='object')
    print()

    p2 = df.pivot_table(values='rating', columns='gender')
    print(p2)
    print()

    # 퀴즈
    # 나이대별로 남녀 성별 평점을 구하세요
    p3 = df.pivot_table(values='rating', index='age', columns='gender')
    print(p3)
    p3.index = ["Under 18", "18-24", "25-34", "35-44", "45-49", "50-55", "56+"]
    print(p3)

    # 퀴즈
    # x축의 눈금을 45도로 회전시키세요
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(p3, '-')

    plt.subplot(1, 2, 2)
    plt.plot(p3)
    plt.xticks(rotation=45)

    # 바로 pivot table 을 그래프로 그리면 서로간의 호한이 잘 되지 않는다.
    # 한 페이지에 그리려고 하지만 계속 따로 노네
    # plt.subplot(1, 3, 3)
    # p3.plot(kind='bar', rot=45)
    # plt.show()

    # 퀴즈
    # 나이대별로 남녀 성별 평점을 구하세요 (index 는 사용하지 말고, columns 만 사용합니다)
    # p4 = df.pivot_table(values='rating', columns=['age', 'gender'])
    # 1, 14 로 나와서 보기 힘들다
    p4 = df.pivot_table(values='rating', index=['age', 'gender'])
    # 14, 1 로 나와서 보기 훨씬 편하다
    print(p4)

    # 퀴즈
    # 남자 25 연령대의 평점 결과를 출력하세요 (2가지)
    print(p4.loc[25].loc['M'])
    print(p4.loc[25, 'M'])
    # print(p4.loc['M', 25])
    # 순서가 바뀌면 에러가 난다.
    print(p4.iloc[5])
    print(p4.iloc[5].values)                        # [3.52678031]
    print(p4.iloc[5, 0])                            # 3.52678031398743
    print(p4.stack())
    # age  gender
    # 1    F       rating    3.616291
    #      M       rating    3.517461
    # 18   F       rating    3.453145
    #      M       rating    3.525476
    # 25   F       rating    3.606700
    #      M       rating    3.526780
    # 35   F       rating    3.659653
    #      M       rating    3.604434
    # 45   F       rating    3.663044
    #      M       rating    3.627942
    # 50   F       rating    3.797110
    #      M       rating    3.687098
    # 56   F       rating    3.915534
    #      M       rating    3.720327
    print(p4.unstack(), end='\n\n')
    #           rating
    # gender         F         M
    # age
    # 1       3.616291  3.517461
    # 18      3.453145  3.525476
    # 25      3.606700  3.526780
    # 35      3.659653  3.604434
    # 45      3.663044  3.627942
    # 50      3.797110  3.687098
    # 56      3.915534  3.720327

    # 퀴즈
    # 남녀 성별과 연령대, 직업에 따른 평점을 알려주세요
    # p5 = df.pivot_table(values='rating', index=['gender', 'age'], columns='occupation')
    # 14, 21 형태
    p5 = df.pivot_table(values='rating', index='occupation', columns=['gender', 'age'])
    # 21, 14 형태
    p5.index = ["other", "academic/educator", "artist", "clerical/admin", "college/grad student", "customer service",
                "doctor/health care", "executive/managerial", "farmer", "homemaker", "K-12 student", "lawyer",
                "programmer", "retired", "sales/marketing", "scientist", "self-employed", "technician/engineer",
                "tradesman/craftsman", "unemployed", "writer"]
    print(p5, end='\n\n')

    # 퀴즈
    # 남녀 성별과 연령대, 직업에 따른 평점을 알려주세요 (결측치를 0으로 채우세요)
    p6 = df.pivot_table(values='rating', index='occupation', columns=['gender', 'age'], fill_value=0)
    # 21, 14 형태
    p6.index = ["other", "academic/educator", "artist", "clerical/admin", "college/grad student", "customer service",
                "doctor/health care", "executive/managerial", "farmer", "homemaker", "K-12 student", "lawyer",
                "programmer", "retired", "sales/marketing", "scientist", "self-employed", "technician/engineer",
                "tradesman/craftsman", "unemployed", "writer"]
    print(p6, end='\n\n')

    # 퀴즈
    # 성별과 연령에 따른 각각의 평균과 합계를 알려주세요
    p7 = df.pivot_table(values='rating', index='age', columns='gender', aggfunc=['mean', 'sum'])
    print(p7, end='\n\n')

    # 퀴즈
    # 평균과 합계를 각각 구한 다음에 p7처럼 하나의 데이터프레임으로 합치세요
    p8 = df.pivot_table(values='rating', index='age', columns='gender', aggfunc=np.mean)
    p9 = df.pivot_table(values='rating', index='age', columns='gender', aggfunc=np.sum)

    print(np.concatenate([p8, p9]))     # 자동으로 axis=0 으로 진행되고 세로로 합쳐지는데 wrong
    print(np.concatenate([p8, p9], axis=1))

    print(pd.concat([p8, p9]))          # wrong
    print(pd.concat([p8, p9], axis=1, keys=['mean', 'sum']), end='\n\n')

    print(pd.merge(p8, p9, left_index=True, right_index=True))

