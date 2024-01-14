# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:45:05 2024

@author: asma.khedri
"""


#LifeGrid class, which will take care of two specific tasks:
#Evolving the grid to the next generation
#Providing a string representation of the grid

import collections



class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern

    def evolve(self):
        neighbors = (
            (-1, -1),  # Above left
            (-1, 0),  # Above
            (-1, 1),  # Above right
            (0, -1),  # Left
            (0, 1),  # Right
            (1, -1),  # Below left
            (1, 0),  # Below
            (1, 1),  # Below right
        )
        
        num_neighbors = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1
        pass   
    #to be continued.
        

    def as_string(self, bbox):
        pass

    def __str__(self):
        pass