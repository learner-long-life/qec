from shape_util import *
import random

###############################################################################
class ShapeRandSymFinder:

  def __init__(self, generator):

    xshapes = generator.xshapes
    yshapes = generator.yshapes
    zshapes = generator.zshapes
    self.gauges = generator.stabilizers

#    f = open("xshapes", "r")
#    xshapes = pickle.load(f)
#    f.close

#    f = open("yshapes", "r")
#    yshapes = pickle.load(f)
#    f.close

#    f = open("zshapes", "r")
#    zshapes = pickle.load(f)
#    f.close

#    f = open("gauges", "r")
#    gauges = pickle.load(f)
#    f.close

    gauge_count = 0
    random.seed()

    while (gauge_count < 20):
      i = random.randint(0, len(xshapes)-1)
      # Choose the X shape
      xshape = xshapes[i]
      yshape = yshapes[i]
      zshape = zshapes[i]
      
      #print "Considering " + str(xshape)
      xvalid = True
      for gauge in self.gauges:
        xvalid = xvalid and (xshape.commutes_with(gauge))
      if (not xvalid):
        continue

      if (yshape.commutes_with(xshape)):
        continue

      yvalid = True
      for gauge in self.gauges:
        yvalid = yvalid and (yshape.commutes_with(gauge))

      if (not yvalid):
        continue

      ycontinue = False

      if (zshape.commutes_with(yshape) or zshape.commutes_with(xshape)):
        continue

      zvalid = True
      for gauge in self.gauges:
        zvalid = zvalid and (zshape.commutes_with(gauge))
      if (not zvalid):
        continue

      xshapes.remove(xshape)
      yshapes.remove(yshape)
      zshapes.remove(zshape)
      gauge_count = gauge_count + 1
      print "Adding X"+str(gauge_count)+": " + str(xshape)
      print "Adding Y"+str(gauge_count)+": " + str(yshape)
      print "Adding Z"+str(gauge_count)+": " + str(zshape)
      self.gauges.extend([xshape, yshape, zshape])
    
