
# Day 36 coding Statement : Write a Program to Capitalize the first and last letter of each word of a string

string=input("Enter the string:")

string=string[0:1].upper()+string[1:-2]+string[-1].upper()

print(string)
