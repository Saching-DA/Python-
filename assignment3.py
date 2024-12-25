# Q1 Check Even or Odd Using Ternary Operator

num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result}.")

#Q2 # Swap Two Numbers

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Swapping using a temporary variable

a, b = b, a

print("After swapping:")
print("First number (a):", a)
print("Second number (b):", b)

# Q3 # Convert Kilometers to Miles

kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

# Q4 # Calculate Simple Interest


principal = 200  
rate = 5         
time = 5         

simple_interest = (principal * rate * time) / 100
print(f"Simple Interest on Rs.{principal} for {time} years at {rate}% per year is Rs.{simple_interest}.")




