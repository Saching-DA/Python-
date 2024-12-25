# Q1 # Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 


def div(a, b):
    return a / b

# Taking input and calling the function
num1 = float(input("Enter the first number (dividend): "))
num2 = float(input("Enter the second number (divisor): "))

if num2 != 0:
    result = div(num1, num2)
    print(f"The result of division is: {result}")
else:
    print("Error: Division by zero is not allowed.")


# Q2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .

# Square Function
def square(num):
    return num * num

# Taking input and calling the function
number = float(input("Enter a number to find its square: "))
result = square(number)
print(f"The square of {number} is: {result}")


# Q3. Using max() and min() functions display the maximum and minimum of 5 random numbers.


import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Display the numbers
print("Five random numbers:", numbers)

# Find maximum and minimum
max_num = max(numbers)
min_num = min(numbers)

print("Maximum number:", max_num)
print("Minimum number:", min_num)

# Q4  # Display Name in Lowercase


name = input("Enter your name: ")
print("Your name in lowercase:", name.lower())


