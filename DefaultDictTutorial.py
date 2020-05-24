
""""
In this challenge, you will be given integers, and . There are words, which might repeat, in word group . There are words belonging to word group . For each words, check whether the word has appeared in group or not. Print the indices of each occurrence of in group . If it does not appear, print

.

Constraints


Input Format

The first line contains integers,
and separated by a space.
The next lines contains the words belonging to group .
The next lines contains the words belonging to group

.

Output Format

Output
lines.
The line should contain the -indexed positions of the occurrences of the word separated by spaces. 



_____CODES___
"""""
from collections import defaultdict
n,m=map(int,input().split())
A = [input() for _ in range(n)]
B=[input() for _ in range(m)]
A_dict=defaultdict(list)
for i ,word in enumerate(A):
    A_dict[word].append(i+1)
for word in B:
    if word in A_dict:
        print(" ".join(str(s) for s in A_dict[word] ))
    else :
        print(-1)
