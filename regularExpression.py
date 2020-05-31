"""
You are given a string .
Your task is to find out whether

is a valid regex or not.

Input Format

The first line contains integer
, the number of test cases.
The next lines contains the string

.

Constraints

Output Format

Print "True" or "False" for each test case without quotes.
___CODES___
"""
import re
for _ in range(int(input())):  
    try:
        print(bool(re.compile(input())))
    except:
        print('False')
