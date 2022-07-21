#将指定文件夹下的文件按顺序解码
import os
import zxing

path = "output"

files= os.listdir(path) 

# 按e和.将文件序号截出排序------依据实际情况修改
# files.sort(key=lambda x:int(x.split('e')[1].split(".")[0]))
files.sort(key=lambda x:int(x.split(".")[0]))
reader = zxing.BarCodeReader()
print(files)
# 结果
string=''
for file in files:
    barcode = reader.decode(path+"\\"+file)
    print(file)
    # print(barcode.parsed,end="") #连续输出
	  # 需要分隔的情况
    # string+=barcode.parsed+','
    string+=barcode.parsed
print(string)

