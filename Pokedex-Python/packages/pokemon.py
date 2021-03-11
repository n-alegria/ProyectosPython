#!/usr/bin/python3
from packages.funcion_main import *

class Pokemon():
    def __init__(self, pkm:dict):
        self.nombre = pkm['name']
        self.id = pkm['id']
        self.peso = pkm['weight']
        self.altura = pkm['height']

