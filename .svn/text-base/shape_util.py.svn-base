import pickle
import random
import math

def factorial(n):
  total = 1
  for i in range(1,n+1):
    total = total * i
  return total

def combo(n, k):
  return factorial(n) / (factorial(k) * factorial(n-k))

def perm(n, k):
  return factorial(n) / factorial(n-k)

def combo_rep(n, k):
  return combo(n - 1 + k, k)

def perm_rep(n, k):
  return math.pow(n,k)

def combo_rep_least(n, k):
  return combo(n - 1, n - k)

def opmult(op1, op2):

  return_phase = (op1[0] + op2[0]) % 4 # Take sum of phase exponents mod 4
  op1 = op1[1]
  op2 = op2[1]
  return_op = 'I'
    
  if (op1 == 'I'):
    return_op = op2
  elif (op2 == 'I'):
    return_op = op1
  elif (op1 == 'X'):
    if (op2 == 'X'):   # X*X = I
      return_op = 'I';
    elif (op2 == 'Y'): # X*Y = iZ
      return_phase = (return_phase + 1) % 4
      return_op = 'Z'
    elif (op2 == 'Z'): # X*Z = -iY
      return_phase = (return_phase + 3) % 4
      return_op = 'Y'
    else:
      assert(False), op2
  elif (op1 == 'Y'):
    if (op2 == 'X'):   # Y*X = -iZ
      return_phase = (return_phase + 3) % 4
      return_op = 'Z'
    elif (op2 == 'Y'): # Y*Y = I
      return_op = 'I'
    elif (op2 == 'Z'): # Y*Z = iX
      return_phase = (return_phase + 1) % 4
      return_op = 'X'
    else:
      assert(False), op2
  elif (op1 == 'Z'):
    if (op2 == 'X'):   # Z*X = iY
      return_phase = (return_phase + 1) % 4
      return_op = 'Y'  # Z*Y = -iX
    elif (op2 == 'Y'):
      return_phase = (return_phase + 3) % 4
      return_op = 'X'
    elif (op2 == 'Z'): # Z*Z = I
      return_op = 'I'
    else:
      assert(False), op2
  else:
    assert (False), "op1='"+op1+"' op2='"+op2+"'"

  return (return_phase, return_op)

def translate_label(label):
  return int(label[1:])

# Wrapper class for static (class) methods:
class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable
