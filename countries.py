# ================================================================================
import pandas as pd
import json
import random

def import_country_data():
    df = pd.read_csv('country-list.csv')
    df_json = df.to_json()
    return json.loads(df_json)
   
def generate_random_country():
    index = random.randint(0, 247)
    countries = import_country_data()
    country = countries['country'][str(index)]
    capital = countries['capital'][str(index)]
    return {"country": country, "capital": capital}

    
def country_game_round():
    place = generate_random_country()
    guess = input('what is the capital of ' + place['country']+ '?\n')

    if guess.lower() == place['capital'].lower():
      print('correct!\n')
      return True
    else:
      print('incorrect. the answer was ' + place['capital'])
      return False

def country_game():
    correct_count = 0
    incorrect_count = 0
    
    while(True):
      was_correct = country_game_round()

      if(was_correct):
         correct_count += 1
      else:
         incorrect_count += 1

      print('play again?')
      print('yes - continue')
      restart = input()

      if(restart.lower() == 'yes'):
        print()
        print('current score:')
        print('correct answers: ' + str(correct_count))
        print('incorrect answers: ' + str(incorrect_count))
        print()

        continue
      else:
         break
# ================================================================================
