car=int(input("enter the car speed:"))
cycle=int(input("enter the cycle speed:"))
if car>0 and cycle>car:
    print("cycle is faster than car")
else:
    print("car is faster than cycle")