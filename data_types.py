fruits = ["apple","bannana","cherry"]
print(fruits)

numbers = [10, 20, 30, 40, 50]
print("Second Element",numbers[1])
print("Third Element",numbers[2])

coordinates = (10.0, 20.0)
print(coordinates)

measurements = (21.5, 22.8, 19.6, 20.0)
print("First value:", measurements[0])
print("Last value:", measurements[-1])

person = {"name": "Alice","Age": 25}
print(person)

book = {"title": "1984", "author": "George Orwell", "year": 1949}
print("Book title:", book["title"])

def add_num(num1, num2):
    return num1 + num2

def diff_num(num1, num2):
    return num1 - num2

print("Adding:", add_num(9, 2))
print("Difference:", diff_num(7, 2))

for i in range(10):
    print("Itirations: ", i)

animals = ["cat","dog","bird"]
for animal in animals:
    print(animal)

x = 10
if x > 5:
    print("x is greater than 5")

number = 4 
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
