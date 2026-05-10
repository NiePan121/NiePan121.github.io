import numpy as np
import matplotlib.pyplot as plt
# Create a 100x100 grid (all susceptible)
size = 100
grid = np.zeros((size, size))
# Place one infected person
x = np.random.randint(0, size)
y = np.random.randint(0, size)
grid[x, y] = 1
beta = 0.3      # infection probability
gamma = 0.05    # recovery probability
for step in range(100):
    new_grid = grid.copy()
    infected_cells = np.where(grid == 1)
    for i, j in zip(*infected_cells):
        # Try to recover
        if np.random.rand() < gamma:
            new_grid[i, j] = 2
            continue
         # Spread to 8 neighbors
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ni = i + di
                nj = j + dj
                if 0 <= ni < size and 0 <= nj < size:
                    if new_grid[ni, nj] == 0:
                        if np.random.rand() < beta:
                            new_grid[ni, nj] = 1
    grid = new_grid
import matplotlib.colors as colors
cmap = colors.ListedColormap(['darkblue', 'green', 'yellow'])
bounds = [0, 1, 2, 3]
norm = colors.BoundaryNorm(bounds, cmap.N)
plt.imshow(grid, cmap=cmap, norm=norm,origin='lower')
plt.title("Spatial SIR Model")
cbar = plt.colorbar(ticks=[0, 1, 2])
cbar.ax.set_yticklabels(['Susceptible (0)', 'Infected (1)', 'Recovered (2)'])
plt.show()