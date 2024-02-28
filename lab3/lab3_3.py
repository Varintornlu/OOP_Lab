def is_plusone_dictionary(d):
  k = list(d.keys())
  val = list(d.values())
  
  for i in range(len(k)-1):
    if k[i]+2 != k[i+1] or val[i]+2 != val[i+1]:
      return False
    
  return True