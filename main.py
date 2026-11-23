# Yuva Intern - Python Development Internship
# Task 2: Core Concepts and Skills

# 1. Variables and Data Types
name = "Abhishek"
age = 20
skills = ["Python", "Git", "Programming"]

print("Name:", name)
print("Age:", age)
print("Skills:", skills)

# 2. Operators
a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 3. Conditional Statements
marks = 75

if marks >= 60:
    print("Result: First Division")
else:
    print("Result: Needs Improvement")

# 4. Loops
print("Numbers from 1 to 5:")
for number in range(1, 6):
    print(number)

# 5. Functions
def calculate_square(number):
    return number * number

print("Square of 5:", calculate_square(5))

# 6. Dictionary
student = {
    "name": "Abhishek",
    "course": "Python Development",
    "status": "Learning"
}

print("Student Details:", student)

# 7. Exception Handling
try:
    result = 10 / 2
    print("Division Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")

print("Task 2 Practical Exercises Completed!")

# 8. Handling Common Errors
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"


print("Normal Division:", safe_division(10, 2))
print("Error Handling Test:", safe_division(10, 0))