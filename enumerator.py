from shape import *

###############################################################################
class ShapeEnumerator:

  def __init__(self, bond_count, allbonds, gauges, disregard = []):
    self.shapes = []
    self.gauges = gauges
    self.disregard = disregard
    self.bond_count = bond_count
    self.bond_enumerate([], bond_count, allbonds)
    print "  " + str(len(self.shapes)) + " shapes"

  def bond_enumerate(self, bonds, bond_count, bonds_left, intersect = False):
    left_copy = list(bonds_left)
    for bond in bonds_left:
      left_copy.remove(bond)
      bonds_copy = list(bonds)
      bond_skip = False
      for bond2 in bonds_copy:
        if (bond2.intersects(bond) and (not intersect)):
          bond_skip = True
          break
      if (bond_skip):
        continue
      bonds_copy.append(bond)
      if (bond_count == 1):
        new_shape = Shape(bonds = bonds_copy)
        if ((new_shape not in self.gauges) and
            (new_shape not in self.disregard)):
          self.shapes.append(new_shape)
      else:
        self.bond_enumerate(bonds_copy, bond_count-1, left_copy)

