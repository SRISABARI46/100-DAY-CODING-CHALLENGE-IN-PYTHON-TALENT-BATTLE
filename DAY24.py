# Day 24 coding Statement : Write a program to print Pyramid pattern using stars

num=int(input("Enter the number of rows:"))
for i in range(num):
    for j in range(i+1):
        print("*",end="")
    print("\n")


