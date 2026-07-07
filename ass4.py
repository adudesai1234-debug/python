
      # Prime Number
def is_prime(n) :
    if n < 2:
        return False
    for i in range(2, n):
        if n %i == 0 :
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



      # Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

N =int(input("Enter N: "))
fibonacci(N)            
#Input: 8-> Output: 0 1 1 2 3 5 8 13



      # Palindrome Number
def is_palindrome(x):
    s = str(x).lower()
    return s == s[: :-1]
num = input("enter number: ")
text = input("Enter string: ")

print(f"{num} -> {'Palindrome' if is_palindrome(num) else 'Not Palindrpme'}")
print(f"{text} -> {'Palindrome' if is_palindrome(text) else 'Not Palindrome'}")




         #armstrong Number
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit)**power for digit in num_str)
    return total == n

num = int(input("Enter number: "))
print(f"{num} -> {'Armstrong' if is_armstrong(num) else 'Not Armstrong'}")



      #Lambda Function


square = lambda x: x * x
cube = lambda x: x * x * x
max_two = lambda a, b: a if a > b else b
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd" 
c_to_f = lambda c: (c *9/5) + 32

print("Square of 6:", square(6))
print("Cube of 4:", cube(4))
print("Max of 15, 9:", max_two(15, 9))
print("22 is:", even_odd(22))
print("25*C to F:", c_to_f(25))
