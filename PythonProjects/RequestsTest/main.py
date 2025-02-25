import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a81abc40eb021adb50e2ed2522e4d566'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name" : "generate",
    "photo_id" : 1
}

body_update = {
    "pokemon_id": "243941",
    "name": "New Name",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "243941"
}

response_create = requests.post(url = f'{URL}/pokemons', headers= HEADER, json = body_create)
print(response_create.text)

response_create = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_update)
print(response_create.text)

response_create = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_update)
print(response_create.text)