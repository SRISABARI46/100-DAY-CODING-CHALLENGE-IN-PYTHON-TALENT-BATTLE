# Day 11 coding Statement:  Write a program to find Fibonacci series up to n


num=int(input("Enter the number:"))
x=0
y=1
z=0

if num<=0:
    print("Please enter value greater than 0")
else:
    for i in range(0,num):
        print(z,end=",")
        x=y
        y=z
        z=x+y
