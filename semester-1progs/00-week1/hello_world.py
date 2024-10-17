# print("Hello, World!")

name = "Kadizha"
print(f"Hello, {name}!")

# or print("Hello, Kadizha!")

'''
Over the summer, temps in Yorkshire reached 38.4°C.
Convert value in Celsius to the equivalent temp in Fahrenheit.
Display both.
Celsius to Fahrenheit: F = C * (9/5) + 32
'''
celsius = 38.4
fahrenheit = (celsius * 9/5 + 32)
print(f"{celsius}°C is equivalent to {fahrenheit}°F.")

'''
Geoffrey Boycott:
played 609 matches
batted 1014 times
was not out 162 times
scored 48426 runs

Calculate and display Geoffrey's batting average.
Batting average: (number of runs scored) / (total times batted - times not out)
'''

matches = 609
batted = 1014
not_out = 162
runs_scored = 48426

batting_average = runs_scored / (batted - not_out)
print(f"Geoffrey Boycott's batting average is: {batting_average:.2f}")

'''
The Head of Computing at the University of Poppleton is tasked with dividing a group of student into lab groups.
A lab group is 24 students
Number of students is equivalent to number of PC's
Calculate how many groups are needed for the following number of students:
113
175
12
Display how many full groups there will be
Display how many students in left over group
'''

students_per_group = 24
students_groups = [113, 175, 12]
for students in students_groups:
    full_groups = students // students_per_group
    leftover_students = students % students_per_group

    print(f"For {students} students: full groups = {full_groups}, leftover students = {leftover_students}")