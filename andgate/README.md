# 想法
* 只要把答案改成orgate要的解答就可以了

# code
```
import numpy as np
import math
import gd3 as gd

def sig(t):
    return 1.0/(1.0+math.exp(-t))

o = [0,0,0,1] # and gate outputs
# o = [0,1,1,1] # or gate outputs
# o = [0,1,1,0] # xor gate outputs
def loss(p):
    [w1,w2,b] = p
    o0 = sig(w1*0+w2*0+b)       #使用sig函數計算o0-o0..o3值
    o1 = sig(w1*0+w2*1+b)
    o2 = sig(w1*1+w2*0+b)
    o3 = sig(w1*1+w2*1+b)
    delta = np.array([o0-o[0], o1-o[1], o2-o[2], o3-o[3]])      #與正解取差值
    print('o0={:.3f} o1={:.3f} o2={:.3f} o3={:.3f}'.format(o0,o1,o2,o3))
    return np.linalg.norm(delta, 2)     #取平方加總

p = [0.0, 0.0, 0.0] # [w1,w2,b] 
gd.gradientDescendent(loss, p, max_loops=1500)      #使用梯度下降法計算
```

# 結果
```
o0=0.158 o1=0.323 o2=0.323 o3=0.548
o0=0.158 o1=0.323 o2=0.325 o3=0.550
o0=0.158 o1=0.323 o2=0.323 o3=0.548
o0=0.158 o1=0.325 o2=0.323 o3=0.550
o0=0.158 o1=0.323 o2=0.323 o3=0.548
o0=0.160 o1=0.325 o2=0.325 o3=0.550
o0=0.158 o1=0.323 o2=0.323 o3=0.548
1499:p=[ 0.93112441  0.93112441 -1.67063948] f(p)=0.662 gp=[-0.06140226 -0.06140226  0.07797474] glen=0.11671
```