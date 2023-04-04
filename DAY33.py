# Day 33 coding Statement : Write a Program to check if String is a palindrome or not

word_1=input("Enter the word:")
word_2=word_1[::-1]

if word_1==word_2:
    print("Palindrome")
else:
    print("Not a Palindrome")
