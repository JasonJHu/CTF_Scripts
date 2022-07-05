#coding:utf-8
#维吉尼亚密码处理
#Create by MAX230 20210912


strCodeList='abcdefghijklmnopqrstuvwxyz'

key='xinancool'
plaintext='cff81fu{72cemb3d9at99c32c93a60tb55f}'
ciphertext='zns81fh{72esam3a9ig99c32p93c60hp55q}'

def Vigenere_encode(key,plaintext):
    strResult=""
    i=0
    j=0
    intKeyLength=len(key)
    
    print(u"维吉尼亚加密...")
    print("Plain Text: "+plaintext)
    print("Key: "+key)
    
    for chrTmp in plaintext:
        if chrTmp in strCodeList:
            j = i % intKeyLength
            k = strCodeList.index(key[j])
            m = strCodeList.index(chrTmp)
            
            i += 1
            
            strResult += strCodeList[(m+k)%26]           
        else:
            strResult += chrTmp
    
    print("Cipher Text: "+strResult)
        
        
def Vigenere_decode(key,ciphertext):
    strResult=""
    i=0
    j=0
    intKeyLength=len(key)
    
    print(u"维吉尼亚解密...")
    print("Cipher Text: "+ciphertext)
    print("Key: "+key)

    for chrTmp in ciphertext:
        if chrTmp in strCodeList:
            j = i % intKeyLength
            k = strCodeList.index(key[j])
            m = strCodeList.index(chrTmp)

            if m < k:
                m += 26

            i += 1
            strResult += strCodeList[(m-k)]           
        else:
            strResult += chrTmp
    
    print("Plain Text: "+strResult)
    
    
choose = input("Input E(encode) or D(decode)\n\t")

if (choose == 'E' or choose == 'e'):
    plaintext = input('input plaintext:\n\t').lower()
    key = input('input key:\n\t').lower()
    Vigenere_encode(key,plaintext)
    
if (choose == 'D' or choose =='d'):
    ciphertext = input('input ciphertext:\n\t').lower()
    key = input('input key:\n\t').lower()
    Vigenere_decode(key,ciphertext)

