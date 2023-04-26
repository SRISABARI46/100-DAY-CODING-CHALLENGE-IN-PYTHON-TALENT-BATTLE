# Day 38 coding Statement : Write a Program to print Non-repeating characters in a string


string=input("Enter the string:")
for i in string:
    c=0
    for j in string:
        if i==j:
            c+=1
        if c>1:
            break
    if  c==1:
        print(i,end=" ")
