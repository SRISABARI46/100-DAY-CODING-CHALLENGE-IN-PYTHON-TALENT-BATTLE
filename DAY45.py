# Day 45 coding Statement : Write Program to find smallest and largest element in an array

print("Enter the size of array :")
n=int(input(""))
print("Enter the elements :")
a=[]
for i in range(0,n):
    x=int(input())
    a.append(x)

a.sort()
print("Smallest Number :")
print(a[0])
print("Largest Number :")
print(a[-1])
