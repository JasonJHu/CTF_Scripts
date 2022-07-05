#-*- coding: UTF-8 -*- 
# Pythen 3.8

# 密文afZ_r9VYfScOeO_UL^RWUc
# 明文flag{...}
# 等差变化 5/6/7/8/9/...

def carsar_decode(sCiper):
    j = 5
    i = 0
    sReturn = []
    for i in range(len(sCiper)):
        m = ord(sCiper[i])          # 将密文的第i个字母变为其ascii码值
        m = m + j                 # ascii值+j
        sReturn.append(chr(m))           # 将递进后的ascii值存入列表lmstr[]
        j += 1
    return ''.join(sReturn)


if __name__ == '__main__':
    sCiper = 'afZ_r9VYfScOeO_UL^RWUc'    # 密文
    sMessage = []
    sMessage = carsar_decode(sCiper)
    print(sMessage)
