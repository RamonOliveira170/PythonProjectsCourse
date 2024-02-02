import math

def greet():
    print("greet")
    print("Greet")

greet()

def greet_with_name(name):
    print("Hello", name)

greet_with_name("Lucas")

def paint_calc(height, width, cover):
  number_of_cans = (height * width) / cover
  number_of_cans = math.ceil(number_of_cans)
  print(f"You'll need {number_of_cans} cans of paint.")
  
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

def prime_checker(number):
  is_prime = True
  for element in range(2, number):
    if number % element == 0:
        is_prime = False
  if is_prime:
      print("It's a prime number.")
  else:
      print("It's not a prime number.")

n = int(input())
prime_checker(number=n)


