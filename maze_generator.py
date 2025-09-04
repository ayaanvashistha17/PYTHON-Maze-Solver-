"""
Simple maze generator for our project
"""

import random
import numpy as np
from settings import WALL, PATH, START, END

class MazeMaker:
    def __init__(self, size=15, wall_density=0.2):
        self.size = size
        self.wall_density = wall_density
        self.maze = None
        self.start = (0, 0)
        self.end = (size-1, size-1)
    
    def make_maze(self):
        """Create a random maze with walls and paths"""
        # Start with all paths
        self.maze = np.full((self.size, self.size), PATH)
        
        # Add random walls
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < self.wall_density:
                    self.maze[i, j] = WALL
        
        # Make sure start and end are not walls
        self.maze[self.start] = START
        self.maze[self.end] = END
        
        return self.maze, self.start, self.end
    
    def is_valid_move(self, row, col):
        """Check if we can move to this position"""
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        return self.maze[row, col] != WALL
