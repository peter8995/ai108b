objs = ["人", "狼", "羊", "菜"]
state= [   0,  0 ,   0,    0 ]

def neighbors(s):
  side = s[0]
  next = []
  checkAdd(next, move(s,0))
  for i in range(s.length ):
      if s[i]==side:
        checkAdd(next, move(s, i))
  return next


def checkAdd(next, s):
  if not isDead(s):
    next.push(s)

def isDead(s):
  if (s[1]==s[2] and s[1]!=s[0]): return True; #狼吃羊
  if (s[2]==s[3] and s[2]!=s[0]): return True; # 羊吃菜
  return False

#帶著 obj 移到另一邊
def move(s, obj) :
  newS = s[:] #複製一份陣列
  side = s[0]
  if side == 0:
    anotherSide = 1
  else :
    anotherSide = 0
  newS[0] = anotherSide
  newS[obj] = anotherSide
  return newS

visitedMap = {}

def visited(s):
  string = ''
  stra = s.join(string)
  if (type(visitedMap[stra]) != None): return True

def isSuccess(s) :
  for i in range(s.length):
    if (s[i]==0) : return False        
  return True

def state2str(s) :
  str1 = ""
  for i in range(s.length):
      str1 += objs[i]+s[i]+" "
  return str1

path = []

def printPath(path) :
  for i in range(path.length):
    print(state2str(path[i]))


def dfs(s) :
  if (visited(s)) :
    path.push(s)
  if (isSuccess(s)) :
    print("success!")
    printPath(path)
    return
  visitedMap[s.join('')] = True
  neighborsList = neighbors(s)
  for i in neighborsList:
    dfs(neighborsList[i])
  path.pop()


dfs(state)