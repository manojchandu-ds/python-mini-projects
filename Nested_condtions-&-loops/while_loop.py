="""========================================================================
WHILE LOOP IN PYTHON - COMPREHENSIVE EXPLANATION
========================================================================

What is a WHILE LOOP?
--------------------
A while loop executes a block of code repeatedly as long as a specified condition
is True. It keeps looping until the condition becomes False. The loop checks the
condition before each iteration.

Key Characteristics:
- Used when the number of iterations is unknown
- Condition-based looping
- Requires manual control of loop variable
- Risk of infinite loops if condition never becomes False
- More flexible than for loops for certain scenarios


BASIC SYNTAX:
-------------
while condition:
    # Code block to be executed
    # This block runs as long as condition is True
    # Use indentation (4 spaces or 1 tab)
    # Must update loop variable to avoid infinite loop


COMPONENTS:
-----------
1. while - The keyword that starts the loop
2. condition - A boolean expression that evaluates to True or False
3. : (colon) - Indicates the start of the code block
4. Indented block - Code that executes in each iteration
5. Loop variable update - Critical to change condition state


EXAMPLE 1: Simple Counter Loop
------------------------------"""

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Increment the counter

Output:
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5


"""EXAMPLE 2: Countdown Loop
---------------------------"""

number = 5
while number > 0:
    print(number)
    number -= 1  # Decrement the counter

print("Blastoff!")

Output:
5
4
3
2
1
Blastoff!


"""EXAMPLE 3: String-Based Loop
------------------------------"""

password = ""
while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Incorrect password. Try again.")

print("Access granted!")

Output:
Enter password: hello
Incorrect password. Try again.
Enter password: python123
Access granted!


"""EXAMPLE 4: Summing User Input
-------------------------------
Loop until user enters -1
"""

total = 0
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break  # Exit the loop
    total += num

print(f"Sum of numbers: {total}")

Output:
Enter a number (-1 to stop): 10
Enter a number (-1 to stop): 20
Enter a number (-1 to stop): 30
Enter a number (-1 to stop): -1
Sum of numbers: 60


"""EXAMPLE 5: Nested While Loops
-------------------------------
Loops within loops - useful for multi-level iterations
"""

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()  # New line after inner loop completes
    i += 1

Output:
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)


"""EXAMPLE 6: Using break Statement
-----------------------------------
break - exits the loop immediately when encountered
"""

count = 0
while count < 10:
    if count == 5:
        print("Reached 5. Exiting loop.")
        break  # Exit loop when count equals 5
    print(count)
    count += 1

Output:
0
1
2
3
4
Reached 5. Exiting loop.


"""EXAMPLE 7: Using continue Statement
--------------------------------------
continue - skips the current iteration and goes to the next one
"""

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip iteration when count equals 3
    print(count)

Output:
1
2
4
5


"""EXAMPLE 8: Using else with while loop
---------------------------------------
else block executes when the loop condition becomes False (no break)
"""

count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed successfully!")

Output:
1
2
3
Loop completed successfully!


"""EXAMPLE 9: Validating User Input
----------------------------------"""

valid_input = False
while not valid_input:
    age = input("Enter your age: ")
    if age.isdigit() and 1 <= int(age) <= 150:
        valid_input = True
        print(f"Valid age entered: {age}")
    else:
        print("Invalid input. Please enter a valid age.")

Output:
Enter your age: abc
Invalid input. Please enter a valid age.
Enter your age: -5
Invalid input. Please enter a valid age.
Enter your age: 25
Valid age entered: 25


"""EXAMPLE 10: Menu-Driven Loop
-----------------------------
Common in user interface design
"""

menu_active = True
while menu_active:
    print("\n=== MENU ===")
    print("1. Print Hello")
    print("2. Print Goodbye")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        menu_active = False  # Exit the loop
        print("Exiting menu...")
    else:
        print("Invalid choice. Try again.")


"""EXAMPLE 11: Processing List Items
-----------------------------------"""

items = ['apple', 'banana', 'orange', 'mango']
index = 0

while index < len(items):
    print(f"Item {index}: {items[index]}")
    index += 1

Output:
Item 0: apple
Item 1: banana
Item 2: orange
Item 3: mango


"""EXAMPLE 12: Checking Boolean Conditions
------------------------------------------"""

is_running = True
speed = 0

while is_running:
    print(f"Speed: {speed} km/h")
    speed += 10
    
    if speed >= 100:
        is_running = False
        print("Maximum speed reached!")

Output:
Speed: 0 km/h
Speed: 10 km/h
Speed: 20 km/h
Speed: 30 km/h
Speed: 40 km/h
Speed: 50 km/h
Speed: 60 km/h
Speed: 70 km/h
Speed: 80 km/h
Speed: 90 km/h
Speed: 100 km/h
Maximum speed reached!


"""IMPORTANT POINTS TO REMEMBER:

1. INDENTATION: Python uses indentation to define code blocks. Always indent code
   inside the while loop (typically 4 spaces).

2. CONDITION: The while condition must eventually become False, or the loop will
   run forever (infinite loop). Always ensure your loop variable is updated.

3. LOOP VARIABLE: You must manually control the loop variable (increment/decrement)
   to avoid infinite loops.

4. RISK OF INFINITE LOOPS: Unlike for loops, while loops can easily become infinite
   if you're not careful with the condition.

5. BREAK: Exits the loop immediately when a condition is met.

6. CONTINUE: Skips to the next iteration without executing remaining statements.

7. ELSE: Optional clause that runs when loop condition becomes False naturally
   (not via break).

8. NESTED LOOPS: Can have loops inside loops, but be careful about nested
   conditions to avoid infinite loops.

9. USER INPUT: While loops are commonly used for input validation and menu-driven
   interfaces.

10. CONDITION EVALUATION: The condition is checked BEFORE each iteration, not after.

COMPON USE CASES:
- Input validation (ensuring user enters valid data)
- Menu-driven interfaces
- Processing unknown number of items
- Waiting for a condition to be met
- Game loops (continues until game ends)
- Real-time monitoring and updates
- Error handling and retry logic
- Time-based operations

FOR LOOP vs WHILE LOOP:

For Loop:
- Used when you know the number of iterations
- Automatically handles iteration
- Works with sequences (lists, strings, ranges)
- Cleaner syntax for iteration
- Less prone to infinite loops

While Loop:
- Used when number of iterations is unknown
- Requires manual variable management
- Condition-based
- More flexible for complex conditions
- Risk of infinite loops if not careful

COMPARISON EXAMPLE:
# FOR LOOP - Cleaner for sequences
for i in range(5):
    print(i)

# WHILE LOOP - Same result but more code
i = 0
while i < 5:
    print(i)
    i += 1

========================================================================
Author: Manoj Chandu
Topic: While Loop - Python Fundamentals
========================================================================
"""
