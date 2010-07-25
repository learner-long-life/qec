from generator_333_xz import *
from hamiltonian_333_xyz import Hamiltonian_333_XYZ, Hamiltonian
import sys

S1 = g.xstabilizers[0]
S2 = g.xstabilizers[1]
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
Z21 = g.zgauges[20]
Z22 = g.zgauges[21]

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
Y21 = g.ygauges[20]
Y22 = g.ygauges[21]

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
X21 = g.xgauges[20]
X22 = g.xgauges[21]

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

ZC1 = multiply_many([ZB1, ZB2, ZB4, ZB5])
ZC2 = multiply_many([ZB2, ZB3, ZB5, ZB6])
ZC3 = multiply_many([ZB4, ZB5, ZB7, ZB8])
ZC4 = multiply_many([ZB5, ZB6, ZB8, ZB9])
ZC5 = multiply_many([ZB10, ZB11, ZB13, ZB14])
ZC6 = multiply_many([ZB11, ZB12, ZB14, ZB15])
ZC7 = multiply_many([ZB13, ZB14, ZB16, ZB17])
ZC8 = multiply_many([ZB14, ZB15, ZB17, ZB18])

ZF228 = multiply_many([Z21, Z13, Z15])
ZF229 = multiply_many([Z13, ZB12, ZB15])
ZF230 = multiply_many([Z15, ZB1, ZB4])
ZF231 = multiply_many([ZF229, ZC5])
ZF232 = multiply_many([ZF231, ZC1])
ZF233 = multiply_many([ZF230, ZC2])
ZF234 = multiply_many([ZF233, ZC6])
ZF235 = multiply_many([Z22, Z14, Z16])
ZF236 = multiply_many([Z14, ZB15, ZB18])
ZF237 = multiply_many([Z16, ZB4, ZB7])
ZF238 = multiply_many([ZF236, ZC7])
ZF239 = multiply_many([ZF238, ZC3], "ZF239")
ZF240 = multiply_many([ZF237, ZC4])
ZF241 = multiply_many([ZF240, ZC8])
ZF243 = multiply_many([ZF228, ZB11, ZB14])
ZF242 = multiply_many([ZF243, ZF229])
ZF244 = multiply_many([ZF243, ZF234])
ZF245 = multiply_many([ZF228, ZF231])
ZF246 = multiply_many([ZF228, ZF233])
ZF248 = multiply_many([ZF228, ZB2, ZB5])
ZF247 = multiply_many([ZF248, ZF232])
ZF249 = multiply_many([ZF248, ZF230])
ZF250 = multiply_many([ZF235, ZB14, ZB17])
ZF251 = multiply_many([ZF235, ZB5, ZB8], "ZF251")
ZF252 = multiply_many([ZF250, ZF236])
ZF253 = multiply_many([ZF250, ZF241])
ZF254 = multiply_many([ZF251, ZF239], "ZF254")
ZF255 = multiply_many([ZF251, ZF237])
ZF256 = multiply_many([ZF235, ZF238])
ZF257 = multiply_many([ZF235, ZF240])

#YZB1 = ZF247
YZB1 = multiply_many([S6, Z1, Z15, Z18, Z2, Z21], "YZB1")
#YZB2 = ZF248
YZB2 = multiply_many([S5, Z1, Z13, Z15, Z19, Z2, Z21, Z4, Z5], "YZB2")
#YZB3 = ZF249
YZB3 = multiply_many([S5, Z13, Z19, Z21, Z4, Z5], "YZB3")
#YZB4 = ZF254
YZB4 = multiply_many([S6, Z16, Z17, Z2, Z22, Z3], "YZB4")
#YZB5 = ZF251
YZB5 = multiply_many([S5, Z14, Z16, Z2, Z20, Z22, Z3, Z5, Z6], "YZB5")
#YZB6 = ZF255
YZB6 = multiply_many([S5, Z14, Z20, Z22, Z5, Z6], "YZB6")
#YZB7 = ZF245
YZB7 = multiply_many([S6, Z15, Z18, Z21], "YZB7")
#YZB8 = ZF228
YZB8 = multiply_many([Z13, Z15, Z21], "YZB8")
#YZB9 = ZF246
YZB9 = multiply_many([S5, Z13, Z19, Z21], "YZB9")
#YZB10 = ZF256
YZB10 = multiply_many([S6, Z16, Z17, Z22], "YZB10")
#YZB11 = ZF235
YZB11 = multiply_many([Z14, Z16, Z22], "YZB11")
#YZB12 = ZF257
YZB12 = multiply_many([S5, Z14, Z20, Z22], "YZB12")
#YZB13 = ZF242
YZB13 = multiply_many([S6, Z15, Z18, Z21, Z7, Z8], "YZB13")
#YZB14 = ZF243
YZB14 = multiply_many([S6, Z10, Z11, Z13, Z15, Z18, Z21, Z7, Z8], "YZB14")
#YZB15 = ZF244
YZB15 = multiply_many([S5, Z10, Z11, Z13, Z19, Z21], "YZB15")
#YZB16 = ZF252
YZB16 = multiply_many([S6, Z16, Z17, Z22, Z8, Z9], "YZB16")
#YZB17 = ZF250
YZB17 = multiply_many([S6, Z11, Z12, Z14, Z16, Z17, Z22, Z8, Z9], "YZB17")
#YZB18 = ZF253
YZB18 = multiply_many([S5, Z11, Z12, Z14, Z20, Z22], "YZB18")

yzbonds = [YZB1, YZB2, YZB3, YZB4, YZB5, YZB6, YZB7, YZB8, YZB9,
           YZB10, YZB11, YZB12, YZB13, YZB14, YZB15, YZB16, YZB17, YZB18]

XC1 = multiply_many([XB1, XB2, XB7, XB8])
XC2 = multiply_many([XB4, XB5, XB10, XB11])
XC3 = multiply_many([XB2, XB3, XB8, XB9])
XC4 = multiply_many([XB5, XB6, XB11, XB12])
XC5 = multiply_many([XB7, XB8, XB13, XB14])
XC6 = multiply_many([XB10, XB11, XB16, XB17])
XC7 = multiply_many([XB8, XB9, XB14, XB15])
XC8 = multiply_many([XB11, XB12, XB17, XB18])

XF258 = multiply_many([X22, X17, XC2])
XF259 = multiply_many([X17, XB13, XB14])
XF260 = multiply_many([X20, X14])
XF261 = multiply_many([XF259, XC1])
XF262 = multiply_many([XF261, XC2])
XF263 = multiply_many([XF260, XC5])
XF264 = multiply_many([XF260, XC6])
XF265 = multiply_many([X21, X18, XC4])
XF266 = multiply_many([X18, XB14, XB15])
XF267 = multiply_many([X19, X13])
XF268 = multiply_many([XF266, XC3])
XF269 = multiply_many([XF268, XC4])
XF270 = multiply_many([XF267, XC7])
XF271 = multiply_many([XF267, XC8])

XF272 = multiply_many([XF258, XB16, XB17])
XF273 = multiply_many([XF272, XB13, XB14])
XF274 = multiply_many([XF258, XF264])
XF275 = multiply_many([XF274, XF262])
XF275B = multiply_many([XF274, XB10, XB11])
XF276 = multiply_many([XF275B, XB7, XB8])
XF277 = multiply_many([XF275, XB4, XB5])
XF278 = multiply_many([XF277, XB1, XB2])
XF279 = multiply_many([XF265, XB17, XB18])
XF280 = multiply_many([XF279, XB14, XB15])
XF281 = multiply_many([XF265, XF271])
XF282 = multiply_many([XF281, XF269])
XF283 = multiply_many([XF281, XB11, XB12])
XF284 = multiply_many([XF283, XB8, XB9])
XF285 = multiply_many([XF282, XB5, XB6])
XF286 = multiply_many([XF285, XB2, XB3])

#YXB1 = XF278
YXB1 = multiply_many([S1, S2, X1, X16, X2, X20, X22], "YXB1")
#YXB2 = XF277
YXB2 = multiply_many([S1, S2, X16, X20, X22], "YXB2")
#YXB3 = XF275
YXB3 = multiply_many([S1, S2, X16, X20, X22, X4, X5], "YXB3")
#YXB4 = XF286
YXB4 = multiply_many([S1, S2, X15, X19, X2, X21, X3], "YXB4")
#YXB5 = XF285
YXB5 = multiply_many([S1, S2, X15, X19, X21], "YXB5")
#YXB6 = XF282
YXB6 = multiply_many([S1, S2, X15, X19, X21, X5, X6], "YXB6")
#YXB7 = XF276
YXB7 = multiply_many([S1, S2, X1, X16, X17, X2, X20, X22, X7, X8], "YXB7")
#YXB8 = XF275B
YXB8 = multiply_many([S2, X17, X20, X22], "YXB8")
#YXB9 = XF274
YXB9 = multiply_many([X10, X11, X14, X17, X20, X22, X4, X5], "YXB9")
#YXB10 = XF284
YXB10 = multiply_many([S1, S2, X15, X18, X19, X2, X21, X3, X8, X9], "YXB10")
#YXB11 = XF283
YXB11 = multiply_many([S2, X18, X19, X21], "YXB11")
#YXB12 = XF281
YXB12 = multiply_many([X11, X12, X13, X18, X19, X21, X5, X6], "YXB12")
#YXB13 = XF273
YXB13 = multiply_many([S2, X14, X17, X22, X7, X8], "YXB13")
#YXB14 = XF272
YXB14 = multiply_many([S2, X14, X17, X22], "YXB14")
#YXB15 = XF258
YXB15 = multiply_many([S2, X10, X11, X14, X17, X22], "YXB15")
#YXB16 = XF280
YXB16 = multiply_many([S2, X13, X18, X21, X8, X9], "YXB16")
#YXB17 = XF279
YXB17 = multiply_many([S2, X13, X18, X21], "YXB17")
#YXB18 = XF265
YXB18 = multiply_many([S2, X11, X12, X13, X18, X21], "YXB18")

yxbonds = [YXB1, YXB2, YXB3, YXB4, YXB5, YXB6, YXB7, YXB8, YXB9,
           YXB10, YXB11, YXB12, YXB13, YXB14, YXB15, YXB16, YXB17, YXB18]

class Hamiltonian_333_XZ(Hamiltonian_333_XYZ):

  def output_matlab(self, args):
    Hamiltonian.output_matlab_helper(self, [6,5,2,1], args)

#------------------------------------------------------------------------------
# Second verse, same as the first (use XYZ b/c nothing has changed for XZ)
h = Hamiltonian_333_XZ(g, [xbonds + yxbonds, zbonds + yzbonds])
