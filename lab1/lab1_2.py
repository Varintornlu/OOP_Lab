inputstr = input("")

lower_count = 0
upper_count = 0

for char in inputstr:
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1

print(lower_count)
print(upper_count)
