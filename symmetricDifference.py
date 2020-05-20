"""
Task
Given sets of integers, and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either or

but do not exist in both.

Input Format

The first line of input contains an integer,
.
The second line contains space-separated integers.
The third line contains an integer, .
The fourth line contains

space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.



____CODES____
"""


m=int(input())
set_m=set(map(int,input().split()))
n=int(input())
set_n=set(map(int,input().split()))
set_union=set_m.union(set_n)
set_inter=set_m.intersection(set_n)
set_result=set_union.difference(set_inter)
thislist=list(set_result)
thislist=sorted(thislist)
for x in (thislist):
    print(x)
