
"""
Task

You are given two values
 a and b .
Perform integer division and printa/b

.

Input Format

The first line contains T
, the number of test cases.
The next T lines each contain the space separated values of a and b

.

Constraints
0<T<100

Output Format

Print the value of a/b
.
In the case of ZeroDivisionError or ValueError, print the error code.

_____CODES____
"""




n=int(input())
for _ in range(n):
    a,b=input().split(" ")
    try:
        z=int(a)//int(b)
    except Exception as e:
        print("Error Code:",e)
    else:
        print(z)
       
