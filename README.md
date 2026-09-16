# 🧩 Logic Box

**Author:** Jenisha Ramani  
**Course/Project:** Python Practical Assignment

A Python-based console application that demonstrates basic programming logic through pattern generation and range analysis. The program provides a simple menu-driven interface where users can generate star patterns, analyze numbers as even or odd, calculate the sum of a range, or exit the program.

## 🎯 Project Objectives

- 🧠 **Develop Programming Logic:** Practice basic logical thinking using loops and conditions.
- ⭐ **Pattern Generation:** Generate a star pattern based on the number of rows entered by the user.
- 🔢 **Number Analysis:** Identify whether numbers in a given range are Even or Odd.
- ➕ **Range Calculation:** Calculate the sum of all numbers within a specified range.
- 📋 **Menu-Driven Program:** Allow users to select different operations through a simple menu.
- 🔄 **Loop Practice:** Use `for` and `while` loops to perform repetitive operations.

## ✨ Features & Functionality

### 1. ⭐ Generate a Pattern

The program generates a right-angle star pattern.

For example, if the user enters `5` rows:

```text
*
**
***
****
*****
```

The pattern is generated using nested `for` loops.

### 2. 🔢 Analyze a Range of Numbers

The program allows the user to enter a starting and ending number.

For each number in the given range, the program checks whether the number is:

- Even
- Odd

The program uses the modulo operator `%` to determine whether a number is divisible by 2.

Example:

```text
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
```

### 3. ➕ Calculate the Sum

After analyzing the numbers, the program calculates the total sum of all numbers in the selected range.

Example:

```text
Sum of all numbers from 1 to 4 is: 10
```

### 4. 📋 Menu-Driven Interface

The program provides three options:

```text
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
```

The user can continue selecting different options until choosing `3`.

### 5. ⚠️ Input Validation

The program checks whether the entered pattern row count is valid.

If the user enters `0` or a negative number, the program displays:

```text
Invalid row count. Please try again.
```

The program also handles invalid menu choices by displaying:

```text
Invalid choice. Please try again.
```

## 🔄 Program Flow

The basic working flow of the program is:

```text
Start
  ↓
Display Logic Box
  ↓
Generate Initial Pattern
  ↓
Display Menu
  ↓
Choose an Option
  ↓
 ┌─────────────────────────────┐
 │ 1 → Generate Pattern        │
 │ 2 → Analyze Number Range    │
 │ 3 → Exit                    │
 └─────────────────────────────┘
  ↓
Perform Selected Operation
  ↓
Return to Menu
  ↓
Exit when Choice = 3
```

## 🧠 Programming Concepts Used

This project covers the following Python concepts:

- `print()`
- `input()`
- Variables
- `int()`
- `for` loop
- `while` loop
- Nested loops
- `if`, `elif`, `else`
- `break`
- `continue`
- Modulo operator `%`
- Arithmetic operations
- Range generation using `range()`
- Menu-driven programming
- Input validation

## 🔍 Important Logic

### Even and Odd Check

The program uses:

```python
if num % 2 == 0:
    print("Number", num, "is Even")
else:
    print("Number", num, "is Odd")
```

If the remainder after dividing a number by `2` is `0`, the number is Even. Otherwise, it is Odd.

### Sum of Numbers

The program calculates the sum using:

```python
total = total + num
```

Each number in the range is added to the `total` variable.

### Star Pattern

The star pattern is created using nested loops:

```python
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
```

## 💻 Technologies Used

- Python 3
- Visual Studio Code
- Git & GitHub

## 📂 Project Files

```text
Logic-Box/
│
├── project2.py
├── README.md
└── output.png
```

## 🖥️ Sample Output

```text
Logic Box
*
**
***
****
*****

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 1
Enter the number of rows: 5
*
**
***
****
*****

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 2
Enter the start of the range: 1
Enter the end of the range: 4
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Sum of all numbers from 1 to 4 is: 10

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 3
Exiting the program. Goodbye!
```

## 🎓 Learning Outcome

Through this project, I practiced Python fundamentals such as loops, conditional statements, nested loops, user input, arithmetic operations, pattern generation, and menu-driven programming. This project helped me improve my logical thinking and problem-solving skills using Python.

## 🚀 Future Improvements

Some possible improvements for this project are:

- Add more pattern types.
- Add Prime Number analysis.
- Add Number Factorial calculation.
- Add a Fibonacci series option.
- Improve input validation.
- Add more mathematical operations.

