="""========================================================================
FOR LOOP IN PYTHON - COMPREHENSIVE EXPLANATION
========================================================================

What is a FOR LOOP?
------------------
A for loop is used to iterate (loop) through a sequence of items. It executes a block
of code repeatedly for each item in a sequence (like lists, tuples, strings, ranges, etc.)
until the sequence is exhausted.

Key Characteristics:
- Used when you know the number of iterations in advance
- Automatically handles iteration through sequences
- Clean and readable syntax
- Commonly used for iterating over collections


BASIC SYNTAX:
-------------
for variable in sequence:
    # Code block to be executed
    # This block runs for each item in the sequence
    # Use indentation (4 spaces or 1 tab)


COMPONENTS:
-----------
1. for - The keyword that starts the loop
2. variable - A name that takes each item value from the sequence
3. in - The keyword that specifies iteration
4. sequence - A list, tuple, string, range, or other iterable
5. : (colon) - Indicates the start of the code block
6. Indented block - Code that executes in each iteration


EXAMPLE 1: Iterating through a List
------------------------------------"""

fruits = ['apple', 'banana', 'orange', 'mango']
for fruit in fruits:
    print(fruit)

Output:
apple
banana
orange
mango


"""EXAMPLE 2: Iterating through a String
-----------------------------------------"""

text = 'Python'
for char in text:
    print(char)

Output:
P
y
t
h
o
n


"""EXAMPLE 3: Using range() function
-------------------------------------
range(stop) - generates numbers from 0 to stop-1
range(start, stop) - generates numbers from start to stop-1
range(start, stop, step) - generates numbers with custom step
"""

# Print numbers from 0 to 4
for i in range(5):
    print(i)

Output:
0
1
2
3
4


"""EXAMPLE 4: Using range with start and stop
----------------------------------------------"""

# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

Output:
1
2
3
4
5


"""EXAMPLE 5: Using range with step
------------------------------------
Print even numbers from 0 to 10
"""

for i in range(0, 11, 2):
    print(i)

Output:
0
2
4
6
8
10


"""EXAMPLE 6: Iterating through List with Index using enumerate()
------------------------------------------------------------------
enumerate() provides both index and value
"""

students = ['Alice', 'Bob', 'Charlie', 'Diana']
for index, name in enumerate(students):
    print(f"Index: {index}, Name: {name}")

Output:
Index: 0, Name: Alice
Index: 1, Name: Bob
Index: 2, Name: Charlie
Index: 3, Name: Diana


"""EXAMPLE 7: Nested For Loops
-----------------------------
Loops within loops - used for 2D lists or multiplication tables
"""

# Creating a 3x3 multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end=" ")
    print()  # New line after inner loop completes

Output:
1 x 1 = 1 1 x 2 = 2 1 x 3 = 3
2 x 1 = 2 2 x 2 = 4 2 x 3 = 6
3 x 1 = 3 3 x 2 = 6 3 x 3 = 9


"""EXAMPLE 8: Using break statement
-----------------------------------
break - exits the loop immediately when encountered
"""

for i in range(10):
    if i == 5:
        break  # Exit loop when i equals 5
    print(i)

Output:
0
1
2
3
4


"""EXAMPLE 9: Using continue statement
--------------------------------------
continue - skips the current iteration and goes to the next one
"""

for i in range(5):
    if i == 2:
        continue  # Skip when i equals 2
    print(i)

Output:
0
1
3
4


"""EXAMPLE 10: Using else with for loop
---------------------------------------
else block executes when the loop completes normally (no break)
"""

for i in range(1, 4):
    print(i)
else:
    print("Loop completed successfully!")

Output:
1
2
3
Loop completed successfully!


"""EXAMPLE 11: Summing values using for loop
-------------------------------------------"""

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num  # Same as: total = total + num

print(f"Sum of numbers: {total}")

Output:
Sum of numbers: 150


"""EXAMPLE 12: Finding maximum value
------------------------------------"""

scores = [45, 78, 92, 67, 88]
max_score = scores[0]
for score in scores:
    if score > max_score:
        max_score = score

print(f"Maximum score: {max_score}")

Output:
Maximum score: 92


"""IMPORTANT POINTS TO REMEMBER:

1. INDENTATION: Python uses indentation to define code blocks. Always indent code
   inside the for loop (typically 4 spaces).

2. VARIABLE SCOPE: The loop variable persists after the loop ends and retains the
   last value it had.

3. SEQUENCES: Can iterate over lists, tuples, strings, sets, dictionaries, and ranges.

4. RANGE FUNCTION: range() is efficient for numeric iterations.

5. ENUMERATE: Use enumerate() when you need both index and value.

6. BREAK: Exits the loop immediately.

7. CONTINUE: Skips to the next iteration.

8. ELSE: Optional clause that runs when loop completes normally.

9. NESTED LOOPS: Can have loops inside loops for multi-dimensional data.

10. PERFORMANCE: For loops are generally preferred over while loops when working
    with sequences because they handle iteration automatically.

COMMON USE CASES:
- Printing elements from a list
- Processing array elements
- Generating sequences of numbers
- Creating multiplication tables
- Calculating sums or products
- Searching for values in collections
- Data transformation and filtering
- Building nested data structures

========================================================================
Author: Manoj Chandu
Topic: For Loop - Python Fundamentals
========================================================================
"""
