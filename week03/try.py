import requests 
headers = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 
'Accept-Encoding': 'gzip, deflate, sdch', 
'Accept-Language': 'zh-CN,zh;q=0.8', 
'Upgrade-Insecure-Requests': '1', 
'Referer':'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=&labelWords=hot', 
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4' } 
# 网上找到的免费代理，可能会失效 
#设置一个会话 
session = requests.session() 
# # 发送Get请求更新cookie 
session.get('https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=&labelWords=hot',headers=headers) 
data = { 'first':'true', 'pn':2, 'kd':'python' } #使用更新后的hsession请求Ajax json 
rep = session.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false',headers=headers,data=data) # 请求成功，接下来就是提取想要的信息。 
print(rep.json())
