"""
is a right triangle, at .
Therefore,

.

Point
is the midpoint of hypotenuse

.

You are given the lengths
and .
Your task is to find (angle

, as shown in the figure) in degrees.

Input Format

The first line contains the length of side
.
The second line contains the length of side

.

Constraints


Lengths and

    are natural numbers.

Output Format

Output

in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°. 


______CODES______
"""

import math
a=int(input())
b=int(input())
print(str(round(math.atan(a/b)*(180/math.pi)))+"°")
