# Day 15 coding Statement : Write a program to identify if the number is Strong number or not

n=int(input("Enter the number:"))
temp=n
sum=0
while(n>0):
  fact=1
  rem=n%10
  for i in range(1,rem+1):
    fact=fact*i
  sum=sum+fact
  n=n//10
if (sum==temp):
  print("Strong number")
else:
  print("Not a Strong number")
