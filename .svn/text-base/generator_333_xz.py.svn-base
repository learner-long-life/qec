from generator import *
from bond import *
from finder_basic import *
import sys

class ShapeGenerator_333_XZ(ShapeGenerator):

  def __init__(self):
    ShapeGenerator.__init__(self, [3,3,3])

  def find_gauges(self, *args):
    f = ShapeBasicFinder(self)
    f.find_gauges()

  #----------------------------------------------------------------------------
  def create_bonds(self):

    # Create xz bonds
    self.xzxbonds = {}
    self.xzzbonds = {}
    self.xzbonds = {}
    for i in range(self.dims[0]):
      for j in range(self.dims[1]-1):
        for k in range(self.dims[2]):
          p1 = (i,j,k)
          p2 = (i,j+1,k)
          self.xzxbonds[(p1,p2)] = Bond(p1, p2, 'X', 0)  
          self.xzzbonds[(p1,p2)] = Bond(p1, p2, 'Z', 0)

    # Create x bonds
    self.xbonds = {}
    for i in range(self.dims[0]-1):
      for j in range(self.dims[1]):
        for k in range(self.dims[2]):
          p1 = (i,j,k)
          p2 = (i+1,j,k)
          self.xbonds[(p1,p2)] = Bond(p1, p2, 'X', 0)

    self.xb_ordered = []
    # X bonds range over y first, then x, then z
    for k in range(self.dims[2]):
      for i in range(self.dims[0]-1):
        for j in range(self.dims[1]):
          self.xb_ordered.append(self.xbonds[(i,j,k),(i+1,j,k)])
    # YX bonds range over x first, then y, then z
    for k in range(self.dims[2]):
      for j in range(self.dims[1]-1):
        for i in range(self.dims[0]):
          self.xb_ordered.append(self.xzxbonds[(i,j,k),(i,j+1,k)])

    # Create z bonds
    self.zbonds = {}
    for i in range(self.dims[0]):
      for j in range(self.dims[1]):
        for k in range(self.dims[2]-1):
          p1 = (i,j,k)
          p2 = (i,j,k+1)
          self.zbonds[(p1,p2)] = Bond(p1, p2, 'Z', 0)

    self.zb_ordered = []
    # Z bonds range over x first, then y, then z
    for k in range(self.dims[2]-1):
      for j in range(self.dims[1]):
        for i in range(self.dims[0]):
          self.zb_ordered.append(self.zbonds[(i,j,k),(i,j,k+1)])
    # YZ bonds range over x first, then y, then z
    for k in range(self.dims[2]):
      for j in range(self.dims[1]-1):
        for i in range(self.dims[0]):
          self.zb_ordered.append(self.xzzbonds[(i,j,k),(i,j+1,k)])
    self.bonds = [self.xb_ordered, self.zb_ordered]

    self.yplaques = {}
    self.xplaques = {}
    self.zplaques = {}
    #self.create_plaques(self.xbonds, self.zbonds, self.yplaques)
    #self.create_plaques(self.xzxbonds, self.zbonds, self.yplaques)
    #self.create_plaques(self.xzzbonds, self.zbonds, self.zplaques)
    #self.create_plaques(self.xzxbonds, self.xbonds, self.xplaques)
    #self.create_plaques(self.xzzbonds, self.xbonds, self.yplaques)

  #----------------------------------------------------------------------------
  def add_stabilizers(self):
    # X stabilizers
    S1 = Shape([self.xbonds[(0,0,0),(1,0,0)], self.xbonds[(0,1,0),(1,1,0)],
                self.xbonds[(0,2,0),(1,2,0)], self.xbonds[(0,0,1),(1,0,1)],
                self.xbonds[(0,1,1),(1,1,1)], self.xbonds[(0,2,1),(1,2,1)],
                self.xbonds[(0,0,2),(1,0,2)], self.xbonds[(0,1,2),(1,1,2)],
                self.xbonds[(0,2,2),(1,2,2)]], "S1")
    S2 = Shape([self.xbonds[(1,0,0),(2,0,0)], self.xbonds[(1,1,0),(2,1,0)],
                self.xbonds[(1,2,0),(2,2,0)], self.xbonds[(1,0,1),(2,0,1)],
                self.xbonds[(1,1,1),(2,1,1)], self.xbonds[(1,2,1),(2,2,1)],
                self.xbonds[(1,0,2),(2,0,2)], self.xbonds[(1,1,2),(2,1,2)],
                self.xbonds[(1,2,2),(2,2,2)]], "S2")
    self.xstabilizers.append(S1)
    self.xstabilizers.append(S2)

    # Z stabilizers
    S5 = Shape([self.zbonds[(0,0,0),(0,0,1)], self.zbonds[(1,0,0),(1,0,1)],
                self.zbonds[(2,0,0),(2,0,1)], self.zbonds[(0,1,0),(0,1,1)],
                self.zbonds[(1,1,0),(1,1,1)], self.zbonds[(2,1,0),(2,1,1)],
                self.zbonds[(0,2,0),(0,2,1)], self.zbonds[(1,2,0),(1,2,1)],
                self.zbonds[(2,2,0),(2,2,1)]], "S5") 
    S6 = Shape([self.zbonds[(0,0,1),(0,0,2)], self.zbonds[(1,0,1),(1,0,2)],
                self.zbonds[(2,0,1),(2,0,2)], self.zbonds[(0,1,1),(0,1,2)],
                self.zbonds[(1,1,1),(1,1,2)], self.zbonds[(2,1,1),(2,1,2)],
                self.zbonds[(0,2,1),(0,2,2)], self.zbonds[(1,2,1),(1,2,2)],
                self.zbonds[(2,2,1),(2,2,2)]], "S6")
    self.zstabilizers.append(S5)
    self.zstabilizers.append(S6)

  def get_xplaque(self, x,y,z):
    return multiply_many([self.xzxbonds[(x,y,z),(x,y+1,z)],
                          self.xzxbonds[(x,y,z+1),(x,y+1,z+1)]])
  #----------------------------------------------------------------------------
  def add_xgauges(self):
    X01 = Shape([self.xbonds[(0,0,0),(1,0,0)]], "X1")
    X02 = Shape([self.xbonds[(0,1,0),(1,1,0)]], "X2")
    X03 = Shape([self.xbonds[(0,2,0),(1,2,0)]], "X3")
    X04 = Shape([self.xbonds[(1,0,0),(2,0,0)]], "X4")
    X05 = Shape([self.xbonds[(1,1,0),(2,1,0)]], "X5")
    X06 = Shape([self.xbonds[(1,2,0),(2,2,0)]], "X6")
    X07 = Shape([self.xbonds[(0,0,2),(1,0,2)]], "X7")
    X08 = Shape([self.xbonds[(0,1,2),(1,1,2)]], "X8")
    X09 = Shape([self.xbonds[(0,2,2),(1,2,2)]], "X9")
    X10 = Shape([self.xbonds[(1,0,2),(2,0,2)]], "X10")
    X11 = Shape([self.xbonds[(1,1,2),(2,1,2)]], "X11")
    X12 = Shape([self.xbonds[(1,2,2),(2,2,2)]], "X12")

    X13 = Shape([self.xbonds[(1,0,0),(2,0,0)], self.xbonds[(1,0,1),(2,0,1)],
                 self.xbonds[(1,0,2),(2,0,2)]], "X13")
    X14 = Shape([self.xbonds[(1,2,0),(2,2,0)], self.xbonds[(1,2,1),(2,2,1)],
                 self.xbonds[(1,2,2),(2,2,2)]], "X14")
    X15 = Shape([self.xbonds[(0,0,0),(1,0,0)],
                 self.xbonds[(0,0,1),(1,0,1)],
                 self.xbonds[(0,0,2),(1,0,2)]], "X15")
    X16 = Shape([self.xbonds[(0,2,0),(1,2,0)],
                 self.xbonds[(0,2,1),(1,2,1)],
                 self.xbonds[(0,2,2),(1,2,2)]], "X16")
    X17 = Shape([self.xbonds[(0,0,2),(1,0,2)], self.xbonds[(0,1,2),(1,1,2)],
                 self.get_xplaque(0,0,0)],
                 "X17")
    X18 = Shape([self.xbonds[(0,2,2),(1,2,2)], self.xbonds[(0,1,2),(1,1,2)],
                 self.get_xplaque(0,1,0)],
                 "X18")
    X19 = Shape([self.xbonds[(1,0,0),(2,0,0)], self.xbonds[(1,0,1),(2,0,1)],
                 self.xbonds[(1,0,2),(2,0,2)],
                 self.get_xplaque(1,1,1)],
                 "X19")
    X20 = Shape([self.xbonds[(1,2,0),(2,2,0)], self.xbonds[(1,2,1),(2,2,1)],
                 self.xbonds[(1,2,2),(2,2,2)],
                 self.get_xplaque(1,0,1)],
                 "X20")
    X21 = Shape([self.xzxbonds[(0,1,0),(0,2,0)],
                 self.xzxbonds[(1,1,0),(1,2,0)],
                 self.xzxbonds[(2,1,0),(2,2,0)],
                 self.xzxbonds[(0,1,1),(0,2,1)],
                 self.xzxbonds[(1,1,1),(1,2,1)],
                 self.xzxbonds[(2,1,1),(2,2,1)],
                 self.xzxbonds[(0,1,2),(0,2,2)],
                 self.xzxbonds[(1,1,2),(1,2,2)],
                 self.xzxbonds[(2,1,2),(2,2,2)]], "X21")
    X22 = Shape([self.xzxbonds[(0,0,0),(0,1,0)],
                 self.xzxbonds[(1,0,0),(1,1,0)],
                 self.xzxbonds[(2,0,0),(2,1,0)],
                 self.xzxbonds[(0,0,1),(0,1,1)],
                 self.xzxbonds[(1,0,1),(1,1,1)],
                 self.xzxbonds[(2,0,1),(2,1,1)],
                 self.xzxbonds[(0,0,2),(0,1,2)],
                 self.xzxbonds[(1,0,2),(1,1,2)],
                 self.xzxbonds[(2,0,2),(2,1,2)]], "X22")

    self.xgauges.extend([X01, X02, X03, X04, X05, X06,
                         X07, X08, X09, X10, X11, X12,
                         X13, X14, X15, X16, X17, X18, X19, X20,
                         X21, X22])

  #----------------------------------------------------------------------------
  def add_ygauges(self): 
    for i in range(len(self.xgauges)):
      yshape = multiply_many([self.xgauges[i], self.zgauges[i]],
                             "Y"+str(i+1))
      self.ygauges.append(yshape)

  def get_zplaque(self, x,y,z):
    return multiply_many([self.xzzbonds[(x,y,z),(x,y+1,z)],
                          self.xzzbonds[(x+1,y,z),(x+1,y+1,z)]])

  #----------------------------------------------------------------------------
  def add_zgauges(self):
    Z01 = Shape([self.zbonds[(0,0,0),(0,0,1)]], "Z1")
    Z02 = Shape([self.zbonds[(0,1,0),(0,1,1)]], "Z2")
    Z03 = Shape([self.zbonds[(0,2,0),(0,2,1)]], "Z3")
    Z04 = Shape([self.zbonds[(2,0,0),(2,0,1)]], "Z4")
    Z05 = Shape([self.zbonds[(2,1,0),(2,1,1)]], "Z5")
    Z06 = Shape([self.zbonds[(2,2,0),(2,2,1)]], "Z6")
    Z07 = Shape([self.zbonds[(0,0,1),(0,0,2)]], "Z7")
    Z08 = Shape([self.zbonds[(0,1,1),(0,1,2)]], "Z8")
    Z09 = Shape([self.zbonds[(0,2,1),(0,2,2)]], "Z9")
    Z10 = Shape([self.zbonds[(2,0,1),(2,0,2)]], "Z10")
    Z11 = Shape([self.zbonds[(2,1,1),(2,1,2)]], "Z11")
    Z12 = Shape([self.zbonds[(2,2,1),(2,2,2)]], "Z12")

    Z13 = Shape([self.zbonds[(2,0,1),(2,0,2)],
                 self.zbonds[(2,1,1),(2,1,2)],
                 self.get_zplaque(0,0,2)], "Z13")
    Z14 = Shape([self.zbonds[(2,1,1),(2,1,2)],
                 self.zbonds[(2,2,1),(2,2,2)],
                 self.get_zplaque(0,1,2)], "Z14")
    Z15 = Shape([self.zbonds[(0,0,0),(0,0,1)],
                 self.zbonds[(0,1,0),(0,1,1)],
                 self.get_zplaque(1,0,0)], "Z15")
    Z16 = Shape([self.zbonds[(0,1,0),(0,1,1)],
                 self.zbonds[(0,2,0),(0,2,1)],
                 self.get_zplaque(1,1,0)], "Z16")
    Z17 = Shape([self.zbonds[(0,0,1),(0,0,2)], self.zbonds[(1,0,1),(1,0,2)],
                 self.zbonds[(2,0,1),(2,0,2)]], "Z17")
    Z18 = Shape([self.zbonds[(0,2,1),(0,2,2)], self.zbonds[(1,2,1),(1,2,2)],
                 self.zbonds[(2,2,1),(2,2,2)]], "Z18")
    Z19 = Shape([self.zbonds[(0,2,0),(0,2,1)], self.zbonds[(1,2,0),(1,2,1)],
                 self.zbonds[(2,2,0),(2,2,1)]], "Z19")
    Z20 = Shape([self.zbonds[(0,0,0),(0,0,1)], self.zbonds[(1,0,0),(1,0,1)],
                 self.zbonds[(2,0,0),(2,0,1)]], "Z20")
    Z21 = Shape([self.xzzbonds[(0,0,0),(0,1,0)],
                 self.xzzbonds[(1,0,0),(1,1,0)],
                 self.xzzbonds[(2,0,0),(2,1,0)],
                 self.xzzbonds[(0,0,1),(0,1,1)],
                 self.xzzbonds[(1,0,1),(1,1,1)],
                 self.xzzbonds[(2,0,1),(2,1,1)],
                 self.xzzbonds[(0,0,2),(0,1,2)],
                 self.xzzbonds[(1,0,2),(1,1,2)],
                 self.xzzbonds[(2,0,2),(2,1,2)]], "Z21")
    Z22 = Shape([self.xzzbonds[(0,1,0),(0,2,0)],
                 self.xzzbonds[(1,1,0),(1,2,0)],
                 self.xzzbonds[(2,1,0),(2,2,0)],
                 self.xzzbonds[(0,1,1),(0,2,1)],
                 self.xzzbonds[(1,1,1),(1,2,1)],
                 self.xzzbonds[(2,1,1),(2,2,1)],
                 self.xzzbonds[(0,1,2),(0,2,2)],
                 self.xzzbonds[(1,1,2),(1,2,2)],
                 self.xzzbonds[(2,1,2),(2,2,2)]], "Z22")
    
    self.zgauges.extend([Z01, Z02, Z03, Z04, Z05, Z06,
                         Z07, Z08, Z09, Z10, Z11, Z12,
                         Z13, Z14, Z15, Z16, Z17, Z18, Z19, Z20,
                         Z21, Z22])

  #----------------------------------------------------------------------------
  def enumerate_shapes(self, max_count = 11):
    self.xshapes = []
    self.yshapes = []
    self.zshapes = []
    xpieces = (self.xbonds.values() + self.xplaques.values())
    xzpieces = (self.xzxbonds.values() + self.xzzbonds.values() +
                self.yplaques.values())
    zpieces = (self.zbonds.values() + self.zplaques.values())

    for i in range(1, max_count):
      print "Enumerating X shapes of " + str(i) + " pieces."
      xe = ShapeEnumerator(i, xpieces, self.xgauges, self.xdisregard)
      self.xshapes.extend(xe.shapes)
      print "Enumerating Y shapes of " + str(i) + " pieces."
      ye = ShapeEnumerator(i, xzpieces, self.ygauges, self.ydisregard)
      self.yshapes.extend(ye.shapes)
      print "Enumerating Z shapes of " + str(i) + " pieces."
      ze = ShapeEnumerator(i, zpieces, self.zgauges, self.zdisregard)
      self.zshapes.extend(ze.shapes)

###############################################################################
g = ShapeGenerator_333_XZ()

