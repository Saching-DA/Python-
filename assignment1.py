# sachin

#Q.2 describe local variable and global variable code

x = "global"

def my_function():
  
    x = "local"
    print("Inside the function:", x)

my_function()
print("Outside the function:", x)

#Q.3 Write a code that describe Indentation error

def example_function():
     print("This will cause an Indentation Error")
     print("This line is improperly indented")


#Q.4 write a code that describe local and global variable with same name


# Global variable
x = 10  

def my_function():
    # Local variable with the same name as global
    x = 20  
    print("Inside the function (Local x):", x)

my_function()
print("Outside the function (Global x):", x)


#Q.5 Write a code for string, int and float input.



name = input("Enter your name: ")

age = int(input("Enter your age: "))

height = float(input("Enter your height in meters: "))

print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)


     




     



