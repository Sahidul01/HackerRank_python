"""
Task

Dr. John Wesley has a spreadsheet containing a list of student's
, , and

.

Your task is to help Dr. Wesley calculate the average marks of the students.

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer
, the total number of students.
The second line contains the names of the columns in any order.
The next lines contains the , , and

, under their respective column names.

Constraints

Output Format

Print the average marks of the list corrected to 2 decimal places.


____CODES___
"""
x= 0;k = input()
m = raw_input().split()
for i in xrange(k): x = x+int(raw_input().split()[m.index('MARKS')])
print float(x)/k
