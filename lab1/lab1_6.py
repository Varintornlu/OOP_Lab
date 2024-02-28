""" 2 loop
n = 10

for row in range(n):
    for col in range(n):
        if row + col < n:
            print(' ', end="")
        else:
            print("#", end='')
    print('#')
"""

## 1 loop
n = 10

for i in range(n):
  print(' ' * (n - i) + '#' * (i + 1))


