#-*- coding: UTF-8 -*- 
# by Python3.8
# 自定义Base64映射表加解密

import base64
import string


strCipher = "xw/YxPtL3rxiXzstEysBEaJW"
origin = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
new    = "4cdpTyFakGmH2LE5K8q3o+hvbxRfXIDi0YzN=ZwQVe1OgtjMA/BSJrlPUn67us9CW"

strCipher="FlZNfnF6Qol6e9w17WwQQoGYBQCgIkGTa9w3IQKw"
origin="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
new='JKLMNOxyUVzABCDEFGH789PQIabcdefghijklmWXYZ0123456RSTnopqrstuvw+/='

strCipher="aPdwI4qwI4qwI4BVnpaeoFxjEgCOUZtiXBdgZ6TCXBsiW8NiNS+mDfdwIPsjDV7jWSNiNSjKaPdwDV7jI4qwI8tmDfsjDfsjIPsjR8bwDVqwDV7jIPsKaPsjI4qwIPsjI8jmDfsjIPsjI47jRZjiycP+yCq4UcqHYxaXZXlNnVlSrm9vLpaYrx6jbrdMDgxfbBywErTg06uB6rhB0PfV0l93xFU8nFIkIDaqovbRLOfiW8nq9myPb6UpZPlRZfTyDmd96xaDxCxrxBGUrFCSYvblUFnK0r5kEgBMEcqToiyfnXUcLpl2I4P/IV9ByOo+HZu3a/m5RZmAUFyuEcylR8bwI47jDVqwI475HvxvYrjKaPdwI4qwI4qwI8mAUryKE/7iwgGfErjJwgGlYr9J8OTf0XbuUD+fI49tDFdfNPU3nr1mw8df0XbuUD+Rw8dKUrCmwOTSEvb1wtKs04PJDFdfNPU3nr1mw8dKID+Rwp7JxgGlNpaloXxlocblU8qx6mjtWV9jy8qcYXItEFdfNgU3nr1mNgdMNpbK0XItovx/nFx/WOj3o4+Rw8dSEvb1wOj30pbhE4+RaVh7UXUGE8tmXBqw6BbEavGG0gCKYZnnRDu="
origin="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
new="7q84PCgpNaRWIyHw9bZD6xrXYU0EonLetGSOmlFiK5QkuhM3jT/VfBvc+12AsdJz="

print("*"*10)
print("len(origin):"+str(len(origin)))
print("len(new):"+str(len(new)))
print (base64.b64decode(strCipher.translate(str.maketrans(new,origin))).decode())
