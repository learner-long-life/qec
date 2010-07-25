from shape import Shape

class Pair:

  def __init__(self, bonds, sign):
    self.bonds = bonds
    self.sign = sign

class Hamiltonian:

  #----------------------------------------------------------------------------
  def __init__(self, generator, bonds):
    self.g = generator
    self.bonds = bonds
    self.dim = []
    current = self.g.bonds
    while (type(current) == type([])):
      current_len = len(current)
      self.dim.append(current_len)
      current = current[0]

    # Create triplets of encoded operators (gauges)
    triple_count = len(bonds[0])
    self.triplets = []

    for i in range(self.g.gauge_count):
      triplet = {'X': self.g.xgauges[i],
                 'Y': self.g.ygauges[i],
                 'Z': self.g.zgauges[i]}
      self.triplets.append(triplet)

    self.errors = {}
    self.create_errors([], self.dim)

  #----------------------------------------------------------------------------
  def create_errors(self, coords, dims):
    if (len(dims) == 1): # Base case, we have bottomed out
      for i in range(dims[0]):
        coord_tuple = tuple(coords + [i])
        triplet = dict()
        for op in ['X', 'Y', 'Z']:
          triplet[op] = Shape.create_singleton(coord_tuple, (0, op))
        self.errors[coord_tuple] = triplet
    else:                # Inductive case
      for i in range(dims[0]):
        self.create_errors(coords + [i], dims[1:])
    
  #----------------------------------------------------------------------------
  def parse(self, argv):
    command = argv[1]
    args = argv[2:]
    if (command == "matlab"): # Produce MATLAB script for finding eigenvals
      self.output_matlab(args)
    elif (command == "latex"): # Output LaTeX figures of gauges
      self.output_gauge_latex()
    elif (command == "verify"): # Verify that gauges form the right interacts.
      self.verify()

  #----------------------------------------------------------------------------
  def verify(self):
    for i in range(len(self.bonds)):
      for j in range(len(self.bonds[i])):
        self.bonds[i][j]
        self.g.bonds[i][j]
        assert (self.bonds[i][j] == self.g.bonds[i][j]), \
               str(self.bonds[i][j].label) + "\n" + \
               str(self.bonds[i][j]) + "\n" + \
               str(self.g.bonds[i][j])

  #----------------------------------------------------------------------------
  def output_gauge_latex(self):
    raise RuntimeError("Not yet implemented, dummy")

  def output_matlab(self, args):
    raise RuntimeError("Not yet implemented")
  #----------------------------------------------------------------------------
  def output_matlab_helper(self, stab_list, argv):
    self.eigenval_count = argv[len(argv)-1]
    self.pairs = []
    for i in range(len(self.bonds)):
      self.pairs.append(Pair(self.bonds[i], argv[i]))

    n = self.g.n
    l = 1
    s = len(self.g.stabilizers)
    r = n-s-l

    size=str(2**r)
    stab_count = 2**s
    stabs = dict()

    for i in range(stab_count):
      filename = "E";
      bits = range(s)
      bits.reverse()
      for j in bits:
        if (((i >> j) & 0x1) == 0x1):
          stabs[stab_list[j]] = -1
          filename += "M"
        else:
          stabs[stab_list[j]] = +1
          filename += "P"

      f = open(filename+".m", 'w')

      f.write("starttime = clock;")
      f.write("Id=speye("+size+");\n")
      f.write("H=Id-Id;\n")
      f.write("clear Id;\n")

      for pair in self.pairs:
        for bond in pair.bonds:
          f.write("display('"+bond.label+"');\n")
          f.write(bond.print_logical_string(r, stabs)+"\n")
          if (pair.sign == '-'):
            f.write("H = H - "+bond.label+";\n")
          else:
            f.write("H = H + "+bond.label+";\n")
          f.write("clear " + bond.label + ";\n")

      f.write("H=-H;\n")
      f.write("OPTS.K="+self.eigenval_count+";\n")
      f.write("OPTS.MAXIT=1000;\n")
      f.write("OPTS.SIGMA='SE';\n")
      f.write("["+filename +"V,"+filename+"D] = irbleigs(H,OPTS)\n")
      f.write("clear H;\n")
      f.write("endtime = clock;\n")
      f.write("etime(endtime, starttime)\n")
      f.write("dlmwrite('"+filename+".dat',"+filename+"V,'precision','%1.15e')\n")
      f.write("dlmwrite('"+filename+"D.dat',"+filename+"D,'precision','%1.15e')\n")
      f.write("system('hostname | mail -s "+filename+" ppham')\n")
      f.write("exit;\n")
      f.close()

  #----------------------------------------------------------------------------
  def translate_errors(self, physical_error):
    encoded_error = Shape([])
    for triplet in self.triplets:
      anticommute_count = 0
      for op in triplet:
        if (not op.commutes_with(physical_error)):
          anticommute_count = anticommute_count + 1
          if (anticommute_count > 1):
            raise RuntimeError("Invalid triplet\n" + str(triplet))
          encoded_error.multiply_with_self(op)
      return encoded_error

  def enumerate_errors(self, erro):
    return

  #----------------------------------------------------------------------------
  def enumerate_error_helper(self, error_count):
    return
