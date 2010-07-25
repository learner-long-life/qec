from pylab import *
import sys

stabs = sys.argv[1]
basedir = "data-"+stabs
title_string = "Eigenvalue Spectrum for H = "

if (stabs[0]=='p'):
  title_string += "+"
else:
  title_string += "-"
title_string += "X "

if (stabs[1]=='p'):
  title_string += "+"
else:
  title_string += "-"
title_string += "Y "

if (stabs[2]=='p'):
  title_string += "+"
else:
  title_string += "-"
title_string += "Z"

print basedir
s = 6
stab_count = 2**s
eigenvalues = dict()
ticks = []

for i in range(stab_count):
  stabs = dict()
  filename = "E";
  bits = range(s)
  bits.reverse()
  for j in bits:
    if (((i >> j) & 0x1) == 0x1):
      stabs[j+1] = -1
      filename += "M"
    else:
      stabs[j+1] = +1
      filename += "P"

  f = open(basedir+"/"+filename+".dat", 'r')
  ev_list = []
  ev = f.readline()
  while (len(ev) != 0):
    ev_list.append(float(ev))
    ev = f.readline()
  eigenvalues[filename] = ev_list
  x = ones(len(ev_list))*(i+1)
  plot(x, ev_list, 'o')
  #ticks.append(text((i+1), 0, filename, rotation='vertical', fontsize=10))

ticks = eigenvalues.keys()
ticks.sort()
ticks.reverse()
xticks( arange(1,stab_count+1), ticks, rotation='vertical', fontsize=10 )
xlabel('Stab')
ylabel('Energy')
title(title_string)
grid(True)
show()
