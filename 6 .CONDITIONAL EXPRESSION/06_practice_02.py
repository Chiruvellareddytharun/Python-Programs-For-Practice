m1 = int(input("enter the marks for sub 1: "))
m2 = int(input("enter the marks for sub 2: "))
m3 = int(input("enter the marks for sub 3: "))

overAll =(m1+m2+m3)/3

if (overAll>=40):
    if(m1>=33 and m2>=33 and m3>=33):
        print("you are passed in all subjects")
        