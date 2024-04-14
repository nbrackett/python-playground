# ================================================================================
# a couple actual backend data responses to help with json
import json
import requests as r

url_start = "https://"

premier_league_standings_url = "www.thesportsdb.com/api/v1/json/3/lookuptable.php?l=4328&s=2020-2021"
former_teams_leao_url = "www.thesportsdb.com/api/v1/json/3/lookupformerteams.php?id=34165647"

urls = [former_teams_leao_url, premier_league_standings_url]

def manage_response(response):
    if response.status_code == 200:
        responseContent = response.json()
        if(print): 
            print(json.dumps(responseContent, indent=2))
        return responseContent
    else:
        print('api call failed with status ' + str(response.status_code))

def choose_request():

    print("Enter a character to choose a request: ")
    for index in range(len(urls)): 
        print(str(index + 1) + ' - ' + urls[index])

    while True:
        userInput = input()
        if len(userInput) == 1:
            if(int(userInput) > len(urls) or int(userInput) < 1):
                print("Please enter a valid selection\n")
            else:
                print(f'Your single character input was: {userInput}')
                break
        else:
            print("Please enter a single character to continue\n")
    
    do_request(urls[int(userInput) - 1])
    

def get_leao_former_teams():
    do_request(former_teams_leao_url)

def get_premier_league_standings():
    do_request(premier_league_standings_url)

def do_request(url):
    response = r.get(url_start + url)
    data = manage_response(response)
    print(json.dumps(data, indent=2))
    return data
# ================================================================================