"""
Problem 1: Program to count occurrences of a given character in a string.
"""
s1 = input("Enter String:")
c1 = input("Enter character to count:")
if c1 in s1:
    print("Output: ",s1.count(c1))
else:
    print("Output: ",c1)