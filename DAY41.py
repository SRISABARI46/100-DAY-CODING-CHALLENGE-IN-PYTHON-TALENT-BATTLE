# Day 41 coding Statement : Check if two strings match where one string contains wildcard characters

def solve(str1,str2):
    a,b=len(str1),len(str2)
    if a==0 and b==0:
        return True
    if (a > 1 and str1[0] == '*') and b == 0:
        return False
    if (a > 1 and str1[0] == '?') or (a != 0 and b !=0 and str1[0] == str2[0]):
        return solve(str1[1:],str2[1:]);
    if a !=0 and str1[0] == '*':
        return solve(str1[1:],str2) or solve(str1,str2[1:])
    return False

str1=input('Enter string with wild characters: ')
str2=input('Enter string without wild characters: ')
if (solve(str1,str2)):
    print("Yes it matches")
else:
    print("Not Matching!")
