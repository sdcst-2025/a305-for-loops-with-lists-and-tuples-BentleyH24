# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")

num = int(input("What is your number (must be greater than 0 and less than 10)"))
if 0 <= num < 10:
    print("The name corresponding to that number is", people[num])
else:
    print("Invalid input")
