# 想法
* 誤差是取近似值時產生的，所以讓step小一點
* 多次測試後發現0.04時誤差已經很小了

# code
```
from math import *

step = 0.04
def df(f, x, h=step):
    return (f(x+h)-f(x-h))/(2*h)

def dfn(f, x, n, h=step):
    if (n == 0): return f(x)
    if (n == 1): return df(f,x,h)
    return (dfn(f, x+h, n-1) - dfn(f, x-h, n-1))/(2*h)

print('df(sin, pi/4)=', df(sin, pi/4))

for i in range(10):
    print('dfn(sin,', i, 'pi/4)=', dfn(sin, pi/4, i))
```

# 結果
```
PS D:\codes\ai2\python\08-scientific\calculus> python diffn.py
df(sin, pi/4)= 0.7069182344626015
dfn(sin, 0 pi/4)= 0.7071067811865476
dfn(sin, 1 pi/4)= 0.7069182344626015
dfn(sin, 2 pi/4)= -0.7067297380137713
dfn(sin, 3 pi/4)= -0.7065412918265054
dfn(sin, 4 pi/4)= 0.7063528958896337
dfn(sin, 5 pi/4)= 0.7061645501450428
dfn(sin, 6 pi/4)= -0.7059762545174986
dfn(sin, 7 pi/4)= -0.705787998569099
dfn(sin, 8 pi/4)= 0.7055993032588705
```