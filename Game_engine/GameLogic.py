import random
class GameLogic:
    
    def __init__(self) :
        self.numericMatrix = [   [13,14,15] ,
                        [6,5,4],
                        [7,8,3],
                        [0,1,2],
                        [10,11,12]  ]
        
        self.displaymatix = [[],[],[],[],[]]
        

    def placeObject(self,cd,rd):
        for i in range(0,5):
            for k in range(0,3):
                if self.numericMatrix[i][k] == cd:
                    self.displaymatix[i][k] = rd
    
    def displayMatrixState(self,o1,o2,o3,c1,c2,c3):
        self.displaymatix = [["","",""],["","",""],["","",""],["","",""],["","",""]]
        positions = [o1,o2,o3,c1,c2,c3]
        replacalpositions = ["o1","o2","o3","c1","c2","c3"]
        for p in range(0,6):
            self.placeObject( positions[p],replacalpositions[p])
        return self.displaymatix
    
    def initialMatrix(self):
        return self.displayMatrixState(13,14,15,10,11,12)
    
    def firstComputerMove(self):
        r  = random.randint(0,100)
        c1 =  r % 9
        return c1
    
    def firstUserInpu_is_tValid(self,c1,o1):
        if o1 != c1 and  o1 < 9:
            return True
        else: return False

    def TakeUserFirstInput(self,c1):
        o1  = int(input("enter you move "))
        while not self.firstUserInpu_is_tValid(c1,o1):
            o1  = int(input("enter you move "))
        if self.firstUserInpu_is_tValid(c1,o1):
            return o1
    
    def SinglePositionTargets(self,position):
        targets = []
        if position%2 == 1:
            targets.append((position -1)%8)
            targets.append((position+1)%8)
            targets.append((position+4)%8)
            targets.append(8)

        if position != 8 and position%2 == 0:
            targets.append((position -1)%8)
            targets.append((position+1)%8)
            targets.append((position -2)%8)
            targets.append((position+2)%8)
            targets.append((position+4)%8)
            targets.append(8)

        if position == 8:
            for i in range(0,8):
                targets.append(i)

        return targets
    
    def is_win(self,FP, SP, TP):
        winmatirx  = [
         [0,1,2],[2,3,4],[4,5,6],[6,7,0],[0,8,4],[1,8,5],[2,8,6],[3,4,7]
         ]
        
        if FP != SP and FP != TP  and SP != TP:
            for wm in winmatirx:
                if SP in wm  and FP in wm  and TP in wm:
                    return True
                
        return False
    
    def secondComputerMove(self,c1,o1):
        targets  = self.SinglePositionTargets(c1)
        if o1 in targets:
            for i in range(0,9):
                if self.is_win(c1,o1,i):
                    od =  i
                    break
            targets.remove(o1)
            targets.remove(od)
        return targets[random.randint(0,targets.__len__()-1)]
    
    def takeUserSecondInput(self,c1,o1,c2):
        o2  = int(input("enter you move "))
        while not self.firstUserInpu_is_tValid(c1,o2) or not self.firstUserInpu_is_tValid(o1,o2) or not self.firstUserInpu_is_tValid(c2,o2):
            o2  = int(input("enter you move "))
        if self.firstUserInpu_is_tValid(c1,o2) and self.firstUserInpu_is_tValid(c2,o2)  and  self.firstUserInpu_is_tValid(o1,o2):
            return o2