# Day 44 coding Statement : Write Program to find number of even and odd elements in an array

n = int(input("Enter size of array: "))
a = []
print("Enter array elements: ")
for i in range(0,n):
    x = int(input())
    a.append(x)
y = 0
z = 0
for i in range(0, n):
    if a[i]%2==0 :
        y += 1
    else:
        z += 1
print("Number of even elements: ")
print(y)
print("Number of odd elements: ")
print(z)
