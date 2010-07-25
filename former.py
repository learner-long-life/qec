from shape_util import *
from shape import *
from process import *

###############################################################################
class ShapeFormer(ShapeProcess):

  def __init__(self, bond_count, allbonds, target, granularity):
    ShapeProcess.__init__(self, granularity)
    self.shapes = []
    self.target = target
    self.bond_count = bond_count
    self.count = 0
    self.find_bond(bond_count, allbonds)
    print "  " + str(len(self.shapes)) + " shapes"

  def find_bond(self, bond_count, allbonds):
    self.total_status = combo(len(allbonds), bond_count)
    print "Total combinations: " + str(self.total_status)
    self.bond_enumerate([], bond_count, allbonds)

  def bond_enumerate(self, bonds, bond_count, bonds_left):
    left_copy = list(bonds_left)
    self.update_status()
    for bond in bonds_left:
      left_copy.remove(bond)
      bonds_copy = list(bonds)
      bonds_copy.append(bond)
      if (bond_count == 1):
        new_shape = Shape(bonds = bonds_copy)
        self.count = self.count + 1
        if (new_shape.qubits == self.target):
          print "Target formed by: "
          for bond in bonds_copy:
            print str(bond)
          print str(new_shape)
      else:
        self.bond_enumerate(bonds_copy, bond_count-1, left_copy)
