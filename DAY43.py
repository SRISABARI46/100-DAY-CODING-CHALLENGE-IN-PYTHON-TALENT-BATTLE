# Day 43 coding Statement : Write Program to find the array type

n=int(input("Enter the size of array:"))
arr=[]
print("Enter size of elements:")

for i in range(0,n):
    t=int(input())
    arr.append(t)

odd=0
even=0
    
for i in range(0,n):
    if(arr[i]%2==1):
        odd+=1
    else:
        even+=1

if(odd==n):
    print("odd")
elif(even==n):
    print("Even")
else:
    print("Mixed")
    
