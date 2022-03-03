from pprint import pprint

import requests

def the_smartest_superhero(*names):
    intelligence_list = {}
    for n in names:
        url = f"https://superheroapi.com/api/2619421814940190/search/{n}"
        response = requests.get(url=url)
        result = response.json()
        for r in list(result['results'])[0:]:
            intelligence_list[n] = int(r["powerstats"]["intelligence"])
    print(max(intelligence_list, key=intelligence_list.get))

the_smartest_superhero("Hulk", "Captain America", "Thanos")