ele = input("Enter Number: ")
n = len(ele)
armstrong = 0

for digit in ele:
    armstrong += int(digit) ** n

if (armstrong == int(ele)):
    print("It's an Armstrong Number!")
else:
    print("Nah!, Not an Armstrong Number!")
