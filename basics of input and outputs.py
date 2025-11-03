Input & Output problems and solutions 
1 .Input & Output - Automated System Greeting for New Users
In this program, an automated system greets new users when they join or log in. The program takes the user's name 
as input and displays a personalized welcome message as output.This demonstrates the concept of input and output operations in programming

solution :
print("Hello, World!")





2.Input & Output - Character Analysis Tool
The Character Analysis Tool is a beginner-friendly program that takes a single character as input from the user and analyzes it to identify its type.
The program determines whether the entered characteris an uppercase letter, lowercase letter, digit, or a special symbol.

solution :
char = input()
print(ord(char))




3.Input & Output - Mathematical Operations Calculator
The Mathematical Operations Calculator is an interactive program that allows users to perform basic arithmetic operations such as addition, subtraction,
multiplication, and division. The program takes two numerical inputsfrom the user and an operator symbol, then displays the calculated result as output.

solution :
import math

num1 = float(input())
num2 = float(input())

# Calculate square root of first number
sqrt_result = math.sqrt(num1)

# Calculate first number raised to power of second number
power_result = num1 ** num2

# Calculate absolute values
abs1 = abs(num1)
abs2 = abs(num2)

# Display results
print(f"Square Root of first number: {sqrt_result}")
print(f"First number raised to the power of second number: {power_result}")
print(f"Absolute value of first number: {abs1}")
print(f"Absolute value of second number: {abs2}")




4 .Input & Output - Student Information Management System
the Student Information Management System (Leaderboard) is a program that collects and displays key details of students such as name, roll number, course, and marks.
After taking the input for multiple students, the system organizes and displaysthe information in a structured leaderboard format, showing top performers first.

solution :
import math

name = input()
age = int(input())
cgpa = float(input())
grade = input()

# Truncate CGPA to 2 decimal places (don't round)
cgpa_truncated = math.floor(cgpa * 100) / 100

print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa_truncated:.2f}")
print(f"Grade: {grade}")




5.Input & Output - ASCII Decoder Tool
The ASCII Decoder Tool is a simple yet powerful program that takes a character or its ASCII value as input and displays its corresponding ASCII code 
or character as output. This program helps users understand how computers represent characters using numerical codes defined by the ASCII
(American Standard Code for Information Interchange) system.

solution :
ascii_value = int(input())
print(chr(ascii_value))







