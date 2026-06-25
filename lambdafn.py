add = lambda a, b: a+b
print(add(25, 20))


square = lambda x: x*x

print(square(25))


numbers = [11,22,33,44,55]
squares  = list(map(lambda x: x*x, numbers))
print(squares)

numbers = [20,30,45,50,60]
even = list(filter(lambda x: x % 2==0, numbers))
print(even)

numbers= [1,11,3,22,5]
cubes = list(map(lambda x: x*x*x, numbers))
print(cubes)