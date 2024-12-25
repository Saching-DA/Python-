#Q.1 Program for Arithmetic Operators

a = 50
b = 25

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

#Q.2 Program for Assignment Operators

x = 10

x += 5

#or
#x = x + 5

print("After +=:", x)

x -= 3  
print("After -=:", x)

x *= 2  
print("After *=:", x)

x /= 4  
print("After /=:", x)

x %= 3
print("After %=:", x)

#Q.3 Program for Bitwise Operators

a = 6  # Binary: 110
b = 3  # Binary: 011

print("Bitwise AND:", a & b)   
print("Bitwise OR:", a | b)   
print("Bitwise XOR:", a ^ b)   
print("Bitwise NOT a:", ~a)    
print("Left Shift a << 1:", a << 1)  
print("Right Shift a >> 1:", a >> 1)

#Q.4 Program to Find Greatest of Three Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Greatest number is:", a)
elif b > c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)


# Q.Program to Calculate the Area of a Circle

radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
print("Area of the Circle:", area)

# Q.Calculate the area of a triangle.

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("Area of the Triangle:", area)

# Q.Calculate the area of a rectangle.

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("Area of the Rectangle:", area)

# Q.# Calculate the Area of a Square

side = float(input("Enter the side length of the square: "))
area = side * side
print("Area of the Square:", area)








    





