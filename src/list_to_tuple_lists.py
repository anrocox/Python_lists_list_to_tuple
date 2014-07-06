#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 3, 2014

@author: anroco

I have a list and I need convert to tuple, how to make it?

Tengo un lista y necesito convertirla en una tupla, como se puede hacer?
'''

#create tuple
tupla = 'a', 'b', 'c', 'd', 'e'
print(tupla)

#use the list() function built-in python, passing as parameter the tuple
lista = list(tupla)
print (lista)
