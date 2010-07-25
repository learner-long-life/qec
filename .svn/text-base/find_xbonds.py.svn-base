from generator_basic import *
from former import *

g = ShapeBasicGenerator(3)
g.create_bonds()
g.create_gauges()

pieces = []
pieces.extend(g.xplaques.values())
pieces.extend(g.xstabilizers)
pieces.extend(g.xgauges)


piece_count = len(pieces)
print str(piece_count) + " pieces"
xbonds = []
xshapes = []

# YB1
#target = dict({(0,0,0): 'Y', (0,1,0):'Y'})
# YB2
target = dict({(0,0,1): 'X', (1,0,1):'X'})
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

for i in range(1, piece_count+1):
  print "Forming from shapes of " + str(i) + " pieces."
  sf = ShapeFormer(i, pieces, target)


