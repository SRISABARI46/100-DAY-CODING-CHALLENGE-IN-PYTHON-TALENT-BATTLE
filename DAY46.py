# Day 46 coding Statement : Write Program to find sum of elements in an array

print("Enter the size of array :")
n=int(input(""))
print("Enter the elements :")
a=[]
for i in range(0,n):
    x=int(input())
    a.append(x)
sum=0
for j in a:
    sum=sum+j

print(sum)
