import cmath as c


n = complex(input("Enter a complex number (in the form a+bj): "))


sine_value = c.sin(n)
square_root_value = c.sqrt(n)
log_value = c.log(n)

print(f"Sine of {n} is: {sine_value}")
print(f"Square root of {n} is: {square_root_value}")
print(f"Natural logarithm of {n} is: {log_value}")
