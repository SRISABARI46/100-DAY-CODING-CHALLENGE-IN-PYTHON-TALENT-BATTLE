# Day 32 coding Statement : Write a Program to Remove vowels from a string

string=input("Enter the string:")

vowels=('a','e','i','o','u','A','E','I','O','U')
ans=""
for i in string:
    if i not in vowels:
        ans=ans+i
print(ans)
