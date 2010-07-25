from finder import *

###############################################################################
class ShapeBasicFinder(ShapeFinder):

  def find_gauges(self):
    self.total_status = len(self.xshapes)
    self.gauges = self.generator.gauges

    # Choose the X shape
    for xshape in self.xshapes:
      self.update_status()
      if (not self.commutes_with_gauges(xshape)):
        continue
        
      for zshape in self.zshapes:
        if (zshape.commutes_with(xshape)):
          continue

        if (not self.commutes_with_gauges(zshape)):
          continue
            
        for yshape in self.yshapes:
          if (yshape.commutes_with(zshape) or yshape.commutes_with(xshape)):
            continue

          if (not self.commutes_with_gauges(yshape)):
            continue

          self.add_gauge(xshape, yshape, zshape)
          break

    
