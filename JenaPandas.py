# JenaPandas.py
import pandas as pd
import time

jena = pd.read_csv('C:/Users/helen/PycharmProjects/PythonBasic/Python Basics/data/jena_climate_2009_2016.csv',
                   index_col=0)
print(jena.info())

border_date = '01.01.2016 00:00:00'
pos = jena.index.get_loc(border_date)
print(pos)                                                              # 368291

print(jena.loc[border_date])
print(jena.iloc[pos])

# 퀴즈
# 2016년 1월 데이터를 추출하세요
print(jena.loc[border_date:'31.01.2016 23:50:00'])
print(jena.loc[border_date:'01.02.2016 00:00:00'])
# pandas 는 두 번째 인자까지 포함해서 출력한다.
# 따라서 바로 위의 코드문은 틀렸다
print(jena.iloc[pos:pos+144*31])

base = time.time()
# jena.index = pd.to_datetime(jena.index)                               # 32.28164052963257
# string => datetime (index 의 개별 형식을 찾는 과정에서 시간이 오래 걸림)

jena.index = pd.to_datetime(jena.index, format='%d.%m.%Y %H:%M:%S')     # 0.7991664409637451

start = time.time()
print(jena.iloc[pos:pos+144*31])

middle = time.time()
print(jena.loc['01.01.2016'])

end = time.time()

print('base     :', start - base)       # base     : 1.3632173538208008, 33.42865777015686
print('slicing  :', middle - start)     # slicing  : 0.06921601295471191
print('datetime :', end - middle)       # datetime : 0.0269167423248291

print(jena.loc['31.01.2016'])                   # 1월 31일
print(jena.loc['01.31.2016'])                   # 1월 31일

print(jena.loc['09.07.2016'])                   # 9월 7일
print(jena.loc['07.09.2016'])                   # 7월 9일

print(jena.loc['2016-01-31'])
print(jena.loc['01-31-2016'])
print(jena.loc['31-01-2016'])
print(jena.loc['2016/01/31'])
print(jena.loc['01/31/2016'])
print(jena.loc['2016/01'])
print(jena.loc['2016-01'])
print(jena.loc['2016 8 15'])
print(jena.loc['160915'])                       # 2015년 9월 16일
print(jena.loc['032015'])                       # 2015년 3월 20일
print(jena.loc['090326'])
print(jena.loc['20090326'])
print(jena.loc['01-2009'])
print(jena.loc['mar 2014'])
print(jena.loc['mar 15, 2014'])
print(jena.loc['mar 15 2014'])
print(jena.loc['2014 dec'])
print(jena.loc['2014 dec 25'])


