# RSA核心公式推导

*2021/11/14 By Jason.J.Hu*

## 模运算

模运算与基本四则运算有些相似，但是除法除外。其规则如下：	

$$
(a + b) \quad mod \quad p = ((a \quad mod \quad p) + (b \quad mod \quad p)) \quad mod \quad p \\
(a - b) \quad mod \quad p = ((a \quad mod \quad p) - (b \quad mod \quad p)) \quad mod \quad p \\
(a * b) \quad mod \quad p = ((a \quad mod \quad p) * (b \quad mod \quad p)) \quad mod \quad p \\
a^b \quad mod \quad p = (a \quad mod \quad p)^b \quad mod \quad p
$$

## 欧拉函数

N的欧拉函数 phi(N) 就是比自然数N小的自然数中与N互质的自然数的个数。

如果p,q互质，那么phi(p x q)=phi(p) x phi(q)，例如：

* phi(2)=(2-1)=1---[1]
* phi(3)=(3-1)=2---[1,2]
* phi(6)=(2-1)(3-1)=2---[1,5]
* phi(N)=N \* (1 - 1/p) \* (1 - 1/q) \* (1 - 1/r) \* ... ...

---

## 欧拉定理

$$
设m,n \in N^+,且gcd(m,n)=1\\
则 n^{\varphi(m)}\equiv1(mod \quad m) \quad \\
或者表达为 \quad n^{\varphi(m)} \quad mod \quad m=1\\
证明过程，详见数论相关知识，此处不做展开
$$

---

## RSA相关推导过程

$$
N = p * q\\
N的欧拉函数, \quad \varphi (N) = (p-1)*(q-1) \\
e和\varphi(N)互质\\
ed \quad mod \quad \varphi(N) \quad = 1\\
------\\
RSA核心公式\\
c=m^e \quad mod \quad N \\
m=c^d \quad mod \quad N \quad \\
Why ??\\
------\\
c^d \quad mod \quad N \quad\\
= (m^e \quad mod \quad N)^d \quad mod \quad N \quad \\
= m^{ed} \quad mod \quad N... [注1]\\
= (m*m^{ed-1}) \quad mod \quad N\\
\because ed \quad mod \quad \varphi(N) \quad = 1\\
=>(ed-1) \quad mod \quad \varphi(N) = 0\\
=>(ed-1)  =  k * \varphi(N)\\
\therefore =m*(m^{k\varphi(N)}) \quad mod \quad N\\
= m*[(m^k)^{\varphi(N)}] \quad mod \quad N \quad... [注2] \\
$$

[注1]
$$
(2 \quad mod \quad10)^8 \quad mod \quad 10\\
= 2^8 \quad mod \quad 10 \\
= 256 \quad mod \quad 10 \\
= 6 \\\\

(12 \quad mod \quad 10)^8 \quad mod \quad 10\\
= ((10+2)*12^7) \quad mod \quad 10\\
= ((2)*(2)*(2)*...*(2)) \quad mod \quad 10\\
= 2^8 \quad mod \quad 10
$$

[注2]
$$
2*(100000*k+t) \quad mod  \quad 100000 \\
= (2*(100000*k) + 2*t) \quad mod \quad 100000\\
= (2*t) \quad mod \quad 100000\\
$$

使用特例验证过以后，继续证明

$$
c^d \quad mod \quad N = m*[(m^k)^{\varphi(N)}] \quad mod \quad N \\
------\\
(一)如果m和N互质 \\
由欧拉定理得出(m)^{\varphi(N)} \quad mod \quad N=1\\
m*(m^k)^{\varphi(N)} \quad mod \quad N\\
= m*(m^{\varphi(N)})^k \quad mod \quad N\\
= m \quad mod \quad N\\
= m\\
(二)如果m和N不互质\\
那么m可以表示为xp,且x<q\\
\because q是素数，\therefore m^{\varphi(q)} \quad mod \quad q = 1 \\
m^{k*\varphi(N)}=m^{k*(p-1)*(q-1)}=(m^{\varphi(q)})^{k*(p-1)}\\
(m^{\varphi(q)})^{k*(p-1)} \quad mod \quad q = 1\\
=> \quad m^{k*\varphi(N)}=(m^{\varphi(q)})^{k*(p-1)}= 1+uq\\
=> \quad m*m^{k*\varphi(N)}=m+m*uq=m+xp*uq=m+xu*N\\
=> \quad m*[(m^k)^{\varphi(N)}]=m*m^{k*\varphi(N)} \quad mod \quad N =m
$$

