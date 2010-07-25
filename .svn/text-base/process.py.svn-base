import math

###############################################################################
class ShapeProcess:

  def __init__(self, granularity = 100):
    self.total_status = 0
    self.current_status = 0
    self.last_percent = 0
    self.granularity = granularity

  def update_status(self):
    self.current_status = self.current_status + 1
    current_percent = math.ceil(self.current_status * self.granularity /
                                     self.total_status)
    if (current_percent != self.last_percent):
      self.last_percent = current_percent
      print "Progress: " + str(current_percent)
