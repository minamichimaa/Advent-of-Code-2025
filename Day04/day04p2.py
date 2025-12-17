from copy import deepcopy

def prettyPrint(array: list[str]):
    for i in array:
        print(i)

def checkDirections(grid: list[list[str]], rollCoord: tuple[int]) -> int:
    coords = ((-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    )

    rX, rY = rollCoord

    rollCount = 0
    for x, y in coords:
        i = x + rX
        j = y + rY
        if (i >= 0 and i < len(grid)) and (j >= 0 and j < len(grid[0])):
            if grid[i][j] == '@':
                rollCount += 1
    
    # print(rollCoord, rollCount)
    return rollCount

def checkRolls(grid: list[list[str]]) -> list[tuple[int, int]]:
    rollsToRemove = []
    for xPos, line in enumerate(grid):
        for yPos, val in enumerate(line):
            if val == '@':
                if checkDirections(grid, (xPos, yPos)) < 4:
                    rollsToRemove.append((xPos, yPos))
    
    return rollsToRemove

def removeRolls(grid: list[list[str]], rollsToRemove: list[tuple[int, int]]) -> list:
    newGrid = deepcopy(grid)

    for rollCoords in rollsToRemove:
        x, y = rollCoords
        newGrid[x][y] = '.'
    
    return newGrid

def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    grid = [list(x.strip()) for x in textIn]

    count = 0
    while True:
        rollsToRemove = checkRolls(grid)

        if len(rollsToRemove) == 0:
            return count
        count += len(rollsToRemove)
        grid = removeRolls(grid, rollsToRemove)


if __name__ == '__main__':
    print(f'The answer is: {main()}')