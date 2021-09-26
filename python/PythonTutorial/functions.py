def greeting(first_name, last_name):
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard!')

greeting("Piotr", "Gryko") # positional arguments

def calc_cost(total, shipping, discount):
    print(f'The total cost is {total + shipping - discount}')

calc_cost(total=50, shipping=10, discount=15) # keyword arguments

def square(number):
    return number * number

print(square(120))

# REUSABLE FUNCTION

message = input(">")
def smiley_creator(message):
    words = message.split(' ')
    emojis = {
    ":)": "😃",
    ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

print(smiley_creator(message))

# EXCEPTIONS

try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print('Invalid Value') 
except ZeroDivisionError:
    print('Age can not be 0')