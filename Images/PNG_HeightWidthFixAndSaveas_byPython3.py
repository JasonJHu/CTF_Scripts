import os
import binascii
import struct
from tqdm import tqdm

img = open("0509.png", "rb").read()
for w in range(10000):
    for h in range(10000):
        data = img[0xc:0x10] + struct.pack('>i', w) + struct.pack('>i', h) + img[0x18:0x1d]
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == struct.unpack('>i', img[0x1d:0x21])[0] & 0xffffffff:
            print(w, h)
            print(hex(w), hex(h))
            open("new2.png", "wb").write(img[:0xc] + data + img[0x1d:])
            exit()
