# Day 26 coding Statement : Write a program to calculate Maximum number of handshakes

people=int(input("Enter the number of people in the room:"))
j=0
for i in range(1,people+1):
    j=j+(people-i)
print(j)
