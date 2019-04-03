n = 4
m = 3

grid = []

for i in range(0,n):
    grid.append([])
    for j in range(0,n):
        grid[i].append([])
        for k in range(0,m):
            grid[i][j].append(0)

datatypes = {
    "int" : 0,
    "float": 1,
    "char": 2,
    "bool": 3,
    "string": 4,
    "set": 5,
    "map": 6,
    "void": 7
}

print(grid)

print(datatypes["void"])
