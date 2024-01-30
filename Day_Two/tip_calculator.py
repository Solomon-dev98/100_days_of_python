#!/usr/bin/python3

# Write your code below this line 👇

print("Welcome to the tip calculator.")

# read the total bill from user
total_bill = input("What was the total bill? $")

# convert total bill entered to a float value
total_bill = float(total_bill)

# read the tip value from user
tip = input("What percentage tip would you like to give? 10, 12, or 15?")

# convert the tip to an int data type
tip = int(tip)

# read number of persons to split the bill among
persons = input("How many people to split the bill?")

# typecast the value of persons to an int data type
persons = int(persons)

# calculating tip
tip = total_bill * (tip / 100)

# calculating the cost per person
cost_per_person = (total_bill + tip) / persons

# print out the cost per person
print(f"Each person should pay: ${(cost_per_person):.2f}")
