a = 465
b = 56
c = 7
d = 99

if (a>b):
    maxNum1 = a
else:
    maxNum1 = b

if (c>d):
    maxNum2 = c
else:
    maxNum2 = d   

    if(maxNum2>maxNum1):
        maxNum = maxNum2
    else:
        maxNum = maxNum1
        print("maximum Number out of these is four numbers is", maxNum)