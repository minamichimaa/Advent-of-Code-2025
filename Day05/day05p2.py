def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def parseInput(input: list[str]) -> list[tuple[int, int]]:
    fresh = []

    for line in input:
        # fresh ranges
        if "-" in line:
            a, b = line.strip().split("-")
            fresh.append((int(a), int(b)))

    return sorted(fresh, key=lambda x: (x[0], x[1]))


def mergeOverlap(sortedList: list[tuple[int, int]]) -> list[tuple[int, int]]:
    newList = []
    startNum, lastNum = sortedList[0]

    for rStart, rEnd in sortedList[1:]:
        # check if rStart in last range
        if rStart >= startNum and rStart <= lastNum:
            lastNum = max(lastNum, rEnd)
        # not in previous range # append previous and set new
        else:
            newList.append((startNum, lastNum))
            startNum = rStart
            lastNum = rEnd
    newList.append((startNum, lastNum))

    return newList


def countFresh(freshList: list[tuple[int, int]]) -> int:
    count = 0

    for rStart, rEnd in freshList:
        count += rEnd - rStart + 1

    return count


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    freshList = parseInput(textIn)
    newFreshList = mergeOverlap(freshList)

    return countFresh(newFreshList)


if __name__ == "__main__":
    print(f"The answer is: {main()}")
