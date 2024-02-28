def count_minus(str):
  count = 0
  for i in str:
    if i == '-':
      count += 1
  return count

x = input("").split()
print(count_minus(x))