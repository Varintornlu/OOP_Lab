def only_english(string1):
  return ''.join([inputt for inputt in string1 if 'a' <= inputt <= 'z' or 'A' <= inputt <= 'Z'])

input = input()
print(only_english(input))