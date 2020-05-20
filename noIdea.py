"""
There is an array of integers. There are also disjoint sets, and , each containing integers. You like all the integers in set and dislike all the integers in set . Your initial happiness is . For each integer in the array, if , you add to your happiness. If , you add

to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since
and

are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints


Input Format

The first line contains integers
and separated by a space.
The second line contains integers, the elements of the array.
The third and fourth lines contain integers, and

, respectively.

Output Format

Output a single integer, your total happiness.



_____CODES_____

"""
n,m=input().split()
this_array=list(map(int,input().split()))
set_A=set(map(int,input().split()))
set_B=set(map(int,input().split()))
happy=0
for x in this_array:
    if x in set_A:
        happy+=1
    if x in set_B:
        happy-=1
print(happy)
