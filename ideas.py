# ================================================================================
# random number matrix to help with numbers and loops
import random
import secrets

def generate_random_number():
    return random.randint(0, 99)

def generate_random_string(length):
  # Generates a random string of the given length
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
# ================================================================================