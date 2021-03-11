#!/usr/bin/python3
import requests

api = 'https://pokeapi.co/api/v2/pokemon/'

def busqueda_pkm(pkm):
    response = requests.get(api+pkm)
    if response.status_code == 200:
        pokemon = response.json()
        return pokemon