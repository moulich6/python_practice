# Write a program that asks for a number and prints "Even" if the number is even, 
# otherwise prints "Odd".
number = int(input('enter your number : '))
if number %2 == 0:
    print('Even')
else:
    print('Odd')


# Ask the user for a number. 
# Print "Positive" if it's greater than 0, otherwise print "Negative or Zero".

number = int(input('enter the number : '))
if number > 0:
    print('Positive')
else:
    print('Negative or Zero')

# Ask for a username and password. If username is "admin" and password is "password123", 
# print "Login successful", otherwise print "Invalid credentials".


username = input('enter your username : ')
password = input('enter your password : ')
if username == 'admin' and password == 'password123':
    print('Login successful')
else:
    print('Invalid credentials')

    # Ask for the purchase amount. If the amount is 1000 or more, 
    # print "You get a 10% discount!", otherwise print "No discount available".
    
amount = int(input('Enter your purchase amount : '))
if amount >= 1000:
        print('You get a 10% discount!')
else:
        print('No discount available')

# Ask for age. If age is 18 or more, print "Adult". Otherwise, print "Minor".

age = int(input('enter your age : '))
if age>= 18:
    print('Adult')
else:
    print('Minor')

