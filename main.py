from Game_engine.GameLogic import GameLogic
Start = GameLogic()
c1 =10
c2 = 11
c3  = 12
o1 = 13
o2 = 14
o3 = 15


c1 = Start.firstComputerMove()
print(Start.displayMatrixState(o1,o2,o3,c1,c2,c3))

o1 = Start.TakeUserFirstInput(c1)
print(Start.displayMatrixState(o1,o2,o3,c1,c2,c3))

c2 = Start.secondComputerMove(c1,o1)
print(Start.displayMatrixState(o1,o2,o3,c1,c2,c3))


o2 = Start.takeUserSecondInput(c1,o1,c2)
print(Start.displayMatrixState(o1,o2,o3,c1,c2,c3))



# print(Start.is_win(6,4,4))
# print(Start.SinglePositionTargets(4))
# print(Start.secondComputerMove(4,3))