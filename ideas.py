# ================================================================================
# random number matrix to help with numbers and loops
import random
import secrets
import constants

import countries

def generate_random_number():
    return random.randint(0, 99)

def generate_random_string(length):
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  random_string = ""
  for i in range(length):
    random_string += secrets.choice(characters)
  return random_string

def generate_matrix():
    array = []
    outputString = ''
    for i in range(100):
        currentNumber = generate_random_number()
        array.append(currentNumber)
        outputString += str(currentNumber) + ', '

        if(i % 10 == 9):
           outputString += '\n'
        
        if(i == 99):
           outputString = outputString[:-3]
           outputString += '\n'
    
    print(outputString)
    return array

def generate_random_name():
    name_index = random.randint(0, len(constants.names) - 1)
    name = constants.names[name_index]
    return name

def generate_person():
    name = generate_random_name()
    birthplace = countries.generate_random_country()
    age = generate_random_number()

    return {"name": name, "birthplace": birthplace, "age": age}

# ================================================================================