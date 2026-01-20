import pygame
import random


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False


class MazeGenerator:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.walls = []

    def generate(self):
        """Returns a list of walls that should be drawn."""
        potential_walls = []
        for r in range(self.rows):
            for c in range(self.cols):
                if c < self.cols - 1: potential_walls.append(((c, r), (c + 1, r), 'v'))
                if r < self.rows - 1: potential_walls.append(((c, r), (c, r + 1), 'h'))

        random.shuffle(potential_walls)
        dsu = DSU(self.rows * self.cols)
        final_walls = []

        for c1_r1, c2_r2, orient in potential_walls:
            id1 = c1_r1[1] * self.cols + c1_r1[0]
            id2 = c2_r2[1] * self.cols + c2_r2[0]

            # If union fails, it means they are already connected; keep the wall
            if not dsu.union(id1, id2):
                final_walls.append((c1_r1, c2_r2, orient))

        self.walls = final_walls
        return self.walls

    def draw(self, screen, cell_size, color=(255, 255, 255)):
        """Utility to render the stored walls."""
        for (c1, r1), (c2, r2), orient in self.walls:
            if orient == 'v':
                start = ((c1 + 1) * cell_size, r1 * cell_size)
                end = ((c1 + 1) * cell_size, (r1 + 1) * cell_size)
            else:
                start = (c1 * cell_size, (r1 + 1) * cell_size)
                end = ((c1 + 1) * cell_size, (r1 + 1) * cell_size)
            pygame.draw.line(screen, color, start, end, 2)