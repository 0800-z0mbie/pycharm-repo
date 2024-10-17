name = input("Hello, what is your name? ")
print(f"Greetings, {name}. A pleasure meeting you!")

'''
Prompt user to enter temp in Celsius
Display corresponding temp in Fahrenheit.
'''

celsius = float(input("Say, enter any temperature in Celsius: "))
fahrenheit = (celsius * 9/5 + 32)
print(f"{celsius}°C is equivalent to {fahrenheit}°F!")

'''
The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups.
A lab group is 24 students
Sometimes varied to create groups of a similar size
Prompt: number of students and group size
Display how many groups will be needed
Display how many left over in smaller group
Students = 113
Required group size = 22
5 groups with 3 students left over

Bonus credit: Fix grammar in output
If 101 students in group of 20: 5 groups with 1 left over
'''

students = int(input("How many students? "))
group_size = int(input("Required group size? "))

full_groups = students // group_size
leftover_students = students % group_size

if leftover_students == 1:
    print(f"There are {full_groups} groups and {leftover_students} student left over.")
else:
    print(f"There are {full_groups} groups and {leftover_students} students left over.")

'''
A kindly teacher wishes to distribute a tub of sweets between her pupils
First she counts the sweet > 
Next she divides them according to how many pupils attend that day
Program: How many sweets teacher gives to each pupil
How many she will have left over.
'''

sweets = int(input("Good morning, teacher. How many sweets have you counted today? "))
students = int(input("How many of your students are in attendance today? "))

sweets_per_student = sweets // students
leftover_sweets = sweets % students

print(f"You can give {sweets_per_student} sweets to each student.")
print(f"And you will have {leftover_sweets} sweets left over.")