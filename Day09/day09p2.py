from array import array
from copy import deepcopy
from itertools import combinations


def prettyPrint(array: list[str]):
    for i in array:
        print(i)


def parse(input: list[str]) -> list[list[int]]:
    coords = []
    for line in input:
        coords.append(tuple(int(x) for x in line.split(",")))

    return coords


def fillGrid(grid: list[array], coordinates: list[tuple[int, int]]) -> list[array]:

    for i in range(len(coordinates)):
        start = coordinates[i]
        if i != len(coordinates) - 1:
            end = coordinates[i + 1]
        else:
            end = coordinates[0]

        # same row
        if start[0] == end[0]:
            a, b = sorted((start[1], end[1]))
            for j in range(a, b + 1):
                grid[start[0]][j] = 1
        # same column
        else:
            a, b = sorted((start[0], end[0]))
            for j in range(a, b + 1):
                grid[j][start[1]] = 1

    return grid


def floodfill(grid: list[array], startCoord: tuple[int, int], num) -> list[list[int]]:

    visited = set()
    queue = {startCoord}

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while len(queue):
        a, b = queue.pop()
        visited.add((a, b))
        if grid[a][b] == 0:
            grid[a][b] = num

        for dX, dY in directions:
            eX = a + dX
            eY = b + dY
            if (
                (eX >= 0 and eX < len(grid))
                and (eY >= 0 and eY < len(grid[0]))
                and (eX, eY) not in visited
                and grid[eX][eY] == 0
            ):
                queue.add((eX, eY))

    return grid


def getValidPoints(grid: list[array]):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0 or grid[x][y] == 1:
                yield (x, y)


def pointsBetween(
    startCoord: tuple[int, int], endCoord: tuple[int, int]
) -> list[tuple[int, int]]:
    points = []

    aX, bX = sorted((startCoord[0], endCoord[0]))
    aY, bY = sorted((startCoord[1], endCoord[1]))

    for x in range(aX, bX + 1):
        for y in range(aY, bY + 1):
            points.append((x, y))

    return points


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    print("parsing")
    coordinates = parse(textIn)

    minX = min(coordinates, key=lambda x: x[0])[0]
    minY = min(coordinates, key=lambda x: x[1])[1]

    newCoords = []

    for x, y in coordinates:
        newCoords.append((x - minX + 1, y - minY + 1))

    maxX = max(newCoords, key=lambda x: x[0])[0]
    maxY = max(newCoords, key=lambda x: x[1])[1]

    print("making grid")
    grid = [array("h", [0 for y in range(maxY + 2)]) for x in range(maxX + 2)]

    print("filling grid")
    newGrid = fillGrid(grid, newCoords)

    print("flooding")
    newNewGrid = floodfill(newGrid, (0, 0), 3)
    print("getting points")
    vPoints = set(getValidPoints(newNewGrid))

    combos = combinations(newCoords, 2)

    print("checking")
    largest = 0
    for a, b in combos:
        valid = True
        pointsToCheck = pointsBetween(a, b)
        for x, y in pointsToCheck:
            if (x, y) not in vPoints:
                valid = False
                break
        if valid:
            if len(pointsToCheck) > largest:
                largest = len(pointsToCheck)

    return largest


if __name__ == "__main__":
    print(f"The answer is: {main()}")
