"""This is board module"""
import Block

class Board:
    def __init__(self, PeaceAreaWidth = 10, BattleAreaWidth = 5):#定义面板类
        self.list=[[0 for i in range(10)] for i in range(25)]
        self.PeaceAreaWidth = PeaceAreaWidth
        self.BattleAreaWidth = BattleAreaWidth

    def erase(self):    #定义消去行的操作
        line1 = 0    #用于返回和平区消行数量
        line2 = 0    #用于返回战争区消行数量

        part1 = self.list[0 : self.PeaceAreaWidth + self.BattleAreaWidth]
        part2 = self.list[self.PeaceAreaWidth + self.BattleAreaWidth : self.PeaceAreaWidth*2 + self.BattleAreaWidth]
        dellist = []
        for i in range(self.PeaceAreaWidth):
            if 0 not in part1[i]:
                dellist.append(i)
                line1 += 1
        for i in range(self.PeaceAreaWidth, self.PeaceAreaWidth + self.BattleAreaWidth):
            if 0 not in part1[i]:
                dellist.append(i)
                line2 += 1
        while dellist:
            part1.pop(dellist.pop())

        part1 = [[0 for i in range(10)] for j in range(line1 + line2)] + part1
        self.list = part1 + part2

        return (line1, line2)


    def writein(self,y,x,direction,type):    # 在某个块生效时写入到面板里
        block = Block.Block(type,direction)
        block.move(x,y)
        for x, y in block.showblock():
            self.list[y][x] = 1
    
    def visualWriteIn(self,act,type,isFirst):
        block = Block.Block(type, act[2])
        block.move(act[1], act[0])
        for x, y in block.showblock():
            self.list[y][x] = type if isFirst else -type # 区分先后手的落块

    def reverse(self):
        for row in self.list:
            row.reverse()
        self.list.reverse()

    def clear(self):
        self.list=[[0 for i in range(10)] for i in range(25)]
    
    def checkFull(self): #用于检测是否需要消行
        for l in self.list:
            if not 0 in l:
                return True
        return False
    
    def eraseVisual(self,isFirst = True): # 返回偷消,并更新棋盘
        stolenLines = []

        part1 = self.list[0 : self.PeaceAreaWidth + self.BattleAreaWidth]
        part2 = self.list[self.PeaceAreaWidth + self.BattleAreaWidth : self.PeaceAreaWidth*2 + self.BattleAreaWidth]
        dellist = []
        for i in range(self.PeaceAreaWidth + self.BattleAreaWidth):
            if 0 not in part1[i]:
                dellist.append(i)
                k = 0 # 先手方块数
                for j in part1[i]:
                    if j > 0:
                        k += 1
                if isFirst and k <= 3:
                    stolenLines.append(i)
                elif not isFirst and k >= 7:
                    stolenLines.append(24 - i)

        n = len(dellist)
        while dellist:
            part1.pop(dellist.pop())

        part1 = [[0 for i in range(10)] for j in range(n)] + part1
        self.list = part1 + part2

        return stolenLines