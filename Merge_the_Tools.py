"""
Consider the following:

    A string, 

, of length where
.
An integer,
, where is a factor of

    .

We can split
into subsegments where each subsegment, , consists of a contiguous block of characters in . Then, use each to create string

such that:

    The characters in 

are a subsequence of the characters in
.
Any repeat occurrence of a character is removed from the string such that each character in
occurs exactly once. In other words, if the character at some index in occurs at a previous index in , then do not include the character in string

    .

Given
and , print lines where each line denotes string

.

Input Format

The first line contains a single string denoting
.
The second line contains an integer,

, denoting the length of each subsegment.

Constraints

, where is the length of It is guaranteed that is a multiple of

    .

Output Format

Print
lines where each line contains string

.

Sample Input

AABCAAADA
3   

Sample Output

AB
CA
AD
______CODES_____   """



from collections import OrderedDict   
def merge_the_tools(string, k):
    q=int(len(string)/k)
    for i in range(0,q):
        string_strip=string[i*k:(i+1)*k]
        string_strip="".join(OrderedDict.fromkeys(string_strip))
        print(string_strip)

    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
