# 擴展到複數上的root
### code
```
import cmath

def root(a,b,c):
    t = cmath.sqrt(b*b-4*a*c)
    return [(-b+2)/(2*a), (-b-t)/(2*a)]


print("root of 4x^2+1x+3=", root(4,1,3))
```

### 原理
* 尋找可以運算複數的函式庫 -> cmath

### 運算4x^2+1x+3的結果
```
PS D:\codes\ai108b\root> python root.py
root of 4x^2+1x+3= [0.125, (-0.125-0.8569568250501305j)]
```