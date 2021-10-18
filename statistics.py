def Average(lst):
    return sum(lst) / len(lst)

def calculateStats(numbers):
  stats = {"avg":float("Nan"),"max":float("Nan"),"min":float("Nan")}

  if numbers:
    stats['avg'] = Average(numbers)
    stats['max'] = max(numbers)
    stats['min'] = min(numbers)

  return stats
