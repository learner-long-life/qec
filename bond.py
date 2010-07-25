class Bond:

  def __init__(self, p1, p2, op, phase, label=""):
    if (sum(p1) < sum(p2)):
      self.p1 = p1
      self.p2 = p2
    else:
      self.p1 = p2
      self.p2 = p1
    assert((op == 'X') or (op == 'Y') or (op == 'Z'))
    self.phase = phase
    self.op = (0, op) # phaseless
    self.qubits = {p1: self.op, p2: self.op}
    self.label = ""
    self.ancestry = ""
    
  def __eq__(self, other):
    return (self.p1 == other.p1) and (self.p2 == other.p2) and \
           (self.op == other.op) and (self.phase == other.phase)

  def add_to_shape(self, shape):
    shape.add_phase(self.phase)
    shape.add_qubit(self.p1, self.op)
    shape.add_qubit(self.p2, self.op)

  def intersects(self, other):
    return other.contains(self.p1) or other.contains(self.p2)

  def contains(self, point):
    return (self.p1 == point) or (self.p2 == point)

