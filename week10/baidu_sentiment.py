import requests 
import json
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR,INT,FLOAT,BIGINT
import time
from tqdm import tqdm
#数据库联接设置
connect_info = 'mysql+pymysql://root:rootroot@localhost:3306/db1?charset=UTF8MB4'
engine = create_engine(connect_info) 
sql = '''
      select * from smzdm;
      '''
#从数据库中读取数据
df = pd.read_sql_query(sql, engine)
#排除字数小于5的评论
df_new = df[df['comment'].str.len()>=5]
#设置百度情感分析api
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=你的client_id&client_secret=你的client_secret'
response = requests.get(host)
if response:
    print(response.json())
access_token = response.json()['access_token']
url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token='+access_token
print(url)
headers={'Content-Type':'application/json'}

#情感分析函数
def sentiment(text):
    global url
    global headers
    body={'text':text}
    try:
        r = requests.post(url,headers = headers,data=json.dumps(body))
        dic=r.json()
    except Exception as e:
        print('分析失败')
        pass
    time.sleep(0.3)#设置分析频率，不设置引发QPS超限额错误
    return dic['items'][0]['sentiment']

tqdm.pandas()
df_new_senti = df_new.copy()
df_new_senti['sentiment'] = df_new['comment'].progress_apply(sentiment)#使用tqdm进度条
df_new_senti.sort_values(by='author',inplace=True)
df_new_senti['id']=df_new_senti.index
#保存到数据库
df_new_senti.to_sql(name = 'smzdm_senti',con = engine,if_exists = 'replace',index = False,dtype = {'id':BIGINT,'author': VARCHAR(length=255),'comment':VARCHAR(length=255),'sentiment':FLOAT(12,10)})