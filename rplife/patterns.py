# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:45:05 2024

@author: asma.khedri
"""
#this is going to be the seed or initial pattern. 

from dataclasses import dataclass


@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]
    # the tuple represents the coordinate of an alive cell in the life grid.
    


#what I've learned:
    
#we're using dataclass decorator in order to get special methods automatically generated
#such as __init__ method. 
#the __init__ method is called when an object is instantiated from a class
#it is used to initialize the attributes of the object
    
#The above code could've been written this way if not for the dataclass decorator:
    #class Pattern:
        #def __init__(self, att1,att2):
            #self.att1= att1
            #self.att2=att2
#the __init__ method is taken care of by the @dataclass decorator, to save time from writing it explicitly.