"""
Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

Input Format

The first line contains the integer,
, the total number of plants.
The second line contains the

space separated heights of the plants.

Constraints

Output Format

Output the average height value on a single line.

________CODES______
"""
def average(array):
    total=0
    Set=set(array)
    total=sum(Set)
    return total/len(Set)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
