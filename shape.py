from shape_util import *
import string

###############################################################################
class Shape:

  #----------------------------------------------------------------------------
  def create_singleton(point, op, label=""):
    new_shape = Shape(bonds = [], label = label)
    new_shape.add_qubit(point, op)
    new_shape.add_logical_qubit(label)
    return new_shape
  create_singleton = Callable(create_singleton)

  #----------------------------------------------------------------------------
  def multiply(shape1, shape2):
    new_shape = Shape([])

    #shape1_stab = (len(shape1.label) == 0) or (shape1.label[0] != 'S')
    
    for qubit in shape1.qubits.keys():
      op = shape1.qubits[qubit]
      new_shape.add_qubit(qubit, op)

    #shape2_stab = (len(shape2.label) == 0) or (shape2.label[0] != 'S')

    new_shape.add_logical_qubit(shape1.label)
    new_shape.add_logical_qubit(shape2.label)

    for qubit in shape2.qubits.keys():
      op = shape2.qubits[qubit]
      new_shape.add_qubit(qubit, op)

    new_shape.ancestry = list(shape1.ancestry) # Deep copy
    for ancestor in shape2.ancestry:
      new_shape.add_to_ancestry(ancestor)

    # Be careful not to stomp on the phase updated by add_qubit
    new_shape.add_phase(shape1.phase + shape2.phase)

    return new_shape

  #----------------------------------------------------------------------------
  def multiply_with_self(self, new_shape):

    #new_stab = (len(new_shape.label) == 0) or (new_shape.label[0] != 'S')
    
    for qubit in new_shape.qubits.keys():
      op = new_shape.qubits[qubit]
      self.add_qubit(qubit, op)

    self.add_logical_qubit(new_shape.label)

    for ancestor in new_shape.ancestry:
      self.add_to_ancestry(ancestor)

    self.add_phase(new_shape.phase)

  #----------------------------------------------------------------------------
  def contains(self, point):
    return (point in self.qubits.keys())

  #----------------------------------------------------------------------------
  def intersects(self, other):
    for qubit in self.qubits.keys():
      if (other.contains(qubit)):
        return True
    return False

  #----------------------------------------------------------------------------
  def __init__(self, bonds, label="", dim=3):
    self.qubits = dict()
    self.phase = 0
    self.logical_qubits = []
    self.label = label
    self.dim = dim
    if (label != ""):
      self.ancestry = [label]
    else:
      self.ancestry = []
    for bond in bonds:
      bond.add_to_shape(self)

  #----------------------------------------------------------------------------
  def add_to_ancestry(self, label):

    if (label in self.ancestry):
      self.ancestry.remove(label)
      return

    # Stabilizers commute with every logical operator
    common = [item for item in self.ancestry
              if ((item[1:] == label[1:]) and (item[0] != 'S'))]
    if ((len(common) == 0) or (label[0] == 'S')):
      self.ancestry.append(label)
      self.ancestry.sort()
      return

    new_op = ''
    for op in common:
      self.ancestry.remove(op)
      new_op = opmult((0, op[0]),(0, label[0]))
      self.ancestry.append(new_op[1]+label[1:])
      self.ancestry.sort()

  #----------------------------------------------------------------------------
  def add_to_shape(self, shape):
    self.add_phase(shape.phase)
    for qubit in self.qubits.keys():
      op = self.qubits[qubit]
      shape.add_qubit(qubit, op)
      shape.add_logical_qubit(self.label)

  #----------------------------------------------------------------------------
  def add_logical_qubit(self, new_label):
    if (len(new_label) > 1):
      if (new_label[0] != 'S'):
        self.logical_qubits += new_label

  #----------------------------------------------------------------------------
  def add_phase(self, phase):
    self.phase = (self.phase + phase) % 4

  #----------------------------------------------------------------------------
  # Add the given point (X,Y,Z) coordinate with given op (phaseless)
  # new_qubit is a 
  def add_qubit(self, new_qubit, op):
    assert(op[0] == 0)
    if (new_qubit in self.qubits):
      old_op = self.qubits[new_qubit]
      assert(old_op[0] == 0)
      new_op = opmult(old_op, op)
      # Add the phase here (may result from opmult)
      self.add_phase(new_op[0])
      if (new_op[1] == 'I'):
        # All identities are implicit and can be removed
        del self.qubits[new_qubit]
      else:
        # Add phaseless operators
        self.qubits[new_qubit] = (0, new_op[1])
    else:
      self.qubits[new_qubit] = op

  #----------------------------------------------------------------------------
  def commutes_with(self, shape):
    parity = 0
    self_qubits = set(self.qubits.keys())
    other_qubits = set(shape.qubits.keys())
    common_qubits = self_qubits.intersection(other_qubits)
    for qubit in common_qubits:
      if (self.qubits[qubit][1] != shape.qubits[qubit][1]):
        parity = parity + 1

    # Even number of different operators, or same operators, commute
    return (parity % 2 == 0)

  #----------------------------------------------------------------------------
  def print_logical_string(self, size, stabs):
    xancestors = []
    yancestors = []
    zancestors = []
    stab_multiplier = 1
    subopx = 0
    subopy = 0
    subopz = 0
    self.rstring = ""

    for ancestor in self.ancestry:
      if (ancestor[0] == 'S'):
        anum = translate_label(ancestor)
        if (anum not in stabs):
          raise RuntimeError("Ancestor " + str(ancestor) + " not in stabs")
        stab_multiplier *= stabs[anum]
      if (ancestor[0] == 'X'):
        subopx = 1
        xancestors.append(translate_label(ancestor))
      elif (ancestor[0] == 'Y'):
        subopy = 1
        yancestors.append(translate_label(ancestor))
      elif (ancestor[0] == 'Z'):
        subopz = 1
        zancestors.append(translate_label(ancestor))

    subops = subopx + subopy + subopz
    self.single_flag = (subops == 1)

    phase = self.phase

    if (stab_multiplier < 0):
      phase = (phase + 2) % 4

    mstring = self.phase_string(phase)

    self.first = False
    self.ostring = self.label+" = "+ mstring
    self.cstring = ""
    self.size = size

    self.logical_string_helper(xancestors, 'X')
    self.logical_string_helper(yancestors, 'Y')
    self.logical_string_helper(zancestors, 'Z')

    self.rstring += self.ostring + ";\n"
    self.rstring += self.cstring + "\n"
    return self.rstring

  #----------------------------------------------------------------------------
  def logical_string_helper(self, ancestors, op):
    gate = "S"+string.lower(op)
    op = string.upper(op)
    if (len(ancestors) > 0):
      pstring = "ProductGate("+str(self.size)+", "+gate+\
                 ", " + str(ancestors) + ")"

      if (not self.first):
        self.first = True
      else:
        self.ostring += " * "
        
      if (self.single_flag):
        self.ostring += pstring
      else:
        self.rstring += self.label + op + " = " + pstring + ";\n"
        self.ostring += self.label+op
        self.cstring += "clear " + self.label+op+"; "

  #----------------------------------------------------------------------------
  def phase_string(phase):
    if (phase == 0):
      return ""
    elif (phase == 1):
      return "i*"
    elif (phase == 2):
      return "-"
    elif (phase == 3):
      return "-i*"
    else:
      raise RuntimeError("Invalid phase " + str(phase))
  phase_string = Callable(phase_string)
    
  #----------------------------------------------------------------------------
  def __str__(self):
    selfstring = self.label + " i^{"+str(self.phase)+"}\n"
    for ancestor in self.ancestry:
      selfstring += ancestor + ", "
    selfstring += "\n"
    yrange = range(3)
    yrange.reverse()
    for j in yrange:
      for k in range(3):
        for i in range(3):
          if ((i,j,k) in self.qubits):
            selfstring += str(self.qubits[(i,j,k)][1]) + ' '
          else:
            selfstring += '_ '
        selfstring += ' | '
      selfstring += "\n"
    return selfstring

  #----------------------------------------------------------------------------
  def __eq__(self, other):
    return (self.phase == other.phase) and (self.qubits == other.qubits)

###############################################################################
def multiply_many(shapes, label=""):
  new_shape = Shape([])
  for shape in shapes:
    new_shape.multiply_with_self(shape)
  new_shape.label = label
  return new_shape

