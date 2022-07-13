# Crypto密码学

---

## Decode(解码)

**ADFGX_decode_byPython38.py**

- ADFGX爆破脚本

**Base64_custom_byPython38.py**

- 自定义Base64映射解码

**Base64_toImage_byPython38.py**

- 通过脚本提取Base64编码的图片

**Base64嵌套解码_byPython38.py**

- 自动嵌套对Base64系列编码进行解码

---

## Cipher(古典密码)

**Carsar_decode_byPython3.py**

- 经典凯撒密码循环/爆破脚本

**Carsar_plus_byPython3.py**

- 变异凯撒密码解码

**Vigenere_decode_byPython3.py**

- 维吉尼亚密码解码

---

## Crypto(现代密码)

### RSA

**RSA_多因数_byPython38.py**

- 当N可以被分解成多个质因数时解题脚本

**RSA_dp_byPython38.py**

- 已知 n/e/dp/c，求m，其中dp ≡ d mod (p-1)

**RSA_b64decode_byPython38.py**

- 通过Base64=>byte=>long，获取c，再做RSA解密

**RSA_c1e1c2e2n_共模攻击_byPython38.py**

- 已知 n/一组e/一组c,求m

**RSA_n1c1n2c2ep_模不互素_byPython38.py**

- 已知n1c1和n2c2，以及e，其中n1和n2不互素，即存在最大公约数p

**RSA_低指数攻击_小e_中国剩余定理_byPython38.py**

-当e较小的时候，对几组nc进行低指数攻击
