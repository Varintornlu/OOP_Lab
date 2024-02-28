def char_count(str):
  countc = {}
  for char in str:
    count = countc.get(char, 0)
    countc[char] = count + 1
  return countc