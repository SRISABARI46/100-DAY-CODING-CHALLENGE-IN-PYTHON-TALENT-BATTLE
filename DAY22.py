# Day 22 coding Statement : Write a program to express a number as a sum of two prime numbers

num=int(input("Enter the number:"))

if num%2 ==1:
    x=num-2
    if x>1:
        for i in range(2,x):
            if x%i == 0:
                print("Can't express with prime numbers")
                break
        else:
            print(num,"can be expressed as a sum of 2 and",x)
            
elif num%2==0:
    arr=[]
    arr2=[]
    for a in range(2,num):
        arr.append(a)
    print(arr)
  
    for b in arr:
            c=0
            for d in  range(1,b):
                if b%d == 0:
                    c=c+1
            if c==1:
                arr2.append(b)
    print(arr2) 
    
    for e in arr2:
        f=num-e
        if f>1:
            for g in range (2,f):
                if( f%g==0):
                    break
        
            else:   
                    print(num,"can be expressed as a sum of{} and {} ".format(e,f))
