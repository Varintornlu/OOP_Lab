inp = [int(i) for i in input().split()]
if len(inp) <= 10:
    inp = sorted(inp)
    while inp[0] == 0:
        for i in range(len(inp)):
            if inp[0] == 0:
                x = inp[0]
                inp[0] = inp[i]
                inp[i] = x
    for i in range(len(inp)):
      print(inp[i], end="")
else:
  print("Error")