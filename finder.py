from generator import *
from process import *
import math

###############################################################################
class ShapeFinder(ShapeProcess):

  def __init__(self, generator):
    self.xshapes = generator.xshapes
    self.yshapes = generator.yshapes
    self.zshapes = generator.zshapes
    self.generator = generator
    self.gauge_count = 0
    ShapeProcess.__init__(self)

  def find_gauges(self):
    raise RuntimeError("Not implemented, dumbass")

  def commutes_with_gauges(self, shape):
    for gauge in (self.gauges + self.generator.gauges):
      if (not shape.commutes_with(gauge)):
        return False
    return True

  def add_gauge(self, xshape, yshape, zshape):
    self.xshapes.remove(xshape)
    #self.yshapes.remove(yshape)
    self.zshapes.remove(zshape)
    self.gauge_count = self.gauge_count + 1
    print "Adding gauge " + str(self.gauge_count)
    print str(xshape)
    print str(yshape)
    print str(zshape)
    self.gauges.extend([xshape, yshape, zshape])

