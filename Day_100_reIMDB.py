# Day_100_reIMDB.py
import requests
import re

url = 'https://www.imdb.com/chart/top/'

temp = requests.get(url).text
print(temp)
temp1 = re.sub('\n|\t|\s','' ,temp)
# <a href="/title/tt0068646/"
# > width="45" height="67" alt="Daeboo"/>
# </a>

titles = re.findall(r'alt="(.+)"/>', temp)
# print(titles)
# print(len(titles))

# <strong title="9.2 based on 2,498,691 user ratings">9.2</strong>
ratings = re.findall(r'<strong title=.+ratings">([0-9.]+)</strong>', temp)
# print(ratings)
# print(len(ratings))

ranks = re.findall(r'<span name="rk" data-value="([0-9]+)"></span>', temp)
ranks2 = re.findall(r'<td class="titleColumn">.*([0-9]+).*<a href', temp1)
print(ranks)
print(len(ranks))
# print(ranks)
# print(len(ranks))
# for i, movie in enumerate(zip(titles, ratings)):
#     print(f'{i+1:03d} :: {movie[0]} | {movie[1]}')

# for i in zip(ranks, titles, ratings):
#     print(f'{int(i[0]):03d} :: {i[1]} | {i[2]}')

# <td class="titleColumn">
#       241.
#       <a href
