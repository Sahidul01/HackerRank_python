"""
Task

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Input Format

The first line contains
, the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains

space separated roll numbers of those students.

Constraints

Output Format

Output the total number of students who have subscriptions to both English and French newspapers.




_____CODES____
"""
m=int(input())
set_english=set(map(int,input().split()))
n=int(input())
set_french=set(map(int,input().split()))
set_inter=set_english.intersection(set_french)
print(len(set_inter))
