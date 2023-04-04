# Day 6 coding Statement:  Write a program to find the Quadrants in which coordinates lie

x=int(input("Enter the x and value:"))
y=int(input("Enter the y and value:"))

if( x > 0 and y > 0 ):
    print(" This point lies in first quadrant.")
elif(x < 0 and y < 0):
    print("This point lies in third quadrant.")
elif(x < 0 and y > 0):
    print("This point  lies in second quadrat.")
else:
    print("This point lies in fourth quadrant.")
