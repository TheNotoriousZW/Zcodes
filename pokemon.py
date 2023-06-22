

import requests
from colorama import Fore, Back, Style
#import needed modules

while True:
    search = input(f"{Fore.MAGENTA} Enter Pokemon Name: ")
    while search.isdigit():
        search = input(f"{Fore.MAGENTA} Enter Pokemon Name: ")


    #fstring for user pokemon input
    search = search.lower()
    #makes all user input valid even if they capitalized
    info = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search}")
    #request the api text where we grab information

    while info.status_code != 200:
        print(f"Pokemon name isnt valid try again")
        search = input(Fore.CYAN + "Enter Pokemon Name: ")
        while search.isdigit():
            search = input(Fore.CYAN + "Enter Pokemon Name: ")
        info = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search}")
    #Error management
    try:
        info = info.json()
        # Turns info into a python dictionairy so we can get data

        abilities = info.get('abilities')
        type = info.get('types')
        # print(info)
        weight = info.get('weight')

        ability = [dict(abilities[0]), dict(abilities[1])]
        powers = (ability[0]['ability']['name'], ability[1]['ability']['name'])
        height = info.get('height')
        poke_type = type[0]['type']['name']
        weight = info.get('weight')
        stats = info.get('stats')
    except TypeError:
        search = input(f"{Fore.MAGENTA} Enter Pokemon Name: ")
    else:
        print(f"Height -- {height}in\n")
        print(f"Weight -- {weight}\n")
        print(f"{search} is a {poke_type} type\n")
        print(f"{search} has {powers} abilities\n")



    # print(stats)
    #Grabbing data from Nested dictionairies




