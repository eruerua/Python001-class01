import requests 
import time
import random
import pandas as pd
#抓取函数
result = []
def Positon(city,page):
    headers = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 
    'Accept-Encoding': 'gzip, deflate, sdch', 
    'Accept-Language': 'zh-CN,zh;q=0.8', 
    'Upgrade-Insecure-Requests': '1', 
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=&labelWords=hot', 
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4' } 
    session = requests.session() 
    # # 发送Get请求更新cookie 
    session.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=&labelWords=hot',headers=headers) 
    data = { 'first':'true', 'pn':page, 'kd':'python' } #使用更新后的hsession请求Ajax json 
    try:
        rep = session.post('https://www.lagou.com/jobs/positionAjax.json?city='+city+'&needAddtionalResult=false',headers=headers,data=data) # 请求成功，接下来就是提取想要的信息。 
        result=rep.json()['content']['positionResult']['result']
        print(city+str(page)+'抓取成功')
    except Exception as e:
        print('抓取失败')
        pass
    return result
#回调函数
def callback(res):
    global result
    result+=res.result()

#多线性爬虫抓取：注意广州只抓取到68个职位，其余每个城市抓取了150个
from concurrent.futures import ThreadPoolExecutor
import time

cities=['北京','广州','深圳','上海']

with ThreadPoolExecutor(4) as executor:
    for c in cities:
        for i in range(1,10):
            try:
                r=executor.submit(Positon,c,i)
                r.add_done_callback(callback)
            except Exception as e:
                print('抓取失败')
                print(e)
            #time.sleep(1)#可设置频率
        time.sleep(1)

#抓取后处理
print('开始对数据进行后处理')
df=pd.DataFrame(result)
df2=df[['city','positionName','salary']]

def cityF(df,cities):
    l=[]
    for i in cities:
        df1 = df[df['city']==i]
        df1=df1.drop_duplicates()
        if len(df1)>100:
            df1=df1[:100]
        print(i,len(df1))
        l.append(df1)
    return pd.concat(l)

df_f=cityF(df2,cities)

#保存到数据库
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.types import CHAR,INT
connect_info = 'mysql+pymysql://root:rootroot@localhost:3306/test?charset=UTF8MB4'
engine = create_engine(connect_info) 
df_f.to_sql(name = 'test1',
con = engine,
if_exists = 'replace',index = False,dtype = {'city': CHAR(length=255),'positionName': CHAR(length=255),'salary': CHAR(length=255)
}
)