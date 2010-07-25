from shape_util import *

###############################################################################
class ShapeReverseFinder:

  def __init__(self, generator):
    xshapes = generator.xshapes
    yshapes = generator.yshapes
    zshapes = generator.zshapes
    xshapes.reverse()
    yshapes.reverse()
    zshapes.reverse()
    self.gauges = generator.stabilizers
    gauge_count = 0

    # Choose the X shape
    for xshape in xshapes:
      #print "Considering " + str(xshape)
      xvalid = True
      for gauge in self.gauges:
        xvalid = xvalid and (xshape.commutes_with(gauge))

      if (not xvalid):
        continue
        
      for yshape in yshapes:
        #print "Considering " + str(yshape)
        if (yshape.commutes_with(xshape)):
          continue
          
        yvalid = True
        for gauge in self.gauges:
          yvalid = yvalid and (yshape.commutes_with(gauge))
            
        if (not yvalid):
          continue
            
        ycontinue = False
        for zshape in zshapes:
          #print "Considering " + str(zshape)
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
          ycontinue = True
          break

        if (ycontinue):
          break
    
