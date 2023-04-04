# Day 17 coding Statement : Write a program to find the Factors of a number

num=int(input("Enter the number:"))
for i in range(1,num):
  if (num%i==0):
    print(i,end=",")
print(num,end="")
