#Given text = "Python Programming", write code to:


# Get the first character 
text = "python programming"
print(text[0])
# Get the last character
print(text[-1])
# Get "Python" using slicing
print(text[0:6])
#  Get "Programming" using slicing
print(text[-11:])
print(text[7:])


#Given email = "user@example.com", check if it contains "@" and ends with ".com"

email = "user@example.com"
print(email.find('@') and email.endswith('.com'))


# Given sentence = " hello world ", convert it to "HELLO WORLD" (remove spaces and uppercase)

sentence = " hello world "
new_sentence = sentence.strip() #removed the space from front and back of the sentence
print(new_sentence.upper())

sentence = " hello world "
new_sentence = sentence.strip().upper() #removed the space from front and back of the sentence and convert to lower to upper
print(new_sentence)


# Given data = "apple,banana,orange,mango", split it into a list of fruits

data = "apple,banana,orange,mango"
list = data.split(',')
print(list)

#Reverse the string "Hello" using slicing
string = "Hello"
reverse_string = string[::-1] 
print(reverse_string)

# Given name = "rahul" and age = 25, 
# create the message "Hello, Rahul! You are 25 years old." using f-strings

name = "rahul"
age = 25
message = f'"Hello, {name.title()}! You are {age} years old."'
print(message)
