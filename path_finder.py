"""
Pathfinding algorithms for our maze solver
"""

import heapq
from settings import WALL

class PathFinder:
    def __init__(self, maze):
        self.maze = maze
        self.size = len(maze)
    
    def find_path_a_star(self, start, end):
        """A* algorithm to find the shortest path"""
        # Priority queue for nodes to explore
        open_list = []
        heapq.heappush(open_list, (0, start))
        
        # Dictionaries to keep track of our path and costs
        came_from = {}
        cost_so_far = {start: 0}
        
        while open_list:
            current = heapq.heappop(open_list)[1]
            
            # Found the end!
            if current == end:
                break
            
            # Check all four directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_row, next_col = current[0] + dr, current[1] + dc
                next_pos = (next_row, next_col)
                
                # Skip if out of bounds or wall
                if (next_row < 0 or next_row >= self.size or 
                    next_col < 0 or next_col >= self.size or 
                    self.maze[next_row][next_col] == WALL):
                    continue
                
                # Calculate new cost
                new_cost = cost_so_far[current] + 1
                
                # If we found a better path to this position
                if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    priority = new_cost + self.heuristic(next_pos, end)
                    heapq.heappush(open_list, (priority, next_pos))
                    came_from[next_pos] = current
        
        # Reconstruct the path
        return self.reconstruct_path(came_from, start, end)
    
    def heuristic(self, a, b):
        """Estimate distance between two points (Manhattan distance)"""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def reconstruct_path(self, came_from, start, end):
        """Build the path from start to end"""
        current = end
        path = []
        
        while current != start:
            path.append(current)
            current = came_from[current]
        
        path.append(start)
        path.reverse()
        return path
    
    def find_path_recursive(self, start, end, visited=None):
        """Simple recursive pathfinding (not very efficient)"""
        if visited is None:
            visited = set()
        
        # Mark current position as visited
        visited.add(start)
        
        # Found the end!
        if start == end:
            return [start]
        
        # Check all four directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_row, next_col = start[0] + dr, start[1] + dc
            next_pos = (next_row, next_col)
            
            # Skip if invalid or already visited
            if (next_row < 0 or next_row >= self.size or 
                next_col < 0 or next_col >= self.size or 
                self.maze[next_row][next_col] == WALL or 
                next_pos in visited):
                continue
            
            # Recursively search from next position
            path = self.find_path_recursive(next_pos, end, visited)
            if path:
                return [start] + path
        
        # No path found from this position
        return None
