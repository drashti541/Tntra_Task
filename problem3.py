""" 
Problem 3:  Biggest and smallest number in an array
Write a program to print the biggest and smallest number in the array. 
"""
a = [5, 3, 7, 4, 2]
print("Maximum is:",max(a))
print("Minimum is:",min(a))

#using for loop
print()
for i in a:
    if i > a[0]:
        maximum = i
    elif i < a[0]:
        minimum = i
print("Maximum is:", maximum)
print("Minimum is:", minimum)