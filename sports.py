# ================================================================================
import json
import requests as r

url_start = "https://"
premier_league_standings_url = "www.thesportsdb.com/api/v1/json/3/lookuptable.php?l=4328&s=2020-2021"

former_teams_leao_url = "www.thesportsdb.com/api/v1/json/3/lookupformerteams.php?id=34165647"

def manage_response(response, print = False):
    if response.status_code == 200:
        responseContent = response.json()
        if(print): 
            print(json.dumps(responseContent, indent=2))
        return responseContent
    else:
        print('api call failed with status ' + str(response.status_code))

def leao_former_teams():
    response = r.get(url_start + former_teams_leao_url)
    manage_response(response)

def get_premier_league_standings():
    response = r.get(url_start + premier_league_standings_url)
    return manage_response(response)
# ================================================================================