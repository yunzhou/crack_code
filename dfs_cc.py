def getAdj(u, grid):
    n = len(grid)
    m = len(grid[0])
    result = []
    delta = (-1, 0, 1)
    for dr in delta:
        for dc in delta:
            new_row = u[0] + dr
            new_col = u[1] + dc
            if n > new_row >= 0 and m > new_col >= 0:
                if u[0] == new_row and u[1] == new_col:
                    pass
                elif grid[new_row][new_col]==1:
                    result.append((new_row, new_col))
    #print(result)
    return result


def getBiggestRegion(grid):
    max_region = 0
    visited = set()
    n = len(grid)
    m = len(grid[0])
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 0:
                visited.add((row, col))
            elif (row, col) not in visited:
                stack = []
                stack.append((row, col))
                region = 1
                while len(stack) > 0:
                    u = stack.pop()
                    if u is not None:
                        visited.add(u)
                        for n in getAdj(u, grid):
                            if n not in visited:
                                region += grid[n[0]][n[1]]
                                visited.add(n)
                                stack.append(n)
                if region > max_region:
                    max_region = region
    return max_region


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
