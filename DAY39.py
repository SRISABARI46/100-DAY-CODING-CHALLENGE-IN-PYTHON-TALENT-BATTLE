# Day 39 coding Statement : Write a Program to check if two strings are Anagram or not

string1,string2=input("Enter the both word:").split()
count=0
for  i in string1:
    for j in string2:
        if i==j:
            count=count+1
if count==len(string1):
    print("Anagram")
else:
    print("Not a Anagram")
