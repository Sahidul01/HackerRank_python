"""
Task

You are given a string
.
Your task is to print all possible combinations, up to size

, of the string in lexicographic sorted order.

Input Format

A single line containing the string
and integer value

separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string
on separate lines.
______CODES______  """

from itertools import combinations
string=input().split()
for i in range(1,int(string[1])+1):
    for j in (combinations(sorted(string[0]),i)):
       print("".join(j))
