'''# Write a program that asks for a number and prints "Even" if the number is even, 
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


# Write a program that takes marks and prints the grade:

#90 or above: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F

marks = int(input('enter your makers : '))
if marks >= 90:
     print('A')
elif marks >=80:
     print('B')
elif marks >=70:
     print('c')
elif marks >=60:
     print('D')
else:
     print("F")


#Question 2: Ticket Price
#Ask for age. Calculate ticket price:
#Under 5: Free
#5-12: ₹100
#13-17: ₹200
#18-64: ₹300
#65 or above: ₹150

age = int(input('Plase provide your age : '))
if age <= 5:
     print('ticket price : Free')
elif age <= 12:
     print('ticket price : 100')
elif age <= 17:
     print('ticket price : 200')
elif age <= 64:
     print("ticket price : 300")
else:
     print('ticket price : 150')


# Login System
#Ask for username and password. Use nested conditionals:
#If username is "admin", check if password is "admin123": "Admin access"
#If username is "user", check if password is "user123": "User access"
#Otherwise: "Access denied" '''

user_name = input('enter your username : ')
password = input('enter your password : ')
if user_name == 'admin':
    if password == 'admin123':
        print('Admin access')
    else:
        print('wrong password \nAccess denied try again')
elif user_name == 'user':
    if password == 'user123':
            print('User access')
    else:
         print('Access denied')
else:
        print('Access denied')

     



