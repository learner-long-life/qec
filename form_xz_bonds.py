from generator_333_xz import g
from former import *

pieces = g.xgauges
#pieces.extend(g.yplaques.values())
#pieces.extend(g.ystabilizers)

piece_count = len(pieces)
print str(piece_count) + " pieces"
ybonds = []
yshapes = []

# YB1
#target = dict({(0,0,0): 'Y', (0,1,0):'Y'})
# YB7
#target = dict({(0,0,1): 'Y', (0,1,1):'Y'})
# YB13
#target = dict({(0,0,2):'Y', (0,1,2):'Y'})
# YB14
# target = dict({(1,0,2):'Y', (1,1,2):'Y'})
# YB15
# target = dict({(2,0,2):'Y', (2,1,2):'Y'})

#S3 in X's
target = dict({
  (0,0,0):(0,'X'),
  (1,0,0):(0,'X'),
  (2,0,0):(0,'X'),
  (0,0,1):(0,'X'),
  (1,0,1):(0,'X'),
  (2,0,1):(0,'X'),
  (0,0,2):(0,'X'),
  (1,0,2):(0,'X'),
  (2,0,2):(0,'X'),
  (0,1,0):(0,'X'),
  (1,1,0):(0,'X'),
  (2,1,0):(0,'X'),
  (0,1,1):(0,'X'),
  (1,1,1):(0,'X'),
  (2,1,1):(0,'X'),
  (0,1,2):(0,'X'),
  (1,1,2):(0,'X'),
  (2,1,2):(0,'X')
  })
  
#target = dict({(0,0,0):'Y', (1,0,0):'Y', (0,0,1):'Y', (1,0,1):'Y',
#               (0,1,0):'Y', (1,1,0):'Y', (0,1,1):'Y', (1,1,1):'Y'})
#target = dict({(0,0,0):'Y', (0,1,0):'Y', (2,0,0):'Y', (2,1,0):'Y',
#               (0,0,2):'Y', (0,1,2):'Y', (2,0,2):'Y', (2,1,2):'Y'})
#target = dict({(0,0,2):'Y', (0,1,2):'Y', (1,0,1):'Y', (1,1,1):'Y',
#               (2,0,0):'Y', (2,1,0):'Y'})

for i in range(1,piece_count+1):
  print "Forming from shapes of " + str(i) + " pieces."
  sf = ShapeFormer(i, pieces, target, 1000)


