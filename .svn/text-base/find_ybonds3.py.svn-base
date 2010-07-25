from generator_basic import *
from former import *

g = ShapeBasicGenerator(3)
g.create_bonds()
g.create_gauges()

pieces = []
pieces.extend(g.yplaques.values())
pieces.extend(g.ystabilizers)

YF154 = Shape([g.ybonds[((1,0,0),(1,1,0))], g.ybonds[((1,0,1),(1,1,1))]])
pieces.append(YF154)
print str(YF154)

YF135 = Shape([g.ybonds[((1,0,1),(1,1,1))], g.ybonds[((2,0,1),(2,1,1))]])
pieces.append(YF135)
print str(YF135)

YF152 = Shape([g.ybonds[((1,1,0),(1,2,0))], g.ybonds[((1,1,1),(1,2,1))]])
pieces.append(YF152)
print str(YF152)

YF164 = Shape([g.ybonds[((1,1,1),(1,2,1))], g.ybonds[((2,1,1),(2,2,1))]])
pieces.append(YF164)
print str(YF164)

YF148 = Shape([g.ybonds[(0,0,1),(0,1,1)], g.ybonds[(1,0,1),(1,1,1)],
               g.ybonds[(2,1,1),(2,2,1)], g.ybonds[(2,1,2),(2,2,2)]])
pieces.append(YF148)
print str(YF148)

YF144 = Shape([g.ybonds[(0,1,1),(0,2,1)], g.ybonds[(1,1,1),(1,2,1)],
               g.ybonds[(2,0,1),(2,1,1)], g.ybonds[(2,0,2),(2,1,2)]])
pieces.append(YF144)
print str(YF144)

YF165 = Shape([g.ybonds[(0,0,1),(0,1,1)], g.ybonds[(0,0,2),(0,1,2)],
               g.ybonds[(0,1,0),(0,2,0)], g.ybonds[(1,1,0),(1,2,0)]])
pieces.append(YF165)
print str(YF165)
  
YF141 = Shape([g.ybonds[(0,1,1),(0,2,1)], g.ybonds[(0,1,2),(0,2,2)],
               g.ybonds[(0,0,0),(0,1,0)], g.ybonds[(1,0,0),(1,1,0)]])
pieces.append(YF141)
print str(YF141)

piece_count = len(pieces)
print str(piece_count) + " pieces"
ybonds = []
yshapes = []

# YB1
#target = dict({(0,0,0): 'Y', (0,1,0):'Y'})
# YB7
target = dict({(0,0,1): 'Y', (0,1,1):'Y'})
# YB13
#target = dict({(0,0,2):'Y', (0,1,2):'Y'})
# YB14
# target = dict({(1,0,2):'Y', (1,1,2):'Y'})
# YB15
# target = dict({(2,0,2):'Y', (2,1,2):'Y'})

#target = dict({(0,0,0):'Y', (1,0,0):'Y', (0,0,1):'Y', (1,0,1):'Y',
#               (0,1,0):'Y', (1,1,0):'Y', (0,1,1):'Y', (1,1,1):'Y'})
#target = dict({(0,0,0):'Y', (0,1,0):'Y', (2,0,0):'Y', (2,1,0):'Y',
#               (0,0,2):'Y', (0,1,2):'Y', (2,0,2):'Y', (2,1,2):'Y'})
#target = dict({(0,0,2):'Y', (0,1,2):'Y', (1,0,1):'Y', (1,1,1):'Y',
#               (2,0,0):'Y', (2,1,0):'Y'})

for i in range(1,piece_count+1):
  print "Forming from shapes of " + str(i) + " pieces."
  sf = ShapeFormer(i, pieces, target)


