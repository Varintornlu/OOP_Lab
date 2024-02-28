""" sol1
def palindrome(n):
    if str(n) == str(n)[::-1]:
        return str(n) == str(n)[::-1]

def find_palin():
    max_palin = 0
    for i in range(100,1000):
        for j in range(100,1000):
            result = i*j
            if palindrome(result) and result >  max_palin:
                max_palin = result
                ##print(i , j)
    return max_palin

answer = find_palin()
print(answer)
"""

""" sol2
def palindrome(n):
    if str(n) == str(n)[::-1]:
        return str(n) == str(n)[::-1]
    
max_palin = 0

for i in range(100,1000):
    for j in range(100,1000):
        result = i*j
        if palindrome(result) and result >  max_palin:
            max_palin = result
            ##print(i , j)
print(max_palin)
"""

##sol3

max_palin = 0

for i in range(100,1000):
    for j in range(100,1000):
        result = i*j
        if str(result) == str(result)[::-1] and result >  max_palin:
            max_palin = result
            ##print(i , j)
print(max_palin)


