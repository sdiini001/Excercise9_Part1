# if statement
i_like_broccoli = False
print("The start")

if i_like_broccoli:
    print("you like broccoli")
    print("I am eating the broccoli")
else:
    print("you DON'T like broccoli")

print("The end")

fruits = ['apple', 'banana', 'cherry']
print(fruits)

if 'cherry' in fruits:
    print('Yummy, I like cherries')

last_fruit = fruits.pop()
print(last_fruit)

print(fruits)

if fruits:
    print("There's still fruit bowl")

last_fruit = fruits.pop()
print(last_fruit)

print(fruits)

last_fruit = fruits.pop()
print(last_fruit)

print(fruits)

if fruits:
    print("There's still fruit in the bowl")
else:
    print("The fruit bowl is empty")

word = 'hello'

if word:
    print('The string is not empty')
else:
    print('The string is empty')
# == is the EQuality operator
if word == 'hi':
    print("Hello you")
elif word == 'bye':
    print("Goodbye you")
else:
    print("Are you okay?")

x = 4
y = 4
if x == y:
    print('x and y are the same')
else:
    print('x and y are different')
if x > y:
    print('x is greater than y')
else:
    print('x is not greater than y')
# you have to later make word in to int
# you cannot compare a string and int
word = '2'
print(type(word))
number = 3

if int(word)< number:
    print('word is less than number')