def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def parseInput(input: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    fresh = []
    ids = []

    for line in input:
        # fresh ranges
        if "-" in line:
            a, b = line.strip().split("-")
            fresh.append((int(a), int(b)))
        # id to check
        elif line != "\n":
            ids.append(int(line))

    return (sorted(fresh, key=lambda x: (x[0], x[1])), sorted(ids, key=lambda x: x))


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


def checkFreshId(freshList: list, id: int) -> int:
    for rStart, rEnd in freshList:
        if id >= rStart and id <= rEnd:
            return True


def checkFreshIds(freshList: list, idList: list[int]) -> int:
    count = 0

    for id in idList:
        if checkFreshId(freshList, id):
            count += 1

    return count


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    freshList, idList = parseInput(textIn)
    newFreshList = mergeOverlap(freshList)

    return checkFreshIds(newFreshList, idList)


if __name__ == "__main__":
    print(f"The answer is: {main()}")
