#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NumberException(Exception):
    def __init__(self):
        super().__init__('Debe ingresar un numero entero')