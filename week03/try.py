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

def callback(future):
    global result
    print('抓取成功')
    result.append(future.result)
# print(len(Positon('北京',1)))
# time.sleep(2)
# print(len(Positon('北京',2)))
# time.sleep(2)
# print(len(Positon('北京',3)))
# time.sleep(2)
# print(len(Positon('北京',4)))
# time.sleep(2)
# print(len(Positon('北京',5)))
# time.sleep(2)
# print(len(Positon('北京',6)))
# time.sleep(2)
# print(len(Positon('北京',7)))
# time.sleep(2)
from concurrent.futures import ThreadPoolExecutor
import time
citys=['北京','上海','广州','深圳']
result = []
with ThreadPoolExecutor(3) as executor:
    for i in range(1,8):
        for c in citys:
            try:
                r=executor.submit(Positon,c,i)
                r.add_done_callback(callback)
                
            except Exception as e:
                print('抓取失败')
                print(e)
            time.sleep(2)
print(len(result))