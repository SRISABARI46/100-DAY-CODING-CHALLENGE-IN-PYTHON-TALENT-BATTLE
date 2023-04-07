# Day 35 coding Statement : Write a Program to Count the sum of numbers in a string


string=input("Enter the string:")
j=0
temp=list(string)
for i in temp:
    if (i.isdigit()):
        j=j+int(i)
    else:
        pass
print(j)
