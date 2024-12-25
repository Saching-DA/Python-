# Q1 Check if a Number is Even or Odd


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q2. Check Voting Eligibility


age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Q3 # Check if a Year is a Leap Year


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")


# Q4 # Check if a Number is Positive, Negative, or Zero


num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Q5 # Find the Largest of Three Numbers


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a >= b and a >= c:
    print(f"The largest number is: {a}")
elif b >= a and b >= c:
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")



    
