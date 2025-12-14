'''
Preparation for coding interviews using ChatGPT's recommendations on how to prepare effectively.
Sample practice problems
Fetch Pokémon data and return the total weight of all fire-type Pokémon.
API: https://pokeapi.co/api/v2/pokemon?limit=20
Fetch crypto market data and return the top 3 coins by price.
API: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd
Fetch weather for a city and categorize it as cold/mild/hot based on temp.
API: https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY
'''
import requests
import json
import os
import random
from typing import Optional

def solve_pokemon():
    # requests documentation: https://docs.python-requests.org/en/latest/ ~ https://www.w3schools.com/python/module_requests.asp
    poke_url = "https://pokeapi.co/api/v2/pokemon"
    limit = 151
    data = requests.get(poke_url, params={"limit": limit}).json()
    if not os.path.exists("bulbasaur.json"):
        print("test")
        bulbasaur = data['results'][0]
        bulbasaur_data = requests.get(bulbasaur['url']).json()
        with open ("bulbasaur.json", "w") as f:
            json.dump(bulbasaur_data, f, indent=2)
    else:
        with open("bulbasaur.json") as f:
            bulbasaur_data = json.load(f)
            # print(bulbasaur_data)
        
    fire_weight = 0
    fire_count = 0
    try:
        for pokemon in data["results"]:
            poke_url = pokemon["url"]
            pokemon_data = requests.get(poke_url).json()
            # determine if fire
            types = [type['type']['name'] for type in pokemon_data['types']]
            if "fire" in types:
                fire_weight += pokemon_data["weight"]
                fire_count += 1
        avg_fire_weight = fire_weight/fire_count
        print(avg_fire_weight)
    except Exception as e:
        print("Encountered exception with Pokemon API or code: ", e)
    return 
def solve_crypto():
    def print_coin(coin):
        # print useful info about a coin
        print("ID: ", coin["id"])
        print("Name: ", coin["name"])
        print("Current price: ", coin["current_price"])
    crypto_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    data = requests.get(crypto_url).json()
    # bitcoin = data[0]
    one = None
    two = None
    three = None
    # what to do about ties? - assume no ties for now
    for coin in data:
        # compare price price and move others down accordingly
        if not one or coin['current_price'] > one['current_price']:
            # make this one and shift the other coins
            three = two
            two = one
            one = coin
        elif not two or coin['current_price'] > two['current_price']:
            three = two
            two = coin
        elif not three or coin['current_price'] > three['current_price']:
            three = coin
        
    print_coin(one)
    print_coin(two)
    print_coin(three)
    return 
def solve_weather():
    weather_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY"
    # need an account to do this one, probably won't do it
    return
class person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def speak(self)->Optional[str]:
        message = f"Hi, I'm {self.name} and I am {self.age} years old"
        print(message)
        return message

def main():
    solve_pokemon()
    # solve_crypto()
    
    response = requests.get("https://api.github.com")
    print(response.status_code)
    Jake = person("Jake", 11)
    Jake.speak()
    pair_list = []
    for i in range(15):
        val = random.randint(0,i)
        tuple = (val, chr(ord('a')+i+val))
        pair_list.append(tuple)
    print(pair_list)
    pair_list.sort(key = lambda x: x[1])
    print(pair_list)

    return 0
if __name__ == "__main__":
    main()