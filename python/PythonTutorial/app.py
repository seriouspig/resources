""" print("Piotr Gryko")
print('o----')
print(' ||||')
print('*' * 10)

price = 10
rating = 4.9
name = "Piotr"
is_published = True
print('The price is ' +  str(price))

patient_name = "John Smith"
patient_age = 20
is_patient_new = True """

""" Getting Input """
""" name1 = input('What is your name? ')
color1 = input('What is your favoutrit color? ')
print(name1 + ' likes ' + color1) """

""" Type Conversion """
""" int()
float()
bool()
str()
type(True)

birth_year = input('Birty year: ')
age = 2021 - int(birth_year)
print(age)

print(type(birth_year))
print(type(age))

weight = input("What is your weight in pounds? ")
weight_kg = str("{:.2f}".format(( float(weight) / 2.205)))
print('You weight ' + weight_kg + ' kgs') """

course = "python's course for beginners"
print(course)
course2 = '"Python" is a book'
print(course2)
course3 = '''
Hi John,

Here is the first email.

Best Regards,

Piotr'''
print(course3)
print(course3[4])
print(course3[-5])
print(course3[0:9])

name = "Piotr Gryko"
print(name[1:-1])

""" FORMATTED STRINGS """
first = "John"
last = "Smith"
message = first + ' [' + last + '] is a coder'
print(message)
message2 = f'{first} [{last}] is a coder'
print(message2)

""" STRING METHODS """
print(len(course))
print(course.upper())
print(course)
print(course.lower())
print(course.find('o'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Amatours'))
print('Python' in course)
print(course.title())

""" ARITHMETIC OPERATIONS """
print(10+3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)

x=10
x+=3
print(x)

""" MATH FUNCTIONS """
import math

x =2.9
print(round(x))
print(abs(-2.9))
print(math.ceil(2.9))
print(math.floor(2.9))

""" IF STATEMENTS """
is_hot = True
is_cold = False

if is_hot:
    print("It is hot. Drink plenty of water")
elif is_cold:
    print("It´s cold. Wear warm clothes")
else:
    print("It´s a great day")
print("Enjoy your day")

buyer_credit_isGood = True
price = 1000000
if buyer_credit_isGood:
    print(f'Buyer needs to put down {round(0.1 * price)}$')
else:
    print(f'Buyer needs to put down {round(0.2 * price)}$')

""" LOGICAL OPERATORS """
buyer_has_highIncome = True
if buyer_credit_isGood and buyer_has_highIncome:
    print("Eligible for loan")
if buyer_credit_isGood or buyer_has_highIncome:
    print("Slightly Eligible for loan")

buyer_has_criminalRecord = False
if buyer_credit_isGood and not buyer_has_criminalRecord:
    print("This guy is good")

""" COMPARISON OPERATEORS """
temperature = 30
if temperature >= 30:
    print("It´s super hot")
else:
    print("It´s not too hot")

name = "Piotr"
if len(name) < 3:
    print("Name too short")
elif len(name) > 50:
    print("Name too long")
else:
    print("Name looks good")

# WEIGHT CONVERTER 
""" weight = input("Please enter your weight:")
unitType = input('Is the weight in (L)bs or (K)gs? ')

if unitType.lower() == 'l':
    print(f'You weight: {"{:.2f}".format(float(weight) / 2.205)} kgs')
elif unitType.lower() == 'k':
    print(f'You weight: {"{:.2f}".format(float(weight) * 2.205)} lbs')
else:
    unitType = (input('Is the weight in (L)bs or (K)gs? ')).lower """

# WHILE LOOPS 
""" i = 1
while i <= 5:
    print('*' * i)
    i += 1

secret_number = 9
guess = input("Guess: ")
while guess != secret_number:
    guess = int(input("Guess: "))
else:
    print(f'You guessed! The secret number was {secret_number}!!!') """

# break to terminate a loop
# while can also have an else


# CAR GAME
""" car_on = False
user_input=""
while user_input != "quit":
    user_input = input()
    if user_input.lower() == 'help':
        print('''
    start - to start the car
    stop - to stop the car
    quit - to ext
        ''')
        
    elif user_input.lower() == 'start':
        if not car_on:
            print('Engine started. You are driving')
            car_on = True
        else:
            print('What are you doing? The car is already on!')

    elif user_input.lower() == 'stop':
        if car_on == True:
            print('The car is stopped')
            car_on = False
        else:
            print("WTF! The car is already stopped!")
    elif user_input.lower() == 'quite':
        break

    else:
        print("I don´t understand") """

# FOR LOOPS

for item in 'Python':
    print(item)

for item in ['John', 'Bill', 'Anne']:
    print(item)

for item in range(1,11, 2):
    print(f'number {item}')

total = 0
price = [10, 20 ,30]
for item in price:
    total += item
    
print(total)

# NESTED LOOPS

for x in range(4):
    for y in range(4):
        print(x, y)

numbers = [5, 2, 5, 2, 2]
numbers2 =[2,2,2,2,5]

for number in numbers:
    print(number * "X")

for number in numbers2:
    output = ''
    for i in range(number):
        output += 'X'
    print(output)

# LISTS
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])
print(names[2])
print(names[-1])
print(names[2:])
print(names[2:4])
print(names[0:2])
names[0] = 'Dick'
print(names)

numbers = [1,4,6,9,3,5,7]
biggest_number = 0
for number in numbers:
    if number > biggest_number:
        biggest_number = number

print(biggest_number)

# 2D LISTS

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][1])

for row in matrix:
    for item in row:
        print(item)

# LIST METHODS

numbers = [5, 2, 1, 3,3,7, 4]

numbers.append(12)
print(numbers)
numbers.pop()
print(numbers)
numbers.insert(0,20)
print(numbers)
numbers.remove(1)
print(numbers)
""" numbers.clear() """
print(numbers)
""" print(numbers.index(5)) """
print(5 in numbers)
print(numbers.count(3))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)

numbers = [5, 2, 1, 3,3,7, 4,5,2]

for number in numbers:
    while numbers.count(number) > 1:
        numbers.remove(number)

print(numbers)

# TUPLES

numbers =[1,2,3] 
numbers_tuple = (1,2,3) # Not mutable, onlt count and index

# UNPACKING

coordinates = (1,2,3)
x,y,z = coordinates

print(x, y, z)

# DICTIONARIES

customer = {
    'name': 'John Smith',
    'email' : 'js@gmail.com',
    'age': 30,
    'is_verified': True 
}

print(customer['name'])
print(customer.get('email')) # Safer - no error
print(customer.get('birthday', '12 March 1980'))

customer["hobby"] = "Fishing"

print(customer.get('hobby'))

phone = input("Your phone number: ")

phone_digits = {
    "1":"one ",
    "2":"two ",
    "3":"three ",
    "4":"four ",
    "5":"five ",
    "6":"six ",
    "7":"seven ",
    "8":"eight ",
    "9":"nine ",
    "0":"zero"
}
phone_words = str(phone)
phone_result = ""
for digit in phone_words:
    phone_result += phone_digits.get(digit, "!")
    
print(phone_result)

# EMOJI CONVERTER

message = input(">")
words = message.split(' ')
print(words)
emojis = {
   ":)": "😃",
   ":(": "😞"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)

