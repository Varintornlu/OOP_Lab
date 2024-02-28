## split1
hrin,minin,hrout,minout = [int(e) for e in input("").split()]
hr = hrout - hrin
min = minout - minin
if min < 0:
    min = min*(-1)
""" split2
time = input("")
timee = time.split()
hrin = int(timee[0])
minin = int(timee[1])
hrout = int(timee[2])
minout = int(timee[3])
hr = hrout - hrin
min = minout - minin
"""
""" รับinputคนละบรรทัด
hrin = int(input(""))
minin = int(input(""))
hrout = int(input(""))
minout = int(input(""))
hr = hrout - hrin
min = minout - minin
"""
if hr == 0 and min <= 15:
    price = 0
    print(price)
elif (0 <= hr <= 3) and (hr == 0 and  min > 15):
    if min != 0:
        min = 1
    else:
        min = 0
    price = hr*10 + min*10
    print(price)
elif hr == 3 and min >= 0:
    if min != 0:
        min = 1
    else:
        min = 0
    price = hr*10 + min*20
    print(price)
elif (hr >= 4 and min >= 0) and (hr <= 6 and min == 0):
    if min != 0:
        min = 1
    else:
        min = 0
    price = hr*20 + min*20
    print(price)
elif hr >= 6 and min > 0:
    price = 200
    print(price)

"""
time = input("")
timee = time.split()
hrin = int(timee[0])
minin = int(timee[1])
hrout = int(timee[2])
minout = int(timee[3])
hr = hrout - hrin
min = minout - minin

if hr == 0 and min <= 15:
    price = 0
    print(price)
elif (1 <= hr < 4 and min >=0) or ((0 <= hr <= 3) and (hr == 0 and  min > 15)):
    if min != 0:
        min = 1
    else:
        min = 0
    price = hr*10 + min*10
    print(price)
elif (hr >= 4 and min >= 0) and (hr <= 6 and min == 0):
    if min != 0:
        min = 1
    else:
        min = 0
    price = hr*20 + min*20
    print(price)
elif hr >= 6 and min > 0:
    price = 200
    print(price)
"""
