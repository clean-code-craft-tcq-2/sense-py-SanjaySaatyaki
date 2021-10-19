def Average(lst):
    return sum(lst) / len(lst)

def calculateStats(numbers):
  stats = {"avg":float("Nan"),"max":float("Nan"),"min":float("Nan")}

  if numbers:
    stats['avg'] = Average(numbers)
    stats['max'] = max(numbers)
    stats['min'] = min(numbers)
  return stats

class EmailAlert:
  def __init__(self):
      self.emailSent = False

class LEDAlert:
  def __init__(self):
      self.ledGlows = False

class StatsAlerter:

   def __init__(self,max_threshold,alerts):
     self.max_threshold = max_threshold
     self.alerts = alerts

   def checkAndAlert(self,numbers):
     calculate_Stats = calculateStats(numbers)

     if calculate_Stats["max"] > self.max_threshold :
       self.alerts[0].emailSent = True
       self.alerts[1].ledGlows = True

