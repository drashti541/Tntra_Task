"""
Problem 2:  Determine whether a given string is Palindrome
"""
s1 = input("Input: ")
if s1 == s1[::-1]:
    print("Output: True")
else:
    print("Output: False")