def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def checkDirections(grid, rollCoord) -> int:
    coords = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    rX, rY = rollCoord

    rollCount = 0
    for x, y in coords:
        i = x + rX
        j = y + rY
        if (i >= 0 and i < len(grid)) and (j >= 0 and j < len(grid[0])):
            if grid[i][j] == "@":
                rollCount += 1

    print(rollCoord, rollCount)
    return rollCount


def checkRolls(grid) -> int:
    count = 0
    for xPos, line in enumerate(grid):
        for yPos, val in enumerate(line):
            if val == "@":
                if checkDirections(grid, (xPos, yPos)) < 4:
                    count += 1

    return count


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    grid = [x.strip() for x in textIn]

    return checkRolls(grid)


if __name__ == "__main__":
    print(f"The answer is: {main()}")
