from generator_333_xyz import *
from hamiltonian import *
import sys

S1 = g.xstabilizers[0]
S2 = g.xstabilizers[1]
S3 = g.ystabilizers[0]
S4 = g.ystabilizers[1]
S5 = g.zstabilizers[0]
S6 = g.zstabilizers[1]

Z1 = g.zgauges[0]
Z2 = g.zgauges[1]
Z3 = g.zgauges[2]
Z4 = g.zgauges[3]
Z5 = g.zgauges[4]
Z6 = g.zgauges[5]
Z7 = g.zgauges[6]
Z8 = g.zgauges[7]
Z9 = g.zgauges[8]
Z10 = g.zgauges[9]
Z11 = g.zgauges[10]
Z12 = g.zgauges[11]
Z13 = g.zgauges[12]
Z14 = g.zgauges[13]
Z15 = g.zgauges[14]
Z16 = g.zgauges[15]
Z17 = g.zgauges[16]
Z18 = g.zgauges[17]
Z19 = g.zgauges[18]
Z20 = g.zgauges[19]

X1 = g.xgauges[0]
X2 = g.xgauges[1]
X3 = g.xgauges[2]
X4 = g.xgauges[3]
X5 = g.xgauges[4]
X6 = g.xgauges[5]
X7 = g.xgauges[6]
X8 = g.xgauges[7]
X9 = g.xgauges[8]
X10 = g.xgauges[9]
X11 = g.xgauges[10]
X12 = g.xgauges[11]
X13 = g.xgauges[12]
X14 = g.xgauges[13]
X15 = g.xgauges[14]
X16 = g.xgauges[15]
X17 = g.xgauges[16]
X18 = g.xgauges[17]
X19 = g.xgauges[18]
X20 = g.xgauges[19]

Y1 = g.ygauges[0]
Y2 = g.ygauges[1]
Y3 = g.ygauges[2]
Y4 = g.ygauges[3]
Y5 = g.ygauges[4]
Y6 = g.ygauges[5]
Y7 = g.ygauges[6]
Y8 = g.ygauges[7]
Y9 = g.ygauges[8]
Y10 = g.ygauges[9]
Y11 = g.ygauges[10]
Y12 = g.ygauges[11]
Y13 = g.ygauges[12]
Y14 = g.ygauges[13]
Y15 = g.ygauges[14]
Y16 = g.ygauges[15]
Y17 = g.ygauges[16]
Y18 = g.ygauges[17]
Y19 = g.ygauges[18]
Y20 = g.ygauges[19]

ZB1 = multiply_many([Z1], "ZB1")

ZB2 = multiply_many([Z20, Z1, Z4], "ZB2")

ZB3 = multiply_many([Z4], "ZB3")

ZB4 = multiply_many([Z2], "ZB4")

ZB5 = multiply_many([S5, Z19, Z20, Z2, Z5], "ZB5")

ZB6 = multiply_many([Z5], "ZB6")

ZB7 = multiply_many([Z3], "ZB7")

ZB8 = multiply_many([Z19, Z3, Z6], "ZB8")

ZB9 = multiply_many([Z6], "ZB9")

ZB10 = multiply_many([Z7], "ZB10")

ZB11 = multiply_many([Z17, Z7, Z10], "ZB11")

ZB12 = multiply_many([Z10], "ZB12")

ZB13 = multiply_many([Z8], "ZB13")

ZB14 = multiply_many([S6, Z17, Z18, Z8, Z11], "ZB14")

ZB15 = multiply_many([Z11], "ZB15")

ZB16 = multiply_many([Z9], "ZB16")

ZB17 = multiply_many([Z18, Z9, Z12], "ZB17")

ZB18 = multiply_many([Z12], "ZB18")

zbonds = [ZB1,  ZB2,  ZB3,  ZB4,  ZB5,  ZB6,  ZB7,  ZB8,  ZB9,
          ZB10, ZB11, ZB12, ZB13, ZB14, ZB15, ZB16, ZB17, ZB18]

XB1 = multiply_many([X1], "XB1")

XB2 = multiply_many([X2], "XB2")

XB3 = multiply_many([X3], "XB3")

XB4 = multiply_many([X4], "XB4")

XB5 = multiply_many([X5], "XB5")

XB6 = multiply_many([X6], "XB6")

XB7 = multiply_many([X15, X1, X7], "XB7")

XB8 = multiply_many([S1, X15, X16, X2, X8], "XB8")

XB9 = multiply_many([X16, X3, X9], "XB9")

XB10 = multiply_many([X13, X4, X10], "XB10")

XB11 = multiply_many([S2, X13, X14, X11, X5], "XB11")

XB12 = multiply_many([X14, X6, X12], "XB12")

XB13 = multiply_many([X7], "XB13")

XB14 = multiply_many([X8], "XB14")

XB15 = multiply_many([X9], "XB15")

XB16 = multiply_many([X10], "XB16")

XB17 = multiply_many([X11], "XB17")

XB18 = multiply_many([X12], "XB18")

xbonds = [XB1,  XB2,  XB3,  XB4,  XB5,  XB6,  XB7,  XB8,  XB9,
          XB10, XB11, XB12, XB13, XB14, XB15, XB16, XB17, XB18]

YP1 = multiply_many([XB1, XB7, ZB1, ZB2], "YP1")
YP2 = multiply_many([XB4, XB10, ZB2, ZB3], "YP2")
YP3 = multiply_many([XB2, XB8, ZB4, ZB5], "YP3")
YP4 = multiply_many([XB5, XB11, ZB5, ZB6], "YP4")
YP5 = multiply_many([XB3, XB9, ZB7, ZB8], "YP5")
YP6 = multiply_many([XB6, XB12, ZB8, ZB9], "YP6")
YP7 = multiply_many([XB7, XB13, ZB10, ZB11], "YP7")
YP8 = multiply_many([XB10, XB16, ZB11, ZB12], "YP8")
YP9 = multiply_many([XB14, XB8, ZB13, ZB14], "YP9")
YP10 = multiply_many([XB17, XB11, ZB14, ZB15], "YP10")
YP11 = multiply_many([XB15, XB9, ZB16, ZB17], "YP11")
YP12 = multiply_many([XB18, XB12, ZB17, ZB18], "YP12")

YC1 = multiply_many([YP1, YP3], "YC1")
YC2 = multiply_many([YP2, YP4], "YC2")
YC3 = multiply_many([YP3, YP5], "YC3")
YC4 = multiply_many([YP4, YP6], "YC4")
YC5 = multiply_many([YP7, YP9], "YC5")
YC6 = multiply_many([YP8, YP10], "YC6")
YC7 = multiply_many([YP9, YP11], "YC7")
YC8 = multiply_many([YP10, YP12], "YC8")

YD1 = multiply_many([S3, YC1], "YD1")
YD2 = multiply_many([S3, YC2], "YD2")
YD3 = multiply_many([S4, YC3], "YD3")
YD4 = multiply_many([S4, YC4], "YD4")
YD5 = multiply_many([S3, YC5], "YD5")
YD6 = multiply_many([S3, YC6], "YD6")
YD7 = multiply_many([S4, YC7], "YD7")
YD8 = multiply_many([S4, YC8], "YD8")

YB1 = multiply_many([S1, S2, S3, S6, Y1, Y2, Z15, Z18, X16, X20], "YB1")

YB2 = multiply_many([S1, S2, S3, S5, Z1, Z2, Z4, Z5, Z13, Z15, Z19, X16, X20], "YB2")

YB3 = multiply_many([S1, S2, S3, S5, Y4, Y5, Z13, Z19, X16, X20], "YB3")

YB4 = multiply_many([S1, S2, S4, S6, Y2, Y3, X15, X19, Z16, Z17], "YB4")

YB5 = multiply_many([S1, S2, S4, S5, Z2, Z3, Z5, Z6, Z14, Z16, Z20, X15, X19], "YB5")

YB6 = multiply_many([S1, S2, S4, S5, Y5, Y6, Z14, Z20, X15, X19], "YB6")

YB13 = multiply_many([S2, S3, S6, Y7, Y8, Z15, Z18, X14, X17], "YB13")

YB14 = multiply_many([S2, S3, S6, Z7, Z8, Z10, Z11, Z13, Z15, Z18, X14, X17], "YB14")

YB15 = multiply_many([S2, S3, S5, Y10, Y11, Z13, Z19, X14, X17], "YB15")

YB16 = multiply_many([S2, S4, S6, Y8, Y9, Z16, Z17, X13, X18], "YB16")

YB17 = multiply_many([S2, S4, S6, Z8, Z9, Z11, Z12, Z14, Z16, Z17, X13, X18], "YB17")

YB18 = multiply_many([S2, S4, S5, Y11, Y12, Z14, Z20, X13, X18], "YB18")

YB7 = multiply_many([S1, S2, S3, S6, Z15, Z18, X1, X2, X7, X8, X16, X17, X20], "YB7")

YB8 = multiply_many([S2, S3, Z13, Z15, X17, X20], "YB8")

YB9 = multiply_many([S3, S5, Z13, Z19, X4, X5, X10, X11, X14, X17, X20], "YB9")

YB10 = multiply_many([S1, S2, S4, S6, Z16, Z17, X2, X3, X8, X9, X15, X18, X19], "YB10")

YB11 = multiply_many([S2, S4, Z14, Z16, X18, X19], "YB11")

YB12 = multiply_many([S4, S5, Z14, Z20, X5, X6, X11, X12, X13, X18, X19], "YB12")

ybonds = [YB1,  YB2,  YB3,  YB4,  YB5,  YB6,  YB7,  YB8,  YB9,
          YB10, YB11, YB12, YB13, YB14, YB15, YB16, YB17, YB18]

#------------------------------------------------------------------------------
class Hamiltonian_333_XYZ(Hamiltonian):

  def output_matlab(self, args):
    Hamiltonian.output_matlab_helper(self, [6,5,4,3,2,1], args)

  #----------------------------------------------------------------------------
  def output_gauge_latex(self):
    for gauge in self.g.gauges:
      filename = "G"+gauge.label+".tex"
      f = open(filename, 'w')

      f.write("$"+Shape.phase_string(gauge.phase) + "$\n")
      f.write("\\begin{pspicture}(-1.5,-2)(1.5,2)\n")
      f.write("\lattice\n")

      for qubit in gauge.qubits.keys():
        op = gauge.qubits[qubit]
        xcoord = str(2 - qubit[0])
        ycoord = str(2 - qubit[1])
        zcoord = str(qubit[2])
        if (op[1] == 'X'):
          f.write("  \pstThreeDDot[dotscale=2,linecolor=red]")
        elif (op[1] == 'Y'):
          f.write("  \pstThreeDDot[dotscale=2,linecolor=green]")
        elif (op[1] == 'Z'):
          f.write("  \pstThreeDDot[dotscale=2,linecolor=blue]")
        f.write("("+xcoord+","+ycoord+","+zcoord+")\n")

      f.write("\end{pspicture}\n")

      f.close()

#------------------------------------------------------------------------------
h = Hamiltonian_333_XYZ(g, [xbonds, ybonds, zbonds])
