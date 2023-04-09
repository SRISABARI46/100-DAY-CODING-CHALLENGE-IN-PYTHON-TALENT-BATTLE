
# Day 37 coding Statement : Write a Program to calculate the Frequency of characters in a string

string=input("Enter the string:")

for i in string:
    frequency = string.count(i)
    print("The frequency of " + str(i) + " is " + str(frequency))
        
