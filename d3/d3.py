print("Welcome to the rollercoaster!")
print("What's your height in cm? ")

height = 120

if height > 120:
    print(f"{height}cm! You can ride the rollercoaster!")
    print("What's your age?")

    age = 18

    if age > 18:
        print("Please pay $12")
    elif age > 12 and age <= 18:
        print("Please pay $7")
    elif age <= 12:
        print("Please pay $5")
    
else:
    print("Sorry, you have to grow taller before you can ride.")

height = float(input())
weight = int(input())
bmi = weight / (height * height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0

if size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
elif size == "L":
  bill += 25
  if add_pepperoni == "Y":
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Thank you for choosing Python Pizza Deliveries! your fi