"""
Simple display for our maze game using matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np
import time
from settings import WALL, PATH, START, END, PLAYER, AI, VISITED

class GameDisplay:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.size = len(maze)
        
        # Create figure for drawing
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        
        # Convert maze to numbers for display
        self.display_grid = np.zeros((self.size, self.size))
        for i in range(self.size):
            for j in range(self.size):
                if maze[i][j] == WALL:
                    self.display_grid[i][j] = 0  # Wall
                elif maze[i][j] == START:
                    self.display_grid[i][j] = 2  # Start
                elif maze[i][j] == END:
                    self.display_grid[i][j] = 3  # End
                else:
                    self.display_grid[i][j] = 1  # Path
        
        # Setup plot
        self.img = self.ax.imshow(self.display_grid, cmap='hot', interpolation='nearest')
        self.ax.set_title('Maze Solver')
        plt.axis('off')
        
        # Track positions
        self.player_pos = start
        self.ai_pos = start
        self.visited = set()
    
    def update_display(self):
        """Update the display with current positions"""
        # Reset display
        display_copy = self.display_grid.copy()
        
        # Mark visited positions
        for pos in self.visited:
            if pos != self.start and pos != self.end:
                display_copy[pos] = 4  # Visited
        
        # Mark player and AI
        display_copy[self.player_pos] = 5  # Player
        display_copy[self.ai_pos] = 6      # AI
        
        # Update image
        self.img.set_data(display_copy)
        plt.draw()
        plt.pause(0.01)
    
    def move_player(self, new_pos):
        """Move player to new position"""
        if 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size:
            if self.maze[new_pos[0]][new_pos[1]] != WALL:
                self.player_pos = new_pos
                self.visited.add(new_pos)
                self.update_display()
                return True
        return False
    
    def show_ai_path(self, path):
        """Show AI following the path"""
        for pos in path:
            self.ai_pos = pos
            self.visited.add(pos)
            self.update_display()
            time.sleep(0.1)
    
    def show_message(self, message):
        """Show a message on the display"""
        self.ax.set_title(message)
        plt.draw()
        plt.pause(1)
    
    def keep_open(self):
        """Keep the display open"""
        plt.show()


