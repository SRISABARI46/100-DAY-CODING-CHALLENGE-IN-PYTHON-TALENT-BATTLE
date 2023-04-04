# Day 16 coding Statement : Write a program to identify if the number is Perfect number or not

num=int(input("Enter the number:"))
sum=0
for i in range(1,num):
  if (num%i==0):
    sum+=i
    
if (num==sum):
  print("Perfect Number")
else:
  print("Not a perfect number ")
