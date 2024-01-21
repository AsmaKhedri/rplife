# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:45:05 2024

@author: asma.khedri
"""
#WARNING: this code is heavily commented, it can be a bit annoying, so you can skip it, but I am learning so I need it ;).



#LifeGrid class, which will take care of two specific tasks:
#Evolving the grid to the next generation
#Providing a string representation of the grid


import collections


ALIVE = "X"
DEAD = " "

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
                
        #explanation of above code: for each alive cell, we're creating a deafultdict
        #with cell coordinates, and a value 1. 
        #this will mean that if a dead cell appeared X times in the count 
        #of neighbohrs of alive cells, then that cell have X alive neighbors, once we determine
        #the number of the neighbors of a dead cell we can decide its future state. 
        #In the same time, if an alive cell is a neighbor to an alive cell, it will apear 
        #in the dict, then we will also determine how many
        #alive neighbors an alive cel have and decide its future.
        
        #num neighbors will be something like [([x,y],n),..] where x,y are the cell coordinate
        #and n is the number of alive neighbors.
        
        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells
        
        #In the previously created dict, there will be also the cells of our alive pattern
        #therefore we can look for our alive cells within the cells in our dict 
        #that have 2 to 3 neighbors
        
        
        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells
        
        #on the other hand, we can see which cells that aren't among our alive cells pattern 
        #that have exactly three neighbirs. These cells are dead cell that will come alive.

        self.pattern.alive_cells = stay_alive | come_alive    # this | is a bitwise OR operator
        
        #the new pattern of alive cells is a union of stay alive cells and come alive cell
        
        

        

    def as_string(self, bbox):
        start_col, start_row, end_col, end_row = bbox
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]      
            display.append(" ".join(display_row))
        return "\n ".join(display)

    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
            )
    #With this method __str__, when you use the built-in print() function to print 
    #an instance of LifeGrid, you get the name of the current pattern 
    #and the set of alive cells in the next line.
    #This information gives you an idea of the current state of the life grid.