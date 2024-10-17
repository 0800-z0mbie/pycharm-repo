name = input("Hello, what is your name? ")
if name:
    print(f"Greetings, {name}. A pleasure meeting you! ")
else:
    print("Hello, Stranger!")

'''
Program: simulate the way a user might choose a password.
Prompt for new password
Prompt again
If both passwords entered are similar say - "Password Set"
Otherwise report error
Password must be between 8 and 12 characters (inclusive) long.
'''

'''
password_1 = input("Enter a new password: ")
password_2 = input("Confirm your password: ")

if password_1 == password_2:
    print("You have no idea what I'm about to do with your personal information.")
else:
    print("Error: Passwords do not match.")
'''

'''
Modify program so that chosen password cannot be in list of common passwords:
password
letmein
sesame
hello
justinbieber

define as: BAD_PASSWORDS
'''


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password_1 = input("Enter a new password: ")
    password_2 = input("Confirm your password: ")

    if len(password_1) < 8 or len(password_1) > 12:
        print("Passwords must be between 8 and 12 characters long.")
    elif password_1 in BAD_PASSWORDS:
        print("Your password is too common.")
    elif password_1 != password_2:
        print("Error: Passwords do not match.")
    else:
        print("You have no idea what I'm about to do with your personal information.")
        break


'''
Program: Displays 7x Tables
0 to 12 inclusive
'''

'''
for i in range(13):
    print(f"{i} x 7 = {i * 7}")
'''

'''
Modify: User has to enter number to receive table
Between 0 and 12 inclusive
'''
print("Here lies the 7 times table. 0-12.")
number = int(input("Enter any number you'd like to multiply by 7: "))

'''
if 0 <= number <= 12:
  result = number * 7
  print(f"{number} x 7 = {result}!")
else:
    print("Error: Number must be between 0 and 12.")
'''

'''
Modify: User enters number of table but if number is negative, table is printed backwards
'''

if number < 0:
    for i in range(12, -1, -1):
        print(f"{i} x {abs(number)} = {i * abs(number)}")
else:
    if 0 <= number <= 12:
        result = number * 7
        print(f"{number} x 7 = {result}")
    else:
        print("Error: Number must be between 0 and 12.")
