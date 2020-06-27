
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import pandas as pd
from time import sleep
from tqdm import tqdm

# 使用第三方库创建user-agent
ua = UserAgent()
header = {'User-Agent': ua.ie}

# 提取并返回电影的名称，类型和上映日期的函数
def get_url_info(myurl):  
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text, 'html.parser')
    #print(bs_info.find_all('div', attrs={'class': 'header'}))
    movie_name=bs_info.find('h1', attrs={'class': 'name'}).text
    movie_type=''
    tags=bs_info.find_all('li', attrs={'class': 'ellipsis'})
    for atag in tags[0].find_all('a',):
        movie_type+=atag.text
    movie_time = tags[2].text
    return [movie_name,movie_type,movie_time]


#根据猫眼电影主页提取热门电影的链接
myurl = 'https://maoyan.com/films?showType=3'
response = requests.get(myurl,headers=header)
bs_info = bs(response.text, 'html.parser')
url_list=[]
#print(bs_info.find_all('div', attrs={'class': 'header'}))
for tags in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'}):
    url_list.append('https://maoyan.com'+tags.find('a').get('href'))
#print(url_list)

#提取前10热门电影的信息并写入csv文件
movie_info = []
for url in tqdm(url_list[:10]):
    movie_info.append(get_url_info(url))
    sleep(5)
#print(movie_info)
name=['电影名称','类型','上映时间']
movie_csv=pd.DataFrame(columns=name,data=movie_info)
movie_csv.to_csv('./week01/task1/movie.csv',encoding='utf8')

