print("Hello"[-1])

print(123_456_789)

two_digit_number = input("Two digit number: ")

sum_numbers = int(two_digit_number[0]) + int(two_digit_number[1])

print("Result: " + str(sum_numbers))

height = input("Height: ")
weight = input("Weight: ")

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **

bmi = weight_as_int / height_as_float ** 2

# or using multiplication and PEMDAS
 
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)

age = input("How old are you?: ")

years = 90 - int(age)

weeks = years * 52

print(f"You have {weeks} weeks left.")
