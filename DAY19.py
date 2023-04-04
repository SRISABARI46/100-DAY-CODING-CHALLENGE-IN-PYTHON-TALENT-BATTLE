#  Write a program to identify if the number is Armstrong number or not

num=int(input("Enter the number:"))
y=len(str(num))
list=[int(x) for x in str(num)]
d=0
for i in list:
    ans=i**y
    d=d+ans
if num==d:
    print("Armstrong number")
else:
    print("Not an Armstrong number ")
