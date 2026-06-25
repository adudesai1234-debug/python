num1 = int (input("Enter the first number"))
num2 = int (input("Enter the seond number"))
print ( "addition:", num1 + num2)
print ( "substraction:", num1 - num2)
print ( "multiplication:", num1 * num2)
print ( "division:", num1 / num2)
print ( "floor:", num1 // num2)
print ( "exponention:", num1 ** num2)
print ( "module:", num1 % num2)


num = 10
if num % 2 ==0:
    print("Even num")
else:
    print("odd num")

for i in range (6):
    print ("*" * i)

rows = 7
for i in range (rows):
    print(" " * (rows - i) + "*" *i)