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
    
       

      