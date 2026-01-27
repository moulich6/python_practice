# Write a program that asks for the user's name and prints "Welcome, [name]!"
name = input("what is your name")
print(f"Welcome, {name}!") 

# Ask the user for length and width, then calculate and print the area of a rectangle.
length = int(input("enter the leangth"))
width = int(input("enter width"))
area = (length * width)
print(f"area of rectangle : {area}")

# Ask the user for temperature in Celsius. 
# Convert it to Fahrenheit using: F = (C * 9/5) + 32

temp = int(input("Enter the temperature in celsius"))
fahrenheit = (temp*9/5)+32
#print(f"entered celsius: {temp}")
print (f"celsius after converting into fahrenheit : {fahrenheit}")

# Ask for item price and quantity. Calculate and print the total with 18% tax.

price = int(input('Enter the price of the item : '))
quantity = int(input('Enter the quantity : '))
subtotal = price * quantity
tax = subtotal*0.18
Total_price = subtotal + tax 
print("\n-------BILL-------")
print(f'sub total : {subtotal}')
print(f'Tax : {tax:.2f}')
print(f'Total price : {Total_price}')

# Ask the user for their name, age, and city. 
# Then print all the information in a nicely formatted way using f-strings.
name = input('enter your name : ')
age = int(input('enter your age : '))
city = input('enter your city : ')
print(f'your name is {name},and you are {age} years old,and you live in {city}.')
