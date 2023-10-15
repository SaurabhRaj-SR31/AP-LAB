import math as m
number = float(input("Enter a number: "))


sine_value = m.sin(m.radians(number))
square_root_value = m.sqrt(number)
log_value = m.log(number)

print(f"Sine of {number} is: {sine_value}")
print(f"Square root of {number} is: {square_root_value}")
print(f"Natural logarithm of {number} is: {log_value}")
