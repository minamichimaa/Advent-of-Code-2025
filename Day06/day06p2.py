import re

from math import prod

pattern = re.compile(r"([\*\+]\s*)(?:\s|$)")


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def parse(input: list[str]) -> tuple[list[list[str]], list[str]]:
    signsList = []
    numDigits = []

    # get signs first
    signsRaw = pattern.findall(input[-1])

    for sign in signsRaw:
        signsList.append(sign.strip())
        numDigits.append(len(sign))

    numbersList = [[] for x in range(len(numDigits))]

    for line in input[:-1]:
        i = 0
        j = 0
        while i < len(line):
            cutoff = i + numDigits[j]
            numbersList[j].append(line[i:cutoff])
            i = cutoff + 1
            j += 1

    return (numbersList, signsList)


def rotateGrid(grid: list[str]) -> list[str]:
    return list(map(list, zip(*grid)))[::-1]


def rotateListAsInts(numbersList: list[list[str]]) -> list[list[str]]:
    newNumList = []
    # rotate each
    for grid in numbersList:
        rGrid = rotateGrid(grid)
        # combine list of strings to int
        newGrid = []
        for line in rGrid:
            newGrid.append(int("".join(line)))
        newNumList.append(newGrid)

    return newNumList


def solve(numbersList, signsList) -> int:
    total = 0

    for i, sign in enumerate(signsList):
        if sign == "*":
            total += prod(numbersList[i])
        else:
            total += sum(numbersList[i])

    return total


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    numbersList, signsList = parse(textIn)
    rotatedInts = rotateListAsInts(numbersList)

    return solve(rotatedInts, signsList)


if __name__ == "__main__":
    print(f"The answer is: {main()}")
