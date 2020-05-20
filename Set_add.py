"""
Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of

country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer
, the total number of country stamps.
The next

lines contains the name of the country where the stamp is from.

Constraints

Output Format

Output the total number of distinct country stamps on a single line.



___codes___

"""
n=int(input())
stamp_set=(set(""))
for _ in range(0,n):
    stamp_set.add(input())
print(len(stamp_set))
