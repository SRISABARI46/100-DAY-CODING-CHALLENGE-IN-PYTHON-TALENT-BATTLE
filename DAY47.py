# Day 47 coding Statement : Write Program to find longest palindrome in an array

print("Enter the size of array")
n=int(input(""))

print("Enter the elements of array")
arr=[]
for i in range(0,n):
    x=input("")
    arr.append(x)
z=[]
for j in arr:
    k=j[::-1]
    if j==k :
        z.append(j)

longest_palindrome=[]
longest_palindrome.append(z[0])

for i in z:
    j=len(z[0])
    if len(i)>j:
            longest_palindrome[0]=i
