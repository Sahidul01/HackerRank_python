"""
Input Format

A single line containing the complex number

. Note: complex() function can be used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number

Output Format

Output two lines:
The first line should contain the value of
.
The second line should contain the value of .

______CODES____
"""


from cmath import phase
c=complex(input())
print(abs(c))
print(phase(c))
