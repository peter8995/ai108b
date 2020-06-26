import random

'''
S = NP VP               名詞子句 + 動詞子句
NP = DET Adj* N PP*     定詞 + 名詞
VP = V NP               動詞 + 名詞子句
PP = P NP               副詞 + 名詞子句
'''

s = ['我', '學長', '學弟', '同學']
time = ['今天', '明天', '後天']
skill = ['自然音階', '五聲音階', '掃弦', '垂勾音']
speed = ['85', '90', '95', '100', '120', '130', '140']
howLong = ['15', '30', '60', '120']

def S():
    return np() + vp()

def np():
    return n() + day()

def vp():
    return '用 ' + bpm() + ' BPM 練習' + skillRand()

def bpm():
    return random.choice(speed) 

def skillRand():
    return random.choice(skill)
def n():
    return random.choice(s)

def day():
    return random.choice(time)

def practiceTime():
    return random.choice(howLong)

print(S())