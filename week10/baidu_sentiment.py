import requests 
import json
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=83WKXn2aG8l27lAjRPibTUNz&client_secret=swZWdavbhmaKGxQzsGPhFzD0fpZ3yaay'
response = requests.get(host)
if response:
    print(response.json())
access_token = response.json()['access_token']
url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token='+access_token
print(url)
headers={'Content-Type':'application/json'}
body={'text':"OV啥意思  我问小米商城说是索尼4800 "}
r = requests.post(url,headers = headers,data=json.dumps(body))
dic=r.json()
print(dic['items'][0]['sentiment'])