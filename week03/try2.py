import pandas as pd
import requests 
import time
headers = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 
'Accept-Encoding': 'gzip, deflate, sdch', 
'Accept-Language': 'zh-CN,zh;q=0.8', 
'Upgrade-Insecure-Requests': '1', 
'Referer':'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=&labelWords=hot', 
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4' } 
session = requests.session() 
# # 发送Get请求更新cookie 
session.get('https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=&labelWords=hot',headers=headers) 
def Positon(city,page):
    data = { 'first':'true', 'pn':page, 'kd':'python' } #使用更新后的hsession请求Ajax json 
    rep = session.post('https://www.lagou.com/jobs/positionAjax.json?city='+city+'&needAddtionalResult=false',headers=headers,data=data) # 请求成功，接下来就是提取想要的信息。 
    result=rep.json()['content']['positionResult']['result']
    return result
l=Positon('北京',1)
df=pd.read_json(l,encoding="utf-8")
print(df.head())