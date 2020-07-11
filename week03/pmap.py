import nmap
import argparse
import json
#扫描tcp端口
# nm = nmap.PortScanner()#端口扫描
# print(nm.scan('180.101.49.12','1-1024','-sV'))
# print(nm['180.101.49.12']['tcp'])
# 扫描主机是否存活
# scan = nm.scan(hosts='192.168.0.1',arguments='-sn')
# print(scan['nmap']['scanstats']['uphosts'])
def deteIp(ip):
    ipList=ip.split('-')
    if len(ipList)==2:
        ipCom= '.'.join(ipList[0].split('.')[:-1])
        n1=int(ipList[0].split('.')[-1])
        n2=int(ipList[1].split('.')[-1])
        return ipCom,range(n1,n2+1)
    else:
        ipCom= '.'.join(ipList[0].split('.')[:-1])
        n1=int(ipList[0].split('.')[-1])
        return ipCom+'.',[n1]
    


def portTest(number, func, ip, write):
    l={}
    result=[]
    ipCom,ipList = deteIp(ip)
    nm = nmap.PortScanner()
    if func == 'ping':
        for i in ipList:
            ip=ipCom+str(i)
            sta=nm.scan(hosts=ip,arguments='-sn')['nmap']['scanstats']['uphosts']
            if sta == 0:
                pass
            else:
                print(ip+' this ip is ok')
                l[ip]=' this ip is ok'
    elif func == 'tcp':
        for i in ipList:
            ip=ipCom+str(i)
            print(ip)
            nm.scan(ip,'1-1024','-sV')
            print(nm[ip]['tcp'])
            l[ip] = nm[ip].all_tcp()
    result.append(l)
    print(result)
    with open(write, 'w') as f:
        json.dump(result, f)

            



parser = argparse.ArgumentParser(description='pmap')
parser.add_argument('--number', '-n', help='并发数量',default=4)
parser.add_argument('--func', '-f', help='选择进行ping测试或者tcp端口测试')
parser.add_argument('--ip', '-i', help='ip地址，必要参数', required=True)
parser.add_argument('--write', '-w', help='保存')
args = parser.parse_args()

if __name__ == '__main__':

    portTest(args.number, args.func, args.ip,args.write)
