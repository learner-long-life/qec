from shape_util import *
from shape import *
from enumerator import *

###############################################################################
class ShapeGenerator:

  def __init__(self, dims):
    self.dims = dims
    self.n = 1
    for dim in self.dims:
      self.n = self.n * dim
    self.bonds = []
    self.create_bonds()
    self.create_gauges()

  #----------------------------------------------------------------------------
  def parse(self, argv):
    if (len(argv) == 1):
      print "Available commands:"
      print "find - finds encoded operators (gauges)"
      return
    command = argv[1]
    args = argv[2:]
    if (command == "find"):
      self.enumerate_shapes(int(args[0]))
      self.find_gauges(args)

  #----------------------------------------------------------------------------
  def find_gauges(self, *args):
    raise RuntimeError("")

  #----------------------------------------------------------------------------
  def create_plaques(self, bonds1, bonds2, plaques):

    bonds1_copy = list(bonds1.values())

    for bond11 in bonds1.values():
      for bond12 in bonds1_copy:
        if (bond11.p1 < bond12.p1):
          point = bond11.p1
        else:
          point = bond12.p1
        bonds2_copy = list(bonds2.values())
        for bond21 in bonds2.values():
          for bond22 in bonds2_copy:
            if (((bond11.p1 == bond21.p1) and (bond11.p2 == bond22.p1) and
                 (bond12.p1 == bond21.p2) and (bond12.p2 == bond22.p2)) or
                ((bond11.p1 == bond22.p1) and (bond11.p2 == bond21.p1) and
                 (bond12.p1 == bond22.p2) and (bond12.p2 == bond21.p2))):
              shape1 = Shape([bond11, bond12])
              shape2 = Shape([bond21, bond22])
              new_plaque = Shape.multiply(shape1, shape2)
              plaques[point] = new_plaque
          bonds2_copy.remove(bond21)

  #----------------------------------------------------------------------------
  def add_xgauges(self):
    raise RuntimeError("")

  #----------------------------------------------------------------------------
  def add_ygauges(self):
    raise RuntimeError("")

  #----------------------------------------------------------------------------
  def add_zgauges(self):
    raise RuntimeError("")

  #----------------------------------------------------------------------------
  def create_bonds(self):
    raise RuntimeError("")

  #----------------------------------------------------------------------------
  def create_gauges(self):
    # Add initial gauges here and remove them from shapes
    self.gauges  = []
    self.xgauges = []
    self.ygauges = []
    self.zgauges = []
    self.xdisregard = []
    self.ydisregard = []
    self.zdisregard = []
    self.stabilizers = []
    self.xstabilizers = []
    self.ystabilizers = []
    self.zstabilizers = []

    self.add_xgauges()
    self.add_zgauges()
    self.add_ygauges()
    self.add_stabilizers()
    
    assert(len(self.xgauges) == len(self.ygauges))
    assert(len(self.ygauges) == len(self.zgauges))
    self.gauge_count = len(self.xgauges)

    # Checking each X gauge commutes with each other
    for gauge in self.xgauges:
      for gauge2 in (self.xgauges + self.xstabilizers):
        if (not gauge.commutes_with(gauge2)):
          print str(gauge)
          print str(gauge2)
          raise RuntimeError("X gauges do not commute.")

    # Checking each Y gauge commutes with each other
    for gauge in self.ygauges:
      for gauge2 in (self.ygauges + self.ystabilizers):
        if (not gauge.commutes_with(gauge2)):
          print str(gauge)
          print str(gauge2)
          raise RuntimeError("Gauges anti-commutes.")
    # Checking each Y gauge anti-commutes with its X
    for i in range(len(self.ygauges)):
      for j in range(len(self.xgauges)):
        if (i == j):
          if (self.ygauges[i].commutes_with(self.xgauges[i])):
            print str(self.ygauges[i])
            print str(self.xgauges[i])
            raise RuntimeError("Y" + str(i+1) + " commutes with X" + str(i+1))
        elif (not self.ygauges[i].commutes_with(self.xgauges[j])):
          print str(self.ygauges[i])
          print str(self.xgauges[j])
          raise RuntimeError("Y"+str(i+1) + " anti-commutes with X" + str(j+1))
      for stab in self.xstabilizers:
        if (not self.ygauges[i].commutes_with(stab)):
          print str(self.ygauges[i])
          print str(stab)
          raise RuntimeError("Y" + str(i+1) + " anti-commutes with stabilizer")

    # Checking each Z gauge commutes with each other
    for gauge in self.zgauges:
      for gauge2 in (self.zgauges + self.zstabilizers):
        if (not gauge.commutes_with(gauge2)):
          print str(gauge)
          print str(gauge2)
          raise RuntimeError("These two gauges anti-commute.")

    # Checking each Z gauge anti-commutes with its X and Y
    for i in range(len(self.zgauges)):
      for j in range(len(self.ygauges)):
        if (i == j):
          if (self.zgauges[i].commutes_with(self.ygauges[i])):
            print str(self.zgauges[i])
            print str(self.ygauges[i])
            raise RuntimeError("Z"+str(i+1) + " commutes with Y" + str(i+1))
        elif (not self.zgauges[i].commutes_with(self.ygauges[j])):
          print str(self.zgauges[i])
          print str(self.ygauges[i])
          raise RuntimeError("Z"+str(i+1) + " anti-commutes with Y" + str(j+1))
        
      for k in range(len(self.xgauges)):
        if (i == k):
            if (self.zgauges[i].commutes_with(self.xgauges[i])):
              print str(self.zgauges[i])
              print str(self.xgauges[i])
              raise RuntimeError("Z"+str(i+1) + " commutes with X" + str(i+1))
        elif (not self.zgauges[i].commutes_with(self.xgauges[k])):
          print str(self.zgauges[i])
          print str(self.xgauges[k])
          raise RuntimeError("Z"+str(i+1) + " anti-commutes with X" + str(k+1))
      for stab in (self.xstabilizers + self.ystabilizers):
        if (not self.zgauges[i].commutes_with(stab)):
          print str(self.zgauges[i])
          print str(stab)
          raise RuntimeError("Z" + str(i+1) + " anti-commutes with stabilizer")
          
    self.gauges.extend(self.xgauges)
    self.gauges.extend(self.ygauges)
    self.gauges.extend(self.zgauges)
    self.gauges.extend(self.xstabilizers)
    self.gauges.extend(self.ystabilizers)
    self.gauges.extend(self.zstabilizers)
    self.stabilizers.extend(self.xstabilizers)
    self.stabilizers.extend(self.ystabilizers)
    self.stabilizers.extend(self.zstabilizers)

    for stab in self.stabilizers:
      for stab2 in self.stabilizers:
        if (not stab.commutes_with(stab2)):
          raise RuntimeError(str(stab) + " anti-commutes with " +
                             str(stab2))

  def enumerate_shapes(self, max_count = 11):
    raise RuntimeError("Not implemented, dumbass")
