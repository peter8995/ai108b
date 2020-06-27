# 圖形搜尋
## 簡介
在離散數學、演算法與人工智慧的領域，很多問題可以表示為「節點與連線所形成的圖形」，一個程式要解決某問題其實是在這個圖形裏把目標節點給找出來，於是問題求解就簡化成了圖形的搜尋，我們只要把解答給「找出來」就行了。

圖形搜尋的方法大致可以分為「深度優先搜尋 (Depth-First Search, DFS)、廣度優先搜尋 (Breath-First Search, BFS)、最佳優先搜尋 (Best-First Search, BestFS) 等三類。 

最佳優先搜尋，有一種具有理論背景，且強大好用的 A* 搜尋法可採用。
## DFS
深度優先搜尋演算法（Depth-First-Search，DFS）。這個演算法會儘可能深的搜尋樹的分支。當節點v的所在邊都己被探尋過，搜尋將回溯到發現節點v的那條邊的起始節點。這一過程一直進行到已發現從源節點可達的所有節點為止。如果還存在未被發現的節點，則選擇其中一個作為源節點並重複以上過程，整個行程反覆進行直到所有節點都被存取為止。
## BFS
與DFS不同的是，會先往寬的方向搜尋
用以下動圖來說明
![image](Animated_BFS.gif)
## A*
在此演算法中，如果以g(n)表示從起點到任意頂點n的實際距離，h(n)表示任意頂點n到目標頂點的估算距離（根據所採用的評估函式的不同而變化），那麼A*演算法的估算函式為：
f(n)=g(n)+h(n)

這個公式遵循以下特性：
* 如果g(n)為0，即只計算任意頂點n到目標的評估函式h(n)，而不計算起點到頂點n的距離，則演算法轉化為使用貪心策略的最良優先搜尋，速度最快，但可能得不出最佳解；
* 如果h(n)不大於頂點n到目標頂點的實際距離，則一定可以求出最佳解，而且h(n)越小，需要計算的節點越多，演算法效率越低，常見的評估函式有——歐幾里得距離、曼哈頓距離、切比雪夫距離；
* 如果h(n)為0，即只需求出起點到任意頂點n的最短路徑g(n)，而不計算任何評估函式h(n)，則轉化為單源最短路徑問題，即Dijkstra演算法，此時需要計算最多的頂點；

### 使用BFS實作拼圖問題
```
from copy import deepcopy

def enqueue(a, o):
    a.insert(0,o)

def dequeue(a):
    return a.pop()

def findXY(board, value):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == value:
                return x,y
    return None

def boardClone(b):
    return deepcopy(b)

def board2str(b):
    rows = []
    for row in b:
        rows.append(str(row))
    return '\n'.join(rows)

def swap(b,x1,y1,x2,y2):
    x2 = round(x2)
    y2 = round(y2)
    if x2<0 or x2 > 2 or y2<0 or y2>2:
        return False
    t = b[x1][y1]
    b[x1][y1]=b[x2][y2]
    b[x2][y2]=t
    return True

def move(board, dir): # 加入所有可能的移動方式
    x,y = findXY(board, 0) # 找出空格 0 的位置
    nboard = boardClone(board)
    s = False
    if dir == 'up':
        s=swap(nboard,x,y,x-1,y) # 空格和上面一格交換
    elif dir == 'right':
        s=swap(nboard,x,y,x,y+1) # 空格和右邊一格交換
    elif dir == 'down':
        s=swap(nboard,x,y,x+1,y) # 空格和下面一格交換
    elif dir == 'left':
        s=swap(nboard,x,y,x,y-1) # 空格和左邊一格交換

    return nboard if s else None

def moveAdd(board, dir, neighbors): # 向 dir 方向移動，並加入到 neighbors 陣列中
    nboard = move(board, dir)
    if nboard != None:
        neighbors.append(nboard)

def getNeighbors(board): # 取得所有鄰居
    neighbors = []
    moveAdd(board, 'up',    neighbors)
    moveAdd(board, 'down',  neighbors)
    moveAdd(board, 'right', neighbors)
    moveAdd(board, 'left',  neighbors)
    return neighbors

def bfs(q, goal): # 廣度優先搜尋
    while len(q) > 0:
        node = dequeue(q) #  否則、取出 queue 的第一個節點。
        nodestr = board2str(node)
        if node == goal: return True
        if visited.get(nodestr) == None: #  如果該節點尚未拜訪過。
            visited[nodestr] = True      #    標示為已拜訪
        else:                            #  否則 (已訪問過)
            continue                     #    不繼續搜尋，直接返回。
        neighbors = getNeighbors(node)   #  取出鄰居。
        for n in neighbors:              #  對於每個鄰居
            nstr = board2str(n)
            if visited.get(nstr) == None:#  假如該鄰居還沒被拜訪過
                parent[nstr] = nodestr
                level[nstr] = level[nodestr] + 1
                enqueue(q, n)            # 就放入 queue 中
    return False

def backtrace(goal):
    print('======= backtrace =========')
    nodestr = board2str(goal)
    while nodestr != None:
        print('{}\n'.format(nodestr))
        nodestr = parent.get(nodestr)

goal = [[1,2,3], 
        [8,0,4],
        [7,6,5]]

start= [[1,3,4], 
        [8,2,5],
        [7,0,6]]

queue=[start] # BFS 用的 queue, 起始點為 1。
visited={}
parent={}
level={}
level[board2str(start)]=0
found = bfs(queue, goal) #  呼叫廣度優先搜尋。
print('bfs:found=', found)
if found:
    backtrace(goal)
```
執行結果
```
PS D:\codes\ai108b\myNote\04-圖形搜尋> python .\puzzleSearch.py
bfs:found= True
======= backtrace =========
[1, 2, 3]
[8, 0, 4]
[7, 6, 5]

[1, 0, 3]
[8, 2, 4]
[7, 6, 5]

[1, 3, 0]
[8, 2, 4]
[7, 6, 5]

[1, 3, 4]
[8, 2, 0]
[7, 6, 5]

[1, 3, 4]
[8, 2, 5]
[7, 6, 0]

[1, 3, 4]
[8, 2, 5]
[7, 0, 6]
```
### [參考資料](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/04-%E5%9C%96%E5%BD%A2%E6%90%9C%E5%B0%8B)
[拼圖問題](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/04-%E5%9C%96%E5%BD%A2%E6%90%9C%E5%B0%8B/D-%E5%AF%A6%E4%BD%9C%EF%BC%9A%E6%8B%BC%E5%9C%96%E5%95%8F%E9%A1%8C)   
[DFS](https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2 )    
[BFS](https://zh.wikipedia.org/zh-tw/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2)    
