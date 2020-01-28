# 21. A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:


import math
l=[0,0]
while True:
    s=input()
    if not s:
        break

    move = s.split(" ")
    direction=move[0]
    step=move[1]
    if direction=='UP':
        l[0]+=step
    elif direction=='DOWN':
        l[0]-=step
    elif direction=='LEFT':
        l[1]-=step
    elif direction=='RIGHT':
        l[1]+=step
    else:
        pass
print(l[0])
print(l[1])
print(int(round(math.sqrt(l[1]**2+l[0]**2))))