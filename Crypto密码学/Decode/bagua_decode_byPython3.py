# 利用八卦来记录二进制01
# 题目：
# 西方的二进制数学的发明者莱布尼茨，从中国的八卦图当中受到启发，演绎并推论出了数学矩阵，
# 最后创造的二进制数学。二进制数学的诞生为计算机的发明奠定了理论基础。而计算机现在改变
# 了我们整个世界，改变了我们生活，而他的源头却是来自于八卦图。现在，给你一组由八卦图方位
# 组成的密文，你能破解出其中的含义吗？
#  震坤艮 震艮震 坤巽坤 坤巽震 震巽兑 震艮震 震离艮 震离艮
# 格式：NSSCTF{}

# 不同题目字典可能会有差异
strList = {"乾": "111", "兑": "110", "离": "101", "震": "100", "巽": "011", "坎": "010", "艮": "001", "坤": "000"}
strList = {"乾": "111", "兑": "011", "离": "101", "震": "001", "巽": "110", "坎": "010", "艮": "100", "坤": "000"}
sCipher = "震坤艮 震艮震 坤巽坤 坤巽震 震巽兑 震艮震 震离艮 震离艮"

flag = ""

for t in (sCipher.split(" ")):
    tFlag = ""
    iBIN = ""
    for c in t:
        iBIN += strList[c]
    flag += chr(int(iBIN, 2))

print(flag)

# Da01sall
