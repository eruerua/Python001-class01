import nmap
import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from functools import partial
result=[]

#拆分IP字段为列表
def deteIp(ip):
    ipList=ip.split('-')
    if len(ipList)!=1:
        ipCom= '.'.join(ipList[0].split('.')[:-1])
        n1=int(ipList[0].split('.')[-1])
        n2=int(ipList[1].split('.')[-1])
        return [ipCom + '.' + str(i) for i in range(n1,n2+1)]
    else:
        return ipList

#端口扫描函数   
def portTest(func, ip):
    print(ip+ ' is start')
    l={}
    global result
    nm = nmap.PortScanner()
    #选择扫描方式
    if func == 'ping':
        try:
            sta=nm.scan(hosts=ip,arguments='-sn')['nmap']['scanstats']['uphosts']
        except Exception as e:
            print(e)
            print(ip+'ping扫描失败')
            pass
        if sta == 0:
                pass
        print(ip+' this ip is ok')
        l[ip]=' this ip is ok'
    elif func == 'tcp':
        try:
            nm.scan(ip,'1-1024','-sV')
            tcps=nm[ip].all_tcp()
        except Exception as e:
            print(e)
            print(ip+'tcp扫描失败')
            pass
        for i in tcps:
            print('{} tcp端口 {} '.format(ip,i))
        l[ip] = tcps
    result.append(l)
    print(ip +' is finished')

#获取终端参数
parser = argparse.ArgumentParser(description='pmap')
parser.add_argument('--number', '-n', help='并发数量',default=4)
parser.add_argument('--func', '-f', help='选择进行ping测试或者tcp端口测试')
parser.add_argument('--ip', '-i', help='ip地址，必要参数', required=True)
parser.add_argument('--write', '-w', help='保存')
args = parser.parse_args()

if __name__ == '__main__':
    #将多个函数参数传递给map函数
    s = ((args.func, b) for b in deteIp(args.ip))
    with ThreadPoolExecutor(int(args.number)) as executor:
        r=executor.map(lambda p: portTest(*p), s)   
    if args.write:
        with open(args.write, 'w') as f:
            json.dump(result, f)