# 邏輯推論
欄位 | 內容
-----|--------
教學網站 | [邏輯推論](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/06-%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96/A-%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96%E7%B0%A1%E4%BB%8B)


## 布林邏輯與公理系統
想要理解甚麼是數學，最快速的捷徑是從公理系統下手，因為公理系統是數學證明的核心，理解了公理系統之後，就可以看懂數學家到底在玩甚麼遊戲了！

但是、很多數學的公理系統太過複雜，因此很難解釋，讀者往往在還沒入門之前，就已經先恍神了，所以為了讓大家很容易的理解公理系統，我們選擇了一個最簡單的數學體系，那就是布林邏輯。

布林邏輯只有兩個值，那就是 0 與 1 ，所以可以說是最簡單的數學體系了，就讓我們從布林邏輯開始，理解何謂公理系統吧！
## 布林邏輯
對於單一變數 x 的布林系統而言，x 只有兩個可能的值 (0 或 1)。

對於兩個變數 x, y 的布林系統而言，(x, y) 的組合則可能有 (0,0), (0,1), (1,0), (1,1) 四種。

對於三個變數 x, y, z 的布林系統而言，(x, y, z) 的組合則可能有 (0,0, 0), (0,0,1), (0,1,0), (0,1,1), (1,0, 0), (1,0,1), (1,1,0), (1,1,1) 八種。

## 範例
```
import re

class KB:
    def __init__(self): # 物件的建構函數
        self.rules = [] # 所有規則
        self.facts = {} # 所有已被滿足的事實

    def load(self, code): # 載入知識庫
        lines = re.split(r'[\.]+ ?', code)
        print(lines)
        for line in lines:
            if len(line.strip()) > 0:
                self.addRule(line)

    def isFact(self, term): # 判斷 term 是否為事實
        if len(term) == 0:
            return True
        return self.facts.get(term) != None

    # check 函數的作用
    #     以 鳥類 <= 會飛 & 生蛋. 為例
    #     rule['terms'] = ['會飛' , '生蛋']
    #     只要 ['會飛' , '生蛋'] 都被滿足了， check 就會傳回 true
    #     此時 forwardChaining 就會把結論 鳥類 加入事實庫。
    
    def check(self, rule): # 檢查規則 rule 是否所有前提都被滿足
        for term in rule['terms']:
            if self.isFact(term.strip()):
                continue
            else:
                return False
        return True

    def addFact(self, term): # 把 term 加入事實庫
        self.facts[term] = True
        print("addFact({})".format(term))

    def addRule(self, line): # 剖析規則
        m = re.match(r"^([^<=]*)(<=(.*))?$", line)
        head = "" if m.group(1)==None else m.group(1).strip()
        terms= "" if m.group(3)==None else m.group(3).strip().split(r"&")
        print("rule:head={} terms={}".format(head, terms))
        rule = {
          'head': head,
          'terms':terms,
          'satisfy':False
        }
        self.rules.append(rule)

    def forwardChaining(self): # 前向推論的演算法
        while True:
            anySatisfy = False

            for rule in self.rules:     # 對於每一條規則
                if not rule['satisfy']: # 如果該規則還沒被滿足
                    if self.check(rule): # 就檢查該規則的前提是否全都滿足
                        self.addFact(rule['head']) # 若是就將結論加入事實庫
                        rule['satisfy'] = True # 設定該規則已被滿足
                        anySatisfy = True # 這次的推理至少有一條新規則被滿足了。
                
            if not anySatisfy: # 若沒有新規則被滿足，推理就結束了。
                break

        print("facts=", self.facts.keys())
```